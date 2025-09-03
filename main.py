import tkinter as tk
from tkinter import messagebox
import subprocess

WG_INTERFACE = "peer-1"

def wg_up():
    try:
        subprocess.run(["sudo", "wg-quick", "up", WG_INTERFACE], check=True)
        set_status(True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Ошибка", "Не удалось включить VPN")

def wg_down():
    try:
        subprocess.run(["sudo", "wg-quick", "down", WG_INTERFACE], check=True)
        set_status(False)
    except subprocess.CalledProcessError:
        messagebox.showerror("Ошибка", "Не удалось выключить VPN")

def toggle():
    global vpn_enabled
    if vpn_enabled:
        wg_down()
    else:
        wg_up()

def set_status(enabled: bool):
    global vpn_enabled
    vpn_enabled = enabled
    if enabled:
        status_label.config(text="VPN on", fg="green")
        canvas.itemconfig(indicator, fill="green")
    else:
        status_label.config(text="VPN off", fg="red")
        canvas.itemconfig(indicator, fill="red")

# GUI
root = tk.Tk()
root.title("WireGuard Control")
root.geometry("250x200")

status_label = tk.Label(root, text="VPN off", fg="red", font=("Arial", 14))
status_label.pack(pady=10)

# Индикатор (лампочка)
canvas = tk.Canvas(root, width=50, height=50, highlightthickness=0)
canvas.pack(pady=5)
indicator = canvas.create_oval(5, 5, 45, 45, fill="red")

toggle_btn = tk.Button(root, text="On / Off", width=15, command=toggle)
toggle_btn.pack(pady=10)

vpn_enabled = False  # начальное состояние

root.mainloop()
