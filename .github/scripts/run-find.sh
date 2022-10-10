cd brook
mkdir ../docs/_data/
find ./spor -type f | sed -e 's/^.//' > find-output.txt
cd ..