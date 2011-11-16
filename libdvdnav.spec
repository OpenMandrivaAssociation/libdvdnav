%define major 4
%define libname %mklibname dvdnav %{major}
%define develname %mklibname dvdnav -d

Name:		libdvdnav
Summary:	DVD Navigation library
Version:	4.2.0
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.mplayerhq.hu
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libdvdread-devel >= 4.1.3

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
Obsoletes:	%{mklibname dvdnav 4 -d}

%description -n	%{develname}
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

This package contains the C headers and support files for compiling 
applications with libdvdnav.

%prep

%setup -q
./autogen.sh
%build
#./configure2 --prefix=%_prefix --libdir=%_libdir --with-dvdread=%_includedir/dvdread
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
#gw remove buildroot
perl -pi -e "s^%buildroot^^" %buildroot%_bindir/dvdnav-config

%multiarch_binaries %{buildroot}%{_bindir}/dvdnav-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig 
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig 
%endif

%clean
rm -r %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/libdvdnavmini.so.%{major}*
%{_libdir}/libdvdnav.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING NEWS TODO AUTHORS
%{_bindir}/dvdnav-config
%{multiarch_bindir}/dvdnav-config
%{_libdir}/libdvdnavmini.so
%{_libdir}/libdvdnavmini.la
%{_libdir}/libdvdnav.so
%{_libdir}/libdvdnav.la
%{_includedir}/dvdnav/
%_datadir/aclocal/dvdnav.m4
%_libdir/pkgconfig/dvdnav.pc
%_libdir/pkgconfig/dvdnavmini.pc
