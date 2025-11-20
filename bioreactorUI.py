import tkinter as tk

root = tk.Tk()
main = tk.Frame(root)
root.geometry("1280x720")



root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=2)  


left_frame = tk.Frame(root, bg="lightgray")
right_frame = tk.Frame(root, bg="lightblue")

left_frame.grid(row=0, column=0, sticky="nesw")
right_frame.grid(row=0, column=1, sticky="nesw")


left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_rowconfigure(1, weight=1)
left_frame.grid_rowconfigure(2, weight = 1)
left_frame.grid_columnconfigure(0, weight=1)

top_left = tk.Frame(left_frame, bg="pink")
mid_left = tk.Frame(left_frame, bg = "black")
bottom_left = tk.Frame(left_frame, bg="orange")


top_left.grid(row=0, column=0, sticky="nesw")
mid_left.grid(row = 1, column = 0, sticky = "nesw")
bottom_left.grid(row=2, column=0, sticky="nesw")    


heat_var = tk.StringVar()
heat_setpoint = tk.DoubleVar()
heat_setpoint.set("25")
heat_label = tk.Label(bottom_left, text="Heating Subsystem", font = ("Arial", 12))
heat_slider = tk.Scale(bottom_left, length = 300, width = 25, from_ = 25, to = 35, orient = "horizontal", variable = heat_setpoint)
heat_entry = tk.Entry(bottom_left, width = 17, textvariable= heat_var)
heat_submit_button = tk.Button(bottom_left, text= "Submit", command = lambda: setVar(1))

heat_label.place(relx = 0.5, rely = 0.2, anchor = "center")
heat_slider.place(relx = 0.725, rely = 0.5, anchor = "ne")
heat_entry.place(relx = 0.74, rely=  0.5, anchor = "nw")
heat_submit_button.place(relx = 0.74, rely=  0.6, anchor = "nw")

stir_var = tk.StringVar()
stir_setpoint = tk.DoubleVar()
stir_setpoint.set("500")
stir_label = tk.Label(mid_left, text="Stirring Subsystem", font = ("Arial", 12))
stir_slider = tk.Scale(mid_left, length = 300, width = 25, from_ = 500, to = 1500, orient = "horizontal", variable = stir_setpoint)
stir_entry = tk.Entry(mid_left, width = 17, textvariable= stir_var)
stir_submit_button = tk.Button(mid_left, text= "Submit", command = lambda: setVar(2))

stir_label.place(relx = 0.5, rely = 0.2, anchor = "center")
stir_slider.place(relx = 0.725, rely = 0.5, anchor = "ne")
stir_entry.place(relx = 0.74, rely=  0.5, anchor = "nw")
stir_submit_button.place(relx = 0.74, rely=  0.6, anchor = "nw")

pH_var = tk.StringVar()
pH_setpoint = tk.DoubleVar()
pH_setpoint.set("3")
pH_label = tk.Label(top_left, text="pH Subsystem", font = ("Arial", 12))
pH_slider = tk.Scale(top_left, length = 300, width = 25, from_ = 3, to = 7, orient = "horizontal", variable = pH_setpoint)
pH_entry = tk.Entry(top_left, width = 17, textvariable= pH_var)
pH_submit_button = tk.Button(top_left, text= "Submit", command = lambda: setVar(3))

pH_label.place(relx = 0.5, rely = 0.2, anchor = "center")
pH_slider.place(relx = 0.725, rely = 0.5, anchor = "ne")
pH_entry.place(relx = 0.74, rely=  0.5, anchor = "nw")
pH_submit_button.place(relx = 0.74, rely=  0.6, anchor = "nw")


def setVar(type):
    match type:
        case 1:
            heat_setpoint.set(round(float(heat_var.get()),1))
        case 2:
            stir_setpoint.set(round(float(stir_var.get()),1))
        case 3:
            pH_setpoint.set(round(float(pH_var.get()),1))

root.mainloop()