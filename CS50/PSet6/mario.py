GAP_SIZE = 2

def main():
    """
    Prints a mario style tower with a gap in the middle.
    """
    height = 0
    while (height <= 0 or height >= 23):
        height = int(input("Enter the height of the tower. (must be between 0 and 23): "))
    
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")
        for k in range(i+1):
            print("#", end="")
        for l in range(GAP_SIZE):
            print(" ", end="")
        for m in range(i+1):
            print("#", end="")
        print()
    
    exit(0)

main()
    
