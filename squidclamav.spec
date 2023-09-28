Name:           squidclamav
Version:        7.2
Release:        3%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL-1.0-or-later
URL:            http://sourceforge.net/projects/%{name}/

Source0:        https://github.com/darold/%{name}/archive/v7.2.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Patch0:         https://github.com/darold/%{name}/commit/6c279b74a61507a6e2118cb8796f5647f4166ecd.patch

BuildRequires:  c-icap-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libarchive-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel

Requires:       squid
Requires:       c-icap

%description
SquidClamav is an antivirus for the Squid proxy based on the ICAP protocol and
the awards-winning ClamAv anti-virus toolkit. Using it will help you secure your
home or enterprise network web traffic. SquidClamav is the most efficient
antivirus tool for HTTP traffic available for free, it is written in C as a
c-icap service and can handle several thousands of connections at once.

%prep
%autosetup

%build
%configure \
  --disable-static \
  --enable-shared \
  --with-c-icap \
  --with-libarchive

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Let rpm pick up the docs in the files section
rm -rf %{buildroot}%{_datadir}/%{name}

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default

%files
%doc AUTHORS ChangeLog README
%license COPYING
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_libdir}/c_icap/*.so
%{_libexecdir}/%{name}/clwarn.cgi
%{_datadir}/c_icap/templates/squidclamav/*
%{_libexecdir}/%{name}/clwarn.cgi.*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 7.2-3
- Review fixes.

* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 7.2-2
- Initial import.
