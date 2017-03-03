#  Create a program that takes some text and return a list of all the characters in the text that are not vowels
# sorted in alphabetical order.
#  you can either enter the text from the keyboard or initialise a string variable with the string.



vowels = {"a", "e", "i", "o", "u"}
print(vowels)
sample_text = "when I walk down the street I wonder what the comfort is on my feet"
text = sample_text.lower()
text_set = set(text)


text_set = text_set - vowels
list(text_set)
print(text)
print(text_set)
print(sorted(text_set))

