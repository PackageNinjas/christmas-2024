#
# spec file for package hedgehogs
#
# Copyright (c) ???? playful bakers
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


Name:           hedgehogs
Version:        2.0
Release:        0
Summary:        Christmas sweet treat
License:        TopRecepty AND HowWeDoIt
URL:            https://www.toprecepty.cz/recept/31887-vanocni-cukrovi-orechovi-jezci/
Source:         hedgehogs.jpg
BuildRequires:  flour = 350 g
BuildRequires:  butter-like = 200 g  # provided by: butter, margarin, lard, etc.
BuildRequires:  sugar = 50 g
BuildRequires:  egg-yolk = 1
BuildRequires:  chocolate >= 80 g
Requires(post): chocolate >= 50 g
Requires(post): fat  # provided by: butter, margarin, oil, coconut oil, etc.
Requires(post): ground-coconut
Requires(post): skewer

%description
Cookies are among the sweetest Christmas traditions. Baking and decorating them takes a lot of time and energy, but the result is worth it. If you have little rascals at home who like to help with the preparation, we have cookies just for them - hedgehogs. 

%prep
%autosetup -p1
mkdir bowl

%build
mv flour butter-like sugar egg-yolk bowl/
%mix bowl/* > dough
sleep $overnight

%cut chocolate > chocolate-pieces
%cut dough > dough-bits
for bit, choc in dough-bits, chocolate-pieces; do
    %flatten bit
    %wrap choc bit > ball
    %shape ball > drop
done

%install
%bake --dir hedgehogs

%post
mkdir pot

%cut chocolate > chocolate-pieces
mv chocolate-pieces fat > pot
%melt pot/*
%soak hedgehogs/* pot

ground-coconut >> hedgehogs/*

%soak skewer pot
%draw[eyes,nose] skewer hedgehogs/*

%files
hedgehogs

%changelog

