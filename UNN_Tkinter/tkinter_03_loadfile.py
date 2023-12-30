import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", \
        filetypes=[("Text files", "*.txt"), ("All files", "*.*"), ("Python files", "*.py")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                # seleccionar todo el texto desde
                # el inicio 1.0 hasta el final tk.END
                file_content = area_text.get('1.0', tk.END)
                file.write(file_content)
                label_msg.config(text=f"File saved as: {file_path}")
        except Exception as e:
            label_msg.config(text=f"Error: {str(e)}")

window = tk.Tk()
window.title("Text file writer")

area_text = tk.Text(window, wrap=tk.WORD, height=15, width=35)
area_text.pack(padx=20, pady=20)

save_button = tk.Button(window, text="Save As", command=save_file)
save_button.pack(padx=20, pady=10)

label_msg = tk.Label(window, text="", padx=20, pady=10)
label_msg.pack()

window.mainloop()
