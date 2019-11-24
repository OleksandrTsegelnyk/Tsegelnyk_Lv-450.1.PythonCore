# Unfinished Loop - Bug Fixing #1
# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!



def create_array(n):
    # initialize an empty list
    res=[]

    i=1
    # initialize while loop
    while i <= n:
        # add i to empty list
        res += [i]
        # incriment i by 1
        i += 1

    return res
