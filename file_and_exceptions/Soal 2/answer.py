import re

masukan = input("Masukkan nama file input dan output: ")
masukan = masukan.split(' ')

with open(masukan[0],'r') as input, open(masukan[1],'w') as output:
    try:
        surat = input.read()
        codes = re.findall("<start>(.*?)<end>", surat)
        translation = ' '.join([code.strip() for code in codes])
        output.write(translation)
    except:
        print(f'File {masukan[0]} bermasalah! Benny lolos kali ini.')
    finally:
        input.close()
        output.close()
        print(f'Rahasia telah terbongkar, silakan cek file {masukan[1]}')
