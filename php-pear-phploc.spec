%define  upstream_name phploc

Summary:	A tool for quickly measuring the size of a PHP project
Name:		php-pear-%{upstream_name}
Version:	1.6.4
Release:	2
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/phploc-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-pear-File_Iterator >= 1.3.0
Suggests:	php-pear-bytekit
Suggests:	php-tokenizer

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides a tool for quickly measuring the size of a PHP project
for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_bindir}/phploc
%{_datadir}/pear/PHPLOC
%{_datadir}/pear/packages/phploc.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-2mdv2012.0
+ Revision: 742323
- fix major breakage by careless packager

* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-1
+ Revision: 730881
- import php-pear-phploc


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-1mdv2010.2
- initial Mandriva package
