#!/bin/bash


echo "# Recipes"

for i in $(find recipes -type d)
do
    title="${i:8}"
    [ -z $title ] && continue
    summary=$(grep -i summary $i/$title.spec | cut -d ":" -f2 | xargs)
    images=$(find $i -type f | grep -e "png$" -e "jpg$")
    echo "## [$title]($i/$title.spec): $summary"
    echo "<p>"
    for img in $images
    do
        echo "<img src=\"$img\" width=200/>"
    done
    echo "</p>"
    echo ""
done
