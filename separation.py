form = 'Ca(NO3)2'
nums = []
def separation(form=form, elements = [], s = ''):
    for i in form:
        try:
            i = int(i)
            nums.append(i)
        except ValueError:
            elements.append(i)
    for a in elements:
        if a == '(' or a == ')':
            elements.remove(a)
    return elements

def metal_acid(lis, met = []):
    if len(lis) == 2:
        metal = lis[0]  
    elif len(lis) == 3:
        if lis[1] == lis[1].lower():
            metal = lis[0]+lis[1]
        else:
            metal = lis[0]
    elif len(lis) == 4:
        if lis[1] == lis[1].lower():
            metal = lis[0]+lis[1]
        else:
            metal = lis[0]
    elif len(lis) == 5:
        metal = lis[0]+lis[1]
    return metal 

def final(s = '', a = '', sl = {}):
    m = metal_acid(separation())

    for i in form.split(m):
        try:    
            s += str(int(i))
        except ValueError:
            if s != '':
                sl[m] = int(s)
            else:
                sl[m] = 1
    if ')' in form:
        a+=form[form.index(')')+1:]
        if a != '':
            sl[form[form.index('(')+1:form.index(')')]] = int(a)
        else:
            sl[form[form.index('(')+1:form.index(')')]] = 1

    return sl
def st_ok():
    slov = final()
    slov2 = {}
    lis_k = []
    for k in slov.keys():
        lis_k.append(k)
    for i in range(0,1000):
        if i // slov[lis_k[0]] and i // slov[lis_k[1]]:
            slov2[lis_k[0]] = i // slov[lis_k[0]]
            slov2[lis_k[1]] = (i // slov[lis_k[1]])*-1
            return slov2
print(st_ok())





        





