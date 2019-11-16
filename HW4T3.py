# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# user_name = input("Input your name and I will say playing you banjo or not ")
############################################
# 1 way
def music_answer(user_name):
    if user_name[0]=='R' or user_name[0]=='r':
        print(user_name, " plays banjo" )
    else:
        print(user_name, " does not play banjo")
music_answer('doma')

#################################################




