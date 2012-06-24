Summary:	A Minesweeper game for the X Window System
Summary(de):	Minesweeper-Game
Summary(es):	Juego Minesweeper
Summary(fr):	Jeu de d�mineur
Summary(pl):	Gra "Saper" dla X Window System
Summary(pt_BR):	Jogo Minesweeper
Summary(tr):	May�n tarlas� oyunu
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
m�ssen.

%description -l es
Este es un juego de intensa concentraci�n, donde debes con �xito
determinar los locales de las minas a trav�s de l�gica y deducci�n.
Muy parecido con la versi�n Windows.

%description -l fr
Jeu d'une concentration extr�me, o� vous devez d�terminer les
emplacements des mines en utilisant la logique et la d�duction.

%description -l pl
Xdemineur to gra "Saper" dla X Window System. Celem gry jest
odnalezienie wszystkich min i oznaczenie ich flagami, unikaj�c
nast�pienia na min� i wysadzenia w powietrze.

%description -l pt_BR
Este � um jogo de intensa concentra��o, onde voc� deve com sucesso
determinar os locais das minas atrav�s de l�gica e dedu��o. Muito
parecido com a vers�o Windows.

%description -l tr
Kom�u karelerde yer alan may�n say�lar�ndan yararlanarak tarlada yer
alan t�m may�nlar� bulman�z ama�lanmaktad�r.

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
