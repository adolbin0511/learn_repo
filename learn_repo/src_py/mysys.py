#!/usr/bin/env python3
import os
import sys
import signal

# Including "lrnref.h" equivalent (contents unknown)
# Constants definitions
EASY = 1
MEDIUM = 2
HARD = 3

# Global flag variable (assuming default value 0)
flag = 0

def mysys(s):
    # ������ system(s) - �����������,
    # �� ��������� �������
    # ��������� ����� �����
    # exec, a �� ����� shell
    p = ""    # char p[300] equivalent, using string in Python
    np_list = []   # char *np[40] equivalent, using list in Python
    t = None   # register char *t; will be used later
    nv = 0
    type_val = EASY
    # Determine the type by scanning the input string
    for char in s:
        if char and type_val != HARD:
            if char in ['*', '[', '?', '>', '<', '$', '\'', '"']:
                type_val = MEDIUM
            elif char in ['|', ';', '&']:
                type_val = HARD

    if type_val == HARD:
        return system(s)
    elif type_val == MEDIUM:
        p = "exec " + s
        return system(p)
    elif type_val == EASY:
        p = s
        nv = getargs(p, np_list)
        t = np_list[0]
        if (t == "mv" or
            t == "cp" or
            t == "rm" or
            t == "ls"):
            child_pid = os.fork()
            if child_pid == 0:
                b = ""    # char b[100] equivalent, using string in Python
                signal.signal(signal.SIGINT, signal.SIG_DFL)
                b = "/bin/" + t
                # In C, np[nv] = 0 is used to null-terminate the argv list.
                # In Python, we simply use the list as is.
                try:
                    os.execv(b, np_list)
                except Exception:
                    if flag:
                        sys.stderr.write("������ ��� ���������� execv\n")
                    else:
                        sys.stderr.write("Execv failed\n")
                    os._exit(1)
            pid, stat = os.waitpid(child_pid, 0)
            return stat
        return system(s)

def system(s):
    # 
    # system():
    #      ������ ������������ ������,
    #      �� ������������� � ����������� ��������
    #      ��������� �������� �� ���������.
    status = 0
    pid = 0
    w = 0
    # Save current signal handlers
    istat = signal.signal(signal.SIGINT, signal.SIG_IGN)
    qstat = signal.signal(signal.SIGQUIT, signal.SIG_IGN)
    pid = os.fork()
    if pid == 0:
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        signal.signal(signal.SIGQUIT, signal.SIG_DFL)
        try:
            os.execl("/bin/sh", "sh", "-c", s)
        except Exception:
            os._exit(127)
    # Wait for the child process to finish
    try:
        # Using os.waitpid to wait for the specific child's termination
        wp = os.waitpid(pid, 0)
        (w, status) = wp
    except ChildProcessError:
        status = -1
    # Restore original signal handlers
    signal.signal(signal.SIGINT, istat)
    signal.signal(signal.SIGQUIT, qstat)
    return status

def getargs(s, v):
    # The function splits the input string into tokens separated by spaces or tabs.
    # register int i;
    i = 0
    # Instead of pointer arithmetic, we use splitting.
    # The C code modifies the string in-place; here we emulate by splitting the string.
    tokens = s.split()
    for token in tokens:
        v.append(token)
        i += 1
    return i

if __name__ == "__main__":
    # Example usage:
    # This section is only for demonstration purposes and is not part of the original C code.
    # You can modify or remove it as needed.
    command = "ls -l /"
    ret = mysys(command)
    sys.exit(ret)
    
