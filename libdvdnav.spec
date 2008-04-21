%define major 4
%define libname %mklibname dvdnav %{major}
%define develname %mklibname dvdnav -d

Name:		libdvdnav
Summary:	DVD Navigation library
Version:	4.1.2
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.mplayerhq.hu
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libdvdread-devel

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

%build
./configure2 --prefix=%_prefix --libdir=%_libdir
make
./configure2 --prefix=%_prefix --libdir=%_libdir --with-dvdread=%_includedir/dvdread
make

%install
rm -rf %{buildroot}
%makeinstall_std
#gw remove buildroot
perl -pi -e "s^%buildroot^^" %buildroot%_bindir/dvdnav-config
%multiarch_binaries %{buildroot}%{_bindir}/dvdnav-config
%if %_lib != lib
mv %buildroot%_prefix/lib/lib* %buildroot%_libdir/
%endif

%post -n %{libname} -p /sbin/ldconfig 

%postun -n %{libname} -p /sbin/ldconfig 

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
%{_bindir}/*/dvdnav-config
%{_libdir}/libdvdnavmini.so
%{_libdir}/libdvdnav.so
%{_libdir}/libdvdnav.a
%{_includedir}/dvdnav/
