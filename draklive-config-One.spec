%define name draklive-config-One
%define version 0.1
%define svnsnap 20090428.1
%define rel 1
%define release %mkrel 0.%{svnsnap}.%{rel}
%define distname %{name}-%{svnsnap}
# DATE=$(date +%Y%m%d)
# svn export http://svn.mandriva.com/svn/config/One/trunk draklive-config-One-$DATE
# tar cjf draklive-config-One-$DATE.tar.bz2 draklive-config-One-$DATE

Summary: Configuration files to build Mandriva One with draklive
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: System/Configuration/Other
Url: http://wiki.mandriva.com/en/Draklive
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This package contains the required configuration files to build
Mandriva One live CDs with the draklive tool.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -a * %{buildroot}%{_sysconfdir}/%{name}

%post
if [ ! -e %{_sysconfdir}/draklive ]; then
   ln -s %{name} %{_sysconfdir}/draklive
fi
:

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/%{name}
