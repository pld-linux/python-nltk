
%define		module	nltk
%define		pre	rc1

Summary:	Natural Language Toolkit
Summary(pl.UTF-8):	Przybornik obsługi języków naturalnych (Natural Language Toolkit)
Name:		python-%{module}
Version:	2.0.1
Release:	0.%{pre}.2
License:	GPL
Group:		Libraries/Python
Source0:	http://nltk.googlecode.com/files/%{module}-%{version}%{pre}.zip
# Source0-md5:	72f745eefd659aea23a44bf1e47e7b9d
URL:		http://www.nltk.org/
BuildRequires:	pydoc
BuildRequires:	python-devel
BuildRequires:	python-PyYAML
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
%pyrequires_eq	python
Requires:	python-PyYAML
Suggests:	python-numpy
Suggests:	python-matplotlib
Suggests:	prover9
#Suggests:	MaltParser: http://w3.msi.vxu.se/~jha/maltparser/dist/malt-1.2.tar.gz
#Suggests:	MegaM: http://hal3.name/megam/megam_src.tgz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Language Toolkit is a Python module for
processing natural language text.

%description -l pl.UTF-8
Natural Language Toolkit jest modułem języka Python
przetwarzającym tekst w języku naturalnym.

%prep
%setup  -q -n %{module}-%{version}%{pre}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{py_sitescriptdir}/*
