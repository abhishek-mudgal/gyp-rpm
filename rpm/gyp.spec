%global		revision	1988
%{expand:	%%global	archivename	gyp-%{version}-svn%{revision}}

Name:		gyp
Version:	0.1
Release:	0.16.%{revision}svn
Summary:	Generate Your Projects

Group:		Development/Tools
License:	BSD
URL:		https://chromium.googlesource.com/external/gyp
Source:		%{name}-%{version}.tar.bz2
Patch1:		patch1.patch
Patch2:		patch2.patch
BuildRequires:  python-setuptools
BuildRequires:	python-devel
Requires:  python-setuptools



%description
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format.

Its syntax is a universal cross-platform build representation
that still allows sufficient per-platform flexibility to accommodate
irreconcilable differences.



%prep
%setup -q -n %{name}-%{version}/gyp

%patch0 -p0
%patch1 -p0



%build
python setup.py build



%install
python setup.py install --root $RPM_BUILD_ROOT --skip-build



%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE
%{_bindir}/gyp
%{python_sitelib}/*
