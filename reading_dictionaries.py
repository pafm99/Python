#PART ONE
info = {
    'name': "paul",
    'age': "35",
    'country': "USA",
    'fav_lang': "Python"
    }
def my_dict(info):
    for key, val in info.iteritems():
            if key == "name":
                print "My", key, "is", val
            elif key == "age":
                print "I am", val, "years old"
            elif key == "country":
                print "My country of birth is the ", val
            elif key == "fav_lang":
                print "My favorite programming language is ", val
my_dict(info)
