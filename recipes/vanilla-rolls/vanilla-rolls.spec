#
# spec file for package vanilla-rolls
#
# Copyright (c) 1683 bakers of Vienna (to mock Osmans)
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


Name:           vanilla-rolls
Version:        2.0
Release:        2024
Summary:	Traditional Christmas sweet coated in vanilla sugar
License:        KPD AND HowWeDoIt  # Kuchařka pro dceru
URL:            https://www.kucharkaprodceru.cz/vanilkove-rohlicky/
Source:         vanilla-rolls.jpg
BuildRequires:  flour = 4 * $spoon
BuildRequires:  butter = 50 g
BuildRequires:  powdered-sugar = $spoon
BuildRequires:  ground-nuts = 2 * $spoon  # provided by ground-hazelnuts, ground-almonds, etc.
BuildRequires:  liquid = $spoon  # provided by water, rum, egg-yolk, etc.
Suggests:       shaping-form[croissant]
Requires(post): powdered-sugar
Requires(post): vanilla-sugar

%description
Delicate Christmas pastries, combining the aromas of sugar, butter, nuts, and love.

%prep
%autosetup -p1
mkdir bowl

%build
mv powdered-sugar flour butter ground-nuts liquid bowl/
%mix bowl/* > dough
sleep $overnight

%cut dough > dough-bits
for bit in dough-bits; do
    %if -e shaping-form/croissant
    	mv bit shaping-form/croissant/
    %else
        %roll bit
        %bend bit
    %endif
done

%install
%bake_rolls --dir vanilla-rolls/

%post
%mix powdered-sugar vanilla-sugar > powdered-vanilla-sugar
powdered-vanilla-sugar >> vanilla-rolls/*

%files
vanilla-rolls

%changelog

