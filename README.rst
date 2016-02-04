Pyandoc: a simple Pandoc wrapper for Python


Requirements
++++++++++++

* Pandoc


Usage
+++++

Get setup.

.. code-block:: python

	import pandoc

	# pandoc.PANDOC_PATH = '/usr/bin/pandoc'


Let's start with a Markdown document:

.. code-block:: python

	doc = pandoc.Document()
	doc.markdown = '''
	# I am an H1 Tag

	* bullet point
	* more points
	* point with [link](http://kennethreitz.com)!
	'''

Now let's convert that into a ReST document: ::

	>>> print doc.rst

	I am an H1 Tag
	==============


	-  bullet point
	-  more points
	-  point with `link <http://kennethreitz.com>`_!

Formats available:
	- asciidoc
	- beamer
	- commonmark
	- context
	- docbook
	- doc- x
	- dokuwiki
	- dzslides
	- epub
	- epub3
	- fb2
	- haddock
	- html
	- html5
	- icml
	- json (pandoc's AST)
	- latex
	- man
	- markdown
	- markdown_github
	- markdown_mmd
	- markdown_phpextra
	- markdown_strict
	- mediawiki
	- native
	- odt
	- opendocument
	- opml
	- org
	- pdf
	- plain
	- revealjs
	- rst
	- rtf
	- s5,
	- slideous
	- slidy
	- texinfo
	- textile

Enjoy.
