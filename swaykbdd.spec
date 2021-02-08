Name:		swaykbdd
Version:	1.0
Release:	1
Summary:	Screen locker for Wayland

License:	MIT
URL:		https://github.com/swaywm/swaylock
Source0:	https://github.com/artemsen/swaykbdd/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.48.0

%description
Swaykbdd: per-window keyboard layout for Sway

%prep
%autosetup

%build
%meson -D%{name}-version=%{version}
%meson_build

%install
%meson_install

%files
%{_bindir}/swaykbdd
%{_mandir}/man1/*
