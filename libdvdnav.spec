%define name    libdvdnav
%define ver     0.1.10
%define rel     %mkrel 5
%define major	4
%define libname %mklibname dvdnav %major

Name: %{name}
Summary: DVD Navigation library
Version: %{ver}
Release: %{rel}
Group: System/Libraries
License: GPL
Url: http://dvd.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/dvd/%{name}-%{version}.tar.bz2
# (fc) 0.1.10-2mdk fix crash with DVD without first play chain (CVS)
Patch0: libdvdnav-0.1.10-fixdvdcrash.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n %libname
Summary: DVD Navigation library
Group: System/Libraries

%description -n %libname
libdvdnav provides support to applications wishing to make use of advanced
DVD features.

%package -n %libname-devel
Summary: DVD Navigation library headers and support files
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname-devel
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%multiarch_binaries %buildroot%_bindir/dvdnav-config
%clean
rm -r $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig 
%postun -n %libname -p /sbin/ldconfig 

%files -n %libname
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/libdvdnav*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%doc COPYING NEWS TODO AUTHORS
%{_bindir}/dvdnav-config
%{_bindir}/*/dvdnav-config
%{_libdir}/libdvdnav*.la
%{_libdir}/libdvdnav*.so
%{_includedir}/dvdnav/
%_datadir/aclocal/dvdnav.m4


