Summary:	MySQL binding for OCaml
Summary(pl):	Wi±zania MySQL dla OCamla
Name:		ocaml-mysql
Version:	0.1.1
Release:	1
License:	BSD
Group:		Libraries
Vendor:		Shawn Wagner <shawnw@speakeasy.org>
URL:		http://raevnos.pennmush.org/code/ocaml.html
Source0:	http://raevnos.pennmush.org/code/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	mysql-devel
BuildRequires:	ocaml
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
autoconf
%configure CFLAGS="%{rpmcflags} -fPIC"
sed -e 's/-cclib $(MYSQLLIB)//; s/-g//' Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile

%{__make} all opt

ocamlmklib -o mysql mysql.cm[ox] ocmysql.o -lmysqlclient

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql
install mysql.cm{[ixa],xa} $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql
install *.a *.so $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql
ln -s mysql.cma $RPM_BUILD_ROOT%{_libdir}/ocaml/mysql/mysqlstatic.cma
(cd $RPM_BUILD_ROOT%{_libdir}/ocaml && ln -s mysql/dll*.so .)

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/mysql
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/mysql/META <<EOF
name="mysql"
version="%{version}"
description="Ocaml bindings to MySQL"
requires=""
linkopts=""
archive(byte) = "mysql.cma"
archive(byte,autolink) = "mysql.cma"
archive(native) = "mysql.cmxa"
directory = "+mysql"
EOF

gzip -9nf README CHANGES COPYING demo.ml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/mysql
%attr(755,root,root) %{_libdir}/ocaml/mysql/*.so
%{_libdir}/ocaml/*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz *.html
%{_libdir}/ocaml/mysql/*.cm[ixa]*
%{_libdir}/ocaml/mysql/*.a
%{_libdir}/ocaml/site-lib/mysql
