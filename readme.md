## Jekyll Test

A test site for showing the features of jekyll using a GitHub Pages site.

Deployed site at: https://chrisparker.github.io/JekyllTest/

## Examples so far:

### 1 Using _layouts. 

This enables you to specify a layout in the `_layouts` directory using tags, and then just have a data file in the right place with the variables. When the data is compiled, the html to generated from the templates. 

See https://chrisparker.github.io/JekyllTest/layoutexample.html

This page is generated from two files:

https://github.com/chrisparker/JekyllTest/blob/main/docs/_layouts/representation.html
https://github.com/chrisparker/JekyllTest/blob/main/docs/layoutexample.html

The point being that you put your template in one file, and just the variables in the other, and this allows you to add new pages by just putting a data file in the right place. Note the 'if' statement that allows you to easily extend the template with new html/properties when you find them without updating all the data.

### 2. Using includes. 

This enables you to "include" another page, allowing static content in some places, and a call out to another file in the middle of the HTML

See https://chrisparker.github.io/JekyllTest/includeexample.html

This page is generated from two files:

https://github.com/chrisparker/JekyllTest/blob/main/docs/_includes/basicinclude.html
https://github.com/chrisparker/JekyllTest/blob/main/docs/includeexample.html

The point being you can include multiple pages inside others.

### 3. Using data iteration. 

This enables you to have a single yml file describing the data, and then iterate over it within a page to create the items you want.

See https://chrisparker.github.io/JekyllTest/dataiterationexample.html

This page is generated from two files:

https://github.com/chrisparker/JekyllTest/blob/main/docs/dataiterationexample.html
https://github.com/chrisparker/JekyllTest/blob/main/docs/_data/representations.yml

The point being that you can construct a row in an html grid from a set of data in a yml file.

### 4. Using data generation. 

A github action generates the yml data file from the files in a directory, and those are input into a template to create the html from an iterated include.

See https://chrisparker.github.io/JekyllTest/data-generation-example.html

This builds on the data include above by using a github action to run this shell script first to generate the yml file, and then building that with jekyll as before. This is the script:

https://github.com/chrisparker/JekyllTest/blob/main/.github/scripts/create-file.sh

As a result, if you were logged into GitHub and added a file to this directory:
https://github.com/chrisparker/JekyllTest/tree/main/docs/spor/Co1/mtx

The link would automatically appear as an extra line on the data generation page after the build was done (takes about 45 seconds).