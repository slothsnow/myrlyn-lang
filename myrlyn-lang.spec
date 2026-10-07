Name:           myrlyn-lang
Version:        0.0.0
Release:        1%{?dist}
Summary:        Myrlyn translation files
License:        GPL-2.0-only
URL:            https://github.com/slothsnow/myrlyn-lang
Source0:        %{name}-%{version}.tar

BuildArch:      noarch

BuildRequires:  gettext
Requires:       gettext

%description
This package contains the translation files for Myrlyn.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/locale

for po in po/*.po; do
  lang=$(basename "$po" .po)
  target=%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mkdir -p "$target"
  msgfmt -o "$target/myrlyn.mo" "$po"
done

%files
%license LICENSE
%doc README.md
%{_datadir}/locale/*/LC_MESSAGES/myrlyn.mo

%changelog
