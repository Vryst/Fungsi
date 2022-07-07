import os

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
bg = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

#latihan fungsi

def header():
     os.system("clear")
     print(f"""{end}{bold}{blue}
{'—'*65}{end}{bold}
{'SELAMAT DATANG':^65}
{'DI':^65}{green}
{'PROGRAM PERHITUNGAN':^65}
{'LUAS DAN KELILING':^65}{end}{bold}{blue}
{'—'*65}
     """)
     
def input_user():
     panjang = int(input(f"{end}{bold}Masukan nilai panjang = {green}"))
     lebar = int(input(f"{end}{bold}Masukan nilai lebar   = {green}"))
     return panjang,lebar
     
def hasil_luas(panjang,lebar):
     return panjang*lebar
     
def hasil_keliling(panjang,lebar):
     return float(2*(panjang+lebar))
     
while True:
     
     header()
     panjang,lebar = input_user()
     luas = float(hasil_luas(panjang,lebar))
     keliling = float(hasil_keliling(panjang,lebar))
     
     isPilih = input(f"{end}\n{bold}{underline}Apa yg mau di hitung?{end}{bold}\nLuas = l\nKeliling = k\n\nPilih (l/k)     = {green}")
     if isPilih == "l":
          print(f"{end}{bold}\nHasilnya adalah = {green}{underline}{luas}")
          isLanjut = input(f"{end}{bold}{bg}\nUlang program (y/n) ? = {end} {green} ")
          if isLanjut == "y":
               continue
          elif isLanjut == "n":
               print(f"{bold}{blue}PROGRAM SELESAI{end}")
               break
          else:
               print(f"{bold}{red}\n\nERROR {end}{bold},{red} PROGRAM DIHENTIKAN{end}")
               break
               
     elif isPilih == "k":
          print(f'{end}{bold}Hasilnya adalah = {green}{underline}{keliling}{end}')
          
          isLanjut = input(f"{end}{bold}{bg}\nUlang program (y/n) ? = {end} {green} ")
          if isLanjut == "y":
               continue
          elif isLanjut == "n":
               print(f"{end}\n\n{bold}PROGRAM SELESAI{end}")
          else:
              print(f"{bold}{red}\n\nERROR {end}{bold},{red} PROGRAM DIHENTIKAN{end}")
              break
         
     else:
          print(f"{bold}{red}\n\nERROR {end}{bold},{red} PROGRAM DIHENTIKAN{end}")
          break
