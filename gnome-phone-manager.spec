%define schemas gnome-phone-manager

Name: 	 	gnome-phone-manager
Summary: 	GNOME Cellular Phone Manager
Version: 	0.68
Release: 	1
License:	GPLv2+
Group:		Communications
URL:		http://live.gnome.org/PhoneManager
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%{version}/%{name}-%{version}.tar.xz
Patch0:		gnome-phone-manager-0.65-format-strings.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  gnome-icon-theme
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	libbtctl-devel >= 0.6
BuildRequires:	gnome-bluetooth-devel
BuildRequires:	libgnokii-devel gnokii
BuildRequires:	libglade2.0-devel
BuildRequires:	librsvg-devel
BuildRequires:  libGConf2-devel
BuildRequires:	libevolution-data-server-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtkspell-devel
BuildRequires:  libtelepathy-glib-devel
%if %mdvver >= 201100
BuildRequires:  libcanberra-gtk-devel
%else
BuildRequires:  libcanberra-devel
%endif

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

%build
%configure2_5x \
	--enable-shared \
	--enable-static
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="GTK" \
	--add-category="GNOME" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %name
rm -fv %{buildroot}%{_libdir}/gnome-bluetooth/plugins/libphonemgr.a

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_libexecdir}/telepathy-phoney
%{_libdir}/gnome-bluetooth/plugins/libphonemgr.*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%{_datadir}/telepathy/managers/phoney.manager
%{_mandir}/man1/*

