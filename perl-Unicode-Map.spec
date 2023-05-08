#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Unicode-Map
Version  : 0.112
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHWARTZ/Unicode-Map-0.112.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHWARTZ/Unicode-Map-0.112.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libu/libunicode-map-perl/libunicode-map-perl_0.112-12.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Unicode-Map-bin = %{version}-%{release}
Requires: perl-Unicode-Map-license = %{version}-%{release}
Requires: perl-Unicode-Map-man = %{version}-%{release}
Requires: perl-Unicode-Map-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Hi,
Welcome to Unicode::Map version 0.112.
This release adds mappings for EUC-JP and EUC-KR.

%package bin
Summary: bin components for the perl-Unicode-Map package.
Group: Binaries
Requires: perl-Unicode-Map-license = %{version}-%{release}

%description bin
bin components for the perl-Unicode-Map package.


%package dev
Summary: dev components for the perl-Unicode-Map package.
Group: Development
Requires: perl-Unicode-Map-bin = %{version}-%{release}
Provides: perl-Unicode-Map-devel = %{version}-%{release}
Requires: perl-Unicode-Map = %{version}-%{release}

%description dev
dev components for the perl-Unicode-Map package.


%package license
Summary: license components for the perl-Unicode-Map package.
Group: Default

%description license
license components for the perl-Unicode-Map package.


%package man
Summary: man components for the perl-Unicode-Map package.
Group: Default

%description man
man components for the perl-Unicode-Map package.


%package perl
Summary: perl components for the perl-Unicode-Map package.
Group: Default
Requires: perl-Unicode-Map = %{version}-%{release}

%description perl
perl components for the perl-Unicode-Map package.


%prep
%setup -q -n Unicode-Map-0.112
cd %{_builddir}
tar xf %{_sourcedir}/libunicode-map-perl_0.112-12.debian.tar.xz
cd %{_builddir}/Unicode-Map-0.112
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Unicode-Map-0.112/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Unicode-Map
cp %{_builddir}/Unicode-Map-0.112/COPYING %{buildroot}/usr/share/package-licenses/perl-Unicode-Map/7f377e336b0bbe851872dc6ae312a1a39607cbe6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/map
/usr/bin/mirrorMappings
/usr/bin/mkCSGB2312
/usr/bin/mkmapfile

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Unicode::Map.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Unicode-Map/7f377e336b0bbe851872dc6ae312a1a39607cbe6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/map.1
/usr/share/man/man1/mkmapfile.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
