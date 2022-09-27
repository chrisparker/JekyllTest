cd docs
find ./spor | sed -e 's/^/ - fileName: /'
find ./spor | sed -e 's/^/ - fileName: /' > ../docs/_data/spor-listing.yml
cd ..