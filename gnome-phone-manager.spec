%define name	gnome-phone-manager
%define version	0.51
%define release %mkrel 1
%define schemas gnome-phone-manager

Name: 	 	%{name}
Summary: 	GNOME Cellular Phone Manager
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%version/%{name}-%{version}.tar.bz2
URL:		http://live.gnome.org/PhoneManager
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gettext intltool ImageMagick
BuildRequires:	libbtctl-devel >= 0.6
BuildRequires:	libgnomebt-devel
BuildRequires:	libgnokii-devel gnokii
BuildRequires:	libglade2.0-devel libgnomeui2-devel
BuildRequires:	librsvg-devel
BuildRequires:  GConf2
BuildRequires:	libevolution-data-server-devel
BuildRequires:	desktop-file-utils
BuildRequires:	automake
BuildRequires:  gstreamer0.10-devel
BuildRequires:	gtkspell-devel
Requires:	pygtk2.0-libglade

%description
Phone Manager is a program created to allow you to control aspects of your
mobile phone from your GNOME 2 desktop. It is free software, licensed under
the GPL.

The software is in its early stages right now. Current features include:
    * Runs in the background; indicates status on the panel notification area.
    * Display on-screen alert when text message (SMS) arrives
    * Text message (SMS) sending facility

Features planned in the near future include:
    * Addressbook integration
    * Call monitoring and dialing
    * Send cluepackets to Dashboard about incoming messages

Phone Manager supports any mobile phone that can connect to your computer as
a serial port: via Bluetooth, IrDA or a serial cable.

%prep
%setup -q

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

%post
%update_menus
%update_icon_cache hicolor
%post_install_gconf_schemas %{schemas}

%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
