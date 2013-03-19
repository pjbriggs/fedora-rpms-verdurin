Name:		BEDTools
Version:	2.15.0
Release:	1%{?dist}
Summary:	A flexible suite of utilities for comparing genomic features

Group:		Applications/Engineering
License:	GPLv2+
URL:		http://code.google.com/p/bedtools/

# Download is listed in an RPM-unfriendly way on the Google Code site
# The file can be obtained at
# http://bedtools.googlecode.com/files/BEDTools.v2.13.4.tar.gz

Source0:	http://bedtools.googlecode.com/files/%{name}.v%{version}.tar.gz
Source1:	http://bedtools.googlecode.com/files/%{name}-User-Manual.v4.pdf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	  zlib-devel
BuildRequires:	  python

%description

The BEDTools utilities allow one to address common genomics tasks such
as finding feature overlaps and computing coverage. The utilities are
largely based on four widely-used file formats: BED, GFF/GTF, VCF, and
SAM/BAM. Using BEDTools, one can develop sophisticated pipelines that
answer complicated research questions by "streaming" several BEDTools
together. 

%package  docs
Summary:  Manual for BEDTools
Group:	  Documentation
License:  GPLv2

%description docs

PDF manual for the BEDTools utilities.


%prep
%setup -q -n %{name}-Version-%{version}

# remove bundled curl library
rm -rf src/utils/curl

# add manual
cp -p %{SOURCE1} .

%build
# gzstream includes a local header file
make %{?_smp_mflags} CXXFLAGS="-I. %{optflags}"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/* %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{_datadir}/%{name}

cp -a genomes/ %{buildroot}/%{_datadir}/%{name}
cp -a data/ %{buildroot}/%{_datadir}/%{name}
# fix permissions
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 0644 {} \;


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.rst RELEASE_HISTORY LICENSE 
%dir %{_datadir}/%{name}
%{_bindir}/annotateBed
%{_bindir}/bamToBed
%{_bindir}/bed12ToBed6
%{_bindir}/bedpeToBam
%{_bindir}/bedToBam
%{_bindir}/bedToIgv
%{_bindir}/bedtools
%{_bindir}/closestBed
%{_bindir}/clusterBed
%{_bindir}/complementBed
%{_bindir}/coverageBed
#%{_bindir}/cuffToTrans
%{_bindir}/fastaFromBed
#%{_bindir}/fjoin
%{_bindir}/flankBed
%{_bindir}/genomeCoverageBed
%{_bindir}/getOverlap
%{_bindir}/groupBy
%{_bindir}/intersectBed
%{_bindir}/linksBed
%{_bindir}/maskFastaFromBed
%{_bindir}/mergeBed
%{_bindir}/multiBamCov
%{_bindir}/multiIntersectBed
%{_bindir}/nucBed
%{_bindir}/pairToBed
%{_bindir}/pairToPair
%{_bindir}/shuffleBed
%{_bindir}/slopBed
%{_bindir}/sortBed
%{_bindir}/subtractBed
%{_bindir}/tagBam
%{_bindir}/unionBedGraphs
%{_bindir}/windowBed
%{_bindir}/windowMaker

%{_datadir}/%{name}/genomes
%{_datadir}/%{name}/data

%files docs
%defattr(-,root,root,-)
%doc %{name}-User-Manual.v4.pdf

%changelog
* Wed Jan  4 2012 Adam Huffman <verdurin@fedoraproject.org> - 2.15.0-1
- update to new upstream release 2.15.0
- new unified command line interface 'bedtools'
- add python BR for new Makefile target to generate legacy commands
- remove 'overlap'
- add 'bedpeToBam', 'clusterBed', 'getOverlap', 'groupBy'
- add 'multiIntersectBed', 'windowMaker'

* Fri Oct 28 2011 Adam Huffman <bloch@verdurin.com> - 2.13.4-1
- new upstream minor bugfix release, see http://code.google.com/p/bedtools/

* Thu Sep  8 2011 Adam Huffman <bloch@verdurin.com> - 2.13.1-1
- new upstream minor release including fixes for tagBam

* Tue Sep  6 2011 Adam Huffman <bloch@verdurin.com> - 2.13.0-1
- new upstream release 2.13.0
- new tools tagBam and nucBed

* Tue Apr 12 2011 Adam Huffman <bloch@verdurin.com> - 2.12.0-1
- new upstream release 2.12.0
- new tools cuffToTrans and flankBed

* Thu Feb 17 2011 Adam Huffman <bloch@verdurin.com> - 2.11.2-1
- new upstream release
- now README.rst
- remove groupBy command, now in filo
- new fjoin command

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Adam Huffman <bloch@verdurin.com> - 2.10.1-1
- new annotateBed tool
- updated manual

* Sun Sep 12 2010 Adam Huffman <bloch@verdurin.com> - 2.9.0-5
- add license for -docs 

* Wed Sep  1 2010 Adam Huffman <bloch@verdurin.com> - 2.9.0-4
- add -docs subpackage including PDF manual

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 2.9.0-3
- remove 'curl' library properly

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 2.9.0-2
- fix license and add LICENSE file
- fix permissions of data/
- remove bundled 'curl' library

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 2.9.0-1
- new upstream release
- add new unionBedGraphs tool

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 2.8.3-1
- initial version
- override upstream CFLAGS
- allow including gzstream header file
