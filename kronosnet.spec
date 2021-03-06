#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kronosnet
Version  : 1.14
Release  : 1
URL      : https://github.com/kronosnet/kronosnet/archive/v1.14.tar.gz
Source0  : https://github.com/kronosnet/kronosnet/archive/v1.14.tar.gz
Summary  : library to manage a pool of tap devices
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kronosnet-lib = %{version}-%{release}
Requires: kronosnet-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : grep
BuildRequires : lksctp-tools-dev
BuildRequires : pkgconfig(bzip2)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : pkgconfig(libqb)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(lzo2)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : valgrind

%description
# Author: Fabio M. Di Nitto <fabbione@kronosnet.org>
# This software licensed under GPL-2.0+

%package dev
Summary: dev components for the kronosnet package.
Group: Development
Requires: kronosnet-lib = %{version}-%{release}
Provides: kronosnet-devel = %{version}-%{release}
Requires: kronosnet = %{version}-%{release}

%description dev
dev components for the kronosnet package.


%package doc
Summary: doc components for the kronosnet package.
Group: Documentation

%description doc
doc components for the kronosnet package.


%package lib
Summary: lib components for the kronosnet package.
Group: Libraries
Requires: kronosnet-license = %{version}-%{release}

%description lib
lib components for the kronosnet package.


%package license
Summary: license components for the kronosnet package.
Group: Default

%description license
license components for the kronosnet package.


%prep
%setup -q -n kronosnet-1.14
cd %{_builddir}/kronosnet-1.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582659432
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1582659432
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kronosnet
cp %{_builddir}/kronosnet-1.14/COPYING.applications %{buildroot}/usr/share/package-licenses/kronosnet/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/kronosnet-1.14/COPYING.libraries %{buildroot}/usr/share/package-licenses/kronosnet/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/kronosnet-1.14/README.licence %{buildroot}/usr/share/package-licenses/kronosnet/6d692c4881e8e1e49c2630c309396cdff577b12b
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libknet.h
/usr/include/libnozzle.h
/usr/lib64/libknet.so
/usr/lib64/libnozzle.so
/usr/lib64/pkgconfig/libknet.pc
/usr/lib64/pkgconfig/libnozzle.pc
/usr/share/man/man3/knet_addrtostr.3
/usr/share/man/man3/knet_get_compress_list.3
/usr/share/man/man3/knet_get_crypto_list.3
/usr/share/man/man3/knet_get_transport_id_by_name.3
/usr/share/man/man3/knet_get_transport_list.3
/usr/share/man/man3/knet_get_transport_name_by_id.3
/usr/share/man/man3/knet_handle_add_datafd.3
/usr/share/man/man3/knet_handle_clear_stats.3
/usr/share/man/man3/knet_handle_compress.3
/usr/share/man/man3/knet_handle_crypto.3
/usr/share/man/man3/knet_handle_enable_access_lists.3
/usr/share/man/man3/knet_handle_enable_filter.3
/usr/share/man/man3/knet_handle_enable_pmtud_notify.3
/usr/share/man/man3/knet_handle_enable_sock_notify.3
/usr/share/man/man3/knet_handle_free.3
/usr/share/man/man3/knet_handle_get_channel.3
/usr/share/man/man3/knet_handle_get_datafd.3
/usr/share/man/man3/knet_handle_get_stats.3
/usr/share/man/man3/knet_handle_get_transport_reconnect_interval.3
/usr/share/man/man3/knet_handle_new.3
/usr/share/man/man3/knet_handle_new_ex.3
/usr/share/man/man3/knet_handle_pmtud_get.3
/usr/share/man/man3/knet_handle_pmtud_getfreq.3
/usr/share/man/man3/knet_handle_pmtud_set.3
/usr/share/man/man3/knet_handle_pmtud_setfreq.3
/usr/share/man/man3/knet_handle_remove_datafd.3
/usr/share/man/man3/knet_handle_set_transport_reconnect_interval.3
/usr/share/man/man3/knet_handle_setfwd.3
/usr/share/man/man3/knet_host_add.3
/usr/share/man/man3/knet_host_enable_status_change_notify.3
/usr/share/man/man3/knet_host_get_host_list.3
/usr/share/man/man3/knet_host_get_id_by_host_name.3
/usr/share/man/man3/knet_host_get_name_by_host_id.3
/usr/share/man/man3/knet_host_get_policy.3
/usr/share/man/man3/knet_host_get_status.3
/usr/share/man/man3/knet_host_remove.3
/usr/share/man/man3/knet_host_set_name.3
/usr/share/man/man3/knet_host_set_policy.3
/usr/share/man/man3/knet_link_add_acl.3
/usr/share/man/man3/knet_link_clear_acl.3
/usr/share/man/man3/knet_link_clear_config.3
/usr/share/man/man3/knet_link_get_config.3
/usr/share/man/man3/knet_link_get_enable.3
/usr/share/man/man3/knet_link_get_link_list.3
/usr/share/man/man3/knet_link_get_ping_timers.3
/usr/share/man/man3/knet_link_get_pong_count.3
/usr/share/man/man3/knet_link_get_priority.3
/usr/share/man/man3/knet_link_get_status.3
/usr/share/man/man3/knet_link_insert_acl.3
/usr/share/man/man3/knet_link_rm_acl.3
/usr/share/man/man3/knet_link_set_config.3
/usr/share/man/man3/knet_link_set_enable.3
/usr/share/man/man3/knet_link_set_ping_timers.3
/usr/share/man/man3/knet_link_set_pong_count.3
/usr/share/man/man3/knet_link_set_priority.3
/usr/share/man/man3/knet_log_get_loglevel.3
/usr/share/man/man3/knet_log_get_loglevel_id.3
/usr/share/man/man3/knet_log_get_loglevel_name.3
/usr/share/man/man3/knet_log_get_subsystem_id.3
/usr/share/man/man3/knet_log_get_subsystem_name.3
/usr/share/man/man3/knet_log_set_loglevel.3
/usr/share/man/man3/knet_recv.3
/usr/share/man/man3/knet_send.3
/usr/share/man/man3/knet_send_sync.3
/usr/share/man/man3/knet_strtoaddr.3
/usr/share/man/man3/nozzle_add_ip.3
/usr/share/man/man3/nozzle_close.3
/usr/share/man/man3/nozzle_del_ip.3
/usr/share/man/man3/nozzle_get_fd.3
/usr/share/man/man3/nozzle_get_handle_by_name.3
/usr/share/man/man3/nozzle_get_ips.3
/usr/share/man/man3/nozzle_get_mac.3
/usr/share/man/man3/nozzle_get_mtu.3
/usr/share/man/man3/nozzle_get_name_by_handle.3
/usr/share/man/man3/nozzle_open.3
/usr/share/man/man3/nozzle_reset_mac.3
/usr/share/man/man3/nozzle_reset_mtu.3
/usr/share/man/man3/nozzle_run_updown.3
/usr/share/man/man3/nozzle_set_down.3
/usr/share/man/man3/nozzle_set_mac.3
/usr/share/man/man3/nozzle_set_mtu.3
/usr/share/man/man3/nozzle_set_up.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/kronosnet/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/kronosnet/compress_bzip2.so
/usr/lib64/kronosnet/compress_lz4.so
/usr/lib64/kronosnet/compress_lz4hc.so
/usr/lib64/kronosnet/compress_lzma.so
/usr/lib64/kronosnet/compress_lzo2.so
/usr/lib64/kronosnet/compress_zlib.so
/usr/lib64/kronosnet/compress_zstd.so
/usr/lib64/kronosnet/crypto_nss.so
/usr/lib64/kronosnet/crypto_openssl.so
/usr/lib64/libknet.so.1
/usr/lib64/libknet.so.1.3.0
/usr/lib64/libnozzle.so.1
/usr/lib64/libnozzle.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kronosnet/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kronosnet/6d692c4881e8e1e49c2630c309396cdff577b12b
/usr/share/package-licenses/kronosnet/9a1929f4700d2407c70b507b3b2aaf6226a9543c
