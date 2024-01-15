import sys
input = sys.stdin.readline
queue = []
def push(num):
    queue.append(num)

def myPop():
    try:
        return queue.pop(0)
    except:
        return -1

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    try:
        return queue[0]
    except:
        return -1
def back():
    try:
        return queue[len(queue)-1]
    except:
        return -1

if __name__ == "__main__":
    for i in range(int(input())):
        command = input().strip().split(" ")
        if command[0] == 'push':
            push(int(command[1]))
        elif command[0] == 'pop':
            print(myPop())
        elif command[0] == 'size':
            print(size())
        elif command[0] == 'empty':
            print(empty())
        elif command[0] == 'front':
            print(front())
        elif command[0] == 'back':
            print(back())
        command.clear()