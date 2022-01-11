input=[[1, 2], [3, 4], [5, 6, 7]]
Reverse=list()
def reverseh(input):
    for i in input:
        if type(i) is list:
            i.reverse()
    input.reverse()
    return input

Reversed=reverseh(input)
print(Reversed)