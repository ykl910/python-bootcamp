import sys
import string

def text_analyzer(text=None):
	"""
	Analyzes text and counts different types of characters.

	Args:
		text (str, optional): Text to analyze. Defaults to None.

	Returns:
		None: Prints analysis results to console.

	Example:
		>>> text_analyzer("Hello World!")
		The text contains 12 printable character(s):
		- 2 upper letter(s)
		- 8 lower letter(s)
		- 1 punctuation mark(s)
		- 1 space(s)
	"""
	if text is None:
		text = input("what is the text to analyze?\n")
	if not text:
		print("please include one string")
		return
	try:
		assert isinstance(text, str)
	except AssertionError:
		print("input must be a string")
		return

	printable = len([c for c in text if c.isprintable()])
	upper = len([c for c in text if c.isupper()])
	lower = len([c for c in text if c.islower()])
	spaces = len([c for c in text if c.isspace()])
	punctuation = len([c for c in text if c in string.punctuation])
	
	print(f"The text contains {printable} printable character(s):")
	print(f"- {upper} upper letter(s)")
	print(f"- {lower} lower letter(s)")
	print(f"- {punctuation} punctuation mark(s)")
	print(f"- {spaces} space(s)")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		text_analyzer()
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		print("please include one string")