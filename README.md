Ally-Py-docs
============

This is the repository holding all documentation related to the Ally-Py framework.

You will find here different documents as they are produced: Reference, Plugin Guide, HowTos, etc. The way the
different documents are organized is simple, each directory corresponds to a document. For example, the
*plugin-guide* directory holds the Plugin Guide, and so on.

Documentation is written using [Sphinx](http://sphinx-doc.org/), if you want to render it in your Web browser
as HTML pages you can easily do it by:

1. Make sure to have Sphinx [installed](http://sphinx-doc.org/install.html)
2. Clone this repository.
3. Run the following in the command line: `$ sphinx-build -b html plugin-guide <target directory>`. Then you will see all generated *Plugin Guide* pages in HTML format within the target directory.
4. Go to your browser and open the index.html page.

Enjoy reading !
