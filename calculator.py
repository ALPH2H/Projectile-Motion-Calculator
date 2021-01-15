from tkinter import *
import math

root = Tk()
root.geometry("400x600")

g=9.8


title = Label(root, fg="blue", font = ('Helvetica', 18, 'bold'), text = "Projectile Motion Calculator")
title.grid(row = 0, sticky = W, column = 0, columnspan = 6)

firstText = Label(root, text='Initial Velocity in m/s:')
firstText.grid(row = 1, column = 0, sticky = W)

secondText = Label(root, text = 'Angle of Launch in Degrees:')
secondText.grid(row = 2 , column = 0, sticky = W)

thirdText = Label(root, text= 'Initial Height in meters: ')
thirdText.grid(row = 3, column = 0, sticky = W)


fourthText = Label(root, text = '  ').grid(row = 5)

# Function to execute when button clicked. 
def onClick():
    initial_velocity = int(initial_velocity_entry.get())
    angle_of_launch = int(angle_of_launch_entry.get())
    initial_height = int(initial_height_entry.get())
    horizontal = initial_velocity * math.cos(math.radians(angle_of_launch))
    exponent = (initial_velocity * math.sin(math.radians(initial_velocity)))**2
    maximum_height = round(initial_height + exponent / (2 * g), 2)
    time_of_flight = round((initial_velocity * math.sin(math.radians(angle_of_launch)) + math.sqrt(exponent + 2 * initial_height * g))/g, 2)
    answer = Label(root, fg = "#B23030", text = 'Your time of flight is '+ str(time_of_flight) + ' seconds.')
    answer.grid(row = 6, column = 0, sticky = W, columnspan = 6)
    distance = round(horizontal * time_of_flight, 2) 
    secondanswer = Label(root, fg = "#B23030", text = 'Your distance traveled is ' + str(distance) + ' meters.')
    secondanswer.grid( row = 7, column = 0, sticky = W, columnspan = 6)
    thirdanswer = Label(root, fg = "#B23030", text = 'Your maximum height is ' + str(maximum_height) + ' meters.')
    thirdanswer.grid(row = 8, column = 0, sticky = W, columnspan = 6)


x = IntVar()
y = IntVar()
z = IntVar()

initial_velocity_entry = Entry(root, borderwidth = 3, textvariable = x,)
initial_velocity_entry.grid(row = 1, column = 1, sticky = E)

angle_of_launch_entry = Entry(root, borderwidth = 3, textvariable = y)
angle_of_launch_entry.grid(row=2, column=1, sticky = E)


initial_height_entry = Entry(root, borderwidth = 3, textvariable = z)
initial_height_entry.grid(row=3, column=1, sticky = E)

calculate_button = Button(root, command = onClick, text = 'CALCULATE!')
calculate_button.grid(row = 4, column = 1, sticky = E)



root.mainloop()
 
