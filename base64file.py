from __future__ import with_statement

from base64 import b64encode
from os.path import split as path_split

def file_contents(filename):
	with open(filename, "r") as f:
		return f.read()

def data_encoder(format, filename):
	content = b64encode(file_contents(filename))
	_, file_without_path = path_split(filename)
	ext = file_without_path.split(".")[1]
	return format % (ext, content)

# For placing in a CSS file
def data_encoded_url(filename):
	return data_encoder("url(data:image/%s;base64,%s)", filename)

# For placing in an HTML file
def data_encoded_img(filename):
	return data_encoder('<img src="data:image/%s;base64,%s" />', filename)

if __name__ == "__main__":
	import sys, glob
	for arg in sys.argv[1:]:
		for filename in glob.glob(arg):
			print data_encoded_url(filename)
