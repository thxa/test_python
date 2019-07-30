import os

from reader.compressed import bz2_opener, gzip_opener

extension_map = {
	'.bz2': bz2_opener,
	'.gz': gzip_opener,
}


class Reader(object):
	def __init__(self, filename):
		extension = os.path.splitext(filename)[1]
		opener = extension_map.get(extension, open)
		self.f = opener(filename, mode="rt")

	def ret(self):
		return self.f.seek(0)
		
	def read(self):
		return self.f.read()

	def close(self):
		self.f.close()