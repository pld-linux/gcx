Summary:	Camera control and data reduction program
Name:		gcx
Version:	0.7.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://astro.corlan.net/gcx/%{name}-%{version}.tar.gz
# Source0-md5:	bee64597bfbb0c011a7d164b21c9f81f
URL:		http://astro.corlan.net/gcx/index.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCX provides a complete set of data-reduction functions for CCD
photometry, with frame WCS fitting, automatic target identification,
aperture photometry of target and standard stars, single-frame
ensemble photometry data reduction, multi-frame color coefficient
fitting, extinction coefficient fitting, and all-sky photometry. It
also controls CCD cameras and telescopes.

%prep
%setup -q

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog docs/gcx.pdf
%attr(755,root,root) %{_bindir}/*
