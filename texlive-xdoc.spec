# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xdoc
# catalog-date 2006-12-05 00:47:24 +0100
# catalog-license lppl
# catalog-version prot2.5
Name:		texlive-xdoc
Version:	prot2.5
Release:	2
Summary:	Extending the LaTeX doc system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xdoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Xdoc is a project to rewrite the implementation of the LaTeX
doc package (in a broader sense) to make its features more
general and flexible. For example, where doc only provides
commands for documenting macros and environments, xdoc also
provides commands for similarly documenting package options and
switches. This is furthermore done in such a way that it is
very easy to add more such commands for documenting things,
such as e.g., templates (an important concept in the future
LaTeX3) and program components for other languages (functions,
classes, procedures, etc.). A side effect is that many minor
bugs in doc are fixed. The design aims to take advantage of
many still experimental features of future versions of LaTeX,
but since these are neither reasonably stable nor widely
available, the configuration interfaces and package author
commands of xdoc are likely to change. To still provide a
stable interface for other packages to build upon, the actual
package names include a "major version number" of sorts. The
drop-in replacement package for standard doc is xdoc2; it
requires nothing outside standard LaTeX2e. The
docindex/docidx2e package changes the index and list of changes
typesetting so that none of the formatting has to be controlled
via the index style file. The docindex package provides control
of formatting via templates (nice interface, but requires
several experimental packages), whereas the docidx2e package
has traditional raw macro interfaces and works with standard
LaTeX2e.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/xdoc/docindex.ist
%{_texmfdistdir}/tex/latex/xdoc/docidx2e.sty
%{_texmfdistdir}/tex/latex/xdoc/docindex.sty
%{_texmfdistdir}/tex/latex/xdoc/xdoc2.sty
%doc %{_texmfdistdir}/doc/latex/xdoc/README
%doc %{_texmfdistdir}/doc/latex/xdoc/docindex.pdf
%doc %{_texmfdistdir}/doc/latex/xdoc/xdoc2.pdf
%doc %{_texmfdistdir}/doc/latex/xdoc/xdocdemo.pdf
%doc %{_texmfdistdir}/doc/latex/xdoc/xdocdemo.tex
#- source
%doc %{_texmfdistdir}/source/latex/xdoc/docindex.dtx
%doc %{_texmfdistdir}/source/latex/xdoc/docindex.ins
%doc %{_texmfdistdir}/source/latex/xdoc/xdoc2.dtx
%doc %{_texmfdistdir}/source/latex/xdoc/xdoc2.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
