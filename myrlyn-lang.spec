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
Requires:       myrlyn
Provides:       locale(myrlyn:ca)
Provides:       locale(myrlyn:de)
Provides:       locale(myrlyn:es)
#Provides:       locale(myrlyn:fr)
#Provides:       locale(myrlyn:it)
Provides:       locale(myrlyn:ja)
Provides:       locale(myrlyn:nl)
Provides:       locale(myrlyn:pl)
#Provides:       locale(myrlyn:ru)
Provides:       locale(myrlyn:sv)
#Provides:       locale(myrlyn:zh_CN)
#Provides:       locale(myrlyn:zh_TW)

Supplements:    myrlyn and namespace language(ca)
Supplements:    myrlyn and namespace language(de)
Supplements:    myrlyn and namespace language(es)
#Supplements:    myrlyn and namespace language(fr)
#Supplements:    myrlyn and namespace language(it)
Supplements:    myrlyn and namespace language(ja)
Supplements:    myrlyn and namespace language(nl)
Supplements:    myrlyn and namespace language(pl)
#Supplements:    myrlyn and namespace language(ru)
Supplements:    myrlyn and namespace language(sv)
#Supplements:    myrlyn and namespace language(zh_CN)
#Supplements:    myrlyn and namespace language(zh_TW)

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
