
%define	module	nltk

Summary:	Natural Language Toolkit
Summary(pl.UTF-8):	Przybornik obsługi języków naturalnych (Natural Language Toolkit)
Name:		python-%{module}
Version:	0.9.8
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://nltk.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	18a6dfd1ff9032f57f905361a453cb32
#Patch0:		%{name}-no-similarity.patch
URL:		http://www.nltk.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Language Toolkit (NLTK-Lite) is a Python module for
processing natural language text. It was developed as a simpler,
lightweight version of NLTK.

%description -l pl.UTF-8
Natural Language Toolkit (NLTK-Lite) jest modułem języka Python
przetwarzającym tekst w języku naturalnym. Został on stworzony
jako prostsza, lekka wersja NLTK.

%prep
%setup  -q -n %{module}-%{version}
#%patch0 -p1

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
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
