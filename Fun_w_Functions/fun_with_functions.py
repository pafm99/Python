#ODD/EVEN

def odd_even(a,b):
    for num in range (a,b):
        if num % 2 != 0:
            print "Number is", num, "This is an odd number"
        else:
            print "Number is", num, "This is an even number"
odd_even(1,5)

#MULTIPLY

a = [2, 4, 10, 16]
b = 5
multiple = 0

def multiply(a,b): #a= array b = number to multiply by
    for i in range(0,len(a)):
        a[i] *= b
    return a
print multiply(a,b)
        
#HACKER CHALLENGE




