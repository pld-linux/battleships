Summary:	Battleships against the computer (character-cell graphics)
Summary(pl.UTF-8):	Gra w statki przeciwko komputerowi
Name:		battleships
Version:	2.8
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://www.catb.org/~esr/bs/bs-%{version}.tar.gz
# Source0-md5:	3add0396d1e7f98c20267634f41a87b1
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
Klasyczna gra w statki, tym razem przeciwko komputerowi. Posiada
wizualny interfejs "wskaż i strzel" (ang. "point and shoot").

Jeśli używasz xterm, mysz nie będzie działać.

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

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/bs
%{_mandir}/man6/bs.6*
