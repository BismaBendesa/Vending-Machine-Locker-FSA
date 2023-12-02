import tkinter as tk
import customtkinter
from PIL import Image
from datetime import datetime, timedelta
import random
# from ui_start import UiStart
# from ui_main_menu import UiMainMenu
# # from contact_screen import ContactScreen

# class NavigateTest(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Vending Machine Locker")
        
#         self.frames = {
#             "home": UiStart(self),
#             "about": UiMainMenu(self),
#             # "contact": ContactScreen(self),
#         }
        
#         self.show_frame("home")
    
#     def show_frame(self, frame_name):
#         frame = self.frames.get(frame_name)
#         if frame:
#             frame.tkraise()

# if __name__ == "__main__":
#     app = NavigateTest()
#     app.geometry("720x480")
#     app.mainloop()

# variable 
daftar_loker = ["kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong"];
password_loker = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
notelp_loker = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]

ambil_sementara = False

i = 0
storage_time = ''

def show_home():
    global ambil_sementara
    entry_no_loker.delete(0, "end")
    entry_no_loker_taruh.delete(0, "end")
    entry_no_telp.delete(0, "end")
    entry_password.delete(0, "end")
    ambil_sementara = False
    print("Memori Vending Machine")
    print("-----------------------------")
    print("Daftar Loker")
    print("-----------------------------")
    print(daftar_loker)
    print("Pass Loker")
    print("-----------------------------")
    print(password_loker)
    print("Pass Loker")
    print("-----------------------------")
    print(notelp_loker)
    home_frame.pack()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    taruh_barang_frame.pack_forget()
    input_loker_frame.pack_forget()
    masukan_password_frame.pack_forget()
    password_salah_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()

def show_about():
    home_frame.pack_forget()
    about_frame.pack()
    main_menu_frame.pack_forget()
    taruh_barang_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()

def show_main_menu():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack()
    taruh_barang_frame.pack_forget()
    password_salah_frame.pack_forget()
    input_loker_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_taruh_barang():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    password_salah_frame.pack_forget()
    taruh_barang_frame.pack()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    input_loker_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()



def show_input_loker_ambil():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    masukan_password_frame.pack_forget()
    password_salah_frame.pack_forget()
    input_loker_frame.pack()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()

def show_input_loker_taruh():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    masukan_password_frame.pack_forget()
    password_salah_frame.pack_forget()
    input_loker_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_masukan_password():
    global global_no_loker
    global_no_loker = int(entry_no_loker.get())
    print(daftar_loker[global_no_loker - 1])
    print(global_no_loker)
    # Kalau benar, mau buka sementara atau logout
    # Kalau salah, tampilkan password salah
    # Kalau salah 5x tampilkan password salah 5x
    loker_penuh_frame.pack_forget()
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    masukan_password_frame.pack()
    lebih_12_jam_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_password_salah():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack()
    masukan_password_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()



    
def show_password_salah5x():
    print(entry_password.get())
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack()
    masukan_password_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()






def show_lebih_12_jam():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_menu_ambil_barang():
    print(entry_password.get())
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack()
    loker_terbuka_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_loker_terbuka():
    global_no_loker = int(entry_no_loker.get())
    print(global_no_loker)
    global ambil_sementara

    if ambil_sementara:
        ambil_sementara = True
    else:
        ambil_sementara = False


    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack()
    loker_penuh_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()
    
def show_loker_terbuka_taruh_barang():
    global_no_loker = int(entry_no_loker_taruh.get())
    print(global_no_loker)
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()





def show_konfirmasi_tutup():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    konfirmasi_tutup_frame.pack()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()


def show_konfirmasi_tutup_taruh_barang():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()








def show_loker_dikunci_ambil_barang():
    global global_no_loker
    global ambil_sementara
    global_no_loker = int(entry_no_loker.get())
    print("Memori Vending Machine")
    print("-----------------------------")
    print("Daftar Loker")
    print("-----------------------------")
    if ambil_sementara:
        daftar_loker[global_no_loker - 1] = "isi"
    else:
        daftar_loker[global_no_loker - 1] = "kosong"
    print(daftar_loker)
    print("Pass Loker")
    print("-----------------------------")
    if ambil_sementara:
        password_loker[global_no_loker - 1] = password_loker[global_no_loker - 1]
    else: 
        password_loker[global_no_loker - 1] = "NULL"
    print(password_loker)
    print("No telp Loker")
    print("-----------------------------")
    if ambil_sementara:
        notelp_loker[global_no_loker - 1] = notelp_loker[global_no_loker - 1]
    else:
        notelp_loker[global_no_loker - 1] = "NULL"
    print(notelp_loker)
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    loker_dikunci_frame.pack()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()






# ----------------------------------------------------------- Taruh Barang Function ----------------------------------------------------------- #

def show_loker_dikunci_taruh_barang():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()




def show_loker_penuh():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()

def show_semua_loker_penuh():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack()

def show_loker_kosong():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack()
    semua_loker_penuh_frame.pack_forget()






    
def show_input_notelp():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()








def show_metode_pembayaran():
    global taruh_barang
    taruh_barang = True
    print(taruh_barang)
    all_same = all(elem == daftar_loker[0] for elem in daftar_loker)
    if all_same and daftar_loker[0] == "isi":
        home_frame.pack_forget()
        about_frame.pack_forget()
        main_menu_frame.pack_forget()
        password_salah_frame.pack_forget()
        taruh_barang_frame.pack_forget()
        masukan_password_frame.pack_forget()
        lebih_12_jam_frame.pack_forget()
        password_salah5x_frame.pack_forget()
        loker_terbuka_frame.pack_forget()
        konfirmasi_tutup_frame.pack_forget()
        loker_dikunci_frame.pack_forget()
        loker_penuh_frame.pack()
        menu_ambil_barang_frame.pack_forget()
        input_loker_frame.pack_forget()
        metode_pembayaran_frame.pack_forget()
        pembayaran_qris_frame.pack_forget()
        pembayaran_tunai_frame.pack_forget()
        cetak_struk_frame.pack_forget()
        pembayaran_berhasil_frame.pack_forget()
        input_notelp_frame.pack_forget()
        input_loker_frame_taruh.pack_forget()
        loker_dikunci_taruh_barang.pack_forget()
        konfirmasi_tutup_frame_taruh_barang.pack_forget()
        loker_dikunci_taruh_barang.pack_forget()
        loker_terbuka_frame_taruh_barang.pack_forget()
        loker_kosong_frame.pack_forget()
        semua_loker_penuh_frame.pack_forget()



        
    else:
        home_frame.pack_forget()
        about_frame.pack_forget()
        main_menu_frame.pack_forget()
        input_loker_frame.pack_forget()
        password_salah_frame.pack_forget()
        password_salah5x_frame.pack_forget()
        masukan_password_frame.pack_forget()
        lebih_12_jam_frame.pack_forget()
        menu_ambil_barang_frame.pack_forget()
        loker_terbuka_frame.pack_forget()
        konfirmasi_tutup_frame.pack_forget()
        loker_dikunci_frame.pack_forget()
        loker_penuh_frame.pack_forget()
        metode_pembayaran_frame.pack()
        pembayaran_qris_frame.pack_forget()
        pembayaran_tunai_frame.pack_forget()
        cetak_struk_frame.pack_forget()
        pembayaran_berhasil_frame.pack_forget()
        input_notelp_frame.pack_forget()
        input_loker_frame_taruh.pack_forget()
        loker_dikunci_taruh_barang.pack_forget()
        konfirmasi_tutup_frame_taruh_barang.pack_forget()
        loker_dikunci_taruh_barang.pack_forget()
        loker_terbuka_frame_taruh_barang.pack_forget()
        loker_kosong_frame.pack_forget()
        semua_loker_penuh_frame.pack_forget()








def show_bayar_qris():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack()
    pembayaran_tunai_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()







def show_bayar_tunai():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    pembayaran_tunai_frame.pack()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()






def show_pembayaran_berhasil():
    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    pembayaran_berhasil_frame.pack()
    cetak_struk_frame.pack_forget()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()



def show_cetak_struk():
    global storage_time
    global global_no_loker
    global global_no_telp_loker
    global_no_telp_loker = entry_no_telp.get()
    global_no_loker = int(entry_no_loker_taruh.get())
    storage_time = datetime.now() 
    random_number = random.randint(10000, 50000) # random number for password
    print("Memori Vending Machine")
    print("-----------------------------")
    print("Daftar Loker")
    print("-----------------------------")
    daftar_loker[global_no_loker - 1] = "isi"
    print(daftar_loker)
    print("Pass Loker")
    print("-----------------------------")
    password_loker[global_no_loker - 1] = str(random_number)
    print(password_loker)
    print("Pass Loker")
    print("-----------------------------")
    notelp_loker[global_no_loker - 1] = global_no_telp_loker
    print(notelp_loker)
    

    home_frame.pack_forget()
    about_frame.pack_forget()
    main_menu_frame.pack_forget()
    input_loker_frame.pack_forget()
    password_salah_frame.pack_forget()
    password_salah5x_frame.pack_forget()
    masukan_password_frame.pack_forget()
    lebih_12_jam_frame.pack_forget()
    menu_ambil_barang_frame.pack_forget()
    loker_terbuka_frame.pack_forget()
    konfirmasi_tutup_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    cetak_struk_frame.pack()
    input_notelp_frame.pack_forget()
    input_loker_frame_taruh.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    konfirmasi_tutup_frame_taruh_barang.pack_forget()
    loker_dikunci_taruh_barang.pack_forget()
    loker_terbuka_frame_taruh_barang.pack_forget()
    loker_kosong_frame.pack_forget()
    semua_loker_penuh_frame.pack_forget()


    
def validasi_password():
    global i
    print("this is i = ")
    global global_password
    global_password = entry_password.get()
    if global_password == password_loker[global_no_loker - 1]:
        show_menu_ambil_barang()
    elif i == 5:
        show_password_salah5x()
    elif global_password != password_loker[global_no_loker -1]:
        show_password_salah()
        i += 1

def check_storage_time(storage_time):
    global ambil_sementara
    ambil_sementara = True
    current_time = datetime.now()
    time_difference = current_time - storage_time
    if time_difference >= timedelta(hours=12):
        print('cannot ambil sementara')
        show_lebih_12_jam()
    else: 
        print('can ambil sementara')
        show_loker_terbuka()

def validation_ambil_barang(): 
    global_no_loker = int(entry_no_loker.get())
    # kalau lokernya kosong tidak bisa ambil barang
    if daftar_loker[global_no_loker - 1] == "kosong":
        print("tidak bisa ambil barang")
        show_loker_kosong();
    else:
        show_masukan_password()

def validation_taruh_barang():
    global_no_loker = int(entry_no_loker_taruh.get())
    # kalau lokernya isi tidak bisa taruh barang
    if daftar_loker[global_no_loker - 1] == "isi":
        print("tidak bisa taruh barang")
        show_loker_penuh()
    else: 
        show_loker_terbuka_taruh_barang()

def cek_ketersediaan_loker_taruh_barang(arr):
    if all(daftar_loker == "isi" for daftar_loker in arr):
        print('masuk kesini ndak gan')
        show_semua_loker_penuh()
    else:
        show_metode_pembayaran()

# Create the main tkinter window
root = customtkinter.CTk()
root.title("Vending Machine Loker")
root.geometry("720x480")

# Font 
font_title = ("Inter", 48, "bold")
font_subtitle = ("Inter", 24)
font_text = ("Inter", 32)

# Create frames for different screens
home_frame = customtkinter.CTkFrame(root, width=720, height=336, fg_color="transparent",)
about_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
main_menu_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
taruh_barang_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
input_loker_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
masukan_password_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
password_salah_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
password_salah5x_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
lebih_12_jam_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
menu_ambil_barang_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
loker_terbuka_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
konfirmasi_tutup_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
loker_dikunci_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")

# ----------------------------------------------------------- Taruh Barang Frame -----------------------------------------------------------
loker_penuh_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
input_notelp_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
metode_pembayaran_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
pembayaran_qris_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
pembayaran_tunai_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
pembayaran_berhasil_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
cetak_struk_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
input_loker_frame_taruh = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
loker_dikunci_taruh_barang = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
konfirmasi_tutup_frame_taruh_barang = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
loker_terbuka_frame_taruh_barang = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
loker_kosong_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
semua_loker_penuh_frame = customtkinter.CTkFrame(root,  width=720, height=336, fg_color="transparent")
# engga ada loker terbuka taruh barang

# variable
# global_no_loker = 0
# loker = ["kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong", "kosong"]
# print(global_no_loker)



# Populate the frames with widgets
# For this example, each frame contains a label to identify the screen

# Home Frame
customtkinter.CTkLabel(home_frame, text="Vending Machine Loker", font=font_title,).pack(pady=20)
customtkinter.CTkButton(home_frame, text="Tekan tombol untuk melanjutkan", font=font_subtitle, command=show_main_menu, fg_color="transparent",).pack()
img1 = customtkinter.CTkImage(Image.open("./assets/logo.png"), size=(220,220))
button1 = customtkinter.CTkButton(home_frame, image=img1, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle)
button1.pack(pady=20)


# blabalb
customtkinter.CTkLabel(about_frame, text="About Screen").pack()

# main menu frame
customtkinter.CTkLabel(main_menu_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(main_menu_frame, text="Pilih Menu", font=font_subtitle).pack()
customtkinter.CTkLabel(main_menu_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(main_menu_frame, text="Ambil Barang >>", command=show_input_loker_ambil, font=font_text, fg_color="transparent", ).pack(pady=10)
customtkinter.CTkButton(main_menu_frame, text="Taruh Barang >>", command=lambda: cek_ketersediaan_loker_taruh_barang(daftar_loker), font=font_text, fg_color="transparent").pack(pady=10) # need an if statement if loker == penuh command = show_loker_penuh else command = show_input_notelp

# input loker frame
customtkinter.CTkLabel(input_loker_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(input_loker_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(input_loker_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(input_loker_frame, text="Pilih nomor loker: (1 - 9)", font=font_text).pack(pady=10)
customtkinter.CTkButton(input_loker_frame, text="Lanjut >>", command=validation_ambil_barang, font=font_text, fg_color="transparent").pack(pady=10)
entry_no_loker = customtkinter.CTkEntry(input_loker_frame, font=font_text, width=30)
entry_no_loker.pack(pady=10)

#  input loker frame taruh
customtkinter.CTkLabel(input_loker_frame_taruh, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(input_loker_frame_taruh, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(input_loker_frame_taruh, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(input_loker_frame_taruh, text="Pilih nomor loker: (1 - 9)", font=font_text).pack(pady=10)
customtkinter.CTkButton(input_loker_frame_taruh, text="Lanjut >>", command=validation_taruh_barang, font=font_text, fg_color="transparent").pack(pady=10)
entry_no_loker_taruh = customtkinter.CTkEntry(input_loker_frame_taruh, font=font_text, width=30)
entry_no_loker_taruh.pack(pady=10)

# masukan password frame
customtkinter.CTkLabel(masukan_password_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(masukan_password_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(masukan_password_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(masukan_password_frame, text="Masukan Password", font=font_subtitle).pack()
entry_password = customtkinter.CTkEntry(masukan_password_frame, font=font_text, width=200, show="*")
entry_password.pack(pady=10)
customtkinter.CTkButton(masukan_password_frame, text="Lanjut >>", command=validasi_password, font=font_text, fg_color="transparent").pack(pady=10)

# password salah frame
customtkinter.CTkLabel(password_salah_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(password_salah_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(password_salah_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(password_salah_frame, text="Max salah 5x", font=font_subtitle).pack(pady=10)
img2 = customtkinter.CTkImage(Image.open("./assets/password_salah.png"), size=(120,120))
button2 = customtkinter.CTkButton(password_salah_frame, image=img2, text="",  fg_color="transparent", command=show_masukan_password, font=font_subtitle)
button2.pack(pady=20)
customtkinter.CTkLabel(password_salah_frame, text="Password Salah", font=font_subtitle).pack()

# password salah 5x frame
customtkinter.CTkLabel(password_salah5x_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(password_salah5x_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(password_salah5x_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img3 = customtkinter.CTkImage(Image.open("./assets/password_salah5x.png"), size=(120,120))
button3 = customtkinter.CTkButton(password_salah5x_frame, image=img3, text="",  fg_color="transparent", command=show_home, font=font_subtitle)
button3.pack(pady=20)
customtkinter.CTkLabel(password_salah5x_frame, text="Password anda salah lebih dari 5x. Kami sudah mengirimkan kode verifikasi ke nomor telepon anda", font=font_subtitle, wraplength=622).pack()

# lebih dari 12 jam frame
customtkinter.CTkLabel(lebih_12_jam_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(lebih_12_jam_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(lebih_12_jam_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button4 = customtkinter.CTkButton(lebih_12_jam_frame, image=img2, text="",  fg_color="transparent", command=show_menu_ambil_barang, font=font_subtitle)
button4.pack(pady=20)
customtkinter.CTkLabel(lebih_12_jam_frame, text="Anda tidak bisa mengambil sementara karena waktu titipan anda sudah melebih 12 jam", font=font_subtitle, wraplength=622).pack()

# menu ambil barang frame
customtkinter.CTkLabel(menu_ambil_barang_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(menu_ambil_barang_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(menu_ambil_barang_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(menu_ambil_barang_frame, text="Pilih salah satu menu", font=font_subtitle, wraplength=622).pack()
customtkinter.CTkButton(menu_ambil_barang_frame, text="Ambil dan Logout >>", command=show_loker_terbuka, font=font_subtitle, fg_color="transparent").pack(pady=10)
customtkinter.CTkButton(menu_ambil_barang_frame, text="Ambil Sementara >>", command=lambda: check_storage_time(storage_time), font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement right here if usingTime < 12 hours = show_loker_terbuka else show_lebih_12_jam

# Loker terbuka frame
customtkinter.CTkLabel(loker_terbuka_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_terbuka_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img4 = customtkinter.CTkImage(Image.open("./assets/success.png"), size=(120,120))
button5 = customtkinter.CTkButton(loker_terbuka_frame, image=img4, text="",  fg_color="transparent", command='', font=font_subtitle)
button5.pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame, text="Loker berhasil terbuka. Silahkan ambil/taruh barang anda!", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_terbuka_frame, text="Tutup Loker >>", command=show_konfirmasi_tutup, font=font_subtitle, fg_color="transparent").pack(pady=10) 


# Konfirmasi tutup loker frame (ambil_barang)
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Tutup Loker?", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame, text="Ya >>", command=show_loker_dikunci_ambil_barang, font=font_subtitle, fg_color="transparent").pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame, text="Tidak >>", command=show_loker_terbuka, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Loker terkunci frame (ambil barang)
customtkinter.CTkLabel(loker_dikunci_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_dikunci_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img5 = customtkinter.CTkImage(Image.open("./assets/loker_terkunci.png"), size=(120,120))
button6 = customtkinter.CTkButton(loker_dikunci_frame, image=img5, text="",  fg_color="transparent", command=show_home, font=font_subtitle)
button6.pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_frame, text="Loker berhasil Terkunci", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_dikunci_frame, text="Lanjut >>", command=show_home, font=font_subtitle, fg_color="transparent").pack(pady=10) # need if statement if AmbilBarang command = show_main_menu else if taruhBarang show_cetak_struk

# ---------------------------------------------------------------------- Taruh barang ---------------------------------------------------------------------- #

# Loker terbuka frame (taruh barang)
customtkinter.CTkLabel(loker_terbuka_frame_taruh_barang, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame_taruh_barang, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_terbuka_frame_taruh_barang, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img4 = customtkinter.CTkImage(Image.open("./assets/success.png"), size=(120,120))
button5 = customtkinter.CTkButton(loker_terbuka_frame_taruh_barang, image=img4, text="",  fg_color="transparent", command='', font=font_subtitle)
button5.pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame_taruh_barang, text="Loker berhasil terbuka. Silahkan ambil/taruh barang anda!", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_terbuka_frame_taruh_barang, text="Tutup Loker >>", command=show_konfirmasi_tutup_taruh_barang, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Konfirmasi tutup loker frame (Taruh Barang)
customtkinter.CTkLabel(konfirmasi_tutup_frame_taruh_barang, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(konfirmasi_tutup_frame_taruh_barang, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(konfirmasi_tutup_frame_taruh_barang, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(konfirmasi_tutup_frame_taruh_barang, text="Tutup Loker?", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame_taruh_barang, text="Ya >>", command=show_loker_dikunci_taruh_barang, font=font_subtitle, fg_color="transparent").pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame_taruh_barang, text="Tidak >>", command=show_loker_terbuka, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Loker terkunci frame (taruh barang)
customtkinter.CTkLabel(loker_dikunci_taruh_barang, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_taruh_barang, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_dikunci_taruh_barang, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img5 = customtkinter.CTkImage(Image.open("./assets/loker_terkunci.png"), size=(120,120))
button6 = customtkinter.CTkButton(loker_dikunci_taruh_barang, image=img5, text="",  fg_color="transparent", command=show_cetak_struk, font=font_subtitle)
button6.pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_taruh_barang, text="Loker berhasil Terkunci", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_dikunci_taruh_barang, text="Lanjut >>", command=show_cetak_struk, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Loker Penuh frame
customtkinter.CTkLabel(loker_penuh_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_penuh_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_penuh_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button7 = customtkinter.CTkButton(loker_penuh_frame, image=img2, text="",  fg_color="transparent", command=show_input_loker_taruh, font=font_subtitle) 
button7.pack(pady=20)
customtkinter.CTkLabel(loker_penuh_frame, text="Mohon Maaf Loker Sudah Penuh", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_penuh_frame, text="Kembali >>", command=show_input_loker_taruh, font=font_subtitle, fg_color="transparent").pack(pady=10)

# semua loker penuh
customtkinter.CTkLabel(semua_loker_penuh_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(semua_loker_penuh_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(semua_loker_penuh_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button7 = customtkinter.CTkButton(semua_loker_penuh_frame, image=img2, text="",  fg_color="transparent", command=show_home, font=font_subtitle) 
button7.pack(pady=20)
customtkinter.CTkLabel(semua_loker_penuh_frame, text="Mohon Maaf, SELURUH LOKER PENUH", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(semua_loker_penuh_frame, text="Kembali >>", command=show_home, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Loker kosong frame
customtkinter.CTkLabel(loker_kosong_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_kosong_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_kosong_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button7 = customtkinter.CTkButton(loker_kosong_frame, image=img2, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle) 
button7.pack(pady=20)
customtkinter.CTkLabel(loker_kosong_frame, text="Mohon Maaf Loker yang anda pilih kosong. Silahkan pilih loker lain.", font=font_subtitle, wraplength=600).pack(pady=10)
customtkinter.CTkButton(loker_kosong_frame, text="Kembali >>", command=show_main_menu, font=font_subtitle, fg_color="transparent").pack(pady=10)

# input notelp frame
customtkinter.CTkLabel(input_notelp_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(input_notelp_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(input_notelp_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(input_notelp_frame, text="Masukan No Telp Anda:", font=font_subtitle).pack(pady=10)
entry_no_telp = customtkinter.CTkEntry(input_notelp_frame, font=font_text, width=250)
entry_no_telp.pack(pady=10)
customtkinter.CTkButton(input_notelp_frame, text="Lanjut >>", command=show_input_loker_taruh, font=font_subtitle, fg_color="transparent").pack(pady=10)

# metode pembayaran frame
customtkinter.CTkLabel(metode_pembayaran_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(metode_pembayaran_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(metode_pembayaran_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(metode_pembayaran_frame, text="Pilih metode pembayaran: ", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(metode_pembayaran_frame, text="QRIS >>", command=show_bayar_qris, font=font_subtitle, fg_color="transparent").pack(pady=10)
customtkinter.CTkButton(metode_pembayaran_frame, text="Tunai >>", command=show_bayar_tunai, font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement

# bayar qris frame
customtkinter.CTkLabel(pembayaran_qris_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(pembayaran_qris_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(pembayaran_qris_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(pembayaran_qris_frame, text="Silahkan scan kode qris tersebut untuk melakukan pembayaran. Biaya pembayaran Rp. 2000", font=font_subtitle, wraplength=360).pack(pady=10)
img6 = customtkinter.CTkImage(Image.open("./assets/qris_dummy.png"), size=(120,120))
button8 = customtkinter.CTkButton(pembayaran_qris_frame, image=img6, text="",  fg_color="transparent", command=show_pembayaran_berhasil, font=font_subtitle)
customtkinter.CTkButton(pembayaran_qris_frame, text="Konfirmasi Pembayaran >>", command=show_pembayaran_berhasil, font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement
button8.pack(pady=20)

# bayar tunai frame
customtkinter.CTkLabel(pembayaran_tunai_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(pembayaran_tunai_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(pembayaran_tunai_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
title = customtkinter.CTkLabel(pembayaran_tunai_frame, text="Masukan 2 uang kertas Rp.1000 atau uang Rp.2000 Biaya pembayaran Rp. 2000. Hanya menerima uang kertas", font=font_subtitle, wraplength=500, anchor="e").pack()
img7 = customtkinter.CTkImage(Image.open("./assets/uang_seribu.png"), size=(120,54))
img8 = customtkinter.CTkImage(Image.open("./assets/uang_duaribu.png"), size=(120,54))


button8 = customtkinter.CTkButton(pembayaran_tunai_frame, image=img7, text="",  fg_color="transparent", font=font_subtitle)
button9 = customtkinter.CTkButton(pembayaran_tunai_frame, image=img8, text="",  fg_color="transparent", font=font_subtitle)
customtkinter.CTkButton(pembayaran_tunai_frame, text="Konfirmasi Pembayaran >>", command=show_pembayaran_berhasil, font=font_subtitle, fg_color="transparent").pack(pady=20) # need some if else statement
button8.pack(side=tk.TOP)
button9.pack()



# pembayaran berhasil frame
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Pembayaran berhasil dilakukan", font=font_subtitle, wraplength=360).pack(pady=10)
button10 = customtkinter.CTkButton(pembayaran_berhasil_frame, image=img4, text="",  fg_color="transparent", command=show_input_notelp   , font=font_subtitle)
button10.pack(pady=20)
customtkinter.CTkButton(pembayaran_berhasil_frame, text="Lanjut >>", command=show_input_notelp, font=font_subtitle, fg_color="transparent").pack(pady=10) 

# cetak struk frame
customtkinter.CTkLabel(cetak_struk_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(cetak_struk_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(cetak_struk_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img9 = customtkinter.CTkImage(Image.open("./assets/cetak_struk.png"), size=(120,120))
button11 = customtkinter.CTkButton(cetak_struk_frame, image=img9, text="",  fg_color="transparent", command=show_home, font=font_subtitle)
button11.pack(pady=20)
customtkinter.CTkLabel(cetak_struk_frame, text="Silahkan ambil struk anda! Struk digunakan ketika mengambil barang. Jangan dihilangkan ya!", font=font_subtitle, wraplength=600).pack(pady=10)
customtkinter.CTkButton(cetak_struk_frame, text="Kembali ke menu awal >>", command=show_home, font=font_subtitle, fg_color="transparent").pack(pady=10) 









# Show the initial screen (Home)
show_home()

# Start the tkinter main loop
root.mainloop()
