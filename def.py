def asep():
     print("Halo asep")
     print("Halo asyep")
     print("Hello Mr.Asep asyep\n")
#memanggil definition
asep() #mudah bukan?

#============================

def fungsi(nama):
     print(f"Halo {nama}")
     '''def dengan input'''
fungsi("otong\n")#input di dalam fungsinya .("disini inputnya")

#============================

def list_peserta(peserta):
     
     data_peserta = peserta.copy()#(2.) lalu data peserta meng-copy data yg ada di input list_peserta {jika dilihat disini maka yg diambil itu variabel "anggota" yg berisikan list
     for peserta in data_peserta: #(3.) setiap data yg ada di input data_peserta (yaitu "anggota" yg ada di list_peserta lalu di copy ke data_peserta sehingga data peserta memiliki input yg sama yaity variabel "anggota") itu diberi tanda sebagai "peserta" 
     #( lanjutan no (3.) ), (masing-masing yg disebut oleh saya "data" itu data yg dibatasi koma dengan data lainnya) 
          print(f"Halo {peserta}") #print "halo + peserta yg ada di data_peserta (karena ada 3, maka akan mengulang print sampai akhir data yg ber-tanda "peserta"
          
anggota = ["ucup","otong","dudung"]

list_peserta(anggota)#(1.)memasukan anggota ke dalam fungsi list_peserta.()

#============================

#def dengan default argument

def say_hello(vama ="bwang"):
     print(f"Halo {vama}") 
     
say_hello("bambang")# jika di biarkan kosong maka akan diganti menjadi setelan argumen default, yaitu = ("bwang")

def sapa(nama = "bang", pesan = "Apa kabar?"): # pesan default ada di sebelah kanan '=' per-variabel
     print(f"\nHalo {nama}, {pesan}")
     
sapa("Jang","kepriwe kabare?\n") #jika kosong (hanya : sapa() ) maka akan menampilkan output " Halo bang, Apa kabar? "

#hitung pangkat

def hitung_pangkat(angka,pangkat=2):
     hasil_pangkat = angka**pangkat
     return hasil_pangkat
     
print(hitung_pangkat(5,10)) #jika hanya 1 variabel yg di input (variabel per-selesai koma) maka yg pangkat(variabel setelah koma) akan memakai argumen default (yaitu 2/ pangkat=2)

print("\nDiubah dengan variabel baru")
hasil = hitung_pangkat(angka=7,pangkat=7)#berguna jika variabel di dalam def fungsi() itu ada banyak, dan sulit untuk diubah langsung di dalam fungsi, maka diubah dengan variabel baru dan di-isi dengan value fungsi(variabel=_data_=_?_ , _data_=_?_)
print(hasil) #memanggil hasil yg sudah diubah tadi

#contoh lain???

def hitungan(input1=1,input2=2,input3=3,input4=4):
     hasil = input1 + input2 + input3 + input4 #hasil = 10, kecuali jika variabel dalam fungsi nilainya diubah
     return hasil
     
print("\nHitungan\n")
print(hitungan())
print(hitungan(input1=6)) #mengubah value dari  variabel "input1" di dalam fungsi hitungan() menjadi bernilai 6, maka output bisa dibilang hasil dari 6 + 2 + 3 + 4 = (15)



#fungsi dengan return

def fungsi_tambah(a,b):
     hasil = a + b
     return hasil
     
quack = int(input("Masukan angka = "))
quek = int(input("Angka 2 = "))
fungsi_tambah(quack,quek)
print(fungsi_tambah(quack,quek))

#atau "simpelnya" =
def tambah(a,b):
     a = a + b
     print(a)
     
a = int(input("Masukan angka pertama = "))
b = int(input("Masukan angka kedua = "))

tambah(a,b)

#simpel?????? relatif?

def data_nama(inama):
     name = inama
     print(name)
     
inama = input("Masukan nama = ")
data_nama(inama)

#y

