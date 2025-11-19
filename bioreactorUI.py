import tkinter as tk

root = tk.Tk()
main = tk.Frame(root)
root.geometry("1280x720")


# Root grid: 1 row, 2 columns
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=2)  

# Frames
leftFrame = tk.Frame(root, bg="lightgray")
rightFrame = tk.Frame(root, bg="lightblue")

leftFrame.grid(row=0, column=0, sticky="nesw")
rightFrame.grid(row=0, column=1, sticky="nesw")

# Inside leftFrame: 2 rows stacked vertically
leftFrame.grid_rowconfigure(0, weight=1)
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight = 1)
leftFrame.grid_columnconfigure(0, weight=1)

topLeft = tk.Frame(leftFrame, bg="pink")
mid = tk.Frame(leftFrame, bg = "black")
bottomLeft = tk.Frame(leftFrame, bg="orange")


topLeft.grid(row=0, column=0, sticky="nesw")
mid.grid(row = 1, column = 0)
bottomLeft.grid(row=2, column=0, sticky="nesw")

root.mainloop()