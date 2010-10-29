import subprocess

PANDOC_PATH = '/Users/kreitz/.cabal/bin/pandoc'

class Document(object):
	"""A generic formatted document"""
	
	INPUT_FORMATS = (
		'native', 'markdown', 'markdown+lhs', 'rst', 
		'rst+lhs', 'html', 'latex', 'latex+lhs'
	)
	
	OUTPUT_FORMATS = (
		'native', 'html', 'html+lhs', 's5', 'slidy', 
		'docbook', 'opendocument', 'odt', 'epub', 
		'latex', 'latex+lhs', 'context', 'texinfo', 
		'man', 'markdown', 'markdown+lhs', 'plain', 
		'rst', 'rst+lhs', 'mediawiki', 'rtf'
	)

	# odt
	# epub
	
	
	def __init__(self):
		self.content = None
		self._register_formats()
			
	@classmethod
	def _register_formats(cls):
		"""Adds format properties."""
		for fmt in cls.OUTPUT_FORMATS:
			clean_fmt = fmt.replace('+', '_')
			setattr(cls, clean_fmt, property(lambda x, fmt=fmt: cls._output(x, fmt)))
		
	
	def _output(self, format):
		# print format
		p = subprocess.Popen(
			[PANDOC_PATH, '--from=html', '--to=%s' % format],
			stdin=subprocess.PIPE, 
			stdout=subprocess.PIPE
		)

		return p.communicate(self.content)[0]
		# 			
		# return format

	
test = """
<h1>dude this is awesome</h1>
<ul>
    <li>hi</li>
    <li>hi</li>
    <li>hi</li>
</ul>
"""


doc = Document()
doc.content = test
print doc.rtf

# print html2rst(test)