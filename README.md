Ally-Py-docs
============

This is the repository holding all documentation related to the Ally-Py framework.

It will contain various documents, each in a separate directory:

* Reference (not yet available)
* Plugin Guide (in `plugin_guide` directory)
* Howto (not yet available)

Documentation is generated using [Sphinx](http://sphinx-doc.org/), and written in [reStructuredTex](http://sphinx-doc.org/rest.html).

To generate an HTML version of the documentation: 

1. Install [Sphinx](http://sphinx-doc.org/install.html).
2. Clone this repository `git clone git@github.com:sourcefabric/Ally-Py-docs.git`.
3. To generate the html version of the Plugin Guide, run `make html` from inside the `plugin_guide` directory.
4. Go to your browser and open `plugin_guide/_build/html/index.html`.

Enjoy reading !

You can also generate a PDF version if you install LaTeX or rst2pdf.
