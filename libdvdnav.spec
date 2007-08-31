%define major 4
%define libname %mklibname dvdnav %{major}
%define develname %mklibname dvdnav -d

Name:		libdvdnav
Summary:	DVD Navigation library
Version:	0.1.10
Release:	%mkrel 6
Group:		System/Libraries
License:	GPL
URL:		http://dvd.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dvd/%{name}-%{version}.tar.bz2
# (fc) 0.1.10-2mdk fix crash with DVD without first play chain (CVS)
Patch0:		libdvdnav-0.1.10-fixdvdcrash.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
%if "%{_lib}" != "lib"
Provides:	%{name}-devel = %{version}-%{release}
%endif
Provides:	%{mklibname dvdnav 4 -d} = %{version}
Obsoletes:	%{mklibname dvdnav 4 -d}

%description -n	%{develname}
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

This package contains the C headers and support files for compiling 
applications with libdvdnav.

%prep

%setup -q
%patch0 -p1 -b .fixdvdcrash

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/dvdnav-config

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

%clean
rm -r %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/libdvdnav*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING NEWS TODO AUTHORS
%{_bindir}/dvdnav-config
%{_bindir}/*/dvdnav-config
%{_libdir}/libdvdnav*.la
%{_libdir}/libdvdnav*.so
%{_includedir}/dvdnav/
%{_datadir}/aclocal/dvdnav.m4
