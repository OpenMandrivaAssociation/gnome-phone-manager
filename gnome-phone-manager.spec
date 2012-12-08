Name: 	 	gnome-phone-manager
Summary: 	GNOME Cellular Phone Manager
Version: 	0.68
Release: 	%mkrel 3
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%version/%{name}-%{version}.tar.xz
Patch0:		gnome-phone-manager-0.68-eds.patch
URL:		http://live.gnome.org/PhoneManager
License:	GPLv2+
Group:		Communications/Mobile
BuildRequires:	intltool >= 0.35.0
BuildRequires:	GConf2
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.25.0
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnokii) >= 0.6.28
BuildRequires:	pkgconfig(gnome-bluetooth-1.0) >= 3.0
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.19.1
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(telepathy-glib)

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
%patch0 -p1

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --enable-shared --disable-static
%make

%install
%makeinstall_std

%find_lang %name

find %{buildroot} -name '*.la' -delete

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%_libexecdir/telepathy-phoney
%_libdir/gnome-bluetooth/plugins/libphonemgr.so
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%_datadir/telepathy/managers/phoney.manager


%changelog

* Wed Oct 03 2012 malo <malo> 0.68-8.mga3
+ Revision: 302550
- update RPM group

* Thu Aug 30 2012 fwang <fwang> 0.68-7.mga3
+ Revision: 285812
- sync with fedora package to build with latest evo

* Thu Jan 19 2012 fwang <fwang> 0.68-7.mga2
+ Revision: 198054
- rebuild for new gnome-bluetooth

* Sat Dec 03 2011 fwang <fwang> 0.68-6.mga2
+ Revision: 175315
- rebuild for new gnokii

* Tue Nov 22 2011 fwang <fwang> 0.68-5.mga2
+ Revision: 170810
- adopt to gnome-bluetooth api change
- drop old symbol
- rebuild for new evo

* Sat Oct 29 2011 fwang <fwang> 0.68-4.mga2
+ Revision: 159501
- rebuild for new evo

* Mon Oct 17 2011 fwang <fwang> 0.68-3.mga2
+ Revision: 155645
- drop .la files

* Mon Oct 17 2011 fwang <fwang> 0.68-2.mga2
+ Revision: 155626
- add post script
- imported package gnome-phone-manager

