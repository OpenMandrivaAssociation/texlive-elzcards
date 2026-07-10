%global tl_name elzcards
%global tl_revision 51894

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.60
Release:	%{tl_revision}.1
Summary:	Typeset business cards, index cards and flash cards easily
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elzcards
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for typesetting business cards, index cards, and flash
cards in an easy and flexible way, optionally also the reverse side. You
will have to furnish the paper size, the desired size of your card, the
printable area of your printer, and the design of the card. Everything
else is taken care of by elzcards.

