line_one = "* * * * "
line_two = " * * * *"
lines = 8
line = 1
while line <= lines:
    if line % 2 != 0:
        print line_one
        line = line + 1
    else:
        print line_two
        line = line + 1
#in a function
def checkerboard():
    for x in range(0, 8):
        if x%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
checkerboard()
