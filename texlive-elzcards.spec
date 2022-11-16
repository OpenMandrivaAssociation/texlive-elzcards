Name:		texlive-elzcards
Version:	51894
Release:	1
Summary:	Typeset business cards, index cards and flash cards easily
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elzcards
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elzcards.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for typesetting business cards, index cards,
and flash cards in an easy and flexible way, optionally also
the reverse side. You will have to furnish the paper size, the
desired size of your card, the printable area of your printer,
and the design of the card. Everything else is taken care of by
elzcards.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/elzcards
%{_texmfdistdir}/tex/latex/elzcards
%doc %{_texmfdistdir}/doc/latex/elzcards

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
