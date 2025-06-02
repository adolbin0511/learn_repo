import os
import sys
import signal
import lrnref

# Global variables equivalent to static variables in C
oldout = None
tee = ""

def maktee():
    global oldout, tee
    # If tee is not initialized then initialize it with the directory from lrnref
    if tee == "":
        tee = "%s/tee" % lrnref.direct
    # Create a pipe; fpip[0] is read end, fpip[1] is write end
    r, w = os.pipe()
    in_fd = r
    out_fd = w
    pid = os.fork()
    if pid == 0:
        # Child process
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        os.close(0)
        os.close(out_fd)
        os.dup(in_fd)
        os.close(in_fd)
        try:
            os.execl(tee, "lrntee")
        except Exception:
            if lrnref.flag:
                sys.stderr.write("������ ��� ���������� tee\n")
            else:
                sys.stderr.write("Tee exec failed\n")
            sys.exit(1)
    os.close(in_fd)
    sys.stdout.flush()
    oldout = os.dup(1)
    os.close(1)
    if os.dup(out_fd) != 1:
        if lrnref.flag:
            sys.stderr.write("������ ��� ���������� tee ��� ������ \n")
        else:
            sys.stderr.write("Error making tee for copyout\n")
    os.close(out_fd)
    return 1

def untee():
    global oldout
    sys.stdout.flush()
    os.close(1)
    os.dup(oldout)
    os.close(oldout)
    os.wait()
    
if __name__ == "__main__":
    # Example usage: call maktee and untee to simulate the behavior.
    maktee()
    # The program can write to stdout here and it will be duplicated by tee.
    print("This is a test output to tee.")
    untee()
