%define _unpackaged_files_terminate_build 1

Name: dropwatch
Version: 1.2
Release: alt1
Summary: Dropwatch is a project I started in an effort to improve the ability for developers and system administrators to diagnose problems in the Linux Networking stack.
License: GPLv2+
Group: Other
URL: https://github.com/radiobanka/dropwatch

Requires: libnl, readline

Source0: %name-%version.tar

#BuildRequires: autoconf, automake, libtool
BuildRequires: kernel-devel, libnl-devel, readline-devel, libreadline-devel-static, libreadline-devel, libpcap-devel
BuildRequires: binutils-devel, binutils, pkgconfig

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%setup -q

%build
autoreconf -vi
%configure
%make_build

%install
%makeinstall

%files
%_defattr
%{_bindir}/*
%{_mandir}/man1/*
%doc README.md
%doc COPYING

%changelog
* Fri May 06 2023 Menshchikov Evgeniy <menshchikovev@altlinux.org> 1.2-alt1
- Assembly package for ALT

* Thu Apr 08 2010 Neil Horman <nhorman@redhat.com> 1.1-0
- Fixing BuildRequires in spec, and removing release variable

* Thu Mar 26 2009 Neil Horman <nhorman@redhat.com> 1.0-3
- Updating Makefile to include release num in tarball

* Fri Mar 20 2009 Neil Horman <nhorman@redhat.com> 1.0-2
- Fixed up Errors found in package review (bz 491240)

* Tue Mar 17 2009 Neil Horman <nhorman@redhat.com> 1.0-1
- Initial build

