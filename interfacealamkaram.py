from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
words=""
res=""
from tkinter import *
def longestRepeatedSubstring(str):

    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
             for y in range(n + 1)]

    resu = ""
    res_length = 0
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):


            if (str[i - 1] == str[j - 1] and
                    LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1


                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)

            else:
                LCSRe[i][j] = 0

    if (res_length > 0):
        for i in range(index - res_length + 1,
                       index + 1):
            resu = resu + str[i - 1]

    return resu
def check_freq(str):
    freq = {}
    for c in str:
        freq[c] = str.count(c)
    return freq

def database():
    k=pada.get()
    return k
def splits(word):
    return [char for char in word]

root = Tk()
root.geometry('500x500')
root.title("karNapUra")
pada=StringVar()
label_0 = Label(root, text="karNapUra",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="pAda",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=pada)
entry_1.place(x=240,y=130)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

txt=Text(root,width=25,height=10,wrap=WORD)
root.mainloop()

def antyanu():
    words = database()
    pad = words.split(" # ")
    words1 = pad[0].split(" ")
    words2 = pad[1].split(" ")
    lastword1 = words1[-1]

    lastword2 = words2[-1]
    itranstr1 = transliterate(lastword1, sanscript.TELUGU, sanscript.ITRANS)
    itranstr2 = transliterate(lastword2, sanscript.TELUGU, sanscript.ITRANS)

    splitr1 = splits(itranstr1)
    splitr2 = splits(itranstr2)
    w1 = splits(lastword1)
    w2 = splits(lastword2)

    if splitr1[-1] != "a" and splitr2[-1] != "a":
        if w1[-2] == w2[-2]:
            res = "antyanuprasa"
            if w1[-1] == w2[-1]:
                res = "antyanuprasa with acchu"
        else:
            res = "not antyanuprasa"
    elif splitr1[-1] == "a" and splitr2[-1] == "a":
        if w1[-1] == w2[-1]:
            res = "antyanuprasa"
        else:
            res = "not antyanuprasa"
    elif splitr1[-1] == "a" and splitr2[-1] != "a":
        if w1[-1] == w2[-2]:
            res = "antyanuprasa"
        else:
            res = "not antyanuprasa"
    elif splitr1[-1] != "a" and splitr2[-1] == "a":
        if w1[-2] == w2[-1]:
            res = "antyanuprasa"
        else:
            res = "not antyanuprasa"
    print(res)
    return res

def mukta():
    str=database()
    res=""
    pada = str.split(" # ")
    p1 = pada[0].split(" ")
    p2 = pada[1].split(" ")
    p3 = pada[2].split(" ")
    p4 = pada[3].split(" ")

    lev = 0
    if p2[0].__contains__(p1[-1]):
        lev += 1
    if p3[0].__contains__(p2[-1]):
        lev += 1
    if p4[0].__contains__(p3[-1]):
        lev += 1

    if lev > 0:
        res="mukta padagrasta"
    else:
        res="no mukta padagrasta"
    print(res)
    return res
def vrutyanu():
    strs = database()
    str=transliterate(strs, sanscript.TELUGU, sanscript.ITRANS)
    lol = check_freq(str)
    try:
        del lol["M"]
    except KeyError:
        pass

    try:
        del lol["a"]
    except KeyError:
        pass

    try:
        del lol["e"]
    except KeyError:
        pass

    try:
        del lol["i"]
    except KeyError:
        pass

    try:
        del lol["o"]
    except KeyError:
        pass

    try:
        del lol["A"]
    except KeyError:
        pass

    try:
        del lol["I"]
    except KeyError:
        pass

    try:
        del lol["E"]
    except KeyError:
        pass
    try:
        del lol["O"]
    except KeyError:
        pass
    try:
        del lol["U"]
    except KeyError:
        pass

    try:
        del lol[" "]
    except KeyError:
        pass

    try:
        del lol["u"]
    except KeyError:
        pass


    u_lol = sorted(lol.items(), key=
    lambda kv: (kv[1], kv[0]))


    vrp = u_lol[-1][0]+"a"
    vrps=transliterate(vrp, sanscript.ITRANS, sanscript.TELUGU)



    count = 0
    for c in str:
        if c.isspace() != True:
            count += 1

    up = u_lol[-1][1]

    perc = ((up / count) * 100).__round__(2)
    print(perc,"%",vrps)
    return (perc,vrps)

def yamaka():
    strs=database()
    strings = transliterate(strs, sanscript.TELUGU, sanscript.ITRANS)
    str=strings.replace(" # "," ")
    repeated = longestRepeatedSubstring(str)

    brk = str.split(" ")

    if repeated in brk:
       res="yamakam"
    else:
        res="chekanuprasa"
    print(res)
    return res
mukta()
antyanu()
vrutyanu()
yamaka()