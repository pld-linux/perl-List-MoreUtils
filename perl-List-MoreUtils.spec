#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	MoreUtils
Summary:	List::MoreUtils - provide the stuff missing in List::Util
Summary(pl.UTF-8):	List::MoreUtils - dostarczenie elementów brakujących w List::Util
Name:		perl-List-MoreUtils
Version:	0.22
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/V/VP/VPARSEVAL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a6ec506f40662ab1296c48c5eb72016
URL:		http://search.cpan.org/dist/List-MoreUtils/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/List
%{perl_vendorarch}/List/MoreUtils.pm
%dir %{perl_vendorarch}/auto/List/MoreUtils
%{perl_vendorarch}/auto/List/MoreUtils/MoreUtils.bs
%attr(755,root,root) %{perl_vendorarch}/auto/List/MoreUtils/MoreUtils.so
%{_mandir}/man3/*
