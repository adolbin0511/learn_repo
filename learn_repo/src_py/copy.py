import signal
import time

last = ""
logf = ""
subdir = ""
nmatch = 0
incopy = None
comfile = -1
more = 1
wrong = False
status = 0
flag = False
logging = False
sname = "example"  # Placeholder for sname
direct = "example_dir"  # Placeholder for direct
todo = "example_todo"  # Placeholder for todo

def copy(prompt, fin):
    global last, logf, subdir, nmatch, incopy, comfile, more, wrong, status, flag, logging, sname, direct, todo

    if subdir == "":
        subdir = f"../../{sname}"

    while True:
        s = pgets(fin, prompt)
        if s is None:
            if fin == sys.stdin:
                continue
            else:
                break
        s = trim(s)

        for r in s:
            if r == '%':
                s1 = s % (subdir, subdir, subdir)
                s = s1
                break

        r, t = wordb(s)
        p = action(t)

        if p[0] == ONCE:
            if wrong:
                scopy(fin, None)
                continue
            s = r
            r, t = wordb(s)
            p = action(t)

        if p is None:
            if comfile >= 0:
                write(comfile, s)
                write(comfile, "\n")
            else:
                signal.signal(signal.SIGINT, signal.SIG_IGN)
                status = mysys(s)
                signal.signal(signal.SIGINT, intrpt)

            if incopy:
                incopy.write(f"{s}\n")
                last = s
            continue

        if p[0] == READY:
            if incopy and r:
                incopy.write(f"{r}\n")
                last = r
            return
        elif p[0] == PRINT:
            if wrong:
                scopy(fin, None)
            elif r:
                list(r)
            else:
                scopy(fin, sys.stdout)
        elif p[0] == NOP:
            pass
        elif p[0] == MATCH:
            if nmatch > 0:
                scopy(fin, None)
            elif (status := (r == last)) == 0:
                nmatch += 1
                scopy(fin, sys.stdout)
            else:
                scopy(fin, None)
        elif p[0] == BAD:
            if r == last:
                scopy(fin, sys.stdout)
            else:
                scopy(fin, None)
        elif p[0] == SUCCEED:
            scopy(fin, (stdout if status == 0 else None))
            resp = input("Please respond with yes or no:\n")
            if resp in ["yes", "y", "да"]:
                more = 0
                return
            elif resp == '':
                break
        elif p[0] == FAIL:
            scopy(fin, (stdout if status != 0 else None))
        elif p[0] == CREATE:
            with open(r, "w") as fout:
                scopy(fin, fout)
        elif p[0] == CMP:
            status = cmp(r)
        elif p[0] == MV:
            nm = f"{subdir}/L{todo}.{r}"
            fcopy(r, nm)
        elif p[0] in [USER, NEXT]:
            more = 1
            return
        elif p[0] == COPYIN:
            incopy = open(".copy", "w")
        elif p[0] == UNCOPIN:
            if incopy:
                incopy.close()
                incopy = None
        elif p[0] == COPYOUT:
            maktee()
        elif p[0] == UNCOPOUT:
            untee()
        elif p[0] == PIPE:
            comfile = makpipe()
        elif p[0] == UNPIPE:
            close(comfile)
            wait(0)
            comfile = -1
        elif p[0] in [YES, NO]:
            if incopy:
                incopy.write(f"{s}\n")
                last = s
            return
        elif p[0] == WHERE:
            print(f"You are in lesson {todo}" if not flag else f"Where is {todo}")
        elif p[0] == BYE:
            more = 0
            return
        elif p[0] == CHDIR:
            print("cd not allowed" if not flag else "Changing directory not allowed")
        elif p[0] == LEARN:
            print("You are already in learn." if flag else "You can learn now.")
        elif p[0] == LOG:
            if not logging:
                break
            if logf == "":
                logf = f"{direct}/log/{sname}"
            with open(r if r else logf, "a") as f:
                tv = time.localtime()
                tod = time.strftime("%Y-%m-%d %H:%M:%S", tv)
        ### Переделка LOG      
                
                case LOG:
			if (!logging)
				break;
			if (logf[0] == 0)
				sprintf(logf, "%s/log/%s", direct, sname);
			f = fopen( (r? r : logf), "a");
			if (f == NULL)
				break;
			time(tv);
			tod = ctime(tv);
			tod[24] = 0;
			fprintf(f, "%s L%-6s %s %2d %s\n", tod,
			todo, status? "fail" : "pass", speed, pwline);
			fclose(f);
			break;
		case REDEFINE:
			reTURN = 1;
			break;
		case REDEFOFF:
			reTURN = 0;
			break;
		}
	}
	return;
}
                