Name:           grandpa-cookies
Version:        1.0.0
Release:        0
Summary:        cookies a bit like gingerbread
License:        CC-BY-SA
URL:            http://127.0.0.1/home/
Source0:        ingredients.tar.gz

BuildRequires:  bowl
BuildRequires:  mixer
BuildRequires:  oven
Requires:       brown sugar >= 250g
Requires:       eggs >= 2
Requires:       flour >= 250g
Requires:       ground almonds >= 50g
Requires:       cocoa powder >= 1-2 tablespoons
Requires:       candied lemon peel >= 40g
Requires:       candied orange peel >= 40g
Requires:       potash >= 2 pinches
Requires:       cinnamon >= 2 teaspoons
Requires:       ground cloves >= 2 teaspoons
Requires:       honey >= 2 teaspoons
Requires:       coffee = small cup

%description
Family recipe for cookies that are a bit like gingerbread and
are perfect to some coffee or tea. Named after my grandpa who liked
them best.

%prep
%setup -n ingredients
mv ingredients/* bowl
echo "mixing ingredients until viscous"
if ![ "$consistency" = "viscous" ]; then
    mv flour bowl || mv coffee bowl
fi

%build
echo "place teaspoon portions of dough on baking sheet"
echo "leave space for the mixture to spread out a bit"
%autobake --temp="200°C" --time="10"
echo "bake until fairly solid"
if [ "$taste" = "crunchy" ]; then
    echo "bake for ca 2 min longer if you like them crunchy"
fi

%install
echo "let cookies cool until cookies are not sticking to baking sheet"
install cookies plate
echo "serve with and dunk in coffee or tea"

%files
/cookies/

%changelog
* Thu Dec 12 2024 Nico Krapp <nico.krapp@suse.com>
- initial recipe


