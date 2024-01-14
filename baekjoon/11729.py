def hanoi(n,t):
    global history
    if n == 0:
        history.append((1,3))
        return
    hanoi()
if __name__ == "__main__":
    n = int(input())
    history = []