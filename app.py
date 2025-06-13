import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            label_result.config(text=f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            label_result.config(text=f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            label_result.config(text=f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")

        else:
            messagebox.showwarning("Invalid Input", "Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.config(bg="#f0f8ff")

# Heading
label_title = tk.Label(root, text="🌡️ Temperature Converter", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
label_title.pack(pady=10)

# Temperature input
entry_temp = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
entry_temp.pack(pady=5)

# Dropdown for unit
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), state="readonly", width=15)
combo_unit.set("Select Unit")
combo_unit.pack(pady=5)

# Convert Button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", command=convert_temperature)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#333")
label_result.pack(pady=10)

# Run the application
root.mainloop()
