Name:           spritzgebaeck
Version:        3.0
Release:        0
Summary:        German X-Mas Cookie recipe

License:        Weber-Family-3rd-Gen
URL:            http://weber-family-recipes.local/spritzgebaeck
Source0:        spritzgebaeck-recipe.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  flour >= 500g, sugar >= 250g, egg, hazelnuts, butter >= 250g
Requires:       bowl, hands, oven, frost, meat-grinder

%description
A recipe for traditional German Spritzgebäck cookies. This family recipe
has been passed down for generations. Delicious, simple, and nostalgic!

%prep
echo "Preparing ingredients..."
if [ "$(butter_state)" = "firm" ]; then
    echo "Heating butter..."
    butter_state="liquid"
fi
echo "Mixing ingredients in a giant bowl."
echo "Exposing dough to cold temperatures (preferably outside) for 24 hours."

%build
echo "Combining dry ingredients and liquid butter."
echo "Kneading dough by hand (mechanical tools strictly prohibited)."
echo "Warning: Enjoy the dough, but don't eat too much!"

%install
mkdir -p %{buildroot}/cookies
echo "Shaping dough into cookies using a meat grinder."
echo "Placing cookies onto baking trays."
bake --temperature=160 --time=12 --output=%{buildroot}/cookies/

%clean
rm -rf %{buildroot}
echo "All traces of dough have been eradicated. Kitchen is clean."

%files
/cookies/*

%changelog
* Wed Dec 13 2024 Anna Maresova <anicka@suse.com>
- Fixed specfile to align with openSUSE packaging guidelines.

* Wed Dec 13 2024 Sascha Weber <saweber@suse.com>
- Initial package creation.
