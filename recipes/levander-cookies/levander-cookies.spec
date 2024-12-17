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

# Please submit bugfixes or comments via https://cookie.opensuse.org/
#


%define all_ingredients flour butter sugar egg baking-powder salt levander-flower

Name:           levander-cookies
Version:        241224
Release:        0
Summary:        Levander Biscuit (Baked)
License:        Copyleft
Group:          Whatever/Opportunity
URL:            https://en.wikipedia.org/wiki/Lavandula
Source0:        %{name}.tar.gz
BuildRequires:  flour-plain >= 1cup
BuildRequires:  flour-amaranth-or-spelt >= 1cup
BuildRequires:  butter >= 100g
BuildRequires:  natural-sugar >= 50g
BuildRequires:  egg >= 1
BuildRequires:  baking-powder >= 1tspn
BuildRequires:  salt >= 1pinch
BuildRequires:  levander-flower >= 1spn
BuildRequires:  crushed-anise
BuildRequires:  fridge
BuildRequires:  spoon
BuildRequires:  tee-spoon
BuildRequires:  bowl
BuildRequires:  rolling-pin
BuildRequires:  cookie-cutters
Requires:       vanilla-or-levander-sugar

%description
Baked cookies with decent levander taste. Suitable for any occasion.

%prep
%autosetup -p1
%buy %{all_ingredients}
%unpack %{all_ingredients}

%build
# prepare dough
mv egg butter sugar bowl
%mix bowl > foam
mv flour baking-powder crushed-anise bowl
%mix bowl > dough
mv bowl > fridge
sleep 30m
# create flat cookies, approx. 3mm thick
# TODO: parallelize
while dough_available; do
  %roll dough > flat_shape
  %cut_out favorite_shapes > pieces
  # bake until golden brown
  %bake 10-12min 200C pieces > baked_pieces
  # wait until pieces cool down
  sleep 20m
done
%cleanup_kitchen

%install
mv baked_pieces %{buildroot}/%{_libdir}/%{name}
# hide sweets from children
%encrypt %{buildroot}/%{_libdir}/%{name}

%post
if [ `date +%d%m%y` == %{version} ]; then
  %decrypt %{_libdir}/%{name}
  # put baked_pieces into bowl with vanilla or levander sugar
  %sugar baked_pieces
else
  echo "Grr, wait until %{version}"
fi


%postun
%cleanup_dishes

%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}

%changelog

