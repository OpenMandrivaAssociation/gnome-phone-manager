%define name	gnome-phone-manager
%define version	0.8
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	GNOME Cellular Phone Manager
Version: 	%{version}
Release: 	%{release}

Source:		ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%version/%{name}-%{version}.tar.bz2
Patch0:		gnome-phone-manager-0.6-new-openobex.patch
# (fc) 0.7-1mdk fix icon location
Patch1:		gnome-phone-manager-0.7-fixicon.patch
# (fc) 0.7-3mdv fix build with eds 1.8 (gnome bug #349726)
Patch2:		gnome-phone-manager-0.7-eds18.patch
URL:		http://usefulinc.com/software/phonemgr/
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gettext intltool ImageMagick
BuildRequires:	libbtctl-devel >= 0.6
BuildRequires:	libgnomebt-devel
BuildRequires:	libgnokii-devel
BuildRequires:	libglade2.0-devel libgnomeui2-devel 
BuildRequires:	librsvg-devel
BuildRequires:  GConf2
BuildRequires:	libevolution-data-server-devel
BuildRequires:	desktop-file-utils
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
%patch0 -p1

#needed by patches 0 & 2
autoconf

%build
%configure2_5x --enable-shared --enable-static
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
mkdir -p $RPM_BUILD_ROOT/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
convert -size 48x48 ui/cellphone.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
convert -size 48x48 ui/cellphone.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%name.png
convert -size 32x32 ui/cellphone.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
convert -size 32x32 ui/cellphone.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%name.png
convert -size 16x16 ui/cellphone.png $RPM_BUILD_ROOT/%_miconsdir/%name.png
convert -size 16x16 ui/cellphone.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/16x16/apps/%name.png

mkdir -p %{buildroot}%{_datadir}/pixmaps/
mv %{buildroot}%{_datadir}/cellphone.png %{buildroot}%{_datadir}/pixmaps/cellphone.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
%update_icon_cache hicolor
		
%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/hicolor/*/apps/%name.png
%{_datadir}/pixmaps/*.png

