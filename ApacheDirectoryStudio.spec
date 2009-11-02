#
%define     _reldate    20090407
Summary:	Apache Directory Studio - LDAP tooling platform
Summary(pl.UTF-8):	Apache Directory Studio - platforma narzędzi LDAP
Name:		ApacheDirectoryStudio
Version:	1.4.0
Release:	0.%{_reldate}.1
License:	Apache
Group:		Applications
Source0:	http://www.apache.org/dist/directory/studio/stable/%{version}.v%{_reldate}/%{name}-linux-x86-%{version}.v%{_reldate}.tar.gz
# Source0-md5:	3bc4b96993eab40f8429893087f0430e
Source1:	http://www.apache.org/dist/directory/studio/stable/%{version}.v%{_reldate}/%{name}-linux-x86_64-%{version}.v%{_reldate}.tar.gz
# Source1-md5:	38c037ebaa0999efe1e3fcce61e3ed50
Source2:    http://www.apache.org/dist/directory/studio/stable/%{version}.v%{_reldate}/%{name}-linux-ppc-%{version}.v%{_reldate}.tar.gz
# Source2-md5:	c16a9f50e270c3fd053336eb72c6f4b8
Source3:    apachedirectorystudio.desktop
URL:		http://directory.apache.org/
BuildRequires:	rpmbuild(macros) >= 1.300
ExclusiveArch:	%{ix86} %{x8664} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache Directory Studio (formerly known as LDAP Studio) is a complete
LDAP tooling platform intended to be used with any LDAP server however
it is particularly designed for use with the Apache Directory Server.

%description -l pl.UTF-8
Apache Directory Studio (wcześniej znane jako LDAP Studio) to
kompletna platforma narzędzi LDAP przeznaczona do użytku z dowolnym
serwerem LDAP, jednak jest najlepiej dopasowana do Apache Directory
Servera.

%prep
%ifarch %{ix86}
%setup -q -b1 -b2 -n %{name}-linux-x86-%{version}.v%{_reldate}
%endif
%ifarch %{x8664}
%setup -q -b1 -b2 -n %{name}-linux-x86_64-%{version}.v%{_reldate}
%endif
%ifarch ppc
%setup -q -b1 -b2 -n %{name}-linux-ppc-%{version}.v%{_reldate}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir},%{_bindir}}
cp -a {configuration,features,plugins} $RPM_BUILD_ROOT%{_datadir}/%{name}
install ApacheDirectoryStudio.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install ApacheDirectoryStudio $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/
ln -s %{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/apachedirectorystudio

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE.txt Release\ Notes.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/ApacheDirectoryStudio
%{_datadir}/%{name}/configuration
%{_datadir}/%{name}/features
%{_datadir}/%{name}/plugins
%{_pixmapsdir}/ApacheDirectoryStudio.xpm
%{_desktopdir}/apachedirectorystudio.desktop
