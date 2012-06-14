Name:		fastq_screen
Version:	0.3.1
Release:	1%{?dist}
Summary:	Contamination screening for next-gen sequence data

Group:		Applications/Engineering
License:	GPLv3+
URL:		http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/
Source0:	http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/%{name}_v%{version}.tar.gz
Source1:	%{name}-README.Fedora
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	bowtie

%description

FastQ Screen provides a simple way to screen a library of short reads
against a set of reference libraries. Its most common use is as part
of a QC pipeline to confirm that a library comes from the expected
source, and to help identify any sources of contamination.

%prep
%setup -q -n FastQScreen_v%{version}

cp -p %{SOURCE1} .

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt license.txt RELEASE_NOTES.txt fastq_screen-README.Fedora
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}


%changelog
* Wed Jun 13 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.3.1-1
- updated to version 0.3.1

* Wed Aug 10 2011 Adam Huffman <bloch@verdurin.com> - 0.2.1-2
- add README explaining use of fastq_screen.conf

* Fri Aug  5 2011 Adam Huffman <bloch@verdurin.com> - 0.2.1-1
- initial version

