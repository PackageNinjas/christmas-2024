Name:           cookies-jam
Version:        1.0.0
Release:        0
Summary:        Favourite christmas cookies in my family
License:        CC-BY-SA
URL:            http://127.0.0.1/home/
Source0:        ingredients.tar.gz

BuildRequires:  round cookie cutter
BuildRequires:  rolling pin
BuildRequires:  oven
BuildRequires:  brush
Requires:       flour >= 250g
Requires:       baking sode >= 6g
Requires:       sugar >= 100g
Requires:       vanilla sugar >=
Requires:       egg = 1
Requires:       butter >= 125g
Requires:       jam
Requires:       icing
Requires:       chocolate decorations

%description
My family's favourite christmas cookies. No translatable name available.

%prep
%setup -n ingredients
echo "mixing flour, baking soda with sugar, vanilla sugar and egg"
echo "slowly adding piece of butter while kneading"
echo "kneading until dough is smooth"
echo "cool dough in fridge"
sleep(1800)

%build
echo "rolling out dough"
echo "adding flour as necessary for the dough to not stick"
echo "cutting out circles"
%define bottom cut-outs
echo "cutting out middle of circle for half of them"
%define top cut-outs with hole
%autobake --temp="200°C" --time="6-8" 

%install
echo "letting cookies cool"
install icing top
install decoration top
install jam bottom
echo "putting both halfs together"
install top bottom

%files
/cookies/

%changelog
* Thu Dec 12 2024 Nico Krapp <nico.krapp@suse.com>
- initial recipe

