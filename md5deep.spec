Summary:	Compute MD5 message digests on an arbitrary number of files
Name:		md5deep
Version:	4.1
Release:	3
Group:		File tools
License:	Public Domain and GPLv2+
URL:		http://md5deep.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/md5deep/md5deep/md5deep-4.0.0/%{name}-%{version}.tar.gz

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*

