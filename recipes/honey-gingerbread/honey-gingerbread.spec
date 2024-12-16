#
# spec file for package honey-gingerbread
#
# Licensed under the NWL - No Whining License.
#
# You may use this, modify this, redistribute this provided you agree to:
# - not whine about it;
# - the fact that there is no warranty of any kind.
# - retain this copyright in full.
#
# Please submit updates to this file via https://build.opensuse.org/
#

Name:           honey-gingerbread
Version:        1.0
Release:        0
Summary:        Traditional Czech Honey Gingerbread Recipe

License:        NWL
URL:            https://www.levneknihy.cz
Source0:        honey-gingerbread-recipe.jpg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  flour >= 500g, sugar >= 150g, honey >= 100g, butter >= 50g, eggs >= 2
Requires:       bowl, refrigerator, rolling-pin, cookie-cutters, oven

%description
A recipe for traditional Czech honey gingerbread cookies (*medové perníčky*), 
adapted from Jarmila Píchová's book *Med v kuchyni labužníka*. This is Anna's 
family's favorite recipe! The cookies are so delicious that her kids often 
struggle to decide whether to eat them or play with their fun shapes of trains, 
planes, and cars. Bake these cookies, age them for two weeks, and enjoy their 
full flavor. Yummy and playful—perfect for the holidays or any time!

%prep
echo "Mixing ingredients to create a smooth dough..."
knead --ingredients=flour:500g,sugar:150g,honey:100g,butter:50g,eggs:2,baking_soda:1.5tsp,spices:1.5tbsp --smoothness=perfect
echo "Letting dough chill in the fridge for 24 hours..."
sleep --duration=24h --temperature=fridge

%build
roll --thickness=5mm --output=flat_dough
cut --shapes=trains,planes,cars --tool=cookie-cutter
brush --tops --coat=egg_white
echo "Ready for the heat!"

%install
bake --temperature=180C --duration=8-10min --output=%{buildroot}/cookies/
cool --rack --time=sufficient
decorate --style=fancy --freestyle=on
echo "Store in an airtight container for 14 days to unleash the flavor gods!"

%clean
rm -rf %{buildroot}
echo "Kitchen is spotless. Deploy the cookies!"

%files
/cookies/*

%changelog
* Thu Dec 12 2024 Anna Maresova <anicka@suse.com>
- Initial package for honey gingerbread recipe.
