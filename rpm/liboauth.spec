Name:           liboauth
Version:        1.0.4
Release:        1
Summary:        OAuth library functions
Group:          Development/Libraries
License:        MIT
URL:            http://liboauth.sourceforge.net/
Source0:        http://liboauth.sourceforge.net/pool/liboauth-%{version}.tar.gz
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(nss)

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}


%build

%configure --disable-static --enable-nss

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING.MIT README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc
%{_mandir}/man3/oauth.*
