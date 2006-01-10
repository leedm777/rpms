# $Id$
# Authority: dries
# Upstream: Jonathan Chin <jon-pause-public$earth,li>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name OpenGL-Simple

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Interface to OpenGL
Name: perl-OpenGL-Simple
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OpenGL-Simple/

Source: http://search.cpan.org/CPAN/authors/id/J/JC/JCHIN/OpenGL-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
This module provides another interface to OpenGL. It does not support
all of OpenGL, but some functions which are supported are also given a
polymorphic interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/OpenGL/Simple.pm
%{perl_vendorarch}/auto/OpenGL/Simple/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.

