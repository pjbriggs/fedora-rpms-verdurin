Name:           hts-preprocess
Version:        0.1
Release:        1%{?dist}
Summary:        High-Throughput Sequencing preprocessing scripts

Group:          Development/Libraries
License:        GPLv3
URL:            http://hts.rutgers.edu/filter/
Source0:        http://hts.rutgers.edu/filter/preprocess_files.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
# Correct for lots of packages, other common choices include eg. Module::Build
#BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description

A set of Perl scripts and Excel templates to aid with the
preprocessing of Applied Biosystems SOLiD short read sequences.

%prep
%setup -q -c %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -m 0755 *.pl %{buildroot}/usr/bin/



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.xls *.pdf 
%{_bindir}/*.pl


%changelog
* Tue May 25 2010 Adam Huffman <bloch@verdurin.com> - 
- initial version

