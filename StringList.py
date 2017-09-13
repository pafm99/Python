words = "It's thanksgiving day. It's my birthday, too!"
day = "day"
month = "month"
print words
print words.find('day')
print words.replace(day, month)


x = [2,54,-2,7,12,98]
print max(x)


y = ["hello",2,54,-2,7,12,98,"world"]
print y[0], y[-1]
z = [y[0], y[-1]]
print z


a = [19,2,54,-2,7,12,98,32,10,-3,6]
a.sort()
print a
print len(a)/2
b = a[0:5]
print b
print a
del a[0:5]
print a
a.insert(0,b)
print a
