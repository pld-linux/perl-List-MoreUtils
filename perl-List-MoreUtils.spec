#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	List
%define		pnam	MoreUtils
Summary:	List::MoreUtils - provide the stuff missing in List::Util
Summary(pl.UTF-8):	List::MoreUtils - dostarczenie elementów brakujących w List::Util
Name:		perl-List-MoreUtils
Version:	0.430
Release:	1
# code before 0.417: same as perl 5.8.4 or later
License:	Apache v2.0 (code since 0.417), GPL v1+ or Artistic (older code)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	daccd6310021231b827dcc943ff1c6b7
URL:		https://metacpan.org/release/List-MoreUtils
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.86
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Exporter-Tiny >= 0.038
BuildRequires:	perl-List-MoreUtils-XS >= 0.430
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-LeakTrace
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::MoreUtils provides some trivial but commonly needed
functionality on lists which is not going to go into List::Util.

All of the below functions are implementable in one line of Perl code.
Using the functions from this module however should give slightly
better performance as everything is implemented in C. The pure-Perl
implementation of these functions only serves as a fallback in case
the C portions of this module couldn't be compiled on this machine.

%description -l pl.UTF-8
List::MoreUtils dostarcza prostych, ale często potrzebnych funkcji do
operacji na listach - elementy, które nie zostaną dołączone do
List::Util.

Wszystkie z funkcji są możliwe do implementowania w jednej linijce
kodu Perla. Używanie funkcji z tego modułu może jednak dać odrobinę
większą wydajność jako, że całość została napisana w C. Implementacja
napisana w Perlu służy w sytuacjach wyjątkowych w przypadkach, gdy
elementy modułu napisane w C nie mogą zostać skompilowane na maszynie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%dir %{perl_vendorlib}/List
%{perl_vendorlib}/List/MoreUtils.pm
%{perl_vendorlib}/List/MoreUtils
%{_mandir}/man3/List::MoreUtils*.3pm*
