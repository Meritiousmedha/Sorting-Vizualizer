from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title('DSA PROJECT Sorting Algorithm Visualizer')
root.geometry("750x600")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []

# Sorting Algorithms

def bubble_sort(data, draw_data, speed):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(speed)

def selection_sort(data, draw_data, speed):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ['red' if x == i or x == min_idx else 'blue' for x in range(len(data))])
        time.sleep(speed)

def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
            time.sleep(speed)
        data[j + 1] = key
        draw_data(data, ['blue' for x in range(len(data))])

def merge_sort(data, draw_data, speed):
    merge_sort_recursive(data, 0, len(data)-1, draw_data, speed)

def merge_sort_recursive(data, left, right, draw_data, speed):
    if left < right:
        mid = (left + right) // 2
        merge_sort_recursive(data, left, mid, draw_data, speed)
        merge_sort_recursive(data, mid+1, right, draw_data, speed)
        merge(data, left, mid, right, draw_data, speed)

def merge(data, left, mid, right, draw_data, speed):
    temp = []
    i, j = left, mid+1

    while i <= mid and j <= right:
        if data[i] < data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1

    while i <= mid:
        temp.append(data[i])
        i += 1
    while j <= right:
        temp.append(data[j])
        j += 1

    for i in range(len(temp)):
        data[left + i] = temp[i]
        draw_data(data, ['red' if left + i == mid or left + i == j else 'blue' for x in range(len(data))])
        time.sleep(speed)

def quick_sort(data, draw_data, speed):
    quick_sort_recursive(data, 0, len(data)-1, draw_data, speed)

def quick_sort_recursive(data, low, high, draw_data, speed):
    if low < high:
        pi = partition(data, low, high, draw_data, speed)
        quick_sort_recursive(data, low, pi-1, draw_data, speed)
        quick_sort_recursive(data, pi+1, high, draw_data, speed)

def partition(data, low, high, draw_data, speed):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        draw_data(data, ['red' if x == i or x == j else 'blue' for x in range(len(data))])
        time.sleep(speed)
    data[i+1], data[high] = data[high], data[i+1]
    return i+1

def heap_sort(data, draw_data, speed):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw_data, speed)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        draw_data(data, ['red' if x == i or x == 0 else 'blue' for x in range(len(data))])
        time.sleep(speed)
        heapify(data, i, 0, draw_data, speed)

def heapify(data, n, i, draw_data, speed):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and data[l] > data[largest]:
        largest = l
    if r < n and data[r] > data[largest]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw_data(data, ['red' if x == i or x == largest else 'blue' for x in range(len(data))])
        time.sleep(speed)
        heapify(data, n, largest, draw_data, speed)

# Generating the array
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    arr = []
    for i in range(size):
        arr.append(random.randrange(lowest, highest+1))

    drawrectangle(arr, ['red' for x in range(len(arr))]) 

# Drawing the array elements as rectangles
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(arr[i]))

    root.update_idletasks()

# Sorting function
def sorting():
    global arr
    selected_algo = select_algorithm.get()
    speed = sortingspeed.get()
    
    if selected_algo == "Bubble Sort":
        bubble_sort(arr, drawrectangle, speed)
    elif selected_algo == "Selection Sort":
        selection_sort(arr, drawrectangle, speed)
    elif selected_algo == "Insertion Sort":
        insertion_sort(arr, drawrectangle, speed)
    elif selected_algo == "Merge Sort":
        merge_sort(arr, drawrectangle, speed)
    elif selected_algo == "Quick Sort":
        quick_sort(arr, drawrectangle, speed)
    elif selected_algo == "Heap Sort":
        heap_sort(arr, drawrectangle, speed)

# GUI Setup
options_frame = Frame(root, width= 700, height=300, bg='green')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=350, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(options_frame, text="Algorithm Choice: ",).grid(row=0, column=0, padx=10, pady=10)

# Algorithm dropdown menu with sorting options
algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort'], width=20)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Sorting Speed")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(options_frame, text="Start Sorting", command=sorting, bg='red', height=5, width=15).grid(row=0, column=3, padx=10, pady=10)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Array Size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Generate Array", command=Generate_array, bg='blue', height=5 , width=15).grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
