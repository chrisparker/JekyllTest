cd brook
find ./spor -type f | sed -e 's/^.//' > find-output.txt
cd ..