#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	List
%define	pnam	MoreUtils
Summary:	List::MoreUtils - provide the stuff missing in List::Util
Summary(pl):	List::MoreUtils - dostarczenie elementów brakuj±cych w List::Util
Name:		perl-List-MoreUtils
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	591e64f035db665a389fc1fea218c8ec
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

%description -l pl
List::MoreUtils dostarcza prostych, ale czêsto potrzebnych funkcji do
operacji na listach - elementy, które nie zostan± do³±czone do
List::Util.

Wszystkie z funkcji s± mo¿liwe do implementowania w jednej linijce
kodu Perla. U¿ywanie funkcji z tego modu³u mo¿e jednak daæ odrobinê
wiêksz± wydajno¶æ jako, ¿e ca³o¶æ zosta³a napisana w C. Implementacja
napisana w Perlu s³u¿y w sytuacjach wyj±tkowych w przypadkach, gdy
elementy modu³u napisane w C nie mog± zostaæ skompilowane na maszynie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/List/*.pm
%{_mandir}/man3/*
