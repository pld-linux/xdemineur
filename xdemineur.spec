Summary:	A Minesweeper game for the X Window System
Summary(de.UTF-8):	Minesweeper-Game
Summary(es.UTF-8):	Juego Minesweeper
Summary(fr.UTF-8):	Jeu de démineur
Summary(pl.UTF-8):	Gra "Saper" dla X Window System
Summary(pt_BR.UTF-8):	Jogo Minesweeper
Summary(tr.UTF-8):	Mayın tarlası oyunu
Name:		xdemineur
Version:	2.1.1
Release:	11
License:	MIT
Group:		X11/Applications/Games
Source0:	ftp://ftp.x.org/contrib/games/%{name}-%{version}.tar.gz
# Source0-md5:	733daa1db17ed8025186236817c013f7
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xdemineur is a Minesweeper game for the X Window System. The object of
the game is to find the mines and place little flags on them, before
you stumble across a mine and get blown up.

%description -l de.UTF-8
Ein Spiel, das intensivste Konzentration erfordert, in dem Sie die
Standorte von Minen durch logisches, deduktives Denken herausfinden
müssen.

%description -l es.UTF-8
Este es un juego de intensa concentración, donde debes con éxito
determinar los locales de las minas a través de lógica y deducción.
Muy parecido con la versión Windows.

%description -l fr.UTF-8
Jeu d'une concentration extrême, où vous devez déterminer les
emplacements des mines en utilisant la logique et la déduction.

%description -l pl.UTF-8
Xdemineur to gra "Saper" dla X Window System. Celem gry jest
odnalezienie wszystkich min i oznaczenie ich flagami, unikając
nastąpienia na minę i wysadzenia w powietrze.

%description -l pt_BR.UTF-8
Este é um jogo de intensa concentração, onde você deve com sucesso
determinar os locais das minas através de lógica e dedução. Muito
parecido com a versão Windows.

%description -l tr.UTF-8
Komşu karelerde yer alan mayın sayılarından yararlanarak tarlada yer
alan tüm mayınları bulmanız amaçlanmaktadır.

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

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

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
