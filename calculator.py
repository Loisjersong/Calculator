import tkinter as tk

# globally declare the expression variable
expression = ""

# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
    # concatenation of string
    expression = expression + str(num)
    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    # Put that code inside the try block
    # which may generate the error
    try:
        global expression
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to clear one character
# of text entry box
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# creates and runs an instance of the window
window = tk.Tk()

# makes the size of the widow
window.geometry("400x700")

# sets a title for the screen
window.title("Calculator")

# sets color of panel background
window["background"] = "#243441"

# StringVar() is the variable class
# we create an instance of this class
equation = tk.StringVar()

# create the text entry box for showing the expression.
expression_field = tk.Entry(window, bg="#243441", fg="white", font=('Georgia 50'), textvariable=equation, border=0, justify="right")
expression_field.place(x=16, y=16, width=368, height=178)

# create the buttons for the window
# 1st layer [AC] [⌫] [%] [÷]
all_clear_button = tk.Button(window, text="AC", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=clear)
all_clear_button.place(x=16, y=210, width=80, height=80)

backspace_button = tk.Button(window, text="⌫", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=backspace)
backspace_button.place(x=112, y=210, width=80, height=80)

percent_button = tk.Button(window, text="%", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=lambda: press("%"))
percent_button.place(x=208, y=210, width=80, height=80)

divide_button = tk.Button(window, text="÷", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=lambda: press("/"))
divide_button.place(x=304, y=210, width=80, height=80)

# 2nd Layer [7] [8] [9] [×]
seven_button = tk.Button(window, text="7", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(7))
seven_button.place(x=16, y=300, width=80, height=80)

eight_button = tk.Button(window, text="8", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(8))
eight_button.place(x=112, y=300, width=80, height=80)

nine_button = tk.Button(window, text="9", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(9))
nine_button.place(x=208, y=300, width=80, height=80)

multiply_button = tk.Button(window, text="×", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=lambda: press("*"))
multiply_button.place(x=304, y=300, width=80, height=80)


# 3rd Layer [4] [5] [6] [−]
four_button = tk.Button(window, text="4", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(4))
four_button.place(x=16, y=400, width=80, height=80)

five_button = tk.Button(window, text="5", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(5))
five_button.place(x=112, y=400, width=80, height=80)

six_button = tk.Button(window, text="6", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(6))
six_button.place(x=208, y=400, width=80, height=80)

subtract_button = tk.Button(window, text="−", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=lambda: press("-"))
subtract_button.place(x=304, y=400, width=80, height=80)


# 4th Layer [1] [2] [3] [+]
one_button = tk.Button(window, text="1", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(1))
one_button.place(x=16, y=500, width=80, height=80)

two_button = tk.Button(window, text="2", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(2))
two_button.place(x=112, y=500, width=80, height=80)

three_button = tk.Button(window, text="3", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(3))
three_button.place(x=208, y=500, width=80, height=80)

add_button = tk.Button(window, text="+", fg="#ed802e", font=('Georgia 20'), bg="#243441", command=lambda: press("+"))
add_button.place(x=304, y=500, width=80, height=80)


# 5th Layer [0] [.] [=]
zero_button = tk.Button(window, text="0", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press(0))
zero_button.place(x=16, y=600, width=80, height=80)

decimal_point_button = tk.Button(window, text=".", fg="#5c6a75", font=('Georgia 20'), bg="#243441", command=lambda: press('.'))
decimal_point_button.place(x=112, y=600, width=80, height=80)

equals_button = tk.Button(window, text="=", fg="#fcd6ad", font=('Georgia 20'), bg="#ed802e", command=equalpress)
equals_button.place(x=208, y=600, width=176, height=80)

window.mainloop()