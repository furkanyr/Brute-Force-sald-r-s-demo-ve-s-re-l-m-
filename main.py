import time
import tkinter as tk
from tkinter import messagebox

def passwordBreaker():
    # Seçilen karakter setini oluştur
    characters = ""
    if var_digits.get():
        characters += "0123456789"
    if var_lowercase.get():
        characters += "abcdefghijklmnopqrstuvwxyz"
    if var_uppercase.get():
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if var_special.get():
        characters += "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    if not characters:
        messagebox.showwarning("Uyarı", "En az bir karakter türü seçilmelidir!")
        return

    passw = entry.get()

    # Girilen şifrenin geçerli karakterler içerip içermediğini kontrol et
    for char in passw:
        if char not in characters:
            messagebox.showerror("Hata", "Girilen şifre, seçilen seçenekler için geçersiz karakterler içeriyor!")
            return

    # Eğer sadece rakam girilmişse ve tüm seçenekler işaretlenmişse hata mesajı göster
    if passw.isdigit() and var_lowercase.get() and var_uppercase.get() and var_special.get():
        messagebox.showerror("Hata", "Sadece rakam girildi. Tüm karakter türleri işaretlenemez!")
        return

    # Girilen şifrenin içeriği dışında bir onay kutusu işaretlenmişse uyarı ver
    if (var_lowercase.get() and not any(c.islower() for c in passw)) or \
       (var_uppercase.get() and not any(c.isupper() for c in passw)) or \
       (var_special.get() and not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in passw)):
        messagebox.showwarning("Uyarı", "Girilen şifre, seçilen karakter türleriyle uyumlu değil!")
        return

    flag = False
    get_input = [len(passw), passw]

    start_time = time.time()

    def try_combinations(current_combination, remaining_length):
        nonlocal flag
        if remaining_length == 0:
            label1.config(text=current_combination)
            screen.update()
            if get_input[1] == current_combination:
                flag = True
                print(f"Şifre: {get_input[1]}")
            return

        for char in characters:
            if flag:
                break
            try_combinations(current_combination + char, remaining_length - 1)

    try_combinations("", get_input[0])

    end_time = time.time()
    elapsed_time = end_time - start_time

    messagebox.showinfo("Geçen Süre", f"{elapsed_time:.6f} saniye")


# Tkinter arayüzünü oluştur
screen = tk.Tk()
screen.geometry("225x300")
screen.title("Brute-Force")

label = tk.Label(screen, text="Şifreyi Girin:", font=("Arial", 12))
label.pack(pady=10)
entry = tk.Entry(screen, width=30)
entry.pack()

# Karakter türü seçimleri için onay kutuları
var_digits = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_uppercase = tk.BooleanVar()
var_special = tk.BooleanVar()

cb_digits = tk.Checkbutton(screen, text="Rakamlar", variable=var_digits)
cb_lowercase = tk.Checkbutton(screen, text="Küçük Harfler", variable=var_lowercase)
cb_uppercase = tk.Checkbutton(screen, text="Büyük Harfler", variable=var_uppercase)
cb_special = tk.Checkbutton(screen, text="Özel Karakterler", variable=var_special)

cb_digits.pack(anchor='w')
cb_lowercase.pack(anchor='w')
cb_uppercase.pack(anchor='w')
cb_special.pack(anchor='w')

button = tk.Button(screen, text="Kır", font=("Arial", 12), command=passwordBreaker)
button.pack(pady=20)

label1 = tk.Label(screen, text="", font=("Arial", 12))
label1.pack(pady=20)

screen.mainloop()