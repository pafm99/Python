for row in range(1, 13): 
    display_string  = ''
    for column in range(1, 13):   
            display_string += ' ' + str(column * row)
    print display_string
