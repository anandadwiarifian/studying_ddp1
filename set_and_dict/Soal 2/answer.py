set_num = int(input('How many sets? '))
print(f'Please input {set_num} set(s) containing the hashcodes')

set_a = set()
for i in range(0,set_num):
    set_b = set(input().strip('{}').replace(' ','').split(','))
    set_a = set_a.symmetric_difference(set_b)

print('Unique hashcode(s) are:')
print(str(set_a).replace("'",""))