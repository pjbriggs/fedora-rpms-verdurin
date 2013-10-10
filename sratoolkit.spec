%define debug_package %{nil}

#It's a binary RPM so don't want requires or provides
%define _use_internal_dependency_generator 0
%define __find_provides %{nil}
%define __find_requires %{nil}

# Work around fact that archive version is now of the form "2.3.3-4"
# Use of hyphen conflicts with RPM's own versioning scheme
%define sratoolkit_version 2.3.3
%define sratoolkit_release 4


Name:           sratoolkit
Version:        %{sratoolkit_version}.%{sratoolkit_release}
Release:        1%{?dist}
Summary:        Binary distribution of Short Read Archive toolkit

Group:          Applications/Engineering
License:        Public Domain
URL:            http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=show&f=software&m=software&s=software
Source0:        %{name}.2.3.3-4-centos_linux64.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description

Various tools for working with Short Read Archive files, including
conversion tools to other formats

%prep
%setup -n %{name}.%{sratoolkit_version}-%{sratoolkit_release}-centos_linux64

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}
tar zxf %SOURCE0

cd %{name}.%{sratoolkit_version}-%{sratoolkit_release}-centos_linux64
mv README schema %{buildroot}%{_docdir}/%{name}-%{version}
mv bin/* %{buildroot}%{_bindir}
cd ..
rm -rf %{name}.%{sratoolkit_version}-%{sratoolkit_release}-centos_linux64

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/schema

%{_bindir}/*

%changelog
* Thu Oct 10 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.3.3-1
- Updated sratoolkit to version 2.3.3-4

* Wed Dec 14 2011 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.1.8-1
- Updated sratoolkit to version 2.1.8

* Tue Aug  2 2011 Adam Huffman <bloch@verdurin.com> - 2.1.2-1
- initial version

