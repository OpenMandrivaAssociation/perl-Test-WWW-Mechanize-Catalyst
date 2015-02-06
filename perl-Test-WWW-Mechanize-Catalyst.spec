%define upstream_name    Test-WWW-Mechanize-Catalyst
%define upstream_version 0.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Test::WWW::Mechanize for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.00
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.04

BuildArch:	noarch

%description
Catalyst is an elegant MVC Web Application
Framework. Test::WWW::Mechanize is a subclass of WWW::Mechanize that
incorporates features for web application testing. The
Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/Test


%changelog
* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.520.0-1mdv2010.1
+ Revision: 515672
- update to 0.52

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.510.0-1mdv2010.0
+ Revision: 406384
- rebuild using %%perl_convert_version

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdv2010.0
+ Revision: 373949
- update to new version 0.51

* Tue Nov 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2009.1
+ Revision: 306765
- update to new version 0.45

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2009.1
+ Revision: 299405
- update to new version 0.44
- fix build dependencies

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdv2008.1
+ Revision: 97971
- update to new version 0.41

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2008.0
+ Revision: 77703
- new version

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2008.0
+ Revision: 47739
- update to new version 0.38


* Wed Jun 14 2006 Scott Karns <scottk@mandriva.org> 0.37-1mdv2007.0
- Version 0.37

* Mon May 08 2006 Scott Karns <scottk@mandriva.org> 0.36-1mdk
- First Mandriva release

