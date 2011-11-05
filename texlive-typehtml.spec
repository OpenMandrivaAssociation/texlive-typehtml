# revision 17134
# category Package
# catalog-ctan /macros/latex/contrib/typehtml
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-typehtml
Version:	20100223
Release:	1
Summary:	Typeset HTML directly from LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typehtml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typehtml.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Can handle almost all of HTML2, and most of the math fragment
of the draft HTML3.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/typehtml/typehtml.sty
%doc %{_texmfdistdir}/doc/latex/typehtml/README
%doc %{_texmfdistdir}/doc/latex/typehtml/typehtml.pdf
#- source
%doc %{_texmfdistdir}/source/latex/typehtml/typehtml.dtx
%doc %{_texmfdistdir}/source/latex/typehtml/typehtml.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
