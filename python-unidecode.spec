%define		module	Unidecode
Summary:	ASCII transliterations of Unicode text
Name:		python-%{module}
Version:	0.04.1
Release:	1
License:	GPL v1+ or Artistic
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/U/Unidecode/%{module}-%{version}.tar.gz
# Source0-md5:	c4c9ed8d40cff25c390ff5d5112b9308
URL:		http://pypi.python.org/pypi/Unidecode/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unidecode provides a function, 'unidecode(...)' that takes Unicode
data and tries to represent it in ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at transliteration -- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text
in some other writing system.

This is a Python port of Text::Unidecode Perl module by Sean M. Burke
<sburke@cpan.org>.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/unidecode
