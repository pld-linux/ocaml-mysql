# TODO
# - (build time) security http://security.gentoo.org/glsa/glsa-200506-08.xml
Summary:	MySQL binding for OCaml
Summary(pl):	Wi±zania MySQL dla OCamla
Name:		ocaml-mysql
Version:	1.0.3
Release:	2
License:	LGPL v2.1+
Vendor:		Shawn Wagner <shawnw@speakeasy.org>
Group:		Libraries
Source0:	http://raevnos.pennmush.org/code/ocaml-mysql/%{name}-%{version}.tar.gz
# Source0-md5:	3254be1cb6ef8801701a5628e60cfee4
URL:		http://raevnos.pennmush.org/code/ocaml-mysql/index.html
BuildRequires:	autoconf
BuildRequires:	mysql-devel
BuildRequires:	ocaml >= 3.08
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows OCaml programs to access MySQL databases. This
package contains files needed to run bytecode OCaml programs using
this library.

%description -l pl
Biblioteka ta umo¿liwia programom pisanym w OCamlu dostêp do baz
danych MySQL. Pakiet ten zawiera binaria potrzebne do uruchamiania
programów u¿ywaj±cych tej biblioteki.

%package devel
Summary:	MySQL binding for OCaml - development part
Summary(pl):	Wi±zania MySQL dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This library allows OCaml programs to access MySQL databases. This
package contains files needed to develop OCaml programs using this
library.

%description devel -l pl
Biblioteka ta umo¿liwia programom pisanym w OCamlu dostêp do baz
danych MySQL. Pakiet ten zawiera pliki niezbêdne do tworzenia
programów u¿ywaj±cych tej biblioteki.

%prep
%setup -q

%build
%{__autoconf}
%configure CFLAGS="%{rpmcflags} -fPIC"

%{__make} all opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{stublibs,mysql,site-lib/mysql}

install *.a mysql.cm{[ixa],xa} $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql
install *.so $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
ln -s mysql.cma $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql/mysqlstatic.cma

install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/mysql/
echo 'directory = "+mysql"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/mysql/META

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc demo.ml doc
%{_libdir}/ocaml/mysql
%{_libdir}/ocaml/site-lib/mysql
