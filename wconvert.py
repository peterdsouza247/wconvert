from tkinter import *
 
window = Tk()
 
def from_kg():
    gms = float(kg_val.get()) * 1000
    lbs = float(kg_val.get()) * 2.20462
    oz = float(kg_val.get()) * 35.274
    display_gms.delete("1.0",  END)
    display_gms.insert(END, round(gms, 4))
    display_lbs.delete("1.0",  END)
    display_lbs.insert(END, round(lbs, 4))
    display_oz.delete("1.0",  END)
    display_oz.insert(END, round(oz, 4))
 
label_kg = Label(window, text = "Kilograms: ")
label_kg.grid(row = 1, column = 1)
 
kg_val = StringVar()
entry = Entry(window, textvariable = kg_val)
entry.grid(row = 1, column = 2)
 
button_convert = Button(window, text = "Convert", command = from_kg)
button_convert.grid(row = 1, column = 3)

label_gms = Label(window, text = "Grams: ")
label_gms.grid(row = 3, column = 1)

label_lbs = Label(window, text = "Pounds: ")
label_lbs.grid(row = 3, column = 2)

label_oz = Label(window, text = "Ounces: ")
label_oz.grid(row = 3, column = 3)
 
display_gms = Text(window, height = 1, width = 20)
display_gms.grid(row = 5, column = 1)
 
display_lbs = Text(window, height = 1, width = 20)
display_lbs.grid(row = 5, column = 2)
 
display_oz = Text(window, height = 1, width = 20)
display_oz.grid(row = 5, column = 3)

col_count, row_count = window.grid_size()

for col in range(col_count + 1):
    window.grid_columnconfigure(col, minsize = 20)

for row in range(row_count + 1):
    window.grid_rowconfigure(row, minsize = 20)

window.title("wconvert.py")
window.mainloop()