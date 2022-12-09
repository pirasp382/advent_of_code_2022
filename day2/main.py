def part_one(data:list)->int:
    a =''
    b = ''
    sum =0
    for item in data:
        a, b = item.split()
        if a == 'A':
            if b == 'X': sum +=3+1
            elif b =='Y': sum+=6+2
            else: sum+=3
        elif a == 'B':
            if b=='Z': sum+=6+3
            elif b=='Y': sum+= 3+2
            else: sum+=1
        else:
            if b == 'X': sum+=6+1
            elif b=='Z':sum+=3+3
            else: sum+=2
    return sum

def part_two(data:list)->int:
    sum = 0
    a=0
    b = 0
    for item in data:
        a, b = item.split()
        if a == 'A':
            if b == 'X': sum +=3
            elif b =='Y': sum+=4
            else: sum+=8
        elif a == 'B':
            if b=='Z': sum+=9
            elif b=='Y': sum+= 3+2
            else: sum+=1
        else:
            if b == 'X': sum+=2
            elif b=='Z':sum+=7
            else: sum+=6
    return sum

file = open('input_1', 'r')
data = file.readlines()
print(part_one(data))
print(part_two(data=data))
