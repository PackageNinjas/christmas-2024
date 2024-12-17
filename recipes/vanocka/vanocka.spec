#
# spec file for package vanocka
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


# Yes, Virginia, RPM SPEC files are defined as UTF-8 not just ASCII (don't try in OBS, though)
Name:           vánočka
Version:        1.0
Release:        2024
Summary:        Traditional Czech Christmas Bread
License:        CC-BY-SA
URL:            http://127.0.0.1/home/
# Actually, this is reall Message-ID of the email, where we got this recipe
# I have still the message saved in my archives
Source:         email:<1.5.4.16.19961213013601.1c3fda3c@popserver.vol.cz>
BuildRequires:  half-coarse flour >= 500g  # also possible to use fine flour
BuildRequires:  baking powder = %coffeespoon
BuildRequires:  raisins >= 50g
BuildRequires:  chopped skinned almonds >= 40g
BuildRequires:  yeast >= 30g
BuildRequires:  sugar >= 120g
BuildRequires:  salt > %little  # otherwise the dough is tasteless
BuildRequires:  baking fat >= 70g # slightly less if fine flour is used
BuildRequires:  butter >= 60g
BuildRequires:  yolk = 2
BuildRequires:  milk >= 250ml
Requires:       kitchen_temperature > 20C  # yeast is alive, it dies when not warm
Requires:       oven
Requires:       large-bowl
Requires:       kneading-machine || strong-husband

%description
Plaited bread, baked in Czech Republic and Slovakia (in Slovak
called vianočka) traditionally at Christmas time. Somewhat
similar to the German Stollen.

When we were for the first time with Markéta on our own doing
Christmas, and it was in the United States, Markéta’s mum sent us
a set of recipes (notice the consideration of American reality,
where there are no different types of flour readily available and
there is just something which would be roughly an equivalent of
the Czech fine flour). We have been doing this every Christmas
ever since.

%prep
%autosetup -p1
mkdir bowl
%oven 180C

%build
MUG=$(warm-milk 30C)  # not less, not much more, or you kill the yeast
MUG+=$(crumble %yeast)
MUG+=%sugar
MUG+=$(amount %flour teaspoon)  # yeast needs to be fed
keep_warm $MUG       # keep the termperature

POT=$(warm-milk %slightly_more)  # DON'T BOIL!
POT+=%fat    # bothing baking fat and butter

# the mixture must be disgustingly salty, otherwise the dough is tasteless
BOWL=%yolks + %sugar + %salt
BOWL+=%almonds + %raisins
BOWL+=$(slowly-adding $POT + %flour)
BOWL+=$(reminder %flour) + $MUG

kneade $BOWL thoroughly
BOWL+=$(sprinkle %flour)
cover $BOWL
while %risen $BOWL  # could be a couple of hours
do
    wait
    ensure_room_warm
done

BREAD=$(for PLAIT in $(%divide $BOWL 10)
do
    weave $PLAIT 4  # multiple layers
    smear $PLAIT %yolk
done)
BREAD+=$(smear %yolk)
BREAD+=$(large-pieces %almonds)

%bake -j 1h  # cover with baking paper when brown

%install
install -m 755 -D -t %{_bindir}/vanocka $BREAD

%files
%doc README.md
%license LICENSE
%{_bindir}/vanocka

%changelog
