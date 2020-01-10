%define _disable_ld_no_undefined 1

%define major	4
%define libname %mklibname dvdnav %{major}
%define devname %mklibname dvdnav -d

Summary:	DVD Navigation library
Name:		libdvdnav
Version:	6.0.1
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.mplayerhq.hu
Source0:	http://download.videolan.org/pub/videolan/libdvdnav/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dvdread) >= 5.0.2

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
%setup -q
%autopatch -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_datadir}/doc/${name}

%files -n %{libname}
%{_libdir}/libdvdnav.so.%{major}*

%files -n %{devname}
%doc COPYING ChangeLog TODO AUTHORS README
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav/
%{_libdir}/pkgconfig/dvdnav.pc

