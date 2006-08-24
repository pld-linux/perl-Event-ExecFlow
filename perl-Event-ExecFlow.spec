#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event-ExecFlow
Summary:	Event::ExecFlow - High level API for event-based execution flow control
Summary(pl):	Event::ExecFlow - wysokopoziomowe API do opartego na zdarzeniach sterowania wykonywaniem
Name:		perl-Event-ExecFlow
Version:	0.62
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e76d36b1e098674907980200aabf2522
URL:		http://search.cpan.org/dist/Event-ExecFlow/
BuildRequires:	perl-AnyEvent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High level API for event-based execution flow control.

%description -l pl
Wysokopoziomowe API do opartego na zdarzeniach sterowania przepływem
wykonywania kodu.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Event/ExecFlow.pm
%{perl_vendorlib}/Event/ExecFlow
%{_mandir}/man3/*
