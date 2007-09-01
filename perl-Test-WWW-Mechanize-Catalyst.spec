%define realname Test-WWW-Mechanize-Catalyst
%define name	perl-%{realname}
%define version	0.40
%define release	%mkrel 1

Summary:	Test::WWW::Mechanize for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{realname}-%{version}.tar.bz2
BuildRequires:	perl(Catalyst) >= 5.00
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.04
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{release}

%description
Catalyst is an elegant MVC Web Application
Framework. Test::WWW::Mechanize is a subclass of WWW::Mechanize that
incorporates features for web application testing. The
Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.


%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/Test

%clean
rm -rf %{buildroot}

