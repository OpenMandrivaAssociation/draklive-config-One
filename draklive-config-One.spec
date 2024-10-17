%define name draklive-config-One
%define version 0.1
%define svnsnap 20090428.1
%define rel 4
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
Url: https://wiki.mandriva.com/en/Draklive
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-0.20090428.1.4mdv2011.0
+ Revision: 663855
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-0.20090428.1.3mdv2011.0
+ Revision: 604820
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-0.20090428.1.2mdv2010.1
+ Revision: 522504
- rebuilt for 2010.1

* Tue Apr 28 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-0.20090428.1.1mdv2010.0
+ Revision: 369112
- New One config snapshot

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 0.1-0.20080403.1.1mdv2008.1
+ Revision: 192262
- enable urpmi step at first boot after installation for live CDs
- remove adjtime UTC hack, now done in installer
- enable network step for live USB, now that is does not pop up if
  network is already configured

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 0.1-0.20080403.1mdv2008.1
+ Revision: 192046
- initial draklive-config-One package
- create draklive-config-One

