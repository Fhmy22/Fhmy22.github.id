import datetime as dt

def hidupmu() :
 #fahmyramadhan :)
 print("======================")
 print("Menghitung Seberapa Lama Anda Hidup")
 #memasukan input data ke dalam variabel tanggal, bulan, tahun
 nama = str(input("Masukan Nama Kamu : "))
 tanggal = int(input("Masukan Tanggal Lahir :"))
 bulan = int(input("Masukan Bulan Lahir :"))
 tahun = int(input("Masukan Tahun Lahir :"))
 tanggal_lahir = dt.date(tahun,bulan,tanggal)
 
 print("========Hasil========")
 print(f"Hallo {nama}")
 print(f"Anda Lahir Pada : {tanggal_lahir}")
 hari_ini = dt.date.today()
 #menghitung lama hidup rumus (today - years-month-day)
 lama_hidup = hari_ini - tanggal_lahir
 #menghitung tahun (lama_hidup // 365)
 tahun_lahir = lama_hidup.days // 365
 bulan_lahir = (lama_hidup.days % 365) // 30
 #memanggil hasil dari masing masing variable
 print(f"Anda lahir pada hari/days : {tanggal_lahir:%A}")
 print(f"Anda telah hidup selama: {lama_hidup},{bulan_lahir}")
 print("Usia anda: {18}},Tahun :)")
 
 #melakukan pengulangan
 #jadi jika user memilih no:1 semua akan di ulangi
while True :
 hidupmu()
 print('''
 Ingin mengulanginya ? :
 1.Ya
 2.Tidak
 ''')
 data = int(input("ingin mengulanginya ? 1/2 :"))
 if data > 1 :
    print("Terimakasih")
    break