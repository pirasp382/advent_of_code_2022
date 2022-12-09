def part_1(data:list)->int:
    max1 = 0
    max2 = 0
    max3 = 0
    sum =0
    list = []
    for item in data:
        if item != '\n': 
            
            sum +=int(item)
        else: 
            list.append(sum)
            sum =0
    list.append(sum)
    max1 = max(list)
    list.remove(max1)
    max2 = max(list)
    list.remove(max2)
    max3 = max(list)
    return max1+max2+max3, max1
file = open('input_1', 'r')
data = file.readlines()
print(part_1(data))