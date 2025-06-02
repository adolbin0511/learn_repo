import sys
import time

def main():
    # Define characters exactly as in the original C code
    c = '*'            # char c = '*';
    d = ' '            # char d = ' ';
    b = chr(7)         # char b = 07; (07 is an octal constant representing the bell character)
    
    # printf ("\n * ");
    sys.stdout.write("\n * ")
    sys.stdout.flush()
    
    # putchar(b);
    sys.stdout.write(b)
    sys.stdout.flush()
    
    # for ( ; ; ) { ... } -> Infinite loop in Python
    while True:
        time.sleep(1)          # sleep(1);
        sys.stdout.write(c)      # putchar(c);
        sys.stdout.write(d)      # putchar(d);
        sys.stdout.write(b)      # putchar(b);
        sys.stdout.flush()

if __name__ == '__main__':
    main()
