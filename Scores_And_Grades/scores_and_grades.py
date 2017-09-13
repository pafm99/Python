import random
def scores():
    for x in range(0, 10):
        random_num = random.randint(60,100)
        if random_num >= 60 and random_num <= 69:
            print "Score: ", random_num, "Your grade is D"
        elif random_num >= 70 and random_num <= 79:
            print "Score: ", random_num, "Your grade is C"
        elif random_num >= 80 and random_num <=89:
            print "Score: ", random_num, "Your grade is B"
        else:
            print "Score: ", random_num, "Your grade is A"
    print "End of program. Bye!"

scores()
