def rut(list_:list,sk_Index:int,ek_Index:int):
    
    if sk_Index < ek_Index:
        ek_Index += 1
        nu = list_[:sk_Index]
        pu = list_[sk_Index+1:ek_Index]
        last = list_[ek_Index:]
        move_Value = list_[sk_Index]
        base = []
        for i in nu:
            base.append(i)
        for i in pu:
            base.append(i)
        base.append(move_Value)
        for i in last:
            base.append(i)
        
        # print(base)
        return base
    elif sk_Index > ek_Index:
        nu = list_[:ek_Index]
        pu = list_[ek_Index:sk_Index]
        last = list_[sk_Index+1:]
        move_Value = list_[sk_Index]
        
        base = []
        for i in nu:
            base.append(i)
            # print(i)
        base.append(move_Value)
        # print(move_Value,"::")
        for i in pu:
            base.append(i)
            # print(i,":::")
        for i in last:
            base.append(i)
            # print(i,"::::")
        
        # print(base)
        return base
    # print(list_)
    return list_

def list_add(list_,Index_,Value):
    a = list_[:Index_]
    b = list_[Index_:]
    france = []
    for i in a:
        france.append(i)
    france.append(Value)
    for i in b:
        france.append(i)
    return(france)

pp = []
key = []
SAME = []
num = int(input())
if num > 100:
    num == 100
for i in range(num):
    a = input()
    b = input()
    if b != "SAME":
        pp.append(a)
        key.append(b)
    else:
        SAME.append([i,a])
r = 0
test = pp
cosp = test
kes = key

for index, value in enumerate(test[::-1]):
    index = len(test) - 1 - index
    index_sub = index + r
    if kes[index] == "DOWN":
        index =index+ 1+r
        if len(test)-1 < index:
            index = 0
        # print(index_sub, ":",index)
        cosp = rut(cosp, index_sub, index)
        r+=1
        # print(cosp)
for i,v in SAME:
    cosp = list_add(cosp, i, v)
for i in cosp:
    print(i)

