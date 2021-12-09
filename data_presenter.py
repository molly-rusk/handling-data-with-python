#3
open_file = open("CupcakeInvoices.csv")

#for line in open_file:
    #print(line)

open_file.seek(0, 0)

#4

for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])

open_file.seek(0, 0)

#5

for line in open_file: 
    line = line.rstrip('\n').split(',')
    
    purchased = line[3]
    price = line[4]
    total = int(purchased) * float(price)
    print(total)

open_file.seek(0, 0)

#6

totals = 0

for line in open_file: 
    line = line.rstrip('\n').split(',')
    purchased = line[3]
    price = line[4]
    totals += int(purchased) * float(price)

print(totals)


open_file.seek(0, 0)

#part 3

total_chocolate = 0
total_vanilla = 0
total_strawberry = 0

for line in open_file:
    line = line.rstrip('\n').split(',')
    line_total = int(line[3]) * float(line[4])
    for value in line:
        if value == 'Chocolate':
            total_chocolate += line_total
        elif value == 'Vanilla':
            total_vanilla += line_total
        elif value == 'Strawberry':
            total_strawberry += line_total

print('Chocolate:', total_chocolate, 'Vanilla:', total_vanilla, 'Strawberry:', total_strawberry)


open_file.close()