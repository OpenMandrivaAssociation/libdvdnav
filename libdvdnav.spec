%define major 4
%define libname %mklibname dvdnav %{major}
%define develname %mklibname dvdnav -d

Name:		libdvdnav
Summary:	DVD Navigation library
Version:	4.2.0
Release:	2
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.mplayerhq.hu
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dvdread)

%description
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n	%{libname}
Summary:	DVD Navigation library
Group:		System/Libraries

%description -n	%{libname}
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n	%{develname}
Summary:	DVD Navigation library headers and support files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname dvdnav 4 -d} < 4.2.0

%description -n	%{develname}
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

This package contains the C headers and support files for compiling 
applications with libdvdnav.

%prep
%setup -q

%build
./autogen.sh
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
%makeinstall_std
#gw remove buildroot
perl -pi -e "s^%{buildroot}^^" %{buildroot}%{_bindir}/dvdnav-config

%multiarch_binaries %{buildroot}%{_bindir}/dvdnav-config

%files -n %{libname}
%doc COPYING README
%{_libdir}/libdvdnavmini.so.%{major}*
%{_libdir}/libdvdnav.so.%{major}*

%files -n %{develname}
%doc COPYING NEWS TODO AUTHORS
%{_bindir}/dvdnav-config
%{multiarch_bindir}/dvdnav-config
%{_libdir}/libdvdnavmini.so
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav/
%{_datadir}/aclocal/dvdnav.m4
%{_libdir}/pkgconfig/dvdnav.pc
%{_libdir}/pkgconfig/dvdnavmini.pc

%changelog
* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 4.2.0-1mdv2012.0
+ Revision: 731125
- new version
- update source URL

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-6
+ Revision: 661677
- multiarch fixes

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-5
+ Revision: 660241
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-4mdv2011.0
+ Revision: 602539
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-3mdv2010.1
+ Revision: 520766
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.1.3-2mdv2010.0
+ Revision: 425534
- rebuild

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-1mdv2009.0
+ Revision: 283000
- version 4.1.3 final
- update source URL

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-0.r1132.1mdv2009.0
+ Revision: 278180
- new snapshot
- fix build
- update file list

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 4.1.2-3mdv2009.0
+ Revision: 264777
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 07 2008 Götz Waschk <waschk@mandriva.org> 4.1.2-2mdv2009.0
+ Revision: 202766
- fix header incompatibility with C++ (bug #40406)
- disable double build

* Mon Apr 21 2008 Götz Waschk <waschk@mandriva.org> 4.1.2-1mdv2009.0
+ Revision: 196230
- new version
- drop patch
- fix installation

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 4.1.1-0.956.2mdv2008.1
+ Revision: 103585
- add requires on libdvdread-devel into libdvdnav-devel

* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 4.1.1-0.956.1mdv2008.1
+ Revision: 96551
- fix installation
- readd libdvdnav.so
- fix soname
- switch to mplayer fork of dvdnav
- update file list

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.10-6mdv2008.0
+ Revision: 76794
- new devel naming


* Thu Oct 26 2006 Götz Waschk <waschk@mandriva.org> 0.1.10-5mdv2007.0
+ Revision: 72723
- Import libdvdnav

* Thu Oct 26 2006 G�tz Waschk <waschk@mandriva.org> 0.1.10-5mdv2007.1
- rebuild

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.1.10-4mdk
- Rebuild

* Mon Jan 31 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.1.10-3mdk
- multiarch support

* Sat Oct 23 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.10-2mdk
- Patch0 (CVS): fix crash with DVD without first play chain

* Sat Jun 12 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1.10-1mdk
- major 4
- add new file
- add source URL
- New release 0.1.10

