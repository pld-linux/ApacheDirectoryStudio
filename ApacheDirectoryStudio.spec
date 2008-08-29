Summary:	Apache Directory Studio - LDAP tooling platform
Summary(pl.UTF-8):	Apache Directory Studio - platforma narzędzi LDAP
Name:		ApacheDirectoryStudio
Version:	1.2.0.v20080724
Release:	0.1
License:	Apache
Group:		Applications
Source0:	http://www.apache.org/dist/directory/studio/stable/1.2.0-RC1/%{name}-sources-%{version}.zip
#Source0-md5:	94dd2c5792dcdcb37cd9cf5b85d5b8f1
URL:		http://directory.apache.org/
BuildRequires:	maven
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		arch	x86

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
%setup -q -n %{name}-sources-%{version}

%build
export M2_HOME="%{_datadir}/maven"
export JAVA_HOME="%{java_home}"
cd studio-plugin
mvn clean install
cd ../studio
mvn clean install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir},%{_bindir}}
pwd
install 'tools/Debian Package/package/usr/share/applications/apachedirectorystudio.desktop' $RPM_BUILD_ROOT%{_desktopdir}
cd target/distributions/%{name}-linux-%{arch}-%{version}
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
