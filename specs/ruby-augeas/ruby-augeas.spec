# $Id$
# Authority: shuff

### EL6 ships with augeas-0.7.2-3.el6, ruby-augeas-0.4+ requires augeas-0.8+
%{?el6:# Tag: rfx}

%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

%global rubyabi 1.8

Summary: Ruby bindings for Augeas
Name: ruby-augeas
Version: 0.4.1
Release: 2%{?dist}
Group: Development/Languages
License: LGPLv2+
URL: http://augeas.net/

Source: http://augeas.net/download/ruby/ruby-augeas-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: augeas-devel >= 0.8.0
BuildRequires: pkgconfig
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygem(rake)

Requires: ruby(abi) = %{rubyabi}
Requires: augeas-libs >= 0.8.0

Provides: ruby(augeas) = %{version}

%description
Ruby bindings for Augeas.

%prep
%setup

%build
export CFLAGS="$RPM_OPT_FLAGS"
rake build

%install
%{__rm} -rf %{buildroot}

# gotta do it by hand
%{__install} -m0755 -d %{buildroot}%{ruby_sitearch}
%{__install} -m0755 -d %{buildroot}%{ruby_sitelib}
%{__install} -m0644 ext/augeas/_augeas.so %{buildroot}%{ruby_sitearch}
%{__install} -m0644 lib/augeas.rb %{buildroot}%{ruby_sitelib}

%check
rake test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING NEWS README.rdoc
%{ruby_sitearch}/*
%{ruby_sitelib}/*

%changelog
* Tue Jun 28 2011 Yury V. Zaytsev <yury@shurup.com> - 0.4.1-2
- RFX on RHEL6, because augeas-0.8+ is RFX.

* Mon Apr 25 2011 Steve Huff <shuff@vecna.org> - 0.4.1-1
- Update to version 0.4.1.

* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 0.3.0-1
- Initial package (ported from EPEL).
