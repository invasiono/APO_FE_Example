# ================ Code here =================
import tkinter as tk
from tkinter import ttk

def create_app():
    print("Created")
    def entry_info():
        info1 = entry1.get()
        info2 = entry2.get()
        info3 = entry3.get()

        if info1 and info2 and info3 != None:
            result.config(text=f"Booking added: {info1} - {info2} - {info3} nights")
            root.after(2000, lambda:result.config(text=" "))
        else:
            result.config(text="Please fill all the entries")
            root.after(2000, lambda:result.config(text=" "))
        pass

    def clear_button():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        result.config(text="Ready!")

    root = tk.Tk()
    root.title("Hotel Booking App")

    label1 = tk.Label(root, text="Guest Name").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(root, text="Roomtype").grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    label3 = tk.Label(root, text="Nights").grid(row=2, column=0)
    entry3 = tk.Entry(root)
    entry3.grid(row=2, column=1)

    enter_button = tk.Button(root, text="Add Booking", width=20, command=entry_info)
    enter_button.grid(row=4, column=1)

    result = tk.Label(root, text="Ready")
    result.grid(row=3, column=1)

    clear = tk.Button(root, text="Clear", width=20, command=clear_button)
    clear.grid(row=4, column=2)

    return root
# ============================================

# ===============Do not edit the code below================
def main() -> None:
    app = create_app()
    app.mainloop()


if __name__ == "__main__":
    main()
# =======================================================
