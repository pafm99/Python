
#PART 1
#x = [4, 6, 1, 3, 5, 7, 25]
#def draw_stars(x):
#    for num in x:
#        print "*" * num
#draw_stars(x)

#PART 2

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(y):
    for x in y:
        if type(x) is int:
            print "*" * x
        elif isinstance(x,str):
                length = len(x)
                letter = x[0].lower()
                print letter * length
draw_stars(y)

