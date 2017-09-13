#PRINT 1-255
def print_1_To_255():
    for x in range(1,256):
        print x
#PRINT INTS AND SUM 0-255
def print_ints_and_sum():
    sum = 0
    for x in range(0,256):
        print x
        sum = sum + x
    print sum
#PRINT ODDS 1-255
def print_odds():
    for x in range (1,255):
        if x % 2 == 0:
            print x
#ITERATE AND PRINT ARRAY
def iterate_arr(arr):
    for x in arr:
        print x 
#FIND AND PRINT MAX
def find_max(arr):
    max = 0
    for x in arr:
        if x > max:
            max = x
    print max
#GET AND PRINT AVG
def get_avg(arr):
    sum = 0
    avg = 0
    for x in arr:
        sum = sum + x
    avg = sum / len(arr)
    print avg
#SQUARE VALUES
myarr = [4,5,6]
def square_vals(arr):
    for x in range(0, len(arr)):
        arr[x] = arr[x] * arr[x]
        print arr[x]
    return arr
#square_vals(myarr)
#print myarr 

#ARRAY WITH ODDS   
def arr_odds():
    arr = []
    for x in range(1,256):
        if x % 2 != 0:
            arr.append(x)
        print arr
#GREATER THAN Y
def greater_y(arr,y):
    count = 0
    for x in arr:
        if x > y:
            count += 1
    print count
#ZERO OUT NEGATIVE NUMBERS
myarr = [-2,3,4,-3]
def zero_out(arr):
    for x in range(0,len(arr)):
        if arr[x] < 0:
            arr[x] = 0
    print arr
#zero_out(myarr)

#MIN MAX AVG
myarr = [2,3,4,5,66,78]
def min_max_avg(arr):
    min = 0
    max = 0
    sum = 0
    for x in arr:
        if x > max:
            max = x
        if x < min:
            min = x
    for x in arr:
        sum = sum + x
    avg = sum / len(arr)
    newarr = [max,min,avg]
    #print newarr
#min_max_avg(myarr)

#SHIFT ARRAY VALUES
#not sure on how to do this one
myarr = [2,3,4,5,6,7,9]
def shift(arr):
    for idx in range(0,len(arr)-1):
        arr[idx] = arr[idx +1]
    return arr
print shift(myarr)
#SWAP STRING FOR ARRAY NEGATIVE VALUES
myarr = [3,-4,5,6,-7,2]
def swap_val(arr):
    for x in range(0,len(arr)):
        if arr[x] < 0:
            arr[x] = "Dojo"
    return arr 
#swap_val(myarr)

#print myarr    
             
        



#print_1_To_255()
#print_ints_and_sum()
#print_odds()
#myarr = [1,2,3,4,5]
#iterate_arr(myarr)
#myarr = [1,7,2,5,3,4]
#find_max(myarr)
#myarr = [2,3,6,8,9,4]
#get_avg(myarr)
#myarr = [4,5,6]
#square_vals(myarr)
#arr_odds()
#myarr = [2,3,4,5,7,9,6]
#y = 5
#greater_y(myarr,y)
#myarr = [2,3,4,-5,-7,-6]
#zero_out(myarr)
#myarr = [2,3,4,5,6,7,33,4,6,8]
#min_max_avg(myarr)
#myarr = [3,-4,5,6,-7,2]
#shift_array(myarr)
#swap_val(myarr)
#print myarr