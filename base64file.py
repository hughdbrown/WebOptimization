from __future__ import with_statement

from base64 import b64encode
from os.path import splitext

def file_contents(filename):
	with open(filename, "r") as f:
		return f.read()

def data_encoder(format, filename):
	content = b64encode(file_contents(filename))
	_, ext = splitext(filename)
	return "data:image/%s;base64,%s" % (ext[1:], content)

# For placing in a CSS file
def data_encoded_url(filename):
	return "url(%s)" % data_encoder(filename)

# For placing in an HTML file
def data_encoded_img(filename):
	return '<img src="%s" />' % data_encoder(filename)

if __name__ == "__main__":
	import sys, glob
	for arg in sys.argv[1:]:
		for filename in glob.glob(arg):
			#print data_encoded_url(filename)
			print data_encoded_img(filename)
