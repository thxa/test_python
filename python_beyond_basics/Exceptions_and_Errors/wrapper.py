
def wrap(text, line_length):
	"""Warp a string to a specified line length.

	Args:
		text: The string to wrap
		line_length: The line length in characters

	Returns:
		A warpped string.

	Raises:
		ValueError: If line_length is not positve.
	"""
	if line_length < 1:
		raise ValueError("line_length {} is not positve.".format(line_length))

	words = text.split()

	if max(map(len, words)) > line_length:
		raise ValueError("line_length must be at least as long as the longest word")
	
	line_of_words = []
	current_line_length = line_length
	for word in words:
		if current_line_length + len(word) > line_length:
			line_of_words.append([]) # new line
			current_line_length = 0
		line_of_words[-1].append(word)
		current_line_length += len(word) + len(' ')
	lines = [' '.join(line_of_words) for line_of_words in line_of_words]
	result = '\n'.join(lines)
	assert all(len(line) <= line_length for line in result.splitlines())
	return result
