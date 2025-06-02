#!/usr/bin/env python3
import os
import time

# Mimicking lrnref.h inclusion from the original C code.
# If lrnref.h defined any globals, they should be defined here.
flag = 0  # Global flag variable (set to 0 or 1 as needed)

def makpipe():
    # register int f[2];
    f = os.pipe()
    
    if os.fork() == 0:
        os.close(f[1])
        os.close(0)
        os.dup2(f[0], 0)
        os.close(f[0])
        # execl ("/bin/sh", "sh", "-i", 0);
        try:
            os.execl("/bin/sh", "sh", "-i")
        except Exception:
            pass
        # execl ("/usr/bin/sh", "sh", "-i", 0);
        try:
            os.execl("/usr/bin/sh", "sh", "-i")
        except Exception:
            pass
        # if (flag)  write(2,"������ ��� ���������� sh\n",28);
        # else  write(2,"Exec error\n",11);
        if flag:
            os.write(2, "������ ��� ���������� sh\n".encode())
        else:
            os.write(2, "Exec error\n".encode())
        os._exit(1)
    os.close(f[0])
    # ��� ����, ����� shell ������ ��� ����������
    time.sleep(2)
    return f[1]

# Example usage:
if __name__ == '__main__':
    # Call makpipe and get the write end of the pipe.
    write_fd = makpipe()
    # The returned file descriptor (write_fd) can be used for further processing.
    print("Write file descriptor:", write_fd)
