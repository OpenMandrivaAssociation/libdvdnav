%define _disable_ld_no_undefined 1

%define major	4
%define libname %mklibname dvdnav %{major}
%define libmini %mklibname dvdnavmini %{major}
%define devname %mklibname dvdnav -d

Summary:	DVD Navigation library
Name:		libdvdnav
Version:	4.2.1
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.mplayerhq.hu
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.xz
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

%package -n	%{libmini}
Summary:	DVD Navigation library
Group:		System/Libraries
Conflicts:	%{_lib}dvdnav4 < 4.2.0-3

%description -n	%{libmini}
libdvdnavmini provides support to applications wishing to make use of advanced
DVD features.

%package -n	%{devname}
Summary:	DVD Navigation library headers and support files
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libmini} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the C headers and support files for compiling 
applications with libdvdnav.

%prep
%setup -q
%apply_patches
./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std
#gw remove buildroot
sed -i -e "s^%{buildroot}^^" %{buildroot}%{_bindir}/dvdnav-config

%multiarch_binaries %{buildroot}%{_bindir}/dvdnav-config

%files -n %{libname}
%{_libdir}/libdvdnav.so.%{major}*

%files -n %{libmini}
%{_libdir}/libdvdnavmini.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS TODO AUTHORS README
%{_bindir}/dvdnav-config
%{multiarch_bindir}/dvdnav-config
%{_libdir}/libdvdnavmini.so
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav/
%{_datadir}/aclocal/dvdnav.m4
%{_libdir}/pkgconfig/dvdnav.pc
%{_libdir}/pkgconfig/dvdnavmini.pc

