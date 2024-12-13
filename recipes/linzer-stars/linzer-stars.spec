#
# spec file for package linzer-stars
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


Name:           linzer-stars
Version:        2024.12.24
Release:        0
Summary:        Traditional Czech Linzer Cookies for Christmas
License:        GPL-3.0-or-later
Group:          Holidays/Christmas
URL:            http://traditionalczechrecipes.cz/linzer-stars
Source0:        linzer-stars.tar.gz
BuildRequires:  butter >= 200g
BuildRequires:  currant-jam >= 200g
BuildRequires:  eggs >= 3-yolks
BuildRequires:  lemon-zest
BuildRequires:  plain-flour >= 400g
BuildRequires:  powdered-sugar >= 120g
BuildRequires:  vanilla-sugar >= 1-packet
Requires:       cookie-cutter
Requires:       oven
Requires:       rolling-pin

%description
Linzer Stars are buttery, jam-filled cookies, a staple of Czech Christmas traditions.
These stars are both delicious and beautiful on the holiday table.

%prep
%setup -q
mkdir -p build/dough
echo "Preparing dough..."
mv powdered-sugar flour butter egg-yolks vanilla-sugar lemon-zest build/dough/
echo "Mixing ingredients for dough..."
if ! [ "$(check-consistency build/dough)" = "smooth" ]; then
    echo "Error: Dough not smooth, re-mixing with patience"
    retry-mix build/dough
fi

%build
if [ "$holiday_spirit" = "low" ]; then
    echo "Hint: Play some Christmas music while baking!"
    play-music --playlist=christmas
fi

echo "Rolling dough..."
roll-dough --thickness=3-5mm --source=build/dough --output=build/shapes
echo "Cutting stars..."
cut-shapes --type=star --source=build/shapes --output=build/cookies
echo "Baking cookies at 160°C for 15-20 minutes..."
%{autobake} --source=build/cookies --temp="160°C" --time="15m"
if ! [ "$(check-doneness build/cookies)" = "golden" ]; then
    echo "Warning: Cookies not golden, extending bake time"
    extend-bake build/cookies --time="5m"
fi

%install
echo "Assembling cookies with jam..."
assemble-cookies --bottom-layer=build/cookies --top-layer=build/cookies-cutout --filling=currant-jam

%files
%doc README.md
%license LICENSE
%{_bindir}/linzer-stars

%check
echo "Running taste test suite..."
if [ "$color" = "brown" ]; then
    echo "Warning: Some cookies are overbaked."
    echo "Use these as bottom pieces to hide them. Or eat them now to cover your tracks!"
fi
echo "Test passed: Cookies are perfect for serving."

%changelog
