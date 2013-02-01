#
# Conditional build:
%bcond_without	silc	# SILC support
#
Summary:	Grubby - GGZ chat bot
Summary(pl.UTF-8):	Grubby - bot dla chatu GGZ
Name:		ggz-grubby
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	32f8a5992ce4c9d6fde19512ea0eee5c
Patch0:		%{name}-silc.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libdir.patch
Patch3:		%{name}-ruby.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	libtool
BuildRequires:	perl-devel >= 1:5.6.0
# not ready
#BuildRequires:	php-devel >= 4
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	ruby-devel >= 1.9
%{?with_silc:BuildRequires:	silc-toolkit-devel >= 1.1}
BuildRequires:	tcl-devel >= 8.5
Requires:	ggz-client-libs-devel >= 0.0.14
Requires:	libggz-devel >= 0.0.14
%{?with_silc:Requires:	silc-toolkit >= 1.1}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains grubby, the almighty chatbot. It's a single
binary, but it is very flexible and extensible by plugins and scripts.

%description -l pl.UTF-8
Ten pakiet zawiera program grubby - wszechmocnego bota dla czatu GGZ.
Jest to pojedyncza binarka, ale jest bardzo elastyczna i rozszerzalna
poprzez wtyczki i skrypty.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I m4/ggz
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/grubby/*modules/*.{la,a}

%find_lang grubby

%clean
rm -rf $RPM_BUILD_ROOT

%files -f grubby.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.GGZ TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggz.modules
%attr(755,root,root) %{_bindir}/grubby
%attr(755,root,root) %{_bindir}/grubby-config
%attr(755,root,root) %{_libdir}/ggz/guru-chess
%attr(755,root,root) %{_libdir}/ggz/guru-ttt
%dir %{_libdir}/grubby
%dir %{_libdir}/grubby/coremodules
%attr(755,root,root) %{_libdir}/grubby/coremodules/libguru_*.so
%dir %{_libdir}/grubby/modules
%attr(755,root,root) %{_libdir}/grubby/modules/libgurumod_*.so
%dir %{_datadir}/grubby
%attr(755,root,root) %{_datadir}/grubby/*.pl
%attr(755,root,root) %{_datadir}/grubby/*.rb
%{_mandir}/man1/grubby-config.1*
%{_mandir}/man6/grubby.6*
%lang(de) %{_mandir}/de/man1/grubby-config.1*
%lang(de) %{_mandir}/de/man6/grubby.6*
