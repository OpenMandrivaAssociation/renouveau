%define cvsver	20121206
%define rel	1

Summary:	A tool to help developers of nouveau
Name:		renouveau
Version:	0
Release:	0.%{cvsver}.%{rel}
License:	MIT
Group:		Development/X11
URL:		http://nouveau.freedesktop.org/
# CVS snapshot
# cvs -z3 -d:pserver:anonymous@nouveau.cvs.sourceforge.net:/cvsroot/nouveau co -d renouveau-$(date +%Y%m%d) renouveau
# tar jcf renouveau-$(date +%Y%m%d).tar.bz2 renouveau-$(date +%Y%m%d)
Source0:	renouveau-%{cvsver}.tar.bz2
Patch0:		renouveau-20121206-rosa-linkage.patch
BuildRequires:	libxvmc-devel
BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig(glu)
ExclusiveArch:	%ix86 x86_64

%description
REnouveau stands for Reverse Engineer nouveau. It is an application
that runs small opengl tests and watches the changes in the video
card registers while the nvidia proprietary video drivers are in
use. This is used to do clean room reverse engineering (this is not
in violation with nvidia driver license).

Read this page if you want to submit a renouveau dump:
http://nouveau.freedesktop.org/wiki/REnouveauDumps

%prep
%setup -q -n %{name}-%{cvsver}
%patch0 -p1

perl -pi -e 's,lXvMCNVIDIA,lXvMCW,' Makefile

cat > README.install.urpmi <<EOF
See the following page for usage instructions:
http://nouveau.freedesktop.org/wiki/REnouveauDumps
EOF

%build
# no optflags as they interfere with results
%make

%install
# install binaries
install -d -m0755 %{buildroot}%{_bindir}
install -m0755 renouveau %{buildroot}%{_bindir}
install -m0755 disasm_shader %{buildroot}%{_bindir}

%files
%doc README README.install.urpmi license.txt
%{_bindir}/renouveau
%{_bindir}/disasm_shader


%changelog
* Mon Aug 16 2010 Anssi Hannula <anssi@mandriva.org> 0-0.20100816.1mdv2011.0
+ Revision: 570265
- new snapshot

* Sat Jul 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0-0.20100724.1mdv2011.0
+ Revision: 558109
- update to new snapshot 20100724

* Sun Jan 03 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0-0.20100103.1mdv2010.1
+ Revision: 485941
- update to new snapshot 20100103

* Mon Sep 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0-0.20090907.1mdv2010.0
+ Revision: 432976
- update to new snapshot 20090907

* Sat May 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0-0.20090530.1mdv2010.0
+ Revision: 381353
- new snapshot

* Sat Feb 21 2009 Anssi Hannula <anssi@mandriva.org> 0-0.20090221.1mdv2009.1
+ Revision: 343659
- new snapshot
- new snapshot

* Tue Apr 15 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080415.1mdv2009.0
+ Revision: 193551
- new snapshot

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080229.1mdv2008.1
+ Revision: 176582
- new snapshot

* Tue Feb 05 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080205.1mdv2008.1
+ Revision: 162740
- new snapshot

* Sun Jan 20 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080120.1mdv2008.1
+ Revision: 155153
- new snapshot

* Fri Jan 11 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080111.1mdv2008.1
+ Revision: 148720
- new snapshot

* Tue Jan 01 2008 Anssi Hannula <anssi@mandriva.org> 0-0.20080101.1mdv2008.1
+ Revision: 140007
- new snapshot

* Mon Dec 24 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20071225.3mdv2008.1
+ Revision: 137614
- restore buildroot

* Mon Dec 24 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20071225.2mdv2008.1
+ Revision: 137613
- new snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 28 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20071028.2mdv2008.1
+ Revision: 102863
- direct users to renouveau wiki page
- buildrequires libxml2-devel
- new snapshot

* Tue Aug 07 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070807.1mdv2008.0
+ Revision: 59587
- new snapshot

* Mon Jul 16 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070716.1mdv2008.0
+ Revision: 52658
- new snapshot

* Thu Jun 28 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070628.1mdv2008.0
+ Revision: 45279
- new snapshot

* Wed Jun 13 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070613.1mdv2008.0
+ Revision: 38402
- new snapshot

* Sat Jun 02 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070602.1mdv2008.0
+ Revision: 34579
- new snapshot

* Wed May 23 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070523.1mdv2008.0
+ Revision: 30432
- new snapshot

* Mon May 07 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070508.1mdv2008.0
+ Revision: 24871
- new snapshot

* Sun Apr 22 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070422.1mdv2008.0
+ Revision: 17023
- new snapshot

* Tue Apr 17 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070417.1mdv2008.0
+ Revision: 13856
- new snapshot


* Mon Apr 02 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070402.1mdv2007.1
+ Revision: 150213
- new snapshot

* Sat Mar 10 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070310.1mdv2007.1
+ Revision: 140532
- new snapshot

* Thu Mar 08 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070308.1mdv2007.1
+ Revision: 138455
- new snapshot

* Tue Feb 27 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070227.1mdv2007.1
+ Revision: 126702
- new snapshot

* Thu Feb 22 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070222.1mdv2007.1
+ Revision: 124749
- new snapshot

* Tue Feb 20 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070220.1mdv2007.1
+ Revision: 123165
- new snapshot

* Sun Feb 18 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070218.1mdv2007.1
+ Revision: 122320
- new snapshot

* Fri Feb 09 2007 Anssi Hannula <anssi@mandriva.org> 0-0.20070209.1mdv2007.1
+ Revision: 118434
- new snapshot
- Import renouveau

