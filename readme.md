## Jekyll Test

A test site for showing the features of jekyll using a GitHub Pages site.

Deployed site at: https://chrisparker.github.io/JekyllTest/

## So far, this

- The build process is controlled by a github actions file: https://github.com/chrisparker/JekyllTest/blob/main/.github/workflows/pages.yml
   - This first runs a bash script to generate a file listing: https://github.com/chrisparker/JekyllTest/blob/main/.github/scripts/run-find.sh
   - Then runs a python script to generate the jekyll YML: https://github.com/chrisparker/JekyllTest/blob/main/.github/scripts/produce-jekyll-yml.py
   - Then runs Jekyll to build and deploy the static website: https://chrisparker.github.io/JekyllTest/

