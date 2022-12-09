def part_one(data):
    count=0
    for line in data:
        first, second = line.split(',')
        if int(first[:first.index('-')]) >= int(second[:second.index('-')]) and int(first[first.index('-')+1:]) <= int(second[second.index('-')+1:]):
            count+=1
        elif int(first[:first.index('-')]) <= int(second[:second.index('-')]) and int(first[first.index('-')+1:]) >= int(second[second.index('-')+1:]):
            count+=1
    return count

def part_two(data):
    count=0
    for line in data:
        first_range, second_range = line.split(',')
        start_a, end_a = map(int, first_range.split('-'))
        start_b, end_b = map(int, second_range.split('-'))
        if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
            count += 1
    return count
            

file = open('input', 'r')
data = file.readlines()
print(part_one(data))
print(part_two(data))