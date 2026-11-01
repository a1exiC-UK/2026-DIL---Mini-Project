from tkinter import * 
import time 

# Main window set up

root = Tk()
root.title("Mini Project")
root.geometry("400x420")


# Function to return to main menu

def returntostart():
    startup.tkraise()

# Function to get to number sort menu

def numbersortmenu():
    numbersort.tkraise()

# Function to get to string sort menu

def stringsortmenu():
    stringsort.tkraise()

# Function to show error if non-number inputted

def show_error(message):
    error_window = Toplevel(root)
    error_window.title("Input Error")
    error_window.geometry("300x120")
    error_window.transient(root)
    Label(error_window, text=message, wraplength=280).pack(pady=15)
    Button(error_window, text="OK", command=error_window.destroy).pack()

# Function for ascending number sort

def ascending(number):
    start = time.perf_counter()

    for i in range(len(number)):
        for x in range(len(number) - 1 - i):
            if number[x] > number[x + 1]:
                number[x], number[x + 1] = number[x + 1], number[x]

    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return number, elapsed

# Function for descending number sort

def descending(number):
    start = time.perf_counter()

    for i in range(len(number)):
        for x in range(len(number) - 1 - i):
            if number[x] < number[x + 1]:
                number[x], number[x + 1] = number[x + 1], number[x]

    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return number, elapsed

# Function to detect ascending or descending

def sortnumbers():
    try:
        number = [float(number1.get()), float(number2.get()), float(number3.get()), float(number4.get()), float(number5.get()), float(number6.get()), float(number7.get()), float(number8.get()), float(number9.get()), float(number10.get())]
    except ValueError:
        show_error("Please enter a valid number in all fields.")
        return

    if sorttype.get() == 1:
        sortednumbers, elapsed = ascending(number)
    else:
        sortednumbers, elapsed = descending(number)

    sortedresults.config(text=f"{sortednumbers} in {elapsed:.3f}ms")

# Function to sort string by ASCII value

def sortstring():
    strng = list(string.get())
    start = time.perf_counter()
    for i in range(len(strng)):
        for x in range(len(strng)-1-i):
            a = 127 if strng[x] == " " else ord(strng[x])
            b = 127 if strng[x+1] == " " else ord(strng[x+1])   
            if a > b:
                strng[x], strng[x+1] = strng[x+1], strng[x]
    end = time.perf_counter()
    result = ''.join(strng)
    elapsed = (end - start) * 1000
    sortedresult.config(text=f"'{result}' in {elapsed:.3f}ms")

# Function to quit program

def quitbuttonfunc():
    quit_button = Toplevel(root)
    quit_button.title("Quit")
    quit_button.geometry("300x120")
    quit_button.transient(root)

    Label(quit_button, text="Thank you for using the program!", wraplength=280).pack(pady=15)
    Button(quit_button, text="OK", command=root.destroy).pack()

# Startup Frame Set-up

startup = Frame(root)
startup.place(x=0, y=0, relwidth=1, relheight=1)

title = Label(startup, text="Mini Project", font=("Arial", 30))
title.place(relx=0.5, rely=0.1, anchor=CENTER)

numbersortbutton = Button(startup, text="Number Sort", width=30, command=numbersortmenu)
numbersortbutton.place(relx=0.5, rely=0.3, anchor=CENTER)

stringsortbutton = Button(startup, text="String Sort", width=30, command=stringsortmenu)
stringsortbutton.place(relx=0.5, rely=0.5, anchor=CENTER)

quitbutton = Button(startup, text="Quit", width=30, command=quitbuttonfunc, fg="red")
quitbutton.place(relx=0.5, rely=0.7, anchor=CENTER)

# Number Sort Frame Set-up

sorttype = IntVar(value=1)
numbersort = Frame(root)
numbersort.place(x=0, y=0, relwidth=1, relheight=1)

for col in range(4):
    numbersort.grid_columnconfigure(col, weight=1)

title = Label(numbersort, text="Number Sort", font=("Arial", 30))
title.grid(row=0, column=0, columnspan=4, pady=10)
instructions = Label(numbersort, text="Enter 10 integers/decimals to sort", font=("Arial", 15))
instructions.grid(row=1, column=0, columnspan=4, pady=5)

Label(numbersort, text="Number 1").grid(row=2, column=0)
number1 = Entry(numbersort)
number1.grid(row=2, column=1)

Label(numbersort, text="Number 2").grid(row=3, column=0)
number2 = Entry(numbersort)
number2.grid(row=3, column=1)

Label(numbersort, text="Number 3").grid(row=4, column=0)
number3 = Entry(numbersort)
number3.grid(row=4, column=1)

Label(numbersort, text="Number 4").grid(row=5, column=0)
number4 = Entry(numbersort)
number4.grid(row=5, column=1)

Label(numbersort, text="Number 5").grid(row=6, column=0)
number5 = Entry(numbersort)
number5.grid(row=6, column=1)

Label(numbersort, text="Number 6").grid(row=2, column=2)
number6 = Entry(numbersort)
number6.grid(row=2, column=3)

Label(numbersort, text="Number 7").grid(row=3, column=2)
number7 = Entry(numbersort)
number7.grid(row=3, column=3)

Label(numbersort, text="Number 8").grid(row=4, column=2)
number8 = Entry(numbersort)
number8.grid(row=4, column=3)

Label(numbersort, text="Number 9").grid(row=5, column=2)
number9 = Entry(numbersort)
number9.grid(row=5, column=3)

Label(numbersort, text="Number 10").grid(row=6, column=2)
number10 = Entry(numbersort)
number10.grid(row=6, column=3)

Button(numbersort, text="Back to Main Menu", fg="blue", cursor="hand2", underline=1, command=returntostart).grid(row=7, column=0, columnspan=4, pady=5)

Radiobutton(numbersort, text="Ascending", variable=sorttype, value=1).grid(row=8, column=1)
Radiobutton(numbersort, text="Descending", variable=sorttype, value=2).grid(row=8, column=2)


sort = Button(numbersort, text="Sort!", width=25, font=(15), command=sortnumbers).grid(row=14, column=0, columnspan=4, pady=10)

sortedresultstitle = Label(numbersort, text="Sorted Results: ", font=(15))
sortedresultstitle.grid(row=15, column=0, columnspan=4, pady=5)

sortedresults = Label(numbersort, text="", wraplength=390)
sortedresults.grid(row=16, column=0, columnspan=4, pady=5)

# String Sort Frame Set-up

stringsort = Frame(root)
stringsort.place(x=0, y=0, relwidth=1, relheight=1)

for col in range(4):
    stringsort.grid_columnconfigure(col, weight=1)

title = Label(stringsort, text="String Sort", font=("Arial", 30))
title.grid(row=0, column=0, columnspan=4, pady=10)
instructions = Label(stringsort, text="Enter a string you want sorted", font=("Arial", 15))
instructions.grid(row=1, column=0, columnspan=4, pady=5)

Label(stringsort, text="String:").grid(row=2, column=0, columnspan=4, pady=5)
string = Entry(stringsort)
string.grid(row=3, column=0, columnspan=6, pady=5)

Button(stringsort, text="Back to Main Menu", fg="blue", cursor="hand2", underline=1, command=returntostart).grid(row=7, column=0, columnspan=4, pady=5)

sort = Button(stringsort, text="Sort!", width=25, font=(15), command=sortstring).grid(row=14, column=0, columnspan=4, pady=10)

sortedresultstitle = Label(stringsort, text="Sorted Results: ", font=(15))
sortedresultstitle.grid(row=15, column=0, columnspan=4, pady=5)

sortedresult = Label(stringsort, text="", wraplength=390)
sortedresult.grid(row=16, column=0, columnspan=4, pady=5)

# Startup

startup.tkraise()
root.mainloop()
