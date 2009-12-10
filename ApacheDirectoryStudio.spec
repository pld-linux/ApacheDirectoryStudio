#
%define     _reldate    20091130
Summary:	Apache Directory Studio - LDAP tooling platform
Summary(pl.UTF-8):	Apache Directory Studio - platforma narzędzi LDAP
Name:		ApacheDirectoryStudio
Version:	1.5.1
Release:	0.%{_reldate}.1
License:	Apache
Group:		Applications
Source0:	http://www.apache.org/dist/directory/studio/stable/%{version}.v%{_reldate}/%{name}-linux-x86-%{version}.V%{_reldate}.tar.gz
# Source0-md5:	d3ffa80932d2eaa194b04dfda34c98aa
Source1:	http://www.apache.org/dist/directory/studio/stable/%{version}.v%{_reldate}/%{name}-linux-x86_64-%{version}.V%{_reldate}.tar.gz
# Source1-md5:	48f91cb44e357c425ee0312787f9ab6d
Source2:	apachedirectorystudio.desktop
URL:		http://directory.apache.org/studio/
BuildRequires:	rpmbuild(macros) >= 1.300
ExclusiveArch:	%{ix86} %{x8664}
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
%setup -q -b1 -n %{name}-linux-x86-%{version}.V%{_reldate}
%endif
%ifarch %{x8664}
%setup -q -b1 -n %{name}-linux-x86_64-%{version}.V%{_reldate}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir},%{_bindir}}
cp -a {configuration,features,plugins} $RPM_BUILD_ROOT%{_datadir}/%{name}
install ApacheDirectoryStudio.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install ApacheDirectoryStudio $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/
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
