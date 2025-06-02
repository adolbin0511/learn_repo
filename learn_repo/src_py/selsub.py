import os
import sys
import subprocess
import list

def selsub(argc, argv):
    ans1 = [''] * 100
    cp = None
    ans2 = [''] * 30
    dirname = [''] * 20
    subname = [''] * 20
    russian = [''] * 20
    wrong = 0
    n = 4  # Number of attempts allowed
    flag = 0

    # Check if the terminal supports Cyrillic
    # This is a placeholder as Python does not have a direct equivalent
    # You may need to implement terminal checking based on your environment

    # Handle directory argument
    if argc > 1 and argv[1][0] == '-':
        direct = argv[1][1:]
        argc -= 1
        argv = argv[1:]

    selsub.chknam(direct)
    if os.chdir(direct) != 0:
        if flag:
            print(f"Cannot change to directory {direct} to exercise a script.", file=sys.stderr)
        else:
            print(f"can't cd to directory {direct} to exercise a script.", file=sys.stderr)
        sys.exit(1)

    if flag:
        lang()

    # Check for subject name
    russian[0] = 'r'
    russian[1] = ''
    sname = argv[1] if argc > 1 else None
    if flag:
        sname = russian + argv[1] if argc > 1 else None

    level = ans2 if argc > 2 else 0
    speed = int(argv[3]) if argc > 3 else None

    if not sname:
        if not flag:
            print("These are the available courses -")
            list_courses("Linfo")
            list_courses("info")
        else:
            print("Доступные курсы :")
            list_courses("rLinfo")
            list_courses("rinfo")
            print("\n$")

        while True:
            subname = input().strip()
            russian[0] = 'r'
            russian[1] = ''
            sname = russian + subname if flag else subname

            if not sname or (sname[0] == 'r' and len(sname) == 1):
                if not wrong:
                    list_courses("rXinfo" if flag else "Xinfo")
                if flag:
                    print("\nКакой предмет вы хотите изучить?\n$ ")
                else:
                    print("\n Which subject?")
                subname = input().strip()
                russian[0] = 'r'
                russian[1] = ''
                sname = russian + subname if flag else subname
            else:
                break

    if os.access(sname, os.R_OK) < 0:
        if flag:
            print(f"\nИзвините, но нет предмета с именем {subname}.")
            print("Попробуйте снова.")
        else:
            print(f"Sorry, but there is no subject named {sname}.")
            print("Try again.")
        wrong += 1
        if wrong <= n:
            subname = [''] * len(subname)
            sname = [''] * len(sname)
            continue
        else:
            chknam(sname)

    if not level:
        list_courses("begin" if not flag else "начать")
        print("\n$")
        ans2 = input().strip()
        if not ans2:
            ans2 = "0"
        level = ans2.split('(')[0].strip()

    if os.chdir("play") != 0:
        if flag:
            print("Не удалось перейти в рабочую директорию.", file=sys.stderr)
        else:
            print("can't cd to playpen.", file=sys.stderr)
        sys.exit(1)

    dir = f"pl{os.getpid()}a"
    subprocess.run(["mkdir", dir])
    if os.chdir(dir) < 0:
        if flag:
            print("Не удалось создать рабочую директорию.", file=sys.stderr)
        else:
            print("couldn't create working directory.", file=sys.stderr)
        sys.exit(1)

    if os.access(f"{direct}/{sname}/init", os.R_OK) == 0:
        if subprocess.run([f"{direct}/{sname}/init", level]) != 0:
            if flag:
                print("Выход из 'learn'.")
            else:
                print("Leaving 'learn'.\nBYE.")
            wrapup(1)

    if level[0] == '-':
        ask = 1