import tkinter as tk
from tkinter import messagebox

# Hesap makinesi sınıfı
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi") 
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.config(bg="#2b2b2b")  # Arka plan rengini koyu yapalım

        # Ekran kısmı
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.create_widgets()

    def create_widgets(self):
        # Ekran
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right", state="readonly", bg="#333333", fg="blue")  # Burada fg="blue" yaptık
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Butonlar
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("⌫", 5, 3)  # Silme butonu
        ]

        # Butonları oluştur
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t), bg="#4CAF50", fg="white", activebackground="#45a049", relief="raised", bd=3)
            button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10, padx=5, pady=5)

        # Buton renkleri
        button_colors = {
            "=": "#FF9800",  # Eşittir butonu turuncu
            "C": "#FF5722",  # Temizle butonu kırmızı
            "/": "#9E9E9E",  # İşlem butonları gri
            "*": "#9E9E9E",
            "-": "#9E9E9E",
            "+": "#9E9E9E",
            "⌫": "#FF5722"  # Silme butonu kırmızı
        }

        # Butonların özel renklerini ayarlamak
        for text, row, col in buttons:
            button = self.root.grid_slaves(row=row, column=col)[0]
            if text in button_colors:
                button.config(bg=button_colors[text])

        # Grid düzeni
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current = self.result_var.get()
        
        if char == "C":
            self.result_var.set("0")
        elif char == "=":
            try:
                expression = current.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz işlem!")
                self.result_var.set("0")
        elif char == "⌫":  # Silme butonu
            if len(current) > 1:
                self.result_var.set(current[:-1])  # Son karakteri sil
            else:
                self.result_var.set("0")  # Eğer sadece bir karakter kaldıysa sıfır yap
        else:
            if current == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

# Ana program
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
