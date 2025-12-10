from packages import tk, simpledialog, messagebox


#   ------     Making the GUI     -------



root = tk.Tk()
root.withdraw()

def ask_text(title,prompt,hidden=False):
    while True:
        if hidden:
            value = simpledialog.askstring(title,prompt,show='*')
        else:
            value = simpledialog.askstring(title,prompt)
        
        if value is None:
            if messagebox.askyesno("Quit","Do you want to quit:"):
                root.destroy()
                quit()
            else:
                continue
        value = value.strip()

        if value == "":
            messagebox.showerror("Error","Please enter a value.")
            continue
        return value

