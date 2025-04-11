Name:           nlohmann_json
Version:        3.12.0
Release:        1
Summary:        JSON for Modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nlohmann.github.io/json/
Source:         https://github.com/nlohmann/json/archive/v%{version}.tar.gz#/json-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pkgconfig
BuildSystem:    cmake
BuildOption:	-DJSON_BuildTests:BOOL=OFF
BuildOption:	-DJSON_MultipleHeaders:BOOL=ON
BuildOption:	-DNLOHMANN_JSON_CONFIG_INSTALL_DIR="%{_datadir}/cmake/nlohmann_json"

%description
C++11 header-only JSON class

%package devel
Summary:        JSON for Modern C++
Group:          Development/Libraries/C and C++
Requires:       stdc++-devel

%description devel
Development files for a header-only library
to make JSON a first-class datatype for C++11

%files devel
%license LICENSE.MIT
%doc README.md
%{_includedir}/nlohmann
%{_datadir}/cmake/nlohmann_json
%{_datadir}/pkgconfig/nlohmann_json.pc
