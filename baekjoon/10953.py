def Official(a, b):
    return a+b
if __name__ == "__main__":
    for i in range(int(input())):
        a,b=map(int,input().split(","))
        print(Official(a,b))