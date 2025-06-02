import os
import random

nsave = 0

def selunit():
    global nsave
    dobuff = ""
    posslev = []
    diff = []
    best = -1
    alts = 0
    zb = ""
    saved = ""

    while True:
        if flag:
            print("����� ����? \n")
        else:
            print("What lesson? ", end="")
        dobuff = input().strip()
        if dobuff == "bye" or dobuff == "����":
            wrapup(0)
        level = todo = dobuff
        s = f"../../{sname}/L{dobuff}"
        if os.access(s, os.R_OK):
            return
        if flag:
            print("������ ����� ��� \n")
        else:
            print("no such lesson\n")

    retry:
    f = scrin
    if f is None:
        fnam = f"../../{sname}/L{level}"
        try:
            f = open(fnam, "r")
        except FileNotFoundError:
            if flag:
                print(f"��� �������� ��� ����� {level}.", file=sys.stderr)
            else:
                print(f"No script for lesson {level}.", file=sys.stderr)
            wrapup(1)

        for line in f:
            zb = line.strip()
            if zb == "#next":
                break

    if f.closed:
        if flag:
            print("������� ���� ������������ ! �� ������ ���� ����.\n")
        else:
            print("Congratulations; you have finished this sequence.\n")
        todo = 0
        return

    for i, line in enumerate(f):
        parts = line.split()
        posslev.append(parts[0])
        diff.append(int(parts[1]))

    n = random.randint(0, i - 1)
    for k in range(i):
        m = (n + k) % i
        if already(posslev[m], 0):
            continue
        if best < 0:
            best = m
        alts += 1
        if abs(diff[m] - speed) < abs(diff[best] - speed):
            best = m

    if best < 0 and nsave:
        nsave -= 1
        level = saved
        goto retry

    if best < 0:
        if flag:
            print("��������,�� ��������������� ����� �� ���� ����� �������� 'learn'")
            print("���� ���.���������� � ������������.")
        else:
            print("Sorry, there are no alternative lessons at this stage.")
            print("See someone for help.")
        todo = 0
        return

    dobuff = posslev[best]
    if alts > 1:
        nsave = 1
        saved = level
    todo = dobuff
    f.close()

def abs(x):
    return x if x >= 0 else -x

def grand():
    global garbage
    a = [0, 0]
    time(a)
    b = a[1] + 10 * garbage
    garbage += 1
    return b & 0o77777