# You need to write a function that reverses the words in a given string. 
# A word can also fit an empty string. If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace
def rev_words(words):
    # split words of string separated by space
    input_words = words.split(" ")
    # reverse list of words
    input_words = input_words[-1::-1]
    # join words with space
    rev_result = ' '.join(input_words)

    return rev_result
print (rev_words('Hello  Sashan 1 Tsegelnyk'))