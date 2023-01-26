import linecache as lc
from googletrans import Translator
from os import system, name
from os import SEEK_END



def rawcount(filename):
    f = open(filename, 'rb')
    lines = 1
    buf_size = 1024 * 1024
    read_f = f.raw.read

    buf = read_f(buf_size)
    while buf:
        lines += buf.count(b'\n')
        buf = read_f(buf_size)
    return lines

def main():
    last_per = 0
    translator = Translator()
    i = 1
    last_line = rawcount("text.txt")
    print("          ------------------------------")
    print("PROGRASS [", end='')
    while (i != last_line):
        # Using linecache.getline() method
        gfg = lc.getline('text.txt', i)
        translation = translator.translate(gfg, dest='fa')
        with open('result.txt', "a", encoding="utf-8") as f2:
            f2.writelines(translation.text)
            f2.writelines("\n")
            #f2.writelines(gfg)
            #f2.writelines("\n")

        percent = int((i / last_line) * 100)

        if(last_per!=percent):
            last_per = percent
            if ((last_per%10) == 0):
                print(" = ", end='')

        i += 1
    print("]\n\nSuccess!")

main()

