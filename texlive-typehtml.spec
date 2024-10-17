Name:		texlive-typehtml
Version:	17134
Release:	2
Summary:	Typeset HTML directly from LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/typehtml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Can handle almost all of HTML2, and most of the math fragment
of the draft HTML3.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/typehtml/typehtml.sty
%doc %{_texmfdistdir}/doc/latex/typehtml/README
%doc %{_texmfdistdir}/doc/latex/typehtml/typehtml.pdf
#- source
%doc %{_texmfdistdir}/source/latex/typehtml/typehtml.dtx
%doc %{_texmfdistdir}/source/latex/typehtml/typehtml.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
