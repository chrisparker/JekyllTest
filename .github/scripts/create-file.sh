cd docs
find ./brook/spor | sed -e 's/^/ - fileName: /' > ../docs/_data/spor-listing.yml
cd ..