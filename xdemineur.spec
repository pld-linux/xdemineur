Summary:	A Minesweeper game for the X Window System
Summary(pl):	Gra "Saper" dla X Window System
Name:		xdemineur
Version:	2.1.1
Release:	6
License:	MIT
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xdemineur is a Minesweeper game for the X Window System. The object of
the game is to find the mines and place little flags on them, before
you stumble across a mine and get blown up.

%description -l pl
Xdemineur to gra "Saper" dla X Window System. Celem gry jest
odnalezienie wszystkich min i oznaczenie ich flagami, unikaj±c
nast±pienia na minê i wysadzenia w powietrze.

%prep
%setup -q

%build
xmkmf -a
%{__make} CFLAGS="%{rpmcflags} -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xdemineur.desktop <<EOF
[Desktop Entry]
Name=xdemineur
Comment=Minesweeper
Exec=xdemineur
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdemineur
%{_mandir}/man1/xdemineur.*
%{_applnkdir}/Games/xdemineur.desktop
