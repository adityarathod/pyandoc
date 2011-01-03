Pyandoc: a simple Pandoc wrapper for Python


Requirements
++++++++++++

* Pandoc


Usage
+++++

Get setup. ::

	import pandoc
	
	pandoc.PANDOC_PATH = '/usr/bin/pandoc'


Let's start with a Markdown document: ::

	
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

Enjoy.


Roadmap
+++++++

* Cleanup
* Figure out epub, odt support
* Figure out better path management
* Proper Exceptions
* Unit testing
* CI
