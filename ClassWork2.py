# 1.  Створити список цілих чисел, які вводяться з терміналу 
# та визначити серед них максимальне та мінімальне число.
# first way
# my_list = []
# x = int(input("Input numbers"))
# for c in range(x):
#     my_list.append(int(input('Entered next number')))
# print('Max value is: ', max(my_list))
# print('Min value is: ', min(my_list))
# second way
# value = [ int(input("Input numbers")) for x in range(int(input("Input amaunt of number your list digits")))]
# print('Max value is:', max(value))
# print('Min value is:', min(value))


# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.
# #####First way
# value = [x for x in range(1,10) if x % 2 == 0]
# print(value) # •  парні, які діляться на 2,
# value = [x for x in range(1,10) if x%2 == 1 and x%3 == 0]
# print(value) # •  непарні, які діляться на 3,

# value = [x for x in range(1,10) if x%3 == 1 and x%2 == 1]
# print(value) # •  числа, які не діляться на 2 та 3.
#### Secod way




# 3.  Написати програму, яка обчислює факторіал числа,
# яке користувач вводить.(не використовувати рекурсивного виклику функції)

factorial = 1
number = int(input("Input number and I will count factorial of this number for you: "))
if number == 0:
    print("Noo1")
elif number<0:
    print("OOps!!!")
else

   for value in range(1,number +1):
       factorial*=value
   print(factorial) 


# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).



