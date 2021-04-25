with open('input.txt', 'r') as f_in:
    try:
        commands = [x.strip() for x in f_in.readlines()]
        names = list()
        teman_list = dict()
        sahabat_list = dict()
        for command in commands:
            if command.startswith('TAMBAH'):
                name = command.replace('TAMBAH ','')
                if name in teman_list:
                    print(f'{name} sudah ada')
                else: 
                    teman_list[name] = set()
                    sahabat_list[name] = set()
                    print(f'{name} sudah ditambah')
            elif command.endswith(' BERTEMAN'):
                nama2 = [x for x in command.replace(' BERTEMAN','').split(' ')]
                if not set(nama2).issubset(teman_list):
                    print('Nama tidak ditemukan')
                else:
                    teman_list[nama2[0]].add(nama2[1])
                    teman_list[nama2[1]].add(nama2[0])
            elif command.endswith(' BERSAHABAT'):
                nama2 = [x.strip() for x in command.replace(' BERSAHABAT','').split(' ')]
                if not set(nama2).issubset(sahabat_list):
                    print('Nama tidak ditemukan')
                else:
                    sahabat_list[nama2[0]].add(nama2[1])
                    sahabat_list[nama2[1]].add(nama2[0])
                    teman_list[nama2[0]].add(nama2[1])
                    teman_list[nama2[1]].add(nama2[0])
            elif command.startswith('SAHABAT ') and command.find(' BUKAN '):
                nama2 = [x.strip() for x in command.replace('SAHABAT ','').replace('BUKAN ','').split(' ')]
                if not set(nama2).issubset(sahabat_list):
                    print('Nama tidak ditemukan')
                else:
                    set_a = sahabat_list[nama2[0]].difference(sahabat_list[nama2[1]])
                    string_set = str(set_a).replace("'","").strip('{}')
                    print(string_set)
            elif command.startswith('TEMAN'):
                nama2 = [x.strip() for x in command.replace('TEMAN ','').split(' ')]
                if not set(nama2).issubset(teman_list):
                    print('Nama tidak ditemukan')
                else:
                    set_a = teman_list[nama2[0]].intersection(teman_list[nama2[1]])
                    string_set = str(set_a).replace("'","").strip('{}')
                    print(f"Teman dari {nama2[0]} dan {nama2[1]} adalah {string_set}")
            elif command == 'END':
                exit(None)
    finally:
        f_in.close()