class Stream:
	def __init__(self, *args, **kwargs):pass

	def reset(self):pass


class ReadableStream(Stream):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def read(self):pass


class WriteableStream(Stream):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def write(self, context):pass


s = ReadableStream()

print(isinstance(s, ReadableStream))
print(isinstance(s, (ReadableStream, WriteableStream)))


class ReadWriteStream(ReadableStream, WriteableStream):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)



print("class ReadableStream  __bases__ -> {0}".format(ReadableStream.__bases__))
print("class WriteableStream __bases__ -> {0}".format(WriteableStream.__bases__))
print("class ReadWriteStream __bases__ -> {0}".format(ReadWriteStream.__bases__))
print("class ReadWriteStream __mro__   -> {0}".format(ReadWriteStream.mro()))

# super(Base, Derived) => class super proxy
# super(Base, self) => instance super proxy