# $Id: $

# Authority: dries
# Upstream: Robby Stephenson <mailto:robby$periapsis,org>
# Screenshot: http://www.periapsis.org/tellico/sshots/main_screen-0.9.png
# ScreenshotURL: http://www.periapsis.org/tellico/sshots.php

Summary: collection manager
Name: tellico
Version: 0.12
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.periapsis.org/tellico/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.periapsis.org/tellico/download/tellico-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, libgcrypt-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, libxslt-devel
BuildRequires: kdelibs-devel, desktop-file-utils, libxml2-devel
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
Tellico is a collection manager for KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from Amazon.com. 

%prep
%setup

%build
source  /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source  /etc/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/apps/tellico
%{_datadir}/applnk/Applications/tellico.desktop
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/doc/HTML/en/tellico
%{_datadir}/icons/hicolor/*/apps/tellico.png
%{_datadir}/mimelnk/application/x-tellico.desktop

%changelog
* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
