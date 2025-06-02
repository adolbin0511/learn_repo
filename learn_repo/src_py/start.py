import os
import sys

ND = 64

def start(lesson):
    dv = os.listdir('.')
    n = len(dv)

    if n == ND:
        if flag:
            print("���� ������� �������", file=sys.stderr)
        else:
            print("lesson too long", file=sys.stderr)

    for name in dv:
        if name.endswith('.c'):
            continue
        c = name[0]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('�' <= c <= '�') or ('�' <= c <= '�'):
            os.unlink(name)

    if ask:
        return

    where = f"../../{sname}/L{lesson}"
    if os.access(where, os.R_OK):
        return

    if flag:
        print(f"��� ����� {lesson}", file=sys.stderr)
    else:
        print(f"No lesson {lesson}", file=sys.stderr)
    
    wrapup(1)

def fcopy(new, old):
    try:
        with open(old, 'rb') as fo, open(new, 'wb') as fn:
            while True:
                b = fo.read(1024)
                if not b:
                    break
                fn.write(b)
    except FileNotFoundError:
        return