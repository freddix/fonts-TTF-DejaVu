%define		rname	dejavu

Summary:	Bitstream Vera True Type fonts fork with latin-ext-A characters
Name:		fonts-TTF-DejaVu
Version:	2.34
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://downloads.sourceforge.net/project/dejavu/dejavu/%{version}/%{rname}-fonts-ttf-%{version}.tar.bz2
# Source0-md5:	161462de16e2ca79873bc2b0d2e6c74c
URL:		http://dejavu-fonts.org/wiki/Main_Page
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
DejaVu is a set of fonts based on Bitstream Vera fonts which have
additional characters from Latin Extended-A set.

%prep
%setup -qn %{rname}-fonts-ttf-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install ttf/*.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
install fontconfig/*.conf $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail

cd fontconfig
for file in *.conf; do
    ln -s %{_datadir}/fontconfig/conf.avail/$file $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README NEWS
%{_ttffontsdir}/*
%{_datadir}/fontconfig/conf.avail/*.conf
%{_sysconfdir}/fonts/conf.d/*.conf

