#!/bin/bash

set -e

# Config
PACKAGE_NAME="myrlyn-lang"
TRANSLATED_PACKAGE="myrlyn"
VERSION="0.2"
REPO_DIR="../po"  # Verzeichnis mit deinen .po-Dateien
BUILDROOT="$HOME/rpmbuild"
LOCALE_DIR="usr/share/locale"
# End of Config

rpmdev-setuptree

WORKDIR="${PACKAGE_NAME}-${VERSION}"
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR/$LOCALE_DIR"


for po_file in "$REPO_DIR"/*.po; do
    lang=$(basename "$po_file" .po)
    mkdir -p "$WORKDIR/$LOCALE_DIR/$lang/LC_MESSAGES"
    msgfmt -o "$WORKDIR/$LOCALE_DIR/$lang/LC_MESSAGES/${TRANSLATED_PACKAGE}.mo" "$po_file"
done

tar czf "${PACKAGE_NAME}-${VERSION}.tar.gz" "$WORKDIR"
mv "${PACKAGE_NAME}-${VERSION}.tar.gz" "$BUILDROOT/SOURCES/"

# SPEC-File
SPECFILE="$BUILDROOT/SPECS/${PACKAGE_NAME}.spec"
cat > "$SPECFILE" <<EOF
Name:           $PACKAGE_NAME
Version:        $VERSION
Release:        1%{?dist}
Summary:        Translations of Myrlyn
License:        EUPL-1.2
Group:          System/I18n
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

%description
This package contains the translations of Myrlyn.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/$LOCALE_DIR
cp -r $LOCALE_DIR/* %{buildroot}/$LOCALE_DIR/

%files
%defattr(-,root,root,-)
/$LOCALE_DIR/*

%changelog

EOF

# 🛠️ RPM bauen
rpmbuild -ba "$SPECFILE"

echo "RPM: $BUILDROOT/RPMS/noarch/${PACKAGE_NAME}-${VERSION}-1.noarch.rpm"

