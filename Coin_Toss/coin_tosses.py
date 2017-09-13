import random
def coin_toss(attempts):
    trial = 0
    tails_count = 0
    heads_count = 0
    while trial < attempts:
        trial = trial + 1
        coin = random.randint(0,1)
        if coin == 0:
            tails_count+=1
            print "Atempt: ", trial, "...Throwing a coin .... it's tails. ... Got", tails_count, "tail(s) so far"
        elif coin == 1:
            heads_count+=1
            print "Atempt: ", trial, "...Throwing a coin .... it's heads. ... Got", heads_count, "head(s) so far"
    print "Total heads: ", heads_count
    print "Total tails: ", tails_count
    print "Ending the program, thank you!"

coin_toss(10)
