input=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
Abo=list()

def flatten(input,Abo):
    for i in input:
        if type(i) is list:
            flatten(i,Abo)
        else:
            Abo.append(i)
    return Abo

FlattenList=flatten(input,Abo)
print(FlattenList)