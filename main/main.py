from tkinter import * ## Imports all functions, classes, and variables from tkinter module directly into global namespace, so tkinter.x isn't needed.
import time 

# Main window set up

root = Tk()
root.title("Mini Project") ## Sets the main menu size and window
root.geometry("400x420")


# Function to return to main menu

def returntostart(): 
    startup.tkraise() ## When called, the user will be returned to the main menu

# Function to get to number sort menu

def numbersortmenu():
    numbersort.tkraise() ## When called, the menu for the Number Sorting will appear

# Function to get to string sort menu

def stringsortmenu():
    stringsort.tkraise() ## When called, the menu for the String Sorting will appear

# Function to show error if non-number inputted

def show_error(message):
    error_window = Toplevel(root) ## Creates a TopLevel window, that will appear above the main window
    error_window.title("Input Error")
    error_window.geometry("300x120")
    error_window.transient(root) ## .transient() assures the window will always stay at the front
    Label(error_window, text=message, wraplength=280).pack(pady=15)
    Button(error_window, text="OK", command=error_window.destroy).pack() ## .destroy will close the window when pressed

# Function for ascending number sort

def ascending(number):
    start = time.perf_counter() ## Starts the timer to time how long the sort takes

    for i in range(len(number)): ## Calculates the length of number[]
        for x in range(len(number) - 1 - i): ## Length of number[]-1 prevents an out-of-range comparison, and -i reduces uneccessary comparisons later on.
            if number[x] > number[x + 1]:
                number[x], number[x + 1] = number[x + 1], number[x] ## Switches the current index and next index in the list if the current number is bigger. 

    end = time.perf_counter() ## Stops the timer
    elapsed = (end - start) * 1000 ## Works out the time taken and * 1000 to find milliseconds
    return number, elapsed ## Returns the sorted numbers and the time taken

# Function for descending number sort

def descending(number): ## The idea is the same for descending() as ascending(), however the operator in ln57 is replaced to be <, so that the current index and next index switch if the next index is larger
    start = time.perf_counter()

    for i in range(len(number)):
        for x in range(len(number) - 1 - i):
            if number[x] < number[x + 1]:
                number[x], number[x + 1] = number[x + 1], number[x]

    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return number, elapsed

# Function to carry out the number sort
def sortnumbers():
    try:
        number = [float(number1.get()), float(number2.get()), float(number3.get()), float(number4.get()), float(number5.get()), float(number6.get()), float(number7.get()), float(number8.get()), float(number9.get()), float(number10.get())]
        ## The list number is formed by grabbing the values entered from the GUI by the user.
    except ValueError:
        show_error("Please enter a valid number in all fields.") ## If a non-float input is given, show_error() is called, and the error window is displayed and prompts the user to re-enter the numbers.
        return

    if sorttype.get() == 1: ## Defined later on, but RadioButtons are assigned a value, where ascending=1 and descending=2. sorttype.get() retrieves this value.
        sortednumbers, elapsed = ascending(number) ## This sets sortednumbers, elapsed to the values of number, elapsed that are returned from ascending (and therefore descending)
    else:
        sortednumbers, elapsed = descending(number)

    sortedresults.config(text=f"{sortednumbers} in {elapsed:.3f}ms") ## sortedresults is defined later on, but is given as blank text. .config(...) changes this to text displaying the sorted numbers and the elapsed time

# Function to sort string by ASCII value

def sortstring():
    strng = list(string.get()) ## The string is grabbed from the user input, and list() separates all of the characters.
    start = time.perf_counter() ## Timer is started
    for i in range(len(strng)):
        for x in range(len(strng)-1-i):
            a = 127 if strng[x] == " " else ord(strng[x]) ## The current index is set to a. If it is a space, it is given the value 127, as I wanted spaces to be displayed last in the sorted string. If not space, a is set to [x]'s ASCII value
            b = 127 if strng[x+1] == " " else ord(strng[x+1]) ## The next index is set to b. If not space, b is set to [x+1]'s ASCII value
            if a > b:
                strng[x], strng[x+1] = strng[x+1], strng[x]  ## Switches the current index and next index in the list if the current ASCII value is bigger. 
    end = time.perf_counter() ## Ends timer
    result = ''.join(strng) ## result is defined as strng joined into one long string, instead of it being displayed as ['x', 'v'...]
    elapsed = (end - start) * 1000 
    sortedresult.config(text=f"'{result}' in {elapsed:.3f}ms") ## This line and previous same as for number sorting, however extra '' are added to be able to see spaces more clearly

# Function to quit program

def quitbuttonfunc():
    quit_button = Toplevel(root) ## same as the error window, it will display a TopLevel window, with .transient() always keeping it there
    quit_button.title("Quit?")
    quit_button.geometry("300x120")
    quit_button.transient(root)

    Label(quit_button, text="Thank you for using the program!", wraplength=280).pack(pady=15)
    Button(quit_button, text="Quit", command=root.destroy).pack() ## root.destroy will delete the main window (root), and as quit_button is a child of root, it will be deleted also, stopping the program. (User can still cross off though if they want)

# Startup Frame Set-up

startup = Frame(root) ## Creates a new frame that is a child of root.
startup.place(x=0, y=0, relwidth=1, relheight=1) ## Positions frame in top left corner of the window and makes it fill up the window

title = Label(startup, text="Mini Project", font=("Arial", 30)) ## Adds a title called Mini Project
title.place(relx=0.5, rely=0.1, anchor=CENTER) ## Places it near the top but in the centre

numbersortbutton = Button(startup, text="Number Sort", width=30, command=numbersortmenu) ## Button for accessing the Number Sort menu
numbersortbutton.place(relx=0.5, rely=0.3, anchor=CENTER) ## Below the title

stringsortbutton = Button(startup, text="String Sort", width=30, command=stringsortmenu) ## Button for accessing the String Sort menu
stringsortbutton.place(relx=0.5, rely=0.5, anchor=CENTER) ## Below numbersortbutton

quitbutton = Button(startup, text="Quit", width=30, command=quitbuttonfunc, fg="red") ## Button to quit
quitbutton.place(relx=0.5, rely=0.7, anchor=CENTER) ## Below stringsortbutton

# Number Sort Frame Set-up

sorttype = IntVar(value=1) ## Creates a Integer Variable that's defaulted to 1 (ascending), this can be overwritten by selecting the desired RadioButton 
numbersort = Frame(root) ## Creates a new frame that's a child of root
numbersort.place(x=0, y=0, relwidth=1, relheight=1) ## Sets it to top-left and makes it fill the window.

for col in range(4):
    numbersort.grid_columnconfigure(col, weight=1) ## Sets the weighting of each column to be equal to centre the widgets

title = Label(numbersort, text="Number Sort", font=("Arial", 30)) ## Adds a title
title.grid(row=0, column=0, columnspan=4, pady=10) ## Sets the position on the grid to be the top row and makes it span all 4 columns, effectively centering it. pady=10 adds gaps above and below the text
instructions = Label(numbersort, text="Enter 10 integers/decimals to sort", font=("Arial", 15)) ## Gives the instructions
instructions.grid(row=1, column=0, columnspan=4, pady=5) ## Sets the position to be below the main title, and gives it vertical padding

Label(numbersort, text="Number 1").grid(row=2, column=0) ## Creates a label displaying "Number X"
number1 = Entry(numbersort) ## Next to the text, an entry box is placed and whatever the input is will be assigned to numberx
number1.grid(row=2, column=1) ## Sets the position for where the entry box is (same row, next column across)

Label(numbersort, text="Number 2").grid(row=3, column=0) ### Refer to lines 138-140
number2 = Entry(numbersort)
number2.grid(row=3, column=1)

Label(numbersort, text="Number 3").grid(row=4, column=0) ### Refer to lines 138-140
number3 = Entry(numbersort)
number3.grid(row=4, column=1)

Label(numbersort, text="Number 4").grid(row=5, column=0) ### Refer to lines 138-140
number4 = Entry(numbersort)
number4.grid(row=5, column=1)

Label(numbersort, text="Number 5").grid(row=6, column=0) ### Refer to lines 138-140
number5 = Entry(numbersort)
number5.grid(row=6, column=1)

Label(numbersort, text="Number 6").grid(row=2, column=2) ### Refer to lines 138-140
number6 = Entry(numbersort)
number6.grid(row=2, column=3)

Label(numbersort, text="Number 7").grid(row=3, column=2) ### Refer to lines 138-140
number7 = Entry(numbersort)
number7.grid(row=3, column=3)

Label(numbersort, text="Number 8").grid(row=4, column=2) ### Refer to lines 138-140
number8 = Entry(numbersort)
number8.grid(row=4, column=3)

Label(numbersort, text="Number 9").grid(row=5, column=2) ### Refer to lines 138-140
number9 = Entry(numbersort)
number9.grid(row=5, column=3)

Label(numbersort, text="Number 10").grid(row=6, column=2) ### Refer to lines 138-140
number10 = Entry(numbersort)
number10.grid(row=6, column=3)

Button(numbersort, text="Back to Main Menu", fg="blue", cursor="hand2", underline=1, command=returntostart).grid(row=7, column=0, columnspan=4, pady=5) ## Creates a button that will return the user to the main menu if pressed.

Radiobutton(numbersort, text="Ascending", variable=sorttype, value=1).grid(row=8, column=1) ## RadioButtons that determine whether the sort is ascending or descending by assigning a value (1 or 2) to the variable sorttype.
Radiobutton(numbersort, text="Descending", variable=sorttype, value=2).grid(row=8, column=2)


sort = Button(numbersort, text="Sort!", width=25, font=(15), command=sortnumbers).grid(row=14, column=0, columnspan=4, pady=10) ## Button that will run the sorting command once pressed

sortedresultstitle = Label(numbersort, text="Sorted Results: ", font=(15)) ## Title that is above the sorted results
sortedresultstitle.grid(row=15, column=0, columnspan=4, pady=5)

sortedresults = Label(numbersort, text="", wraplength=390) ## Blank text to be overwritten by the output from the sorting algorithm. wraplength gives a maxiumum width and text will go over multiple lines if the inputs are large.
sortedresults.grid(row=16, column=0, columnspan=4, pady=5)

# String Sort Frame Set-up

stringsort = Frame(root) ## Creates a new frame that is the child of root
stringsort.place(x=0, y=0, relwidth=1, relheight=1) ## Places in top left and makes it fill the entire window

for col in range(4):
    stringsort.grid_columnconfigure(col, weight=1) ## Sets the weighting of each column to be equal to centre the widgets

title = Label(stringsort, text="String Sort", font=("Arial", 30)) ## Adds a title
title.grid(row=0, column=0, columnspan=4, pady=10) ## Same as before, making the title span all 4 columns, effectively centering it.
instructions = Label(stringsort, text="Enter a string you want sorted", font=("Arial", 15)) ## Gives the instructions
instructions.grid(row=1, column=0, columnspan=4, pady=5)

Label(stringsort, text="String:").grid(row=2, column=0, columnspan=4, pady=5) ## Sets where string is to be input
string = Entry(stringsort) ## Sets the entry to be a varibale called string
string.grid(row=3, column=0, columnspan=6, pady=5) ## Input box set below the title

Button(stringsort, text="Back to Main Menu", fg="blue", cursor="hand2", underline=1, command=returntostart).grid(row=7, column=0, columnspan=4, pady=5) ## Creates a button that will return the user to the main menu if pressed.

sort = Button(stringsort, text="Sort!", width=25, font=(15), command=sortstring).grid(row=14, column=0, columnspan=4, pady=10) ## Button that will run the sorting command once pressed

sortedresultstitle = Label(stringsort, text="Sorted Results: ", font=(15)) ## Title that is above the sorted results
sortedresultstitle.grid(row=15, column=0, columnspan=4, pady=5)

sortedresult = Label(stringsort, text="", wraplength=390) ## Blank text to be overwritten by the output from the sorting algorithm. wraplength gives a maxiumum width and text will go over multiple lines if the inputs are large.
sortedresult.grid(row=16, column=0, columnspan=4, pady=5)

# Startup

startup.tkraise() ## Raises the startup menu, as it's the first one defined, it won't be displayed first otherwise
root.mainloop() ## Constantly runs the GUI.
