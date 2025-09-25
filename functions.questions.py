#1.
def mul_nums(a,b):
    mul = ( a * b )
    print(mul)
    return mul

mul_nums(3,5)

#2.
def fun_val():
    for i in range(1,11):
        if i % 2 == 0 :
            print(i,"even")
        else:
            print(i,"odd")
fun_val()


#3.           
    
def calc_fact(num):
    i = 1
    fact = 1
    while i <= num:
        fact *= i
        i += 1
    return fact    
num = int(input("enter the num:"))
result = calc_fact(num)
print(result)

        
#4.


def largest_of_three(a,b,c):
   if a >= b and a >= c :
       return a
   elif b >= a and b >= c :
       return b
   else :
       return c

largest = largest_of_three(3,6,9)
print(largest)


#5.
def func_str(str):
    str = "ashwithaeshwar"
    print(str[::-1])
    return str
func_str(str)



#6.
s = input("enter the name:")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels: 
           count += 1
    return count
print(count_vowels(s))























       













        
