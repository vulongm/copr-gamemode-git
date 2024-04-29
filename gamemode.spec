%global commit a2fe0108b59948ed861ccc087aa91af9273b036f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240327
%global tag 1.8.1

Name:       gamemode
Version:    %{tag}^%{git_date}.git%{shortcommit}
Release:    %autorelease
Summary:    Optimize system performance for games on demand
License:    BSD
URL:        https://github.com/FeralInteractive/gamemode
Source0:    %{url}/archive/%{commit}.tar.gz

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(inih) >= 49
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimizations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU "powersave" or "ondemand" governors, but is
now host to a range of optimisation features and configurations, like
tweaking various settings: the CPU govenor, the I/O priority, the
kernel scheduler, the GPU performance mode and gpu overclocking
(NVIDIA). It can also excute custom scripts when launching games.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson -Ddefault_library=both
%meson_build

%check
%meson_test

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc     README.md
%{_bindir}/gamemoded
%{_bindir}/gamemodelist
%{_bindir}/gamemoderun
%{_bindir}/gamemode-simulate-game
%{_libexecdir}/cpucorectl
%{_libexecdir}/cpugovctl
%{_libexecdir}/gpuclockctl
%{_libexecdir}/procsysctl
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/polkit-1/rules.d/gamemode.rules
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_datadir}/gamemode/gamemode.ini
%{_libdir}/libgamemode*.so.*
%{_libdir}/libgamemode*.so
%{_sysconfdir}/security/limits.d/10-gamemode.conf
%{_prefix}/lib/sysusers.d/gamemode.conf
%{_userunitdir}/gamemoded.service
%{_mandir}/man8/gamemoded.8*
%{_mandir}/man1/gamemoderun.1*
%{_mandir}/man1/gamemodelist.1*
%{_mandir}/man1/gamemode-simulate-game.1*
%{_metainfodir}/io.github.feralinteractive.gamemode.metainfo.xml

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/libgamemodeauto.a
%{_libdir}/pkgconfig/gamemode*.pc
%{_libdir}/pkgconfig/libgamemodeauto.pc

%changelog
%autochangelog
