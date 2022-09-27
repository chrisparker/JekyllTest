cd brook
find ./spor -type f | sed -e 's/^./ - fileName: /' > ../docs/_data/spor-listing.yml
cd ..