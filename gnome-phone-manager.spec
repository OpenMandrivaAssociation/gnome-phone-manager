Summary: 	GNOME Cellular Phone Manager
Name: 	 	gnome-phone-manager
Version: 	0.69
Release: 	15
License:	GPLv2+
Group:		Communications
Url:		https://live.gnome.org/PhoneManager
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%{version}/%{name}-%{version}.tar.xz
Patch0:		gnome-phone-manager-0.68-eds.patch
Patch1:		gnome-phone-manager-automake-1.13.patch
Patch2:		gnome-phone-manager-0.69-adwaita-icon-theme.patch
Patch3:		gnome-phone-manager-0.69-drop-plugin.patch

BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0) >= 2.25.0
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnokii) >= 0.6.28
BuildRequires:	pkgconfig(gnome-bluetooth-1.0) >= 3.0
BuildRequires:	pkgconfig(adwaita-icon-theme) >= 2.19.1
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	GConf2
%description
Phone Manager allows you to control aspects of your mobile phone from the
GNOME desktop.

Current features include:
    * Runs in the background; indicates status on the panel notification area.
    * Display on-screen alert when text message (SMS) arrives
    * Text message (SMS) sending facility
    * Evolution Addressbook integration when sending messages 

Phone Manager supports any mobile phone that can connect to your computer as a
serial port: via Bluetooth, IrDA, or a serial cable.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure \
	--enable-shared \
	--enable-compile-warnings=no \
	--enable-cxx-warnings=no
%make_build

%install
%make_install

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_libexecdir}/telepathy-phoney
%{_libdir}/gnome-bluetooth/plugins/libphonemgr.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%{_datadir}/telepathy/managers/phoney.manager
%{_datadir}/%{name}
%{_mandir}/man1/*

