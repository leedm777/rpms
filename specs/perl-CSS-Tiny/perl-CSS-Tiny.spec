# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-Tiny

Summary: Read and write CSS files
Name: perl-CSS-Tiny
Version: 1.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Tiny/

Source: http://www.cpan.org/modules/by-module/CSS/CSS-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-ExtUtils-AutoInstall, perl(File::Spec) >= 0.82, perl(Test::More) >= 0.47

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead. CSS.pm
requires about 2.6 meg or ram to load, which is a large amount of
overhead if you only want to do trivial things. Memory usage is normally
scoffed at in Perl, but in my opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and
anything we write shouldn't need to have documentation/comments. If you
need something with more power, move up to CSS.pm. With the increasing
complexity of CSS, this is becoming more common, but many situations can
still live with simple CSS files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/CSS/
%{perl_vendorlib}/CSS/Tiny.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
