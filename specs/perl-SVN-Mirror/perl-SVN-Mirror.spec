# $Id$
# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Mirror

Summary: Subversion repository mirroring tool
Name: perl-SVN-Mirror
Version: 0.67
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Mirror/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVN-Mirror-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, subversion-perl, perl-Data-UUID, perl-Term-ReadKey
BuildRequires: perl-SVN-Simple

%description
SVN::Mirror is a subversion repository mirroring tool.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc CHANGES README SIGNATURE TODO
%doc %{_mandir}/man?/*
%{_bindir}/svm
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Mirror.pm
%{perl_vendorlib}/SVN/Mirror/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Update to release 0.49.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Initial package.
