%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define require_ibus_version 1.2.0.20100111
%define require_pygtk2_version 2.15.2
Name:       ibus-anthy
Version:    1.2.1
Release:    1%{?dist}
Summary:    The Anthy engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    ibus-anthy.png
Patch0:     ibus-anthy-HEAD.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  anthy-devel
# sleep, touch
BuildRequires:  coreutils
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  sed
BuildRequires:  swig

Requires:   ibus >= %{require_ibus_version}
Requires:   anthy
Requires:   pygtk2 >= %{require_pygtk2_version}
Requires:   kasumi

%description
The Anthy engine for IBus platform. It provides Japanese input method from
libanthy.

%prep
%setup -q
cp %SOURCE1 icons
%patch0 -p1

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT%{python_sitearch}/_anthy.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
# %dir %{python_sitearch}/ibus
%{python_sitearch}/anthy.py*
%{python_sitearch}/_anthy.so
%{_libexecdir}/ibus-*-anthy
%{_datadir}/ibus-anthy
%{_datadir}/ibus/component/*

%changelog
* Fri Apr 23 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Mon Apr 05 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100313-2
- Update icon

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100313-1
- Update to 1.2.0.20100313
- Update fr.po

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100312.1-1
- Update to 1.2.0.20100312.1
- Minor fix for a translation

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100312-1
- Update to 1.2.0.20100312
- Fix bug 564268 - Crash with enabled global input method

* Fri Jan 15 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100115-1
- Update to 1.2.0.20100115
- Fix bug 550001 - kasumi should be accessible from ibus-anthy

* Fri Nov 27 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20091127-1
- Update to 1.2.0.20091127
- Fix bug 520989 - ibus-anthy icon enhancement
- Fix bug 531696 - ibus-anthy KeyError is still reported by abrt
- Fix bug 536716 - ibus-anthy: Symbol type change support in ibus-anthy

* Fri Oct 23 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090917-2
- Fix bug 526881 - ibus-anthy backtrace is reported by the latest abrt

* Thu Sep 17 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090917-1
- Update to 1.2.0.20090917
- Fix bug 523642 - ibus-anthy convert_to_char_type_{for,back}ward()

* Mon Sep 07 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090907-2
- Fix a build issue

* Mon Sep 07 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090907-1
- Update to 1.2.0.20090907
- Fix bug 510978 - "Typing Method" configuration doesn't work
- Fix bug 518373 - ibus setup tools need to set gettext textdomain dir.

* Thu Aug 13 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090813-1
- Update to 1.2.0.20090813
- Fix bug 509483 - reconversion feature doesn't work
- Fix bug 509485 - commit_first_segment feature doesn't work

* Tue Aug 04 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090804-1
- Update to 1.2.0.20090804
- Fix bug 508358 - ANTHY_HISTORY_FILE record only a single word

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-1
- Update to 1.2.0.20090617

* Wed Jun 17 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090603-2
- require kasumi to pull in dictionary tool

* Wed Jun 03 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090603-1
- Update to 1.1.0.20090603
- Implement setup ui.

* Thu Apr 30 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090402-2
- Update to upstream HEAD version
- Fix bug 498250 - Cannot type zenkaku-space

* Thu Apr 02 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090402-1
- Update to 1.1.0.20090402.
- Fix bug 490747 - Muhenkan (no-conversion) key does not undo conversion
- Fix bug 490750 - Henkan key for candidate conversion doesn't do anything
- Fix bug 490748 - Kana key doesn't do anything

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update to 1.1.0.20090205.

* Tue Feb 03 2009 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20090203-1
- Update to 0.1.1.20090203.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20080912-2
- Rebuild for Python 2.6

* Fri Sep 12 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080912-1
- Update to 0.1.1.20080912.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Thu Aug 28 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080828-1
- Update to 0.1.1.20080828.

* Wed Aug 27 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080827-1
- Update to 0.1.1.20080827.

* Tue Aug 26 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080826-1
- Update to 0.1.1.20080826.

* Sat Aug 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- Update to 0.1.1.20080823.

* Fri Aug 15 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080815-1
- Update to 0.1.1.20080815.

* Thu Aug 12 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080812-1
- Update to 0.1.1.20080812.

* Fri Aug 08 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.0.20080810-1
- The first version.
