%define major	1
%define libname	%mklibname matekeyring %{major}
%define devname	%mklibname -d matekeyring

Summary:	Keyring library for the GNOME desktop
Name:		libmatekeyring
Version:	1.2.0
Release:	1
License:	LGPLv2+
Group:		Networking/Remote access
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)

%description
matekeyring is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.
 
The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package lang
Group:		System/Libraries
Summary:	Localization data files for %{name}

%description lang
This package contains the translations for %{name}.

%package -n %{libname}
Summary:	Library for integration with the gnome keyring system
Group:		System/Libraries
Suggests:	%{name}-lang >= %{version}

%description -n %{libname}
The library libmatekeyring is used by applications to integrate with
the gnome keyring system. However, at this point the library hasn't been
tested and used enought to consider the API to be publically
exposed. Therefore use of libmatekeyring is at the moment limited to
internal use in the gnome desktop. However, we hope that the
matekeyring API will turn out useful and good, so that later it
can be made public for any application to use.

%package -n %{devname}
Group:		Development/C
Summary:	Library for integration with the gnome keyring system
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files lang -f %{name}.lang

%files -n %{libname}
%{_libdir}/libmate-keyring.so.%{major}*

%files -n %{devname}
%doc ChangeLog README NEWS
%dir %{_includedir}/mate-keyring-1/
%{_includedir}/mate-keyring-1/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_datadir}/gtk-doc/html/mate-keyring

