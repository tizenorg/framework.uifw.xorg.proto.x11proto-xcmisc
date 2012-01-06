
Name:       xorg-x11-proto-xcmiscproto
Summary:    X.Org X11 Protocol xcmiscproto
Version:    1.2.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xcmiscproto-%{version}.tar.gz
Provides:   xcmiscproto
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n xcmiscproto-%{version}

%build

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xcmiscproto.pc
%{_includedir}/X11/extensions
%{_includedir}/X11/extensions/xcmiscstr.h
%{_docdir}/xcmiscproto


