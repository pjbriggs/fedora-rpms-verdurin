Name:		    MACS
Version:	    1.4.2
Release:	    1%{?dist}
Summary:	    Model-based Analysis for ChIP-Seq

Group:		    Applications/Engineering
License:	    Artistic 2.0
URL:		    http://liulab.dfci.harvard.edu/MACS/index.html
#Source now available on Github
#Source0:   https://github.com/taoliu/MACS/tarball/v1.4.1
Source0:	    taoliu-MACS-v1.4.2-0-g26a7258.tar.gz
patch0:		    MACS-macs142-version.patch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	    noarch
BuildRequires:	    python-devel


%description

Next generation parallel sequencing technologies made chromatin
immunoprecipitation followed by sequencing (ChIP-Seq) a popular
strategy to study genome-wide protein-DNA interactions, while creating
challenges for analysis algorithms. We present Model-based Analysis of
ChIP-Seq (MACS) on short reads sequencers such as Genome Analyzer
(Illumina / Solexa). MACS empirically models the length of the
sequenced ChIP fragments, which tends to be shorter than sonication or
library construction size estimates, and uses it to improve the
spatial resolution of predicted binding sites. MACS also uses a
dynamic Poisson distribution to effectively capture local biases in
the genome sequence, allowing for more sensitive and robust
prediction. MACS compares favorably to existing ChIP-Seq peak-finding
algorithms, is publicly available open source, and can be used for
ChIP-Seq with or without control samples.

%prep
%setup -q -n taoliu-MACS-94f2543
# Patch to fix bad version number in 'macs14'
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 DEBIAN/macs.man %{buildroot}/%{_mandir}/man1/macs.1

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README ChangeLog COPYING NEW_IN_MACS14
%{_mandir}/man1/macs.1.*
%{python_sitelib}/%{name}*
%{python_sitelib}/%{name}-%{version}-py*.egg*
%{_bindir}/macs14
%{_bindir}/eland*
%{_bindir}/sam2bed
%{_bindir}/wignorm

%changelog
* Wed Apr 11 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.4.2-1
- new upstream release 1.4.2
- see https://github.com/taoliu/MACS/blob/macs_v1/ChangeLog for fixes

* Sun Oct  9 2011 Adam Huffman <bloch@verdurin.com> - 1.4.1-2
- remove EPEL-specific macros
- make files and manpages more specific

* Wed Jun 29 2011 Adam Huffman <bloch@verdurin.com> - 1.4.1-1
- new upstream release 1.4.1
- see https://github.com/taoliu/MACS/blob/macs_v1/ChangeLog for fixes

* Fri Jun 24 2011 Adam Huffman <bloch@verdurin.com> - 1.4.0-1
- add manpage generated for Debian

* Tue Jun 21 2011 Adam Huffman <bloch@verdurin.com> - 1.4.0-1
- final 1.4.0 release
- see https://raw.github.com/taoliu/MACS/v1.4.0/ChangeLog

* Thu Apr 21 2011 Adam Huffman <bloch@verdurin.com> - 1.4.0-0.1.rc2
- new upstream release
- new binary names

* Thu Dec 16 2010 Adam Huffman <bloch@verdurin.com> - 1.4.0beta-1
- initial version

