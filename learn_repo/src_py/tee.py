import os

# Global variables corresponding to the static buffer and pointer in the original C code
ln = []  # This list represents the buffer "ln[BUFSIZ]" from the C code
p = 0    # This integer represents the pointer "p" that initially points to the start of ln

def put(c, f):
    global ln, p
    # Equivalent to "*p++ = c" in C: append the character to the buffer and increment the pointer index
    ln.append(c)
    p += 1
    if c == ord('\n'):
        fl(f)
        # Reset the buffer and pointer as "p = ln" in C (i.e. pointer reset to the beginning)
        ln.clear()
        p = 0

def fl(f):
    global ln, p
    s = 0  # s is like a pointer starting at the beginning of ln
    if p > 0 and ln[0] == ord('$'):
        s += 1
        if p > s and ln[s] == ord(' '):
            s += 1
    if s < p:
        # Write the slice of the buffer from index s up to the current pointer p to file descriptor f
        os.write(f, bytes(ln[s:p]))

def main():
    global ln, p
    # Create (or truncate) the file ".ocopy" with permissions 0666, equivalent to creat(".ocopy", 0666)
    f = os.open(".ocopy", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666)
    while True:
        # Read one byte from file descriptor 0 (standard input)
        data = os.read(0, 1)
        if not data:
            break
        # Extract the integer value of the read byte; equivalent to storing in variable c
        c = data[0]
        c &= 0xFF  # Ensures c is in the range 0-255, just like c &= 0377 in C
        # Write the byte to file descriptor 1 (standard output)
        os.write(1, bytes([c]))
        put(c, f)
    fl(f)
    os.close(f)

if __name__ == '__main__':
    main()
