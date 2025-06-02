import sys

def main():  #Подсчёт строк 
    n = 0
    # Using a loop to read one character at a time, similar to C's getchar()
    while True:
        c = sys.stdin.read(1)
        if c == '':  # End of File
            break
        if c == '\n':
            n += 1
    print(f"{n}")

if __name__ == "__main__":
    main()
