#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
p = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"

# input
q = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
numSum = 0
stringX = ''
stringXt = False
integerXt= False
for x in l:
    if type(x) == int or type(x) == float:
        numSum = numSum + x
        integerXt = True
    else:
        stringX = stringX + x + ' '
        stringXt = True
        
if integerXt == stringXt:
    print "The list you enteres is of Mixed Type"
    print numSum
    print stringX
elif type(x) == int or type(x) == float:
    print "The list you Entered is of Integer type"
    print numSum
else:
    print "The list you entered is of string type"
    print stringX
    
        
        
        
