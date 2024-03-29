# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

# is_uppercase("c") == False
# is_uppercase("C") == True
# is_uppercase("hello I AM DONALD") == False
# is_uppercase("HELLO I AM DONALD") == True
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
# is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True


# Return True if all cased characters in inp are uppercase 
# and there is at least one cased character in Sinp, False otherwise.
def is_uppercase(inp):
    return inp.isupper()
# print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))

