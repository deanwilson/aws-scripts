Name:           aws-regions
Version:        1.0.0
Release:        1%{?dist}
Summary:        Command line tool to print the AWS region code and descriptive name

License:        GPLv2
URL:            https://github.com/deanwilson/aws-scripts
Source0:        https://raw.githubusercontent.com/deanwilson/aws-scripts/master/aws-regions.go

BuildRequires:  golang > 1.4

%description
A simple command line tool to print the AWS region code and description.
Written to stop people asking 'Is that one Virginia?'

%prep
cp %{SOURCE0} .

%build
export GOPATH="$PWD"
go build -o %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Mon Sep 07 2015 Dean Wilson <dean.wilson@gmail.com> - 1.0.0-1
- Initial RPM release
