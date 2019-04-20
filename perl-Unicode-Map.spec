#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Unicode-Map
Version  : 0.112
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHWARTZ/Unicode-Map-0.112.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHWARTZ/Unicode-Map-0.112.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libu/libunicode-map-perl/libunicode-map-perl_0.112-12.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Unicode-Map-bin = %{version}-%{release}
Requires: perl-Unicode-Map-lib = %{version}-%{release}
Requires: perl-Unicode-Map-license = %{version}-%{release}
Requires: perl-Unicode-Map-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Hi,
Welcome to Unicode::Map version 0.112.
This release adds mappings for EUC-JP and EUC-KR.

%package bin
Summary: bin components for the perl-Unicode-Map package.
Group: Binaries
Requires: perl-Unicode-Map-license = %{version}-%{release}
Requires: perl-Unicode-Map-man = %{version}-%{release}

%description bin
bin components for the perl-Unicode-Map package.


%package dev
Summary: dev components for the perl-Unicode-Map package.
Group: Development
Requires: perl-Unicode-Map-lib = %{version}-%{release}
Requires: perl-Unicode-Map-bin = %{version}-%{release}
Provides: perl-Unicode-Map-devel = %{version}-%{release}

%description dev
dev components for the perl-Unicode-Map package.


%package lib
Summary: lib components for the perl-Unicode-Map package.
Group: Libraries
Requires: perl-Unicode-Map-license = %{version}-%{release}

%description lib
lib components for the perl-Unicode-Map package.


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


%prep
%setup -q -n Unicode-Map-0.112
cd ..
%setup -q -T -D -n Unicode-Map-0.112 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Unicode-Map-0.112/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Unicode-Map
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Unicode-Map/COPYING
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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ADOBE/STDENC.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ADOBE/SYMBOL.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ADOBE/ZDINGBAT.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/ARABIC.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/CENTEURO.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/CHINSIMP.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/CHINTRAD.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/CROATIAN.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/CYRILLIC.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/DEVANAGA.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/DINGBATS.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/GREEK.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/GUJARATI.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/GURMUKHI.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/HEBREW.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/ICELAND.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/JAPANESE.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/KOREAN.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/ROMAN.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/ROMANIAN.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/SYMBOL.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/THAI.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/APPLE/TURKISH.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/BIG5.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/CNS-11643-1986.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/EUC-JP.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/EUC-KR.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/GB12345-80.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/GB2312-80.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/GB2312.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/JIS-X-0201.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/JIS-X-0208.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/JIS-X-0212.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/JOHAB.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/KSC1001.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/KSC5601-1992.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/EASTASIA/SHIFTJIS.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/IBM/IBM038.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-1.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-10.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-13.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-14.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-15.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-2.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-3.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-4.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-5.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-6.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-7.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-8.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/8859-9.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/ISO/ISO646-US.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP437.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP737.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP775.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP850.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP852.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP855.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP857.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP860.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP861.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP862.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP863.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP864.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP865.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP866.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP869.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/DOS/CP874.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/EBCDIC/CP037.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/EBCDIC/CP1026.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/EBCDIC/CP500.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/EBCDIC/CP875.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/CYRILLIC.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/GREEK.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/ICELAND.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/LATIN2.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/ROMAN.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/MAC/TURKISH.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1250.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1251.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1252.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1253.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1254.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1255.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1256.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1257.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP1258.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP932.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP936.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP949.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/MS/WIN/CP950.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/NEXT/NEXTSTEP.map
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Unicode/Map/REGISTRY

%files bin
%defattr(-,root,root,-)
/usr/bin/map
/usr/bin/mirrorMappings
/usr/bin/mkCSGB2312
/usr/bin/mkmapfile

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Unicode::Map.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Unicode/Map/Map.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Unicode-Map/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/map.1
/usr/share/man/man1/mkmapfile.1
