%define _disable_ld_no_undefined 1

%define major	4
%define libname %mklibname dvdnav %{major}
%define devname %mklibname dvdnav -d

Summary:	DVD Navigation library
Name:		libdvdnav
Version:	7.0.0
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		https://www.mplayerhq.hu
Source0:  https://code.videolan.org/videolan/libdvdnav/-/archive/%{version}/libdvdnav-%{version}.tar.bz2
#Source0:	http://download.videolan.org/pub/videolan/libdvdnav/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dvdread) >= 7.0.0

%description
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n	%{libname}
Summary:	DVD Navigation library
Group:		System/Libraries

%description -n	%{libname}
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n	%{devname}
Summary:	DVD Navigation library headers and support files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the C headers and support files for compiling 
applications with libdvdnav.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/doc/${name}

%files -n %{libname}
%{_libdir}/libdvdnav.so.%{major}*

%files -n %{devname}
%doc COPYING ChangeLog TODO AUTHORS README
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav/
%{_libdir}/pkgconfig/dvdnav.pc
