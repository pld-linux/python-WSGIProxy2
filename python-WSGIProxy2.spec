#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	WSGI Proxy with various HTTP client backends
Summary(pl.UTF-8):	Proxy WSGI z różnymi backendami klienta HTTP
Name:		python-WSGIProxy2
# keep 0.4.x here for python2 support
Version:	0.4.6
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wsgiproxy2/
Source0:	https://files.pythonhosted.org/packages/source/W/WSGIProxy2/WSGIProxy2-%{version}.tar.gz
# Source0-md5:	cf4f45bed6ab74ad644bee58bcad4e83
URL:		https://github.com/gawel/WSGIProxy2/
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-WebOb
BuildRequires:	python-requests
BuildRequires:	python-six
BuildRequires:	python-urllib3
BuildRequires:	python-webtest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WSGI Proxy with various HTTP client backends.

%description -l pl.UTF-8
Proxy WSGI z różnymi backendami klienta HTTP.

%package apidocs
Summary:	API documentation for Python WSGIProxy2 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona WSGIProxy2
Group:		Documentation

%description apidocs
API documentation for Python WSGIProxy2 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona WSGIProxy2.

%prep
%setup -q -n WSGIProxy2-%{version}

%build
%py_build

%if %{with tests}
# test_quoted_utf8_url fails with InvalidURL
nosetests-%{py_ver} wsgiproxy -e test_quoted_utf8_url
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYING README.rst
%{py_sitescriptdir}/wsgiproxy
%{py_sitescriptdir}/WSGIProxy2-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
