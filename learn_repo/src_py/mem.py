import sys

SAME = 0

class Key:
    def __init__(self, k_wd, k_val):
        self.k_wd = k_wd
        self.k_val = k_val

keybuff = [
    Key("ready", READY),
    Key("�����", READY),
    Key("�����", READY),
    Key("answer", READY),
    Key("", READY),
    Key("#redefine", REDEFINE),
    Key("#redefoff", REDEFOFF),
    Key("#print", PRINT),
    Key("#copyin", COPYIN),
    Key("#uncopyin", UNCOPIN),
    Key("#copyout", COPYOUT),
    Key("#uncopyout", UNCOPOUT),
    Key("#pipe", PIPE),
    Key("#unpipe", UNPIPE),
    Key("#succeed", SUCCEED),
    Key("#fail", FAIL),
    Key("����", BYE),
    Key("bye", BYE),
    Key("chdir", CHDIR),
    Key("cd", CHDIR),
    Key("learn", LEARN),
    Key("#log", LOG),
    Key("��", YES),
    Key("yes", YES),
    Key("���", NO),
    Key("no", NO),
    Key("#mv", MV),
    Key("#user", USER),
    Key("#next", NEXT),
    Key("�������", SKIP),
    Key("skip", SKIP),
    Key("#where", WHERE),
    Key("���", WHERE),
    Key("#match", MATCH),
    Key("#bad", BAD),
    Key("#create", CREATE),
    Key("#cmp", CMP),
    Key("#once", ONCE),
    Key("#", NOP),
    Key(None, 0)
]

def action(s):
    global reTURN
    if reTURN:
        for kp in keybuff[4:]:
            if kp.k_wd == s:
                return kp.k_val
    else:
        for kp in keybuff:
            if kp.k_wd == s:
                return kp.k_val
    return None

NW = 100
NWCH = 800

class WhichDid:
    def __init__(self, w_less, w_seq):
        self.w_less = w_less
        self.w_seq = w_seq

which = [WhichDid(None, 0) for _ in range(NW)]
nwh = 0
whbuff = [''] * NWCH
whcp = 0

def setdid(lesson, sequence):
    global nwh, whcp
    for pw in which[:nwh]:
        if pw.w_less == lesson:
            pw.w_seq = sequence
            return
    pw = which[nwh]
    nwh += 1
    if nwh >= NW:
        sys.stderr.write("nwh>=NW\n")
        wrapup(1)
    pw.w_seq = sequence
    pw.w_less = whbuff[whcp:whcp + len(lesson)]
    whbuff[whcp:whcp + len(lesson)] = lesson
    whcp += len(lesson)
    if whcp >= NWCH:
        if flag:
            sys.stderr.write("������ ������� ������� ��� �����\n")
        else:
            sys.stderr.write("lesson name too long\n")
        wrapup(1)

def already(lesson, sequence):
    for pw in which[:nwh]:
        if pw.w_less == lesson:
            return 1
    return 0