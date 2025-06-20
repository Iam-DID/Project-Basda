from core.Database import curr_db as db
import time
from controller.terminal import clear_terminal, kembali
from model.akun import mlogin

def login():
    clear_terminal()
    print('\n' + '=' * 20 + ' LOGIN ' + '=' * 20 + '\n')
    no_hp = input("No HP: ")
    password = input("Password: ")

    try:
        user = mlogin(no_hp, password)

        if user:
            id_akun= user[0]
            nama= user[1]
            status = user[2]
            # password = user[3]
            
            if status == "O":
                return("owner", nama, id_akun)
                
            else : 
                return("petani", id_akun, nama)
            
        else:
            input("Login gagal: Nomor HP atau Password Salah")
            time.sleep(1)
            kembali()

    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        time.sleep(1)
        kembali()
        
    finally:
        conn, cur = db()
        cur.close()
        conn.close()