Summary:	Battleships against the computer (character-cell graphics)
Summary(pl.UTF-8):	Gra w statki przeciwko komputerowi
Name:		battleships
Version:	2.13
Release:	1
License:	BSD
Group:		Applications/Games
Source0:	http://www.catb.org/~esr/bs/bs-%{version}.tar.gz
# Source0-md5:	ea60abdbce9283eee201c8c854aa9749
Patch0:		%{name}-ldflags.patch
URL:		http://www.catb.org/~esr/bs/
BuildRequires:	ncurses-devel
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The classic game of Battleships against the computer. Uses
character-cell graphics with a visual point-and-shoot interface.

If you're using an xterm the mouse will work.

%description -l pl.UTF-8
Klasyczna gra w statki, tym razem przeciwko komputerowi. Wykorzystuje
grafikę znakową i ma wizualny interfejs "wskaż i strzel" (ang. "point
and shoot").

Mysz działa w xtermie.

%prep
%setup -q -n bs-%{version}
%patch0 -p1

%build
%{__make} \
	TERMLIB="-lncurses -ltinfo" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I /usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/bs
%{_datadir}/appdata/bs.adoc
%{_desktopdir}/bs.desktop
%{_iconsdir}/hicolor/32x32/apps/battleship.png
%{_mandir}/man6/bs.6*
