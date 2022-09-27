cd brook
find -type f ./spor | sed -e 's/^./ - fileName: /' > ../docs/_data/spor-listing.yml
cd ..