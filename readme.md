## Jekyll Test

A test site for showing the features of jekyll using a GitHub Pages site.

Deployed site at: https://chrisparker.github.io/JekyllTest/

## So far, this

- The build process is controlled by a github actions file: https://github.com/chrisparker/JekyllTest/blob/main/.github/workflows/pages.yml
   1. The key file is brook/theta.json, which is uploaded to the repository manually.
   2. Run a python script to generate the jekyll YML: https://github.com/chrisparker/JekyllTest/blob/main/.github/scripts/produce-jekyll-yml.py
   3. Run Jekyll to build and deploy the static website. That runs the code in this file to produce the HTML: https://github.com/chrisparker/JekyllTest/blob/main/docs/index.html
   4. Upload generated website to github pages https://chrisparker.github.io/JekyllTest/

## Building and viewing the website locally

1. Download the contents of this repository.
2. Follow the instructions at https://jekyllrb.com/docs/ to get jekyll running on your operating system. For windows, use this page: https://jekyllrb.com/docs/installation/windows/
3. Navigate to the `docs` folder within the cloned repository, and run the console command `jekyll build`. 
4. Browse to `http://localhost:4000`.

## TODO on samples

- How to convert L2(5) into L<sub>2</sub>(5) [Both for simpleGroup and isoGroup]
- Assume that if there are no representations of a given type, neither the title nor table exist.