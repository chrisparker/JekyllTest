rmdir /S /Q "docs/_allrep"
rmdir /S /Q "docs/_data"
rmdir /S /Q "docs/_matrep"
rmdir /S /Q "docs/_permrep"
rmdir /S /Q "docs/_site"

python3 .github\scripts\produce-jekyll-files.py

cd docs

jekyll build

pause