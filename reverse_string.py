# ---  Reverse a String (without slicing or built-ins) --
# ------------------------------------------------------
def reverse_string(my_string):
    result = ""
    for ch in my_string:
        result = ch + result
    return result
print(reverse_string("hello"))  # Output: "olleh"

# ---------------  Reverse using slicing ---------------
# ------------------------------------------------------
text = "Python"
reversed_text = text[::-1]
print(reversed_text)   # Output: nohtyP

# ----  Reverse using reversed() built-in function  ----
# ------------------------------------------------------

text = "Python"
reversed_text = "".join(reversed(text))
print(reversed_text)   # Output: nohtyP

# ----  Reverse using for loop + concatenation (less efficient, but simple) ------
# --------------------------------------------------------------------------------

text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)   # Output: nohtyP
