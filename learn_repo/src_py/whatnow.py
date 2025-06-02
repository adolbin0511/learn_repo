import os

def whatnow():
    global todo, didok, speed, wrong, more, level, flag

    if todo == 0:
        more = 0
        return
    if didok:
        level = todo
        if speed <= 9:
            speed += 1
    else:
        speed -= 4
        if speed < 0:
            speed = 0
    if wrong:
        speed -= 2
        if speed < 0:
            speed = 0
    if didok and more:
        if flag:
            print(f"\n�� ��������� ���� {level} .")
            print(f"\n�������� ������� �� ����� {speed} .\n\n")
        else:
            print(f"\nGood.  Lesson {level} ({speed})\n\n")
    
    os.system("clear")