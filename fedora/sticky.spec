Name:           sticky
Version:        1.14
Release:        1%{?dist}
Summary:        A notes app for the linux desktop

License:        GPLv2
URL:            https://github.com/paseaf/sticky
Source:         https://github.com/paseaf/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       python3-gobject
Requires:       python3-setuptools
Requires:       python3-pip
Requires:       gtk3
Requires:       gspell
Requires:       xapps
Requires:       python3-xapp

%{?python_disable_dependency_generator}

%description
Sticky is a note-taking app for the Linux desktop.


%global debug_package %{nil}

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_bindir}

cp -r usr/lib/ %{buildroot}/usr/lib
chmod +x %{buildroot}/usr/lib/%{name}/*
cp -r usr/bin/* %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}
cp -r usr/share/* %{buildroot}/%{_datadir}
chmod +x %{buildroot}%{_bindir}/%{name}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
/usr/lib/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.x.sticky.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/%{name}*.svg
%{_datadir}/%{name}/*



%changelog
* Fri Feb 17 2023 Ziyang Li <paseaf@me.com> - 1.14-1
- Initial release
