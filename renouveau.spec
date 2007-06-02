
%define version	0
%define cvsver	20070602
%define rel	1
%define name	renouveau

Name:		%name
Version:	%version
Release:	%mkrel 0.%cvsver.%rel
Summary:	A tool to help developers of nouveau (a free driver for nvidia video cards)
Group:		Development/X11
URL:		http://nouveau.freedesktop.org/
# CVS snapshot
# cvs -z3 -d:pserver:anonymous@nouveau.cvs.sourceforge.net:/cvsroot/nouveau co -d renouveau-$(date +%Y%m%d) renouveau
# tar jcf renouveau-$(date +%Y%m%d).tar.bz2 renouveau-$(date +%Y%m%d)
Source:		renouveau-%{cvsver}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libxvmc-devel
BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
ExclusiveArch:	%ix86 x86_64

%description
REnouveau stands for Reverse Engineer nouveau. It is an application
that runs small opengl tests and watches the changes in the video
card registers while the nvidia proprietary video drivers are in
use. This is used to do clean room reverse engineering (this is not
in violation with nvidia driver license).

Usage instructions are in README.install.urpmi.

%prep
%setup -q -n %{name}-%{cvsver}

perl -pi -e 's,lXvMCNVIDIA,lXvMCW,' Makefile

cat > README.install.urpmi <<EOF
Instructions:
Make a writable directory and cd into it. Make sure your screensaver
will not start in the next few minutes. Then fire up renouveau and
wait. A window should appear where renouveau does its OpenGL tests.
Do not move your mouse over that window nor move that window. Make
sure no other window overlaps with the renouveau window. When
renouveau quits the directory should be full of files. Compress them
and mail them to renouveau.dumps (at) gmail.com or ask what to do at 
irc.freenode.net, channel #nouveau.
EOF

%ifarch x86_64
%if %mdkversion <= 200700
cat >> README.install.urpmi <<EOF

NOTE: Renouveau may not start on x86_64 versions of Mandriva 2007.0
      and older before you run this as root:
chrpath -d %{_libdir}/libSDL-1.2.so.0
EOF
%endif
%endif

%build
# no optflags as they interfere with results
%make

%install
rm -rf %{buildroot}

# install binaries
install -d -m0755 %{buildroot}%{_bindir}
install -m0755 renouveau %{buildroot}%{_bindir}
install -m0755 disasm_shader %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.install.urpmi license.txt
%{_bindir}/renouveau
%{_bindir}/disasm_shader


