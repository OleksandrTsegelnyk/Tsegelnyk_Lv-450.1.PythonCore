# Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.

# Examples:
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me

def filter_words(st):
    st2 = " ".join(st.split()).capitalize()
    return st2

# print(filter_words("HELOO my Libe LALALAL"))