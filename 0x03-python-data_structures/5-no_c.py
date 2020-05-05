#!/usr/bin/python3
def no_c(my_string):
    for j in my_string:
        for i in range(len(j)):
            if ord(j[i]) == 67 or ord(j[i]) == 99:
                new_string = my_string[:i] + my_string[i + 1:]
            else:
                new_string = my_string
            return(new_string)
