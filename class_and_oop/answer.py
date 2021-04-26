class Driver:
    '''
    Class for Benjek Driver data template
    Attributes:
        name (str): Driver's name
        ride_type (str): Driver's ride type (Normal / Sport / Cruiser)
        income (int): Driver's income
    '''

    def __init__(self, name, ride_type):
        '''
        Construct a BenJek Driver
        Attributes:
            name (str): Driver's name
            ride_type (str): Driver's ride type (Normal / Sport / Cruiser)
            income (int): Driver's income
        '''
        self.name = name
        self.ride_type = ride_type
        self.income = 0

    def ride(self, distance: float) -> str:
        '''
        Method to allow a driver to escort the customer and 
        save the fare of the ride based on the distance (float)
        '''
        if distance <= 0:
            return 'Jarak yang diinput salah. Silahkan coba lagi'
        if self.ride_type == 'NORMAL':
            cost = distance*ride_types['NORMAL']*0.8
        if self.ride_type == 'SPORT':
            if distance < 10:
                return f'{self.name} tidak bisa melakukan perjalanan'
            cost = distance*ride_types['SPORT']*0.8
        if self.ride_type == 'CRUISER':
            if distance < 25:
                return f'{self.name} tidak bisa melakukan perjalanan'
            cost = distance*ride_types['CRUISER']*0.8

        self.income += cost
        return f'{self.name} melakukan perjalanan sejauh {distance} dan mendapatkan pendapatan sebesar Rp.{cost:.2f}'

    def incomeCheck(self) -> str:
        '''
        Method to check the driver's current income
        '''
        return f'{self.name} memiliki pendapatan sebesar Rp.{self.income:.2f}'


def driversApply(name: str, ride_type: str) -> str:
    if name in drivers:
        return f'{name} gagal mendaftar sebagai driver BenJek'
    if ride_type not in ride_types:
        return 'Tipe driver yang dimasukkan salah'
    drivers[name] = Driver(name, ride_type)
    return f'{name} berhasil mendaftar sebagai driver BenJek layanan {ride_type}'


def endOfMonth(monthIncome: float) -> str:
    string = f'Sudah akhir bulan! Pendapatan BenJek bulan ini adalah Rp.{benjekIncome:.2f}\n'
    string += 'Daftar pendapatan pengemudi:\n'
    for key in drivers:
        string += f'{key}: Rp.{drivers[key].income:.2f}\n'
    return string


drivers = {}
ride_types = dict(zip(['NORMAL', 'SPORT', 'CRUISER'], [1000, 2500, 7500]))
benjekIncome = 0

print(('Selamat datang di program pengelola pangkalan data BenJek.\n'
       'Berikut adalah perintah yang bisa Anda jalankan:\n'
       'DAFTAR <nama_driver> <NORMAL/SPORT>\n'
       'MULAI PERJALANAN <nama_driver> <jarak_ditempuh_km>\n'
       'CEK PENDAPATAN <nama_driver>'
       'AKHIR BULAN\n'
       'END PROGRAM -> untuk mengakhiri program\n'
       'Masukkan perintah yang ingin Anda jalankan:\n'))

while True:
    command = input()
    com = command.split()

    if com[0] == 'DAFTAR':
        print(driversApply(com[1], com[2]))
    elif com[0] + ' ' + com[1] == 'MULAI PERJALANAN':
        if com[2] not in drivers:
            print(f'{com[2]} belum mendaftar sebagai driver BenJek')
        else:
            print(drivers[com[2]].ride(float(com[3])))
        benjekIncome += drivers[com[2]].income * 0.25
    elif com[0] + ' ' + com[1] == 'CEK PENDAPATAN':
        if com[2] not in drivers:
            print(f'{com[2]} belum mendaftar sebagai driver BenJek')
        else:
            print(drivers[com[2]].incomeCheck())
    elif command == 'AKHIR BULAN':
        print(endOfMonth(benjekIncome))
    elif command == 'END PROGRAM':
        exit('Terima kasih sudah menggunakan aplikasi ini')
    else:
        print('Perintah yang anda masukan salah')
