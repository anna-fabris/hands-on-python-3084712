greet = "Hello World" 
# string definition

extened_grt = "Hello World, " + "this is a long string"
# concatenating 2 strings

name = "John"

intrupution = f"Hello {name}"
# interpolatiom of a string

greet_format = "Hello {}"
# template for formatting

formatted = greet_format.format(name)
# using the format template

print(intrupution, formatted)

print(formatted.upper()) # upper case
print(formatted.lower()) # lower case

print(formatted.replace("John","Paul"))
# to replace "John" with "Paul"
# BE CAREFUL: no replacing happens if you misspell! 