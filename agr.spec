Name:           agr
Version:        0.8.4
Release:        %autorelease
Summary:        A package manager for AI agents

License:        MIT
URL:            https://github.com/computerlovetech/agr
Source:         %{url}/archive/v%{version}/agr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A package manager for AI agents. Install agent skills from GitHub
with a single command.}

%description %_description

%package -n python3-agr
Summary:        %{summary}

%description -n python3-agr %_description


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l agr agrx


%check
%pytest
%pyproject_check_import


%files -n agr -f %{pyproject_files}
%doc README.*
%{_bindir}/agr
%{_bindir}/agrx


%changelog
%autochangelog
