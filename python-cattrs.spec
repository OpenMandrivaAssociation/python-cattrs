%define module cattrs

Name:		python-cattrs
Version:	25.3.0
Release:	1
Summary:	Composable complex class support for attrs and dataclasses.
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/cattrs/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Composable complex class support for attrs and dataclasses.

%files
%{py_sitedir}/cattr
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
