%global tl_name xdoc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	prot2.5
Release:	%{tl_revision}.1
Summary:	Extending the LaTeX doc system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xdoc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Xdoc is a project to rewrite the implementation of the LaTeX doc package
(in a broader sense) to make its features more general and flexible. For
example, where doc only provides commands for documenting macros and
environments, xdoc also provides commands for similarly documenting
package options and switches. This is furthermore done in such a way
that it is very easy to add more such commands for documenting things,
such as e.g., templates (an important concept in the future LaTeX3) and
program components for other languages (functions, classes, procedures,
etc.). A side effect is that many minor bugs in doc are fixed. The
design aims to take advantage of many still experimental features of
future versions of LaTeX, but since these are neither reasonably stable
nor widely available, the configuration interfaces and package author
commands of xdoc are likely to change. To still provide a stable
interface for other packages to build upon, the actual package names
include a "major version number" of sorts. The drop-in replacement
package for standard doc is xdoc2; it requires nothing outside standard
LaTeX2e. The docindex/docidx2e package changes the index and list of
changes typesetting so that none of the formatting has to be controlled
via the index style file. The docindex package provides control of
formatting via templates (nice interface, but requires several
experimental packages), whereas the docidx2e package has traditional raw
macro interfaces and works with standard LaTeX2e.

