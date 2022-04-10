import psycopg2 as db
import os
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(
        host='localhost', 
        database="dbr1",
        port=5432,
        user="aji",
        password="12345"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected == True):
        cursor.close()
        con.close()
    else:
        con = None
        connected = False

def Buat():
    global connected
    global con
    global cursor
    a = connect()
    a.execute("""
                CREATE TABLE pegawai
                (
                    idpegawai serial primary key,
                    nik varchar(15) unique not null,
                    nama varchar(40) not null,
                    jabatan varchar(30) not null,
                    nohp varchar(30) not null
                    )
                    """)
    con.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")

def Entry():
    global connected
    global con
    global cursor
    xnik = input("Masukan nik : ")
    xnama = input("Masukan Nama Lengkap : ")
    xjbt = input("Masukan Posisi jabatan : ")
    xnohp = input("Masukkan No Hp  : ")
    a = connect()
    sql = "insert into pegawai (nik, nama, jabatan, nohp) values ('"+xnik+"', '"+xnama+"', '"+xjbt+"', '"+xnohp+"')" 
    a.execute(sql)
    con.commit()
    print("Entry is done.")

def Cari():
    global connected
    global con
    global cursor
    xnik = input("Masukan nik yang di cari : ")
    a = connect()
    sql = "select * from pegawai where nik='"+xnik+"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("Search is done.")

def Ubah():
    global connected
    global con
    global cursor
    xnik = input("Masukan nik yang di cari : ")
    a = connect()
    sql = "select * from pegawai where nik='"+xnik+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini")
    print(record)
    row = a.rowcount
    if (row == 1):
        print("Silakan untuk mengubah data..")
        xnama = input("Masukan Nama Lengkap : ")
        xjbt = input("Masukan Posisi Jabatan: ")
        xnohp = input("Masukan no hp : ")
        a = connect()
        sql = "update pegawai set nama='"+xnama+"', jabatan='"+xjbt+"', nohp='"+xnohp+"' where nik='"+xnik+"'" 
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql = "select * from pegawai where nik='"+xnik+"'"
        a.execute(sql)
        record = a.fetchall()
        print("Data setelah di ubah :")
        print(record)
    else:
        print("Data tidak di temukan")

def Hapus():
    global connected
    global con
    global cursor
    xnik = input("Masukkan nik yang dicari : ")
    a = connect()
    sql = "select * from pegawai where nik ='"+xnik+"'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("Apakah anda ingin menghapus data? (y/t) > > > ")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from pegawai where nik ='"+xnik+"'"
            a.execute(sql)
            con.commit()
            print("Delete is done.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan")

def show_menu():
  print("\n=== APLIKASI DATABASE POSTGRESQL PYTHON ===")
  print("1. Membuat Tabel Pegawai")
  print("2. Buat Data")
  print("3. Cari Data")
  print("4. Ubah Data")
  print("5. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")
  os.system("cls")
  if menu == "1":
    Buat()
  elif menu == "2":
    Entry()
  elif menu == "3":
    Cari()
  elif menu == "4":
    Ubah()
  elif menu == "5":
    Hapus()
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")
if __name__ == "__main__":
  while(True):
       show_menu()