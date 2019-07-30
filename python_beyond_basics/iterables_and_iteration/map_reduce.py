def count_word(doc):
	normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
	frequencies = {}
	for word in normalised_doc.split():
		frequencies[word] = frequencies.get(word, 0) + 1
	return frequencies


print(count_word("IT was the best of times, it was the worst of times."))
# print(count_word("كان احسن وقت و كان السواء وقت"))

documents = [
	"IT was the best of times, it was the worst of times.",
	"IT was the best of times, it was the worst of times.",
	"IT was the best of times, it was the worst of times.",
	]

counts = map(count_word, documents)

def combine_counts(d1, d2):
	d = d1.copy()
	for word, count in d2.items():
		d[word] = d.get(word, 0) + 1
	return d


from functools import reduce
total_counts = reduce(combine_counts, counts)
print(total_counts)