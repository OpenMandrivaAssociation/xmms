%define	name	xmms
%define	version 1.2.11
%define release	%mkrel 4
%define	fname	%{name}-%{version}

%define additional_effect_plugin_a sox-effect-0.0.1
%define additional_misc_plugin_a xmms-shell-0.99.3
%define major 1
%define libname %mklibname xmms %{major}
%define develname %mklibname -d xmms

# Define arches where we build the Mesa3d capable plugin
%define mesa_arches %{ix86} ppc sparc x86_64

Name:		%{name}
Summary:	The Sound player with the WinAmp GUI
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sound
URL:		http://www.xmms.org/
Source0:	http://www.xmms.org/files/1.2.x/%{fname}.tar.bz2
Source4:	%{name}-icons.tar.bz2
Source10:	%{name}.16.png
Source11:	%{name}.32.png
Source12:	%{name}.48.png
Source50:	http://staff.xmms.org/zinx/xmms/%{additional_effect_plugin_a}.tar.bz2
Source51:	http://xmms-shell.sourceforge.net/%{additional_misc_plugin_a}.tar.bz2
Source100:	xmms-logo.xpm
Patch:		xmms-1.2.11-remove-libtool-from-acinclude.patch
Patch3:		xmms-1.2.4-latin1.patch
Patch4:		xmms-1.2.11-audio.patch
Patch7:		xmms-shell-0.99.3-fix-missing-ncurses.patch
Patch8:		xmms-1.2.7-sox-fix-bootstrap.patch
Patch9:		xmms-shell-0.99.3-fix-bootstrap.patch
Patch10:	xmms-fix-smallfiles.patch
Patch12:	xmms-fix-textbox.patch
Patch15:	xmms-1.2.11-do-not-override-our-flags.patch
Patch16:	xmms-1.2.4-sox-do-not-override-our-flags.patch
Patch18:	xmms-1.2.11-fix-http-title-mpg123.patch
Patch20:	xmms-shell-0.99.3-empty-playlist.patch
Patch22:	xmms-shell-0.99.3-g++-3.3-build.patch
Patch23:	xmms-shell-0.99.3-configure-fix.patch
Patch25:	xmms-1.2.10-cvs-fix-alsa-unpause.patch
Patch27:	xmms-1.2.11-recode-id3.patch
Patch32:	xmms-1.2.10-sox_effect-gcc4.patch
Patch33:	xmms-shell-0.99.3-gcc4.3.patch
# 3dse patch by Cornelis Frank <Frank.Cornelis@rug.ac.be>, web http://studwww.rug.ac.be/~fcorneli/xmms/, license GPL
Patch50:	 xmms-1.2.11-3dse.patch
# rediffed from this mail:
# http://lists.xmms.org/pipermail/xmms-devel/2002-January/002282.html
Patch60:	xmms-1.2.11-ab.patch
Patch100:	xmms-1.2.11-rva.patch
Patch104:	xmms-1.2.10-fonts.patch
Patch106:	xmms-1.2.10-ipv6.patch
Patch107:	xmms-1.2.10-ipv6-address.patch
Patch108:	xmms-1.2.11-ipv6-merge.patch
Patch109:	xmms-1.2.10-crossfade-0.3.9.patch
# #29976, CVE-2007-0653,0654
Patch111:	xmms-1.2.11-CVE-2007-0653.0654.patch
BuildRequires:	ORBit-devel
BuildRequires:	automake1.4
BuildRequires:	automake1.7
BuildRequires:	db1-devel
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	libgtk+-devel
BuildRequires:	libtool
BuildRequires:	libsm-devel
BuildRequires:	libxml-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	readline-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires:	soundwrapper

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp GUI, it
can use WinAmp skins, and play mp3s, mods, s3ms, and other formats. It now has
support for input, output, and general plugins, and has also been GPLd.

This package also provides an effect plugin based on Sox and a shell for xmms
in order to command the running xmms from any script/commandline.


%package -n	%{libname}
Summary:	Library associated with xmms, needed for xmms and its plugins
Group:		System/Libraries

%description -n	%{libname}
This library is mandatory for xmms and for all its plugins to run.

%package -n	%develname
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libxmms-devel = %{version}-%{release} 
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: %mklibname -d xmms 1

%description -n	%develname
Static libraries and header files required for compiling xmms plugins.

%package	esd
Summary:	ESound output backend
Group:		Sound
BuildRequires:	esound-devel
Requires:	%{name} = %{version}-%{release}
Requires:	esound >= 0.2.14

%description	esd
Output plugin for xmms for use with the esound package

%package	alsa
Summary:	ALSA output backend
Group:		Sound
BuildRequires:	alsa-lib-devel
Requires:	%{name} = %{version}-%{release}

%description	alsa
Output plugin for xmms for use with the ALSA drivers

%package	diskwriter
Summary:	DiskWriter output backend
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	diskwriter
Output plugin for xmms in order to output *.wav files instead of playing
sound on the soundcard.


%package	mikmod
Summary:	Sound player with the WinAmp GUI, Mikmod output backend
Group:		Sound
BuildRequires:	libmikmod-devel
Requires:	%{name} = %{version}-%{release}
Requires:	libmikmod >= 3.1.6

%description	mikmod
Input plugin for XMMS to play MODs (.MOD,.XM,.S3M, etc)

%package	mesa
Summary:	Visualization plugins that use the Mesa3d library
Group:		Sound
Requires:	%{name} = %{version}-%{release}
BuildRequires:	mesagl-devel

%description	mesa
3D Visualization plugins for XMMS that use the Mesa3d library.

%prep

%setup -q -n %{fname} -a 50 -a 51
%patch -p1
%patch3 -p0
%patch4 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1
%patch12 -p1
%patch15 -p1
%patch16 -p0
%patch18 -p1
%patch20 -p0
%patch22 -p0
%patch23 -p0 -b .no-system-xmms-devel
#%patch25 -p0 -b .alsa-unpause
%patch27 -p1 -b .recode
%patch32 -p0 -b .gcc4
%ifnarch sparc ppc
%patch50 -p1 -b .3dse
%endif
%patch33 -p0

# rediffed from this mail:
# http://lists.xmms.org/pipermail/xmms-devel/2002-January/002282.html
%patch60 -p1 -b .ab

%patch100 -p1 -b .rva
%patch104 -p1 -b .fonts
%patch106 -p0 -b .ipv6
%patch107 -p0 -b .ipv6addr
%patch108 -p1 -b .ipv6merge
%patch109 -p1 -b .crossfade
%patch111 -p1 -b .CVE-2007-0653.0654

export WANT_AUTOCONF_2_5="1"
rm -f configure
libtoolize --copy --force; aclocal; autoconf --force; automake --add-missing --copy

pushd %{additional_effect_plugin_a}
  # (blino) @PTHREAD_LIBS@ has never worked here, it was magically ignored by old libtool
  #         pthread libraries are already present in the gtk linking options
  perl -pi -e 's/\s*\@PTHREAD_LIBS\@//' src/Makefile.*
popd

%build

%configure2_5x \
%ifarch %ix86
    --enable-simd \
%endif
%ifarch sparc sparcv8 sparcv9 sparc64
    --disable-oss \
%endif
    --disable-rpath 

%make EGREP=egrep

# (pablo) the po files are in oncorrect format; this is needed to compile them
export OLD_PO_FILE_INPUT=1

# (pablo) withouth the --escape parameter xgettext fails as there are
# non-ascii chars in the msgid entries
export XGETTEXT="/usr/bin/xgettext --escape"

# (oe) from now on and down use this common compiler flag
export CFLAGS="%{optflags} `glib-config --cflags` `gtk-config --cflags`"

# (gc) I want to grab the xmms-config built in .., for bootstrapping nicely
export PATH=.:$PATH

pushd %{additional_effect_plugin_a}
    rm -f configure
    libtoolize --install --force; aclocal-1.4; autoconf; automake-1.4 --add-missing --copy
    %configure2_5x
    %make
popd

pushd %{additional_misc_plugin_a}
    rm -f configure
    libtoolize --copy --force; aclocal-1.7; autoconf --force; automake-1.7 --add-missing --copy
    %configure2_5x
    %make
popd

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_libdir}/xmms/Effect
install -d %{buildroot}/%{_libdir}/xmms/General
install -d %{buildroot}/%{_libdir}/xmms/Input
install -d %{buildroot}/%{_libdir}/xmms/Output
install -d %{buildroot}/%{_libdir}/xmms/Visualization
install -d %{buildroot}/%{_datadir}/xmms/Skins
install -d %{buildroot}/%{_docdir}

%makeinstall_std EGREP=egrep

%multiarch_binaries %{buildroot}%{_bindir}/xmms-config

pushd %{additional_effect_plugin_a}
    %makeinstall libdir=%{buildroot}/%{_libdir}/xmms/Effect
popd

pushd %{additional_misc_plugin_a}
    %makeinstall PREFIX=%{buildroot}/%{_prefix}
popd

install -m644 %{SOURCE100} %{buildroot}/%{_datadir}/xmms/xmms.xpm

install -d %{buildroot}/%{_datadir}/mime-info
cat > %{buildroot}/%{_datadir}/mime-info/xmms.keys << EOF
audio/x-mp3:
	open=xmms %f
	view=xmms %f
EOF
chmod 644 %{buildroot}/%{_datadir}/mime-info/xmms.keys

install -d %{buildroot}/%{_datadir}/pixmaps
if [ ! -r %{buildroot}/%{_datadir}/pixmaps/xmms_logo.xpm ]; then
    cp %{SOURCE100} %{buildroot}/%{_datadir}/pixmaps/xmms.xpm
fi

#xdg menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xmms
Comment=Multimedia Player
Exec=soundwrapper xmms %U
Icon=%{name}
Terminal=false
Type=Application
MimeType=audio/x-mp3;audio/x-ogg;application/x-ogg;audio/x-mpegurl;audio/x-wav;audio/x-scpls;audio/mpegurl;audio/mp3;audio/mpeg;audio/x-mpeg;
StartupNotify=true
Categories=Audio;Player;X-MandrivaLinux-Multimedia-Audio;AudioVideo;
EOF

# Icons
install -d %{buildroot}/%{_miconsdir}
install -d %{buildroot}/%{_liconsdir}
install -m 644 %{SOURCE10} %{buildroot}/%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE11} %{buildroot}/%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE12} %{buildroot}/%{_liconsdir}/%{name}.png

# replaced with zh_??
rm -rf %{buildroot}/%{_datadir}/locale/zh_??.*

# RTL is not supported in gtk1
rm -rf %{buildroot}/%{_datadir}/locale/{ar,fa,he}
# complex scripts are not supported in gtk1
rm -rf %{buildroot}/%{_datadir}/locale/{bn,hi,ta}

# nuke unpackaged files
%ifnarch %{mesa_arches}
rm -f %{buildroot}%{_libdir}/xmms/Visualization/libogl_spectrum*
%endif	

%find_lang %{name}

rm -f %{buildroot}/%{_mandir}/*/gnomexmms.*
rm -rf %{buildroot}/%{_datadir}/pixmaps
rm -f %{buildroot}/%{_datadir}/mime-info/xmms.keys

rm -f %{buildroot}%{_libdir}/xmms/*/*.*a

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README FAQ README.MDK
%{_bindir}/xmms
%{_bindir}/wmxmms
%{_bindir}/xmms-shell
%dir %{_libdir}/xmms
%dir %{_libdir}/xmms/Input
%{_libdir}/xmms/Input/libcdaudio*
%{_libdir}/xmms/Input/libmpg123*
%{_libdir}/xmms/Input/libwav*
%{_libdir}/xmms/Input/libtonegen*
%{_libdir}/xmms/Input/libvorbis*
%dir %{_libdir}/xmms/Output
%ifnarch sparc sparcv8 sparcv9 sparc64
%{_libdir}/xmms/Output/libOSS*
%endif
%dir %{_libdir}/xmms/General
%{_libdir}/xmms/General/*
%dir %{_libdir}/xmms/Effect
%{_libdir}/xmms/Effect/*
%dir %{_libdir}/xmms/Visualization
%{_libdir}/xmms/Visualization/libbscope*
%{_libdir}/xmms/Visualization/libsanalyzer*
%dir %{_datadir}/xmms
%dir %{_datadir}/xmms/Skins
%{_datadir}/xmms/wmxmms.xpm
%{_datadir}/xmms/xmms.xpm
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%_datadir/applications/mandriva*
%{_mandir}/*/xmms.*
%{_mandir}/*/wmxmms.*
%{_mandir}/*/xmms-shell.*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libxmms.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc COPYING ChangeLog 
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_datadir}/aclocal/xmms.m4
%{_bindir}/xmms-config
%multiarch %{multiarch_bindir}/xmms-config

%files esd
%defattr(-, root, root)
%doc COPYING
%{_libdir}/xmms/Output/libesdout*

%files alsa
%defattr(-, root, root)
%doc COPYING
%{_libdir}/xmms/Output/libALSA.so

%files diskwriter
%defattr(-, root, root)
%doc COPYING
%{_libdir}/xmms/Output/libdisk_writer*


%files mikmod
%defattr(-, root, root)
%doc Input/mikmod/COPYING
%{_libdir}/xmms/Input/libmikmod*

%ifarch %{mesa_arches}
%files mesa
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xmms/Visualization/libogl_spectrum*
%endif


