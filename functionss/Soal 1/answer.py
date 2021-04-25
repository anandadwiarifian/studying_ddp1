def median(numbers_: list) -> float:
    urut = sorted(numbers_)
    if len(urut) % 2 == 0:
        return 1/2*(urut[int(len(urut)/2)] + urut[int(len(urut)/2+1)])
    else:
        return urut[int((len(urut)-1)/2)]

def mean(numbers_: list) -> float:
    return sum(numbers_)/len(numbers_)

def variance(numbers_: list) -> float:
    rata2 = mean(numbers_)
    temp = [(i - rata2)**2 for i in numbers_]

    return sum(temp)/(len(numbers_) - 1)

with open('input.txt','r') as f_input, open('output.txt','w') as f_output:
    try:
        content = f_input.readlines()
        content = [x.strip() for x in content]
        numbers = [float(x) for x in content[0].split(' ')]
        num_of_op = int(content[1])
        operations = content[2:7]

        for operation in operations:
            if operation.lower() == 'max':
                f_output.write(f'Nilai maksimum adalah {max(numbers)}')
            elif operation.lower() == 'min':
                f_output.write(f'Nilai minimum adalah {min(numbers)}')
            elif operation.lower() == 'median':
                f_output.write(f'Nilai median adalah {median(numbers):.2f}')
            elif operation.lower() == 'varian':
                f_output.write(f'Nilai varian adalah {variance(numbers):.2f}')
            elif operation.lower() == 'mean':
                f_output.write(f'Nilai mean adalah {mean(numbers):.2f}')
            else:
                f_output.write(f'Operasi {operation} tidak ada')
            f_output.write('\n')
    finally:
        f_input.close()
        f_output.close()
    