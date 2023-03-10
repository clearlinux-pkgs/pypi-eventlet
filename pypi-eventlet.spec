#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-eventlet
Version  : 0.33.3
Release  : 1
URL      : https://files.pythonhosted.org/packages/81/0c/5e0bcf715a2bae9169c77bfdcbc460a4aeeb0bb1067cf8071cf14d7d1b39/eventlet-0.33.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/0c/5e0bcf715a2bae9169c77bfdcbc460a4aeeb0bb1067cf8071cf14d7d1b39/eventlet-0.33.3.tar.gz
Summary  : Highly concurrent networking library
Group    : Development/Tools
License  : MIT
Requires: pypi-eventlet-license = %{version}-%{release}
Requires: pypi-eventlet-python = %{version}-%{release}
Requires: pypi-eventlet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pypi(dnspython)
BuildRequires : pypi(greenlet)
BuildRequires : pypi(six)
BuildRequires : pypi-nose
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

%package license
Summary: license components for the pypi-eventlet package.
Group: Default

%description license
license components for the pypi-eventlet package.


%package python
Summary: python components for the pypi-eventlet package.
Group: Default
Requires: pypi-eventlet-python3 = %{version}-%{release}

%description python
python components for the pypi-eventlet package.


%package python3
Summary: python3 components for the pypi-eventlet package.
Group: Default
Requires: python3-core
Provides: pypi(eventlet)
Requires: pypi(dnspython)
Requires: pypi(greenlet)
Requires: pypi(six)

%description python3
python3 components for the pypi-eventlet package.


%prep
%setup -q -n eventlet-0.33.3
cd %{_builddir}/eventlet-0.33.3
pushd ..
cp -a eventlet-0.33.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677268293
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-eventlet
cp %{_builddir}/eventlet-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-eventlet/ad33faded4baaba18a31704973874c531e94d910 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-eventlet/ad33faded4baaba18a31704973874c531e94d910

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
