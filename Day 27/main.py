import tkinter as tk

FONT = ("Arial", 13)


def calculate_km():
    miles = float(miles_entry.get())
    km = 1.60934 * miles
    km = round(km, 2)
    converted_label.config(text=km)


window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.grid_columnconfigure((0, 1, 2), weight=5)


miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0, column=1, sticky="ew")

miles_label = tk.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0, sticky="ew")
miles_label.config(padx=5, pady=0)

equal_label = tk.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1, sticky="ew")
equal_label.config(padx=5, pady=0)

converted_label = tk.Label(text="0", font=FONT)
converted_label.grid(column=1, row=1, sticky="ew")
converted_label.config(padx=5, pady=0)

km_label = tk.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1, sticky="ew")
km_label.config(padx=5, pady=0)

button = tk.Button(text="Calculate", command=calculate_km, font=FONT)
button.grid(column=1, row=3, sticky="ew")

window.mainloop()
