from os import terminal_size
from tkinter import *
from tkinter import ttk
import random
from typing import Collection
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root =Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg='black')

#vars
selected_alg=StringVar()
data= []
def drawData(data, colorSelect):
    canvas.delete("all")
    c_height = 380
    c_width = 625
    x_width = c_width / (len(data)+1)
    offset= 30
    spacing= 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 360
        #botton right
        x1 = (i + 1) * x_width +offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorSelect[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update()

def Generate():
    global data
    minVal= int(minEntry.get())     
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    
    data = []
    for num in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data,['red' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data:
        return
    if (algMenu.get()=='Quick Sort'):
        quick_sort(data, 0 , len(data)-1, drawData, speedScale.get())
    elif (algMenu.get()=='Bubble Sort'):
        bubble_sort(data, drawData, speedScale.get())
    elif (algMenu.get()=='Merge Sort'):
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])

    

    
#frame / base layout
UI_frame = Frame(root,width=600 , height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=650, height=380, bg='white')
canvas.grid(row=1, column=0, pady=5, padx=10)

#Userinterface area
#row[0]
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
speedScale = Scale(UI_frame, from_=0.2 , to= 2, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Speed:")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, pady=5, padx=5)

#row[1]
sizeEntry= Scale(UI_frame, from_=8 , to= 35, length=100, digits=1, resolution=0.2, orient=HORIZONTAL, label="Size:")
sizeEntry.grid(row=1,column=1,pady=5,padx=5, sticky=W)

minEntry= Scale(UI_frame, from_= 0, to= 100, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Min Value:")
minEntry.grid(row=1,column=2,pady=5,padx=5, sticky=W)

maxEntry= Scale(UI_frame, from_=10 , to= 100, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Max Value:")
maxEntry.grid(row=1,column=3,pady=5,padx=5, sticky=W)


Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=1, column=4, pady=5, padx=5)

root.mainloop()