import subprocess

PANDOC_PATH = '/Users/kreitz/.cabal/bin//pandoc'


class Document(object):
	"""A formatted document."""
	
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

	# TODO: Add odt, epub formats (requires file access, not stdout)
	
	def __init__(self):
		self._content = None
		self._format = None
		self._register_formats()
			
	@classmethod
	def _register_formats(cls):
		"""Adds format properties."""
		for fmt in cls.OUTPUT_FORMATS:
			clean_fmt = fmt.replace('+', '_')
			setattr(cls, clean_fmt, property(
				(lambda x, fmt=fmt: cls._output(x, fmt)), # fget
				(lambda x, y, fmt=fmt: cls._input(x, y, fmt)))) # fset
	
	def _input(self, value, format=None):
		# format = format.replace('_', '+')
		self._content = value
		self._format = format
	
	def _output(self, format):
		# print format
		p = subprocess.Popen(
			[PANDOC_PATH, '--from=%s' % self._format, '--to=%s' % format],
			stdin=subprocess.PIPE, 
			stdout=subprocess.PIPE
		)

		return p.communicate(self._content)[0]
