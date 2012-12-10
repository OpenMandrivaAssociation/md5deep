Summary:	Compute MD5 message digests on an arbitrary number of files
Name:		md5deep
Version:	4.1
Release:	1
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


%changelog
* Fri Mar 23 2012 Andrey Bondrov <abondrov@mandriva.org> 4.1-1
+ Revision: 786418
- New version 4.1

* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.1-1
+ Revision: 771290
- version update 4.0.1

* Mon Jan 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.0-1
+ Revision: 759165
- version update 4.0.0

* Thu Dec 22 2011 Andrey Bondrov <abondrov@mandriva.org> 3.9.2-1
+ Revision: 744466
- New version 3.9.2

* Mon Mar 14 2011 Stéphane Téletchéa <steletch@mandriva.org> 3.7-1
+ Revision: 644719
- update to new version 3.7

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.1-3mdv2011.0
+ Revision: 612842
- the mass rebuild of 2010.1 packages

* Mon Feb 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.5.1-2mdv2010.1
+ Revision: 499134
- Increment release
- Use %%configure2_5x instead of %%configure

* Fri Jan 01 2010 Jérôme Brenier <incubusss@mandriva.org> 3.5.1-1mdv2010.1
+ Revision: 484641
- new version 3.5.1
- use %%configure instead of %%configure2_5x
- finish to remove Patch0

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.1-2mdv2010.0
+ Revision: 439792
- rebuild

* Mon Oct 27 2008 Funda Wang <fwang@mandriva.org> 3.1-1mdv2009.1
+ Revision: 297521
- New version 3.1

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.13-3mdv2009.0
+ Revision: 252177
- rebuild
- fix no-buildroot-tag

* Thu Feb 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2008.1
+ Revision: 163682
- update to new version 1.13
- update to new version 1.13

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.12-1mdv2007.0
- 1.12
- rediffed P0

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdk
- rebuild

* Sun May 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-2mdk
- fix the %%vendor and %%distribution string

* Mon Apr 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-1mdk
- 1.2
- added P0
- added the sha1deep stuff

