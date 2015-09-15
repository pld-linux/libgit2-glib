#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	python		# Python binding
%bcond_without	static_libs	# static library
#
Summary:	GLib wrapper library around the libgit2 git access library
Summary(pl.UTF-8):	Biblioteka obudowania GLib do biblioteki dostępu do gita libgit2
Name:		libgit2-glib
Version:	0.22.8
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgit2-glib/0.22/%{name}-%{version}.tar.xz
# Source0-md5:	b775250b57a7cdb65809b967e3e67a95
URL:		https://wiki.gnome.org/Libgit2-glib
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.10.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.11}
BuildRequires:	libgit2-devel >= 0.21.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2.3
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2 >= 1:2.28.0
Requires:	libgit2 >= 0.21.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgit2-glib is a glib wrapper library around the libgit2 git access
library.

libgit2 only implements the core plumbing functions, not really the
higher level porcelain stuff.

%description -l pl.UTF-8
libgit2-glib to biblioteka obudowania glib dla biblioteki dostępu do
gita libgit2.

libgit2 implementuje tylko niskopoziomowe funkcje, bez całej otoczki
wyższego poziomu.

%package devel
Summary:	Header files for libgit2-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgit2-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gobject-introspection-devel >= 0.10.1
Requires:	libgit2-devel >= 0.20.0

%description devel
Header files for libgit2-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgit2-glib.

%package static
Summary:	Static libgit2-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libgit2-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgit2-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka libgit2-glib.

%package apidocs
Summary:	libgit2-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgit2-glib
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for libgit2-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgit2-glib.

%package -n python3-libgit2-glib
Summary:	Python 3 binding for libgit2-glib library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki libgit2-glib
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3 >= 3.2.3
Requires:	python3-pygobject3 >= 3.0.0

%description -n python3-libgit2-glib
Python 3 binding for libgit2-glib library.

%description -n python3-libgit2-glib -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki libgit2-glib.

%package -n vala-libgit2-glib
Summary:	Vala API for libgit2-glib library
Summary(pl.UTF-8):	API języka Vala do biblioteki libgit2-glib
Group:		Development/Libraries
Requires:	libgit2-glib-devel = %{version}-%{release}
Requires:	vala

%description -n vala-libgit2-glib
Vala API for libgit2-glib library.

%description -n vala-libgit2-glib -l pl.UTF-8
API języka Vala do biblioteki libgit2-glib.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgit2-glib-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgit2-glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgit2-glib-1.0.so.0
%{_libdir}/girepository-1.0/Ggit-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgit2-glib-1.0.so
%{_includedir}/libgit2-glib-1.0
%{_datadir}/gir-1.0/Ggit-1.0.gir
%{_pkgconfigdir}/libgit2-glib-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgit2-glib-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgit2-glib-1.0
%endif

%if %{with python}
%files -n python3-libgit2-glib
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/Ggit.py
%{py3_sitedir}/gi/overrides/__pycache__/Ggit.cpython-3*.py[co]
%endif

%files -n vala-libgit2-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ggit-1.0.deps
%{_datadir}/vala/vapi/ggit-1.0.vapi
