def invo(x,y):
    return(x**y)

k = float(input("First number: "))
l = int(input("Second number: "))

def main():
    print("Involution Operator")
    print(invo(k,l))

if __name__ == '__main__':
    main()