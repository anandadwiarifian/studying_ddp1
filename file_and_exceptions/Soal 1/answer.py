
with open('input1.txt', 'r') as input1, open('input2.txt', 'r') as input2, \
        open('output.txt', 'w') as output:
    try:
        belanja_saya = input1.read().splitlines()
        total_belanja = input2.read()
        for item in belanja_saya:
            count = total_belanja.count(item)
            if count == 0:
                output.write(f'Tidak ada {item} di dalam daftar belanja\n')
            else:
                output.write(
                    f'Jumlah {item} dalam daftar belanja adalah sebanyak {count} buah\n')
    finally:
        input1.close()
        input2.close()
        output.close()


# input1 = open('input1.txt','r')

# belanja = input1.read().split('\n')
