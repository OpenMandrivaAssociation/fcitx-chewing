%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-chewing
Version:	0.2.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release:	2
Source0: http://download.fcitx-im.org/fcitx-chewing/%{name}-%{version}.tar.xz
%else
Release:	2
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release:	2
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release:	2
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Chewing/Qooing (Chinese IM) plugin for fcitx
URL: https://www.fcitx-im.org
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(chewing)

%description
Chewing/Qooing (Chinese IM) plugin for fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/fcitx-chewing.so
%_datadir/fcitx/addon/fcitx-chewing.conf
%_datadir/fcitx/configdesc/fcitx-chewing.desc
%_datadir/fcitx/imicon/chewing.png
%_datadir/fcitx/inputmethod/chewing.conf
%_datadir/fcitx/skin/classic/chewing.png
%_datadir/fcitx/skin/dark/chewing.png
%_datadir/fcitx/skin/default/chewing.png
%_iconsdir/hicolor/48x48/apps/fcitx-chewing.png

