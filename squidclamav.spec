Name:           squidclamav
Version:        7.2
Release:        2%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL+
URL:            http://sourceforge.net/projects/%{name}/

Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Patch0:         https://github.com/darold/squidclamav/commit/6c279b74a61507a6e2118cb8796f5647f4166ecd.patch

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
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_libdir}/c_icap/*.so
%config(noreplace) %{_libexecdir}/%{name}/clwarn.cgi
%{_datadir}/c_icap/templates/squidclamav/*
%{_libexecdir}/%{name}/clwarn.cgi.*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 7.2-2
- Clean up SPEC file, use packaging guidelines where possible and fix rpmlint
  issues.

* Sat Jul 09 2022 Frank Crawford <frank@crawford.emu.id.au> - 7.2-1
- Update to 7.2

* Sun Mar 14 2021 Frank Crawford <frank@crawford.emu.id.au> - 7.1-2
- Rebuild with new c-icap release
- Added EPEL 8 version

* Sun Jun 09 2019 Frank Crawford <frank@crawford.emu.id.au> - 7.1-1
- Update to 7.1
- Enabled libarchive

* Wed Nov 09 2016 momo-i <webmaster@momo-i.org> - 6.16-1
- Update to 6.16

* Tue Jan 26 2016 momo-i <webmaster@momo-i.org> - 6.15-1
- Update to 6.15

* Mon Nov 09 2015 momo-i <webmaster@momo-i.org> - 6.14-1
- Update to 6.14

* Thu Sep 03 2015 momo-i <webmaster@momo-i.org> - 6.13-7
- Update dist for centos7

* Mon Aug 10 2015 momo-i <webmaster@momo-i.org> - 6.13-6
- Rebuilt for fc23

* Wed Jun 17 2015 momo-i <webmaster@momo-i.org> - 6.13-5
- Update to 6.13

* Thu Apr 16 2015 momo-i <webmaster@momo-i.org> - 6.12-5
- Rebilt for fc22

* Thu Feb  5 2015 momo-i <webmaster@momo-i.org> - 6.12-4
- Update to 6.12
- Change license dir

* Sat Sep 20 2014 momo-i <webmaster@momo-i.org> - 6.11-4
- Update to 6.11

* Tue Nov 19 2013 momo-i <webmaster@momo-i.org> - 6.10-4
- change noreplace for default clwarn.cgi

* Tue Nov 19 2013 momo-i <webmaster@momo-i.org> - 6.10-3
- Add Japanese clwarn.cgi

* Mon Nov 11 2013 momo-i <webmaster@momo-i.org> - 6.10-2
- Add required package

* Wed Oct  9 2013 momo-i <webmaster@momo-i.org> - 6.10-1
- Initial rpm release.
