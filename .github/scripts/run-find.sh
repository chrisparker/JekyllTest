cd brook
mkdir ../docs/_data/
find ./spor -type f | sed -e 's/^.//' > ../.github/scripts/find-output.txt
cd ..