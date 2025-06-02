import signal
import sys

# Global variable equivalent to the C 'int istop;'
istop = 0

def intrpt(signum, frame):
    # This function corresponds to the 'intrpt' signal handler.
    # In the original C code, its implementation is provided externally (likely in "lrnref.h").
    # Here we provide a complete implementation that does nothing.
    pass

def stop(signum, frame):
    # Equivalent to the C function:
    # stop()
    # {
    #     istop=0;
    # }
    global istop
    istop = 0

def list(r):
    # Equivalent to the C function:
    # list(r)
    # register char *r;
    #
    #     if (r==0)
    #         return;
    #
    #     istop = 1;
    #     signal(SIGINT, stop);
    #     ft = fopen(r, "r");
    #     if (ft != NULL) {
    #         while (fgets(s, 100, ft) && istop)
    #             fputs(s, stdout);
    #         fclose(ft);
    #     }
    #     signal(SIGINT, intrpt);
    if r is None:
        return
    global istop
    istop = 1
    signal.signal(signal.SIGINT, stop)
    try:
        ft = open(r, "r")
    except IOError:
        ft = None
    if ft is not None:
        while istop:
            # Read one line from the file; similar to fgets(s, 100, ft) in C.
            s = ft.readline()
            if not s:
                break
            # Output the string; equivalent to fputs(s, stdout) in C.
            sys.stdout.write(s)
        ft.close()
    signal.signal(signal.SIGINT, intrpt)
    
