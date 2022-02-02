import time
def bubble_sort(data, drawData, speed):
    for k in range(len(data)-1):
        for y in range(len(data)-1):
            if (data[y] > data[y+1]):
                data[y], data[y+1] = data[y+1], data[y]
                drawData(data,['yellow' if x==y or x==y+1 else 'red' for x in range(len(data))])
                time.sleep(speed)
    drawData(data, ['green' for x in range(len(data))])