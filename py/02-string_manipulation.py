# single_quote = 'Azren'
# double_quote = "Muhammad Azren"
# triple_quote = """Muhammad
# Azren
# Hasnen"""

# print(single_quote)
# print(double_quote)
# print(triple_quote)

# text = "Python Programming"

# print(text[0])          # (first character)
# print(text[-1])         # (last character)
# print(text[0:6])        # (slice 0 to 5)
# print(text[:6])         # (from start to 5)
# print(text[7:])         # (7 to end)

# name = " muhammad azren hasnen "

# print(len(name))                        # length includes whitespace
# print(name.strip())                     # remove whitespace beginning/end, not in between
# print(name.upper())                     # uppercase
# print(name.lower())                     # lowercase
# print(name.title())                     # title case - first char of the word
# print(name.replace("muhammad", "m"))    # replace - case sensitive

# name = "muhammad azren"
# age = 35

# message_1 = f"My name is {name.title()} and I am {age} years old."              # f-strings
# message_2 = "My name is {} and I am {} years old.".format(name, age)    # str.format()
# message_3 = "My name is %s and I am %d years old." % (name, age)        # %-formatting

# # for f-formatting:
# # s - string
# # d - decimal interger
# # f - float
# # g - general

# print(message_1)
# print(message_2)
# print(message_3)

text = """Python is a powerful programming language. It's easy to learn
and versatile! You  can  use  Python  for  web  development,  data  science,  and automation. The syntax is clean and readable. This makes Python perfect for beginners and experts alike."""

characters = len(text)                                              # Count characters (including spaces)
characters_no_space = len(text.replace(' ', ''))                    # Count characters (excluding spaces) by replacing whitespace with blank
words = len(text.split())                                           # Count words by looking for empty space/whitespace
sentences = text.count('.') + text.count('!') + text.count('?')     # Count sentences by looking for symbol

print("Characters:", characters)
print("Characters Without Space:", characters_no_space)
print("Words:", words)
print("Sentences:", sentences)

# another way to do it:
print(f"Character count (including space): {characters}")
print(f"Character count (excluding space): {characters_no_space}")
print(f"Word count: {words}")
print(f"Sentence count: {sentences}")