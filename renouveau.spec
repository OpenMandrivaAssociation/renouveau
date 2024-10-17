%define cvsver	20121206
%define rel	3

Summary:	A tool to help developers of nouveau
Name:		renouveau
Version:	0
Release:	0.%{cvsver}.%{rel}
License:	MIT
Group:		Development/X11
URL:		https://nouveau.freedesktop.org/
# CVS snapshot
# cvs -z3 -d:pserver:anonymous@nouveau.cvs.sourceforge.net:/cvsroot/nouveau co -d renouveau-$(date +%Y%m%d) renouveau
# tar jcf renouveau-$(date +%Y%m%d).tar.bz2 renouveau-$(date +%Y%m%d)
Source0:	renouveau-%{cvsver}.tar.bz2
Patch0:		renouveau-20121206-rosa-linkage.patch
BuildRequires:	libxvmc-devel
BuildRequires:	SDL-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gl)
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
