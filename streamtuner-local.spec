Summary:	Plugin for streamtuner providing access to local music collection
Summary(pl):	Wtyczka dla streamtunera daj±ca dostêp do lokalnej kolekcji muzyki
Name:		streamtuner-local
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/streamtuner/%{name}-%{version}.tar.gz
# Source0-md5:	b400e40b6e4e0f603ea0d706dcf0f90a
Patch0:		%{name}-gcc34.patch
URL:		http://www.nongnu.org/streamtuner/
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libid3tag-devel >= 0.15.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	streamtuner-devel >= 0.12.0
Requires:	streamtuner >= 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin providing access to your local music collection. It can read
and modify ID3 and Vorbis metadata.

%description -l pl
Wtyczka dla streamtunera daj±ca dostêp do lokalnej kolekcji muzyki.
Dziêki tej wtyczce mo¿na odczytywaæ i modyfikowaæ metadane ID3 i
Vorbis.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/streamtuner/plugins/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/streamtuner/plugins/*.so
