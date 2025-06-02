import os
import signal
import sys
В программе не используется




def wrapup(n):
    # Restore terminal settings
    os.system("stty sane")  # Placeholder for ioctl calls
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    os.chdir("..")
    
    pid = os.fork()
    if pid == 0:
        signal.signal(signal.SIGHUP, signal.SIG_IGN)
        try:
            os.execl("/bin/rm", "rm", "-r", dir)
        except FileNotFoundError:
            try:
                os.execl("/usr/bin/rm", "rm", "-r", dir)
            except FileNotFoundError:
                if flag:
                    sys.stderr.write("Can't find 'rm' command.\n")
                sys.exit(0)

    if flag:
        print("Done.")
    else:
        print("Bye.")
    sys.stdout.flush()
    sys.exit(n)