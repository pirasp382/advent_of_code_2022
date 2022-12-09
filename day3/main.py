def part_one(data):
    sum =0
    list = []
    for line in data:
        item1 = line[:int(len(line)/2)]
        item2 = line[int(len(line)/2):]
        for letter in item1:
            if item2.__contains__(letter): 
                list.append(letter)
                break
    
    for item in list:
        if item.isupper(): sum+= (ord(item)-ord('A')) +27
        else: sum+= (ord(item)-ord('a')+1)
    return sum

def part_two(data):
    sum = 0
    list = []
    for i in range(0,len(data)-2, +3):
        item1 = data[i]
        item2 = data[i+1]
        item3 = data[i+2]
        for letter in item1:
            if item2.__contains__(letter) and item3.__contains__(letter):
                list.append(letter)
                break
    for item in list:
        if item.isupper(): sum+= (ord(item)-ord('A')) +27
        else: sum+= (ord(item)-ord('a')+1)
    return sum
            

file = open('input', 'r')
data = file.readlines()
print(part_one(data=data))
print(part_two(data))