%define upstream_name    Test-WWW-Mechanize-Catalyst
%define upstream_version 0.52

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Test::WWW::Mechanize for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.00
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.04

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Catalyst is an elegant MVC Web Application
Framework. Test::WWW::Mechanize is a subclass of WWW::Mechanize that
incorporates features for web application testing. The
Test::WWW::Mechanize::Catalyst module meshes the two to allow easy
testing of Catalyst applications without starting up a web server.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
%make test

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
