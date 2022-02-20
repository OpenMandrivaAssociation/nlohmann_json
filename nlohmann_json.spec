Name:           nlohmann_json
Version:        3.10.5
Release:        1
Summary:        JSON for Modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nlohmann.github.io/json/
Source:         https://github.com/nlohmann/json/archive/v%{version}.tar.gz#/json-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig

%description
C++11 header-only JSON class

%package devel
Summary:        JSON for Modern C++
Group:          Development/Libraries/C and C++
Requires:       stdc++-devel

%description devel
Development files for a header-only library
to make JSON a first-class datatype for C++11

%prep
%autosetup -n json-%{version} -p1

%build
%cmake \
  -DJSON_BuildTests:BOOL=OFF \
  -DJSON_MultipleHeaders=ON \
  -DNLOHMANN_JSON_CONFIG_INSTALL_DIR="%{_libdir}/cmake/nlohmann_json"

%make_build

%install
%make_install -C build

%files devel
%license LICENSE.MIT
%doc README.md
%{_includedir}/nlohmann
%dir %{_libdir}/cmake/nlohmann_json
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonConfigVersion.cmake
%{_libdir}/cmake/nlohmann_json/nlohmann_jsonTargets.cmake
%{_libdir}/pkgconfig/nlohmann_json.pc
