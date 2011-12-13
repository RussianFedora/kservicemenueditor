Name: kservicemenueditor
Version: 0.2a
Release: 1%{?dist}.R
Summary: KDE Service Menu Editor
Group: Applications/Editors
License: GPL
Source0: http://www.sharpley.org.uk/sites/default/files/software/servicemenu/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://www.sharpley.org.uk/node/3
BuildArch: noarch

Requires: python, PyKDE4, PyQt4
BuildRequires: desktop-file-utils

%description
Editor of the Dolphin`s content menu.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_desktopdir}
mkdir -p $RPM_BUILD_ROOT/%{_kde4_appsdir}/servicemenueditor/
install -D -m 755 -p servicemenueditor $RPM_BUILD_ROOT/%{_bindir}/servicemenueditor
install -D -m 644 -p *.ui $RPM_BUILD_ROOT/%{_kde4_appsdir}/servicemenueditor/

desktop-file-install --delete-original		\
	--dir ${RPM_BUILD_ROOT}%{_desktopdir} servicemenueditor.desktop
desktop-file-validate %{buildroot}/%{_desktopdir}/servicemenueditor.desktop

%files
%defattr(-,root,root)
%{_bindir}/servicemenueditor
%{_desktopdir}/servicemenueditor.desktop
%dir %{_kde4_appsdir}/servicemenueditor
%{_kde4_appsdir}/servicemenueditor/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Dec 5 2011 Fl@sh <kaperang07@gmail.com> - 0.2a-1.R
- Initial build
