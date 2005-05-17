Summary:	A Minesweeper game for the X Window System
Summary(de):	Minesweeper-Game
Summary(es):	Juego Minesweeper
Summary(fr):	Jeu de démineur
Summary(pl):	Gra "Saper" dla X Window System
Summary(pt_BR):	Jogo Minesweeper
Summary(tr):	Mayýn tarlasý oyunu
Name:		xdemineur
Version:	2.1.1
Release:	10
License:	MIT
Group:		X11/Applications/Games
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tar.gz
# Source0-md5:	733daa1db17ed8025186236817c013f7
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xdemineur is a Minesweeper game for the X Window System. The object of
the game is to find the mines and place little flags on them, before
you stumble across a mine and get blown up.

%description -l de
Ein Spiel, das intensivste Konzentration erfordert, in dem Sie die
Standorte von Minen durch logisches, deduktives Denken herausfinden
müssen.

%description -l es
Este es un juego de intensa concentración, donde debes con éxito
determinar los locales de las minas a través de lógica y deducción.
Muy parecido con la versión Windows.

%description -l fr
Jeu d'une concentration extrême, où vous devez déterminer les
emplacements des mines en utilisant la logique et la déduction.

%description -l pl
Xdemineur to gra "Saper" dla X Window System. Celem gry jest
odnalezienie wszystkich min i oznaczenie ich flagami, unikaj±c
nast±pienia na minê i wysadzenia w powietrze.

%description -l pt_BR
Este é um jogo de intensa concentração, onde você deve com sucesso
determinar os locais das minas através de lógica e dedução. Muito
parecido com a versão Windows.

%description -l tr
Komþu karelerde yer alan mayýn sayýlarýndan yararlanarak tarlada yer
alan tüm mayýnlarý bulmanýz amaçlanmaktadýr.

%prep
%setup -q

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdemineur
%{_mandir}/man1/xdemineur.*
%{_desktopdir}/xdemineur.desktop
%{_pixmapsdir}/*
