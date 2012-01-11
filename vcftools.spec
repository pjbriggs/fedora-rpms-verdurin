Name:		vcftools
Version:	0.1.7
Release:	1%{?dist}
Summary:	VCF file manipulation tools

Group:		Applications/Engineering
License:	GPLv3 
URL:		http://vcftools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}_%{version}.tar.gz
Patch0:		vcftools-perl-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel


%description
A program package designed for working with VCF files, such as those
generated by the 1000 Genomes Project. The aim of VCFtools is to
provide methods for working with VCF files: validating, merging,
comparing and calculate some basic population genetic statistics.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
make %{?_smp_mflags} CPPFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}/usr MODDIR="%{buildroot}/%{perl_vendorarch}" \
BINDIR="%{buildroot}/%{_bindir}"

install -m 0775 %{_builddir}/%{name}_%{version}/cpp/vcftools %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/vcf-compare
%{_bindir}/fill-aa
%{_bindir}/fill-an-ac
#%%{_bindir}/fill-rsIDs
%{_bindir}/vcf-merge
%{_bindir}/vcf-query
%{_bindir}/vcf-annotate
%{_bindir}/vcf-concat
%{_bindir}/vcf-convert
%{_bindir}/vcf-isec
%{_bindir}/vcf-sort
%{_bindir}/vcf-stats
%{_bindir}/vcf-subset
%{_bindir}/vcf-to-tab
%{_bindir}/vcf-validator
%attr(0755, root, root) %{_bindir}/vcftools
%{perl_vendorarch}/FaSlice.pm
%{perl_vendorarch}/Vcf.pm
%{perl_vendorarch}/VcfStats.pm

%changelog
* Thu Jan  5 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.1.7-1
- update to upstream release 0.1.7
- remove fill-rsIDs
- update Perl makefile patch

* Sun Jul 31 2011 Adam Huffman <bloch@verdurin.com> - 0.1.6-1
- update to 0.1.6

* Tue May  3 2011 Adam Huffman <bloch@verdurin.com> - 0.1.5-2
- minor fix to Jack's Perl patch
- permissions fix
- hardcoded path fix
- cleaner Makefile fix

* Sun May 1 2011 Jack Tanner <ihok@hotmail.com> - 0.1.5-1
- bump to 0.1.5
- rename compare-vcf, merge-vcf, and query-vcf to vcf-compare,
  vcf-merge, and vcf-query
- add VcfStats.pm to perl export
- patch perl/Makefile to export VcfStats.pm

* Mon Mar 21 2011 Adam Huffman <bloch@verdurin.com> - 0.1.4a-1
- initial version
- fix CPPFLAGS
- fix hardcoded installation location

