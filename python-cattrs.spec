Name:		python-cattrs
Version:	25.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
Summary:	Composable complex class support for attrs and dataclasses.
URL:		https://pypi.org/project/cattrs/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-hatchling
BuildSystem:	python
BuildArch:	noarch

%description
Composable complex class support for attrs and dataclasses.

%files
%{py_sitedir}/cattr/
%{py_sitedir}/cattrs
%{py_sitedir}/cattrs-*.*-info
