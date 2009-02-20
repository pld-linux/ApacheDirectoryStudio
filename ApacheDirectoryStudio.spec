#
%define	_snap	745477
Summary:	Apache Directory Studio - LDAP tooling platform
Summary(pl.UTF-8):	Apache Directory Studio - platforma narzędzi LDAP
Name:		ApacheDirectoryStudio
Version:	1.4.0
Release:	0.%{_snap}.1
License:	Apache
Group:		Applications
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	dcb0c4a4be7ee9aefcd71c205d189f51
URL:		http://directory.apache.org/
BuildRequires:	java-sun-jre
BuildRequires:	maven
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
ExclusiveArch:	i586 i686 athlon pentium3 pentium4 %{x8664}
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
%setup -q -n studio

%build
export M2_HOME="%{_datadir}/maven"
export JAVA_HOME="%{_prefix}/%{_lib}/jvm/java"
mvn clean install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir},%{_bindir}}
pwd
install 'tools/Debian Package/package%{_datadir}/applications/apachedirectorystudio.desktop' $RPM_BUILD_ROOT%{_desktopdir}
%if "%{_lib}" == "lib64"
cd target/distributions/%{name}-linux-x86_64-%{version}-SNAPSHOT
%else
cd target/distributions/%{name}-linux-x86-%{version}-SNAPSHOT
%endif
cp -rf configuration $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf features $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf plugins $RPM_BUILD_ROOT%{_datadir}/%{name}
install ApacheDirectoryStudio $RPM_BUILD_ROOT%{_datadir}/%{name}
install ApacheDirectoryStudio.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
ln -s %{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/apachedirectorystudio

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE.txt docs/Release\ Notes.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/ApacheDirectoryStudio
%{_datadir}/%{name}/configuration
%{_datadir}/%{name}/features
%{_datadir}/%{name}/plugins
%{_pixmapsdir}/ApacheDirectoryStudio.xpm
%{_desktopdir}/apachedirectorystudio.desktop
