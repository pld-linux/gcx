Summary:	Camera control and data reduction program
Summary(pl.UTF-8):	Program do sterowania aparatem i redukcji danych
Name:		gcx
Version:	0.8.8
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://gcx.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	61e30144404e6a6ede9b92b4d2ec09c7
URL:		http://gcx.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCX provides a complete set of data-reduction functions for CCD
photometry, with frame WCS fitting, automatic target identification,
aperture photometry of target and standard stars, single-frame
ensemble photometry data reduction, multi-frame color coefficient
fitting, extinction coefficient fitting, and all-sky photometry. It
also controls CCD cameras and telescopes.

%description -l pl.UTF-8
GCX dostarcza pełny zestaw funkcji do redukcji danych dla fotometrii
CCD wraz z dopasowywaniem klatek WCD, automatyczną identyfikacją celu,
fotometrią apertury celu i standardowych gwiazd, redukcją danych
fotometrii całościowej pojedynczej klatki, dopasowywaniem
współczynników kolorów dla wielu klatek, dopasowywaniem współczynników
ekstynkcji oraz fotometrią całego nieba. Steruje także aparatami i
teleskopami CCD.

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
