#
# spec file for package beehives
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


Name:           beehives
Version:        2024.12.24
Release:        0
Summary:        No-Bake Czech Christmas Beehives
License:        GPL-3.0-or-later
Group:          Holidays/Christmas
URL:            http://traditionalczechrecipes.cz/beehives
Source0:        beehives.tar.gz
BuildRequires:  butter >= 110g
BuildRequires:  cocoa >= 2-tbsp
BuildRequires:  egg-yolk >= 1
BuildRequires:  hazelnuts >= 70g
BuildRequires:  milk >= 3-tbsp
BuildRequires:  powdered-sugar >= 150g
# Default rum amount is 50ml, but rumors claim that doubling it makes the beehives "way better"
# Uncomment the following line for the festive and more joyful version:
# BuildRequires:  rum >= 100ml
BuildRequires:  rum >= 50ml
# These are called "piškoty" or "dětské piškoty" in Czech. They are round sponge biscuits,
# similar to soft vanilla wafers or small baby sponge biscuits commonly used in Central European desserts.
# Think of them as a smaller, round version of ladyfingers.
BuildRequires:  round-sponge-biscuits >= 160g
Requires:       hive-mold
Requires:       round-sponge-biscuits

%description
Beehives (Vosí hnízda) are an iconic Czech no-bake Christmas treat.
These sweet confections are made from a rich cocoa dough and filled with creamy, rum-infused filling.

%prep
%setup -q
mkdir -p build/dough
mkdir -p build/filling
echo "Grinding ingredients for dough..."
mv sponge-biscuits hazelnuts build/dough
grind --source=build/dough --output=build/ground-mix
echo "Adding butter, sugar, cocoa, milk, and rum to dough..."
combine build/ground-mix butter sugar cocoa milk rum --output=build/dough
echo "Checking dough consistency..."
if ! [ "$(check-consistency build/dough)" = "pliable" ]; then
    echo "Error: Dough not pliable, adjusting with more milk/rum"
    adjust-consistency build/dough
fi

%build
echo "Preparing filling..."
mix --source=butter powdered-sugar egg-yolk rum --output=build/filling
echo "Shaping beehives..."
shape --dough=build/dough --mold=hive --filling=build/filling --base=round-biscuits --output=build/beehives
if ! [ "$(check-structure build/beehives)" = "stable" ]; then
    echo "Warning: Beehives unstable, re-checking molds"
    retry-shape build/beehives
fi

%install
echo "Final touch: Arranging beehives for presentation..."
arrange build/beehives --style="festive"

%files
%doc README.md
%license LICENSE
%{_bindir}/beehives

%changelog
