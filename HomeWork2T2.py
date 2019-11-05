# Задано чотирицифрове натуральне число. 
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число
 
#c = 5387
 
# d = (list(str(c)))
# print(d)
c = input("Enter 4 digit number ")

conv_c = [int(x) for x in str(c)] 
print ("Numbers:" + str(conv_c)) 
# Calculetion of the multiply of the ints
def multiplyList(myL): 
 result = 1
 for x in myL: 
  result = result * x 
 return result 
#Print results of the multiply
print("multiplyResult", multiplyList(conv_c))


# Creating variable reverced list"rev_list"
rev_list = conv_c[::-1]
print("Reversed list ", rev_list)

# Joining integers from the list to the one number
def convToInt(rev_list):      
    s = [str(i) for i in rev_list]     
    res = int("".join(s))     
    return(res) 
   
print("Reversed C number: ", convToInt(rev_list))

# Sort the list in Descending order
rev_list.sort(reverse=True)

print(rev_list)
