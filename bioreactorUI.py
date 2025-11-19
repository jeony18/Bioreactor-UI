import tkinter as tk

root = tk.Tk()
main = tk.Frame(root)
root.geometry("1280x720")


#Top and bottom sections 2:1
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=1)  
root.grid_columnconfigure(0, weight=1) 

topFrame = tk.Frame(root, bg="lightgray")
botFrame = tk.Frame(root, bg="lightblue")


topFrame.grid(row=0, column=0, sticky="nesw")
botFrame.grid(row=1, column=0, sticky="nesw")

botFrame.grid_columnconfigure(0, weight=1)
botFrame.grid_columnconfigure(1, weight=1)
botFrame.grid_columnconfigure(2, weight = 1)
botFrame.grid_rowconfigure(0, weight=1)

botLeft = tk.Frame(botFrame, bg="pink")
botMid = tk.Frame(botFrame, bg = "red")
botRight = tk.Frame(botFrame, bg="orange")


botLeft.grid(row=0, column=0, sticky="nesw")
botMid.grid(row = 0, column = 1, sticky = "nesw")
botRight.grid(row=0, column=2, sticky="nesw")

root.mainloop()