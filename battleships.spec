Summary:	Battleships against the computer (character-cell graphics)
Summary(pl.UTF-8):   Gra w statki przeciwko komputerowi
Name:		battleships
Version:	2.7
Release:	1
License:	GPL
Group:		Applications/Games
Vendor:		Eric S. Raymond <esr@snark.thyrsus.com>
Source0:	http://www.catb.org/~esr/bs/bs-%{version}.tar.gz
# Source0-md5:	5786c6006e503d100e65139dadb5d5a7
URL:		http://www.catb.org/~esr/bs/
BuildRequires:	ncurses-devel
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The classic game of Battleships against the computer. Uses
character-cell graphics with a visual point-and-shoot interface.

If you're using an xterm the mouse will work.

%description -l pl.UTF-8
Klasyczna gra w statki, tym razem przeciwko komputerowi. Posiada
wizualny interfejs "wskaż i strzel" (ang. "point and shoot").

Jeśli używasz xterm, mysz nie będzie działać.

%prep
%setup -q -n bs-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-I /usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/bs.6*
