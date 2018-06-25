# revision 17134
# category Package
# catalog-ctan /macros/latex/contrib/typehtml
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-typehtml
Version:	20180303
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100223-2
+ Revision: 757167
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100223-1
+ Revision: 719826
- texlive-typehtml
- texlive-typehtml
- texlive-typehtml

