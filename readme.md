## Jekyll Test

A test site for showing the features of jekyll using a GitHub Pages site.

Deployed site at: https://chrisparker.github.io/JekyllTest/

## Examples so far:

1. Using _layouts. This enables you to specify a layout in the `_layouts` directory using tags, and then just have a data file in the right place with the variables. When the data is compiled, the html to generated from the templates. 

See https://chrisparker.github.io/JekyllTest/layoutexample.html

2. Using includes. This enables you to "include" another page, allowing static content in some places, and a call out to another file in the middle of the HTML

See https://chrisparker.github.io/JekyllTest/includeexample.html

3. Using data iteration. This enables you to have a single yml file describing the data, and then iterate over it within a page to create the items you want.

See https://chrisparker.github.io/JekyllTest/dataiterationexample.html

4. Using data generation. A github action generates the yml data file from the files in a directory, and those are input into a template to create the html from an iterated include.

See https://chrisparker.github.io/JekyllTest/data-generation-example.html