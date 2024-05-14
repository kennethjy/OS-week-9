def FCFS(filename, head):
    file = open(filename, 'r')
    lines = [l.strip() for l in file.readlines()]
    movement = 0
    for l in lines:
        movement += abs(int(l) - head)
        head = int(l)
    return movement

def FCFSopt(filename, head):
    file = open(filename, 'r')
    lines = sorted([int(l.strip()) for l in file.readlines()])
    mid = 0
    while lines[mid] < head:
        mid += 1
    left = lines[:mid]
    left.reverse()
    lines = left + lines[mid:]
    movement = 0
    for l in lines:
        movement += abs(int(l) - head)
        head = int(l)
    return movement


def SCAN(filename, head):
    file = open(filename, 'r')
    lines = [int(l.strip()) for l in file.readlines()]

    movement = 0
    dir = "left"
    for l in lines:
        if dir == "left":
            if l <= head:
                movement += abs(head - l)
            else:
                movement += head
                movement += l
                dir = "right"
            head = l
        else:
            if l >= head:
                movement += abs(head - l)
            else:
                movement += 5000 - head
                movement += 5000 - l
                dir = "left"
            head = l
    return movement


def SCANopt(filename, head):
    file = open(filename, 'r')
    lines = [int(l.strip()) for l in file.readlines()]
    left = []
    right = []
    for l in lines:
        if l < head:
            left.append(l)
        else:
            right.append(l)

    left = sorted(left)
    left.reverse()
    right = sorted(right)

    lines = left + right

    movement = 0
    dir = "left"
    for l in lines:
        if dir == "left":
            if l <= head:
                movement += abs(head - l)
            else:
                movement += head
                movement += l
                dir = "right"
            head = l
        else:
            if l >= head:
                movement += abs(head - l)
            else:
                movement += 5000 - head
                movement += 5000 - l
                dir = "left"
            head = l
    return movement


def cSCAN(filename, head):
    file = open(filename, 'r')
    lines = [int(l.strip()) for l in file.readlines()]

    movement = 0
    for l in lines:
        if l <= head:
            movement += abs(head - l)
        else:
            movement += head + 5000
            movement += 5000 - l
        head = l
    return movement


def cSCANopt(filename, head):
    file = open(filename, 'r')
    lines = [int(l.strip()) for l in file.readlines()]
    left = []
    right = []
    for l in lines:
        if l <= head:
            left.append(l)
        else:
            right.append(l)

    left = sorted(left)
    left.reverse()
    right = sorted(right)
    right.reverse()

    lines = left + right

    movement = 0
    for l in lines:
        if l <= head:
            movement += abs(head - l)
        else:
            movement += head + 5000
            movement += 5000 - l
        head = l
    return movement

filename = input("Enter file path to input: ")
head = int(input("Enter the starting position of the head: "))

print(f"FCFS: {FCFS(filename, head)}")
print(f"FCFS (optimized): {FCFSopt(filename, head)}")
print(f"SCAN: {SCAN(filename, head)}")
print(f"SCAN (optimized): {SCANopt(filename, head)}")
print(f"C-SCAN: {cSCAN(filename, head)}")
print(f"C-SCAN (optimized): {cSCANopt(filename, head)}")