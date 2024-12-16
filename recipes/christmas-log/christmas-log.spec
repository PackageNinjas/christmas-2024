#
# spec file for package christmas-log
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           christmas-log
Version:        1.0
Release:        2024
Summary:        Traditional French Christmas cake
License:        CC-BY-SA
URL:            http://127.0.0.1/home/
Source:         -
BuildRequires:  flour
BuildRequires:  sugar
BuildRequires:  eggs
BuildRequires:  cocoa
BuildRequires:  cream
Requires:       oven

%description
Sponge cake roll with log shape.

%prep
%autosetup -p1
mkdir bowl
%oven 180C

%build
mv eggs sugar bowl/
%mix bowl/*

mv flour bowl/
%slow_mix bowl/*

mv bowl/* oven/
%bake -j 10m
mv oven sponge_cake

# filling
%mix cream cocoa
%whip cream

put filling sponge_cake
roll sponge_cake

# topping
%mix cream cocoa
put topping rolled_sponge_cake

%install
# decorate with a fork
%draw "Wood grain"

%files
%doc README.md
%license LICENSE
%{_bindir}/christmas-log

%changelog

