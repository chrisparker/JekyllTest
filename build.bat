rmdir /S /Q "docs/_allrep"
rmdir /S /Q "docs/_data"
rmdir /S /Q "docs/_char0rep"
rmdir /S /Q "docs/_modularrep"
rmdir /S /Q "docs/_permrep"
rmdir /S /Q "docs/_site"

python3 .github\scripts\produce-jekyll-files.py

cd docs

jekyll build

pause