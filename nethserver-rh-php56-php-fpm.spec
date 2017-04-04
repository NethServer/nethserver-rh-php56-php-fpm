Name: nethserver-rh-php56-php-fpm
Version: 1.0.0
Release: 1%{?dist}
Summary: NethServer rh-php56-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php56, rh-php56-php-fpm

%description
Basic support for PHP 5.6 using SCL

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- First release
- Nextcloud 11 - NethServer/dev#5242

