Name: kservicemenueditor
Version: 0.2a
Release: 2%{?dist}.R
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/kde4/apps/servicemenueditor
install -D -m 755 -p servicemenueditor $RPM_BUILD_ROOT%{_bindir}/servicemenueditor
install -D -m 644 -p *.ui $RPM_BUILD_ROOT%{_datadir}/kde4/apps/servicemenueditor

desktop-file-install --delete-original		\
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications servicemenueditor.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/servicemenueditor.desktop

%files
%defattr(-,root,root)
%{_bindir}/servicemenueditor
%{_datadir}/applications/servicemenueditor.desktop
%{_datadir}/kde4/apps/servicemenueditor/*
%dir %{_datadir}/kde4/apps/servicemenueditor

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Dec 14 2011 Fl@sh <kaperang07@gmail.com> - 0.2a-2.R
- fixed path

* Mon Dec 5 2011 Fl@sh <kaperang07@gmail.com> - 0.2a-1.R
- Initial build
