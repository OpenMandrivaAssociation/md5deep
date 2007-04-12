Summary:	Compute MD5 message digests on an arbitrary number of files
Name:		md5deep
Version:	1.12
Release:	%mkrel 1
Group:		File tools
License:	Public Domain
URL:		http://md5deep.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/md5deep/%{name}-%{version}.tar.bz2
Patch0:		md5deep-1.12-optflags.diff
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
md5deep is a cross-platform program to compute MD5 message digests
on an arbitrary number of files. The program is known to run on
Windows(tm), Linux, FreeBSD, OS X, Solaris, and should run on most
other platforms. md5deep is similar to the md5sum program found in
the GNU Coreutils package, but has the following additional
features: 

* Recursive operation - md5deep is able to recursive examine an
  entire directory tree. That is, compute the MD5 for every file
  in a directory andf for every file in every subdirectory. 

* Time estimation - md5deep can produce a time estimate when it's
  processing very large files. 

* Comparison mode - md5deep can accept a list of known hashes and
  compare them to a set of input files. The program can display
  either those input files that match the list of known hashes or
  those that do not match. 

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 md5deep %{buildroot}%{_bindir}/
install -m0755 sha1deep %{buildroot}%{_bindir}/
install -m0755 sha256deep %{buildroot}%{_bindir}/
install -m0755 tigerdeep %{buildroot}%{_bindir}/
install -m0755 whirlpooldeep %{buildroot}%{_bindir}/
 
install -m0644 md5deep.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/md5deep
%{_bindir}/sha1deep
%{_bindir}/sha256deep
%{_bindir}/tigerdeep
%{_bindir}/whirlpooldeep
%{_mandir}/man1/md5deep.1*

