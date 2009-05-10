%define module Test-WWW-Mechanize-Catalyst
%define name	perl-%{module}
%define version	0.51
%define release	%mkrel 1

Summary:	Test::WWW::Mechanize for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Catalyst) >= 5.00
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.04
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{release}

%description
Catalyst is an elegant MVC Web Application
Framework. Test::WWW::Mechanize is a subclass of WWW::Mechanize that
incorporates features for web application testing. The
Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.


%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/Test

