## Jekyll Test

A test site for showing the features of jekyll using a GitHub Pages site.

Deployed site at: https://chrisparker.github.io/JekyllTest/

## So far, this

- The build process is controlled by a github actions file: \.github\workflowspages.yml
   - This first runs a bash script to generate a file listing: \.github\scripts\run-find.sh
   - Then runs a python script to generate the jekyll YML: produce-jekyll-yml.py
   - Then runs Jekyll to build and deploy the static website: https://chrisparker.github.io/JekyllTest/

