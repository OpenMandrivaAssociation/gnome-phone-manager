%define schemas gnome-phone-manager

Name: 	 	gnome-phone-manager
Summary: 	GNOME Cellular Phone Manager
Version: 	0.68
Release: 	1
License:	GPLv2+
Group:		Communications
URL:		http://live.gnome.org/PhoneManager
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%{version}/%{name}-%{version}.tar.xz
# already upstream
Patch0:		gnome-phone-manager-0.68_bluetooth3.3api.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnokii) gnokii
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-icon-theme)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libbtctl)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(libcanberra-gtk3)

%description
Phone Manager allows you to control aspects of your mobile phone from the
GNOME 2 desktop.

Current features include:
    * Runs in the background; indicates status on the panel notification area.
    * Display on-screen alert when text message (SMS) arrives
    * Text message (SMS) sending facility
    * Evolution Addressbook integration when sending messages 

Phone Manager supports any mobile phone that can connect to your computer as a
serial port: via Bluetooth, IrDA, or a serial cable.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-shared \
	--enable-static

%make LIBS='-lgthread-2.0'

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="GTK" \
	--add-category="GNOME" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}
rm -fv %{buildroot}%{_libdir}/gnome-bluetooth/plugins/libphonemgr.a

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_libexecdir}/telepathy-phoney
%{_libdir}/gnome-bluetooth/plugins/libphonemgr.*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%{_datadir}/telepathy/managers/phoney.manager
%{_mandir}/man1/*

