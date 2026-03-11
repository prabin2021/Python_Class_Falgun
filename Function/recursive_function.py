""" 
Recursive function: A function call itself
Base case and recursive case


Factorial:
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2* 1 = 

"""

# def count(n):
#     if n == -10:
#         return
#     print(n)
#     count(n - 1)
    
# count(5)


#Factorial :

def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n * factorial( n-1 )  # 4 * factorial(4-1)  ->  4 * 3 * factorial( 3-1)  -> 4 * 3 * 2 * factorial(2 -1 ) -> 4 * 3 * 2 * 1
        return fact
    
result = factorial(6)
print(result)