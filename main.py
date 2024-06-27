import tkinter

height = 0
weight = 0
bmi = 0
output_string = ""

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200,height= 200)

main_label = tkinter.Label(text="BMI Calculator")
main_label.pack()


def onclick_calculate_button():
    global weight
    global height
    global bmi
    global output_string

    weight = int(weigth_entry.get())
    height = int(height_entry.get()) / 100
    bmi = int(weight / (height * height))

    print(weight)
    print(height)
    print(int(bmi))

    if bmi <= 18.4:
        output_string = "BMI is " + str(bmi) + " Underweight"
    elif (18.5 <= bmi and bmi <= 24.9):
        output_string = "BMI is " + str(bmi) + " Normal"
    elif (25 <= bmi and bmi >= 39.9):
        output_string = "BMI is " + str(bmi) + " Overweight"
    else:
        output_string = "BMI is " + str(bmi) + " Obese"
    output_label.config(text=output_string)

weight_label = tkinter.Label(text="Weight")
weight_label.pack()
weight_label.config(padx=0,pady=10)
weigth_entry = tkinter.Entry()
weigth_entry.pack()




#height
height_label = tkinter.Label(text="Height")
height_label.pack()
height_label.config(padx=0,pady=10)
height_entry = tkinter.Entry()
height_entry.pack()


#calculate button
calculate_button = tkinter.Button(text="Calculate",command=onclick_calculate_button)
calculate_button.config(padx=0,pady=1)
calculate_button.pack()


output_label = tkinter.Label(text=output_string)
output_label.pack()

window.mainloop()