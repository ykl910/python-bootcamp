import sys
import string

if len(sys.argv) != 3:
	print("ERROR")
	sys.exit(1)

try:
	min_length = int(sys.argv[2])
except:
	print("ERROR")
	sys.exit(1)

text_no_punct = ''.join(c for c in sys.argv[1] if c not in string.punctuation)
words = [c.strip() for c in text_no_punct.split()]
list_words = [word for word in words if len(word) > min_length]
print(list_words)