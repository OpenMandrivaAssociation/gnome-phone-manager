%define name	gnome-phone-manager
%define version	0.65
%define release %mkrel 1
%define schemas gnome-phone-manager

Name: 	 	%{name}
Summary: 	GNOME Cellular Phone Manager
Version: 	%{version}
Release: 	%{release}
Source:		ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%version/%{name}-%{version}.tar.bz2
Patch:		gnome-phone-manager-0.65-format-strings.patch
URL:		http://live.gnome.org/PhoneManager
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gettext intltool imagemagick
BuildRequires:	libbtctl-devel >= 0.6
BuildRequires:	gnome-bluetooth-devel
BuildRequires:	libgnokii-devel gnokii
BuildRequires:	libglade2.0-devel
BuildRequires:	librsvg-devel
BuildRequires:  libGConf2-devel
BuildRequires:	libevolution-data-server-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	automake
BuildRequires:	gtkspell-devel
BuildRequires:  libtelepathy-glib-devel
BuildRequires:  libcanberra-devel

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
%patch -p1

%build
%configure2_5x --enable-shared --enable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%post_install_gconf_schemas %{schemas}
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%_libexecdir/telepathy-phoney
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%_datadir/telepathy/managers/phoney.manager
