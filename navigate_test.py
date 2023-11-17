import tkinter as tk
import customtkinter
from PIL import Image
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

def show_home():
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





def show_input_loker():
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





def show_masukan_password():
    print(entry_no_loker.get())
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
    loker_penuh_frame.pack_forget()
    loker_dikunci_frame.pack_forget()
    metode_pembayaran_frame.pack_forget()
    pembayaran_qris_frame.pack_forget()
    loker_penuh_frame.pack_forget()
    pembayaran_tunai_frame.pack_forget()
    cetak_struk_frame.pack_forget()
    pembayaran_berhasil_frame.pack_forget()
    input_notelp_frame.pack_forget()





def show_password_salah():
    print(entry_password.get())
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




def show_loker_terbuka():
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







def show_dikunci_dikosongkan():
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

    





# ----------------------------------------------------------- Taruh Barang Function ----------------------------------------------------------- #

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




def show_metode_pembayaran():
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



def show_cetak_struk():
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
customtkinter.CTkButton(main_menu_frame, text="Ambil Barang >>", command=show_input_loker, font=font_text, fg_color="transparent", ).pack(pady=10)
customtkinter.CTkButton(main_menu_frame, text="Taruh Barang >>", command=show_input_notelp, font=font_text, fg_color="transparent").pack(pady=10) # need an if statement if loker == penuh command = show_loker_penuh else command = show_input_notelp

# inpu loker frame
customtkinter.CTkLabel(input_loker_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(input_loker_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(input_loker_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(input_loker_frame, text="Pilih nomor loker: ", font=font_text).pack(pady=10)
entry_no_loker = customtkinter.CTkEntry(input_loker_frame, font=font_text, width=30)
entry_no_loker.pack(pady=10)
customtkinter.CTkButton(input_loker_frame, text="Lanjut >>", command=show_metode_pembayaran, font=font_text, fg_color="transparent").pack(pady=10) # need an if statement if ambilBarang command = show_masukan password else if taruhBarang show_metode pembayaran

# masukan password frame
customtkinter.CTkLabel(masukan_password_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(masukan_password_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(masukan_password_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(masukan_password_frame, text="Masukan Password", font=font_subtitle).pack()
entry_password = customtkinter.CTkEntry(masukan_password_frame, font=font_text, width=200, show="*")
entry_password.pack(pady=10)
customtkinter.CTkButton(masukan_password_frame, text="Lanjut >>", command=show_menu_ambil_barang, font=font_text, fg_color="transparent").pack(pady=10)

# password salah frame
customtkinter.CTkLabel(password_salah_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(password_salah_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(password_salah_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img2 = customtkinter.CTkImage(Image.open("./assets/password_salah.png"), size=(120,120))
button2 = customtkinter.CTkButton(password_salah_frame, image=img2, text="",  fg_color="transparent", command=show_masukan_password, font=font_subtitle)
button2.pack(pady=20)
customtkinter.CTkLabel(password_salah_frame, text="Password Salah", font=font_subtitle).pack()

# password salah 5x frame
customtkinter.CTkLabel(password_salah5x_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(password_salah5x_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(password_salah5x_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img3 = customtkinter.CTkImage(Image.open("./assets/password_salah5x.png"), size=(120,120))
button3 = customtkinter.CTkButton(password_salah5x_frame, image=img3, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle)
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
customtkinter.CTkButton(menu_ambil_barang_frame, text="Ambil Sementara >>", command=show_lebih_12_jam, font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement right here if usingTime < 12 hours = show_loker_terbuka else show_lebih_12_jam

# Loker terbuka frame
customtkinter.CTkLabel(loker_terbuka_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_terbuka_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img4 = customtkinter.CTkImage(Image.open("./assets/success.png"), size=(120,120))
button5 = customtkinter.CTkButton(loker_terbuka_frame, image=img4, text="",  fg_color="transparent", command=show_menu_ambil_barang, font=font_subtitle)
button5.pack(pady=20)
customtkinter.CTkLabel(loker_terbuka_frame, text="Loker berhasil terbuka. Silahkan ambil/taruh barang anda!", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_terbuka_frame, text="Tutup Loker >>", command=show_konfirmasi_tutup, font=font_subtitle, fg_color="transparent").pack(pady=10)


# Konfirmasi tutup loker frame
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(konfirmasi_tutup_frame, text="Tutup Loker?", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame, text="Ya >>", command=show_dikunci_dikosongkan, font=font_subtitle, fg_color="transparent").pack(pady=10)
customtkinter.CTkButton(konfirmasi_tutup_frame, text="Tidak >>", command=show_loker_terbuka, font=font_subtitle, fg_color="transparent").pack(pady=10)

# Loker terkunci frame
customtkinter.CTkLabel(loker_dikunci_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_frame, text="Ambil Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_dikunci_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img5 = customtkinter.CTkImage(Image.open("./assets/loker_terkunci.png"), size=(120,120))
button6 = customtkinter.CTkButton(loker_dikunci_frame, image=img5, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle)
button6.pack(pady=20)
customtkinter.CTkLabel(loker_dikunci_frame, text="Loker berhasil Terkunci", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_dikunci_frame, text="Lanjut >>", command=show_cetak_struk, font=font_subtitle, fg_color="transparent").pack(pady=10) # need if statement if AmbilBarang command = show_main_menu else if taruhBarang show_cetak_struk

# ---------------------------------------------------------------------- Taruh barang ---------------------------------------------------------------------- #

# Loker Penuh frame
customtkinter.CTkLabel(loker_penuh_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(loker_penuh_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(loker_penuh_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button7 = customtkinter.CTkButton(loker_penuh_frame, image=img2, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle) 
button7.pack(pady=20)
customtkinter.CTkLabel(loker_penuh_frame, text="Mohon Maaf Loker Sudah Penuh", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(loker_penuh_frame, text="Kembali >>", command=show_main_menu, font=font_subtitle, fg_color="transparent").pack(pady=10)

# input notelp frame
customtkinter.CTkLabel(input_notelp_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(input_notelp_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(input_notelp_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(input_notelp_frame, text="Masukan No Telp Anda:", font=font_subtitle).pack(pady=10)
entry_no_telp = customtkinter.CTkEntry(input_notelp_frame, font=font_text, width=250)
entry_no_telp.pack(pady=10)
customtkinter.CTkButton(input_notelp_frame, text="Lanjut >>", command=show_input_loker, font=font_subtitle, fg_color="transparent").pack(pady=10)

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
customtkinter.CTkButton(pembayaran_qris_frame, text="Konfirmasi Pembayaran >>", command=show_bayar_tunai, font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement
button8.pack(pady=20)

# bayar tunai frame
customtkinter.CTkLabel(pembayaran_tunai_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(pembayaran_tunai_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(pembayaran_tunai_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
customtkinter.CTkLabel(pembayaran_tunai_frame, text="Masukan 2 uang Rp.1000 atau uang Rp.2000 Biaya pembayaran Rp. 2000. Hanya menerima uang kertas.", font=font_subtitle, wraplength=360).pack(pady=10)
img7 = customtkinter.CTkImage(Image.open("./assets/uang_seribu.png"), size=(120,120))
img8 = customtkinter.CTkImage(Image.open("./assets/uang_duaribu.png"), size=(120,120))
button8 = customtkinter.CTkButton(pembayaran_tunai_frame, image=img7, text="",  fg_color="transparent", font=font_subtitle)
button9 = customtkinter.CTkButton(pembayaran_tunai_frame, image=img8, text="",  fg_color="transparent", font=font_subtitle)
button8.pack(pady=20)
button9.pack(pady=20)
customtkinter.CTkButton(pembayaran_tunai_frame, text="Konfirmasi Pembayaran >>", command=show_pembayaran_berhasil, font=font_subtitle, fg_color="transparent").pack(pady=10) # need some if else statement

# pembayaran berhasil frame
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
button10 = customtkinter.CTkButton(pembayaran_berhasil_frame, image=img4, text="",  fg_color="transparent", command=show_loker_terbuka, font=font_subtitle)
customtkinter.CTkLabel(pembayaran_berhasil_frame, text="Pembayaran berhasil dilakukan", font=font_subtitle, wraplength=360).pack(pady=10)
customtkinter.CTkButton(pembayaran_berhasil_frame, text="Lanjut >>", command=show_loker_terbuka, font=font_subtitle, fg_color="transparent").pack(pady=10) 
button10.pack(pady=20)

# cetak struk frame
customtkinter.CTkLabel(cetak_struk_frame, text="Vending Machine Loker", font=font_title).pack(pady=20)
customtkinter.CTkLabel(cetak_struk_frame, text="Taruh Barang", font=font_subtitle).pack()
customtkinter.CTkLabel(cetak_struk_frame, text="------------------------------------------------------------------------------", font=font_subtitle).pack(pady=10)
img9 = customtkinter.CTkImage(Image.open("./assets/cetak_struk.png"), size=(120,120))
button11 = customtkinter.CTkButton(cetak_struk_frame, image=img9, text="",  fg_color="transparent", command=show_main_menu, font=font_subtitle)
button11.pack(pady=20)
customtkinter.CTkLabel(cetak_struk_frame, text="Silahkan ambil struk anda! Struk digunakan ketika mengambil barang. Jangan Dihilangkan ya!", font=font_subtitle).pack(pady=10)
customtkinter.CTkButton(cetak_struk_frame, text="Kembali ke menu awal >>", command=show_main_menu, font=font_subtitle, fg_color="transparent").pack(pady=10) 









# Show the initial screen (Home)
show_home()

# Start the tkinter main loop
root.mainloop()
