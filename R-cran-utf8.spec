%define		fversion	%(echo %{version} |tr r -)
%define		modulename	utf8
Summary:	Unicode text processing
Name:		R-cran-%{modulename}
Version:	1.2.6
Release:	2
License:	Apache v2.0
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	12037c186ddded4d9b289762b69fc435
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R

Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode text processing.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
