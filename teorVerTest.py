import random
import sympy
import win32com.client as win32
import win32com.client

import os
import glob


from math import cos, pi
from scipy import integrate

wordApp = win32.gencache.EnsureDispatch('Word.Application')
# create a word application object
wordApp.Visible = False  # hide the word application
#doc = wordApp.Documents.Open("C:/Users/Даниэль/Desktop/template.docx")  # opening the template file


# for creating a new one: doc = wordApp.Documents.Add()

def nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def prived(a, b):
    return a // nod(a, b), b // nod(a, b)


def f1():
    s1 = random.randint(4, 7)
    s2 = random.randint(8, 10)
    s3 = random.randint(11, 13)
    s4 = random.randint(14, 17)
    s = random.choice([s1, s4])

    m1, m2, m3, m4, m = 0, 0, 0, 0, 0
    n = 216

    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k >= s1:
                    m1 += 1
                if i + j + k >= s2:
                    m2 += 1
                if i + j + k >= s3:
                    m3 += 1
                if i + j + k >= s4:
                    m4 += 1
                if i + j + k >= s:
                    m += 1

    m1, n1 = prived(m1, n)
    m2, n2 = prived(m2, n)
    m3, n3 = prived(m3, n)
    m4, n4 = prived(m4, n)
    m, n = prived(m, n)
    a = ["а)", "б)", "в)", "г)"]
    str1 = str(m1) + "/" + str(n1)
    str2 = str(m2) + "/" + str(n2)
    str3 = str(m3) + "/" + str(n3)
    str4 = str(m4) + "/" + str(n4)
    str5 = str(m) + "/" + str(n)
    b = [str1, str2, str3, str4]
    random.shuffle(b)

    for i in range(4):
        if b[i] == str5:
            x1 = a[i]

    rng1 = doc.Bookmarks("Zadaniye_1_a").Range
    rng1.Text = str(b[0])

    rng2 = doc.Bookmarks("Zadaniye_1_b").Range
    rng2.Text = str(b[1])

    rng3 = doc.Bookmarks("Zadaniye_1_v").Range
    rng3.Text = str(b[2])

    rng4 = doc.Bookmarks("Zadaniye_1_g").Range
    rng4.Text = str(b[3])

    rng5 = doc.Bookmarks("Zadaniye_1_otvet").Range
    rng5.Text = str(x1)

    rng6 = doc.Bookmarks("Zadaniye_1_usloviye").Range
    rng6.Text = str(s)

    return


def f2():
    form1 = "Вероятность, что наудачу брошенная в круг точка окажется вне вписанного в него квадрата"
    form2 = "Вероятность, что наудачу брошенная в круг точка окажется внутри вписанного в него правильного " \
            "треугольника "
    form3 = "Вероятность, что наудачу брошенная в круг точка окажется вне вписанного в него правильного " \
            "треугольника "

    ans = ["1-2/π", "3√3/4π", "1-3√3/4π"]  # правильные ответы
    a = ["а)", "б)", "в)", "г)"]
    s = random.choice([form1, form2, form3])

    rng1 = doc.Bookmarks("Zadaniye_2_usloviye").Range
    rng1.Text = str(s)

    # неправильные ответы
    notans = ["1-" + str(random.randint(1, 4)) + "/" + "π", "1" + "/" + str(random.randint(2, 8)) + "π",
              "π" + "/" + str(random.randint(2, 38)),
              "√3" + "/" + str(random.randint(1, 8))]
    vernOtvet = {
        form1: ans[0],
        form2: ans[1],
        form3: ans[2],
    }
    variant = []
    variant.append(str(vernOtvet[s]))
    variant = variant + (random.sample(notans, 3))
    random.shuffle(variant)
    # variant[i] - один из ответов

    rng2 = doc.Bookmarks("Zadaniye_2_a").Range
    rng2.Text = str(variant[0])
    rng3 = doc.Bookmarks("Zadaniye_2_b").Range
    rng3.Text = str(variant[1])
    rng4 = doc.Bookmarks("Zadaniye_2_v").Range
    rng4.Text = str(variant[2])
    rng5 = doc.Bookmarks("Zadaniye_2_g").Range
    rng5.Text = str(variant[3])

    for i in range(4):
        if variant[i] == vernOtvet[s]:
            x2 = str(a[i])  # номер ответа

    rng6 = doc.Bookmarks("Zadaniye_2_otvet").Range
    rng6.Text = str(x2)

    return


def f3():
    p1 = random.choice([0.1, 0.2])
    p2 = random.choice([0.1, 0.2, 0.2, 0.3])
    p3 = random.choice([0.1, 0.1, 0.2, 0.2, 0.3, 0.4])

    rng1 = doc.Bookmarks("Zadaniye_3_usloviye_1").Range
    rng1.Text = str(p1)
    rng2 = doc.Bookmarks("Zadaniye_3_usloviye_2").Range
    rng2.Text = str(p2)
    rng3 = doc.Bookmarks("Zadaniye_3_usloviye_3").Range
    rng3.Text = str(p3)

    znach = round(1 - ((1 - p1) * (1 - p2) * (1 - p3)), 3)
    z1 = round(znach - 0.05, 3)
    z2 = round(znach - 0.1, 3)
    z3 = round(znach + 0.15, 3)

    a = ["а)", "б)", "в)", "г)"]
    b = [znach, z1, z2, z3]
    random.shuffle(b)

    for i in range(4):
        if b[i] == znach:
            x3 = a[i]

    rng4 = doc.Bookmarks("Zadaniye_3_a").Range
    rng4.Text = str(b[0])
    rng5 = doc.Bookmarks("Zadaniye_3_b").Range
    rng5.Text = str(b[1])
    rng6 = doc.Bookmarks("Zadaniye_3_v").Range
    rng6.Text = str(b[2])
    rng7 = doc.Bookmarks("Zadaniye_3_g").Range
    rng7.Text = str(b[3])

    rng8 = doc.Bookmarks("Zadaniye_3_otvet").Range
    rng8.Text = str(x3)

    return


def f4():
    s1 = random.randint(30, 60)
    s2 = 100 - s1
    s3 = random.choice([0.1, 0.2, 0.3, 0.4])
    s4 = random.choice([0.05, 0.15, 0.25, 0.35])

    rng1 = doc.Bookmarks("Zadaniye_4_usloviye_1").Range
    rng1.Text = str(s1)
    rng2 = doc.Bookmarks("Zadaniye_4_usloviye_2").Range
    rng2.Text = str(s2)
    rng3 = doc.Bookmarks("Zadaniye_4_usloviye_3").Range
    rng3.Text = str(s3)
    rng4 = doc.Bookmarks("Zadaniye_4_usloviye_4").Range
    rng4.Text = str(s4)

    znach = round(1 - (((s1 / 100) * s3) + ((s2 / 100) * s4)), 3)
    z1 = round(1 - znach, 3)
    z2 = round(1 - znach / 2, 3)
    z3 = round(znach + 0.017, 3)

    a = ["а)", "б)", "в)", "г)"]
    b = [znach, z1, z2, z3]
    random.shuffle(b)

    rng5 = doc.Bookmarks("Zadaniye_4_a").Range
    rng5.Text = str(b[0])
    rng6 = doc.Bookmarks("Zadaniye_4_b").Range
    rng6.Text = str(b[1])
    rng7 = doc.Bookmarks("Zadaniye_4_v").Range
    rng7.Text = str(b[2])
    rng8 = doc.Bookmarks("Zadaniye_4_g").Range
    rng8.Text = str(b[3])

    for i in range(4):
        if b[i] == znach:
            x4 = a[i]

    rng9 = doc.Bookmarks("Zadaniye_4_otvet").Range
    rng9.Text = str(x4)

    return


def f5():
    # расстановка котят в первой серии коробок
    # s1 специально имеет такие узкие значения, на основе него вычисляется s3
    # и мы не можем расположить котов в соотношении  1-9 или 9-1, т.к. текст условия станет некрасивым :/
    s1 = random.choice([2, 3, 4, 6, 7, 8])
    s2 = 10 - s1

    rng1 = doc.Bookmarks("Zadaniye_5_usloviye_1").Range
    rng1.Text = str(s1)
    rng2 = doc.Bookmarks("Zadaniye_5_usloviye_2").Range
    rng2.Text = str(s2)

    # расстановка котят во второй серии коробок
    # важно - она должна быть другой, иначе вероятности для серий коробок будут одинаковыми
    # считаю, что s3 достаточно вариативен и продуман.
    ne_peresekayet = []
    for i in range(2, 8):
        if i != s1 and i != s2 and i != 5:
            ne_peresekayet.append(i)

    s3 = random.choice(ne_peresekayet)
    s4 = 10 - s3

    rng3 = doc.Bookmarks("Zadaniye_5_usloviye_3").Range
    rng3.Text = str(s3)
    rng4 = doc.Bookmarks("Zadaniye_5_usloviye_4").Range
    rng4.Text = str(s4)

    # котенок оказался черным/белым из первой/второй серии коробок
    # генерируем условие задачи, для остальных условий можно даже рассчитать ответ и внести в список а) б) в) г)
    usl = random.randint(0, 3)
    if usl == 0:
        usl1 = "белым"
        usl2 = "первой"
    if usl == 1:
        usl1 = "черным"
        usl2 = "первой"
    if usl == 2:
        usl1 = "белым"
        usl2 = "второй"
    if usl == 3:
        usl1 = "черным"
        usl2 = "второй"

    rng1 = doc.Bookmarks("Zadaniye_5_usloviye_5").Range
    rng1.Text = str(usl1)
    rng1 = doc.Bookmarks("Zadaniye_5_usloviye_6").Range
    rng1.Text = str(usl2)

    # всегда в первой серии 4 коробки, во второй 6, всего 100 котят
    # s1, s3 - белые, s2, s4 - черные
    # shuffle не нужен, т.к. номер правильного ответа зависит от usl, которое случайное
    a = ["а)", "б)", "в)", "г)"]
    b1 = round(((4 * s1) / 100) / ((4 * s1 + 6 * s3) / 100), 3)
    b2 = round(((4 * s2) / 100) / ((4 * s4 + 6 * s3) / 100), 3)
    b3 = round(((6 * s1) / 100) / ((4 * s1 + 6 * s3) / 100), 3)
    b4 = round(((6 * s1) / 100) / ((4 * s2 + 6 * s4) / 100), 3)
    b = [str(b1), str(b2), str(b3), str(b4)]

    rng1 = doc.Bookmarks("Zadaniye_5_a").Range
    rng1.Text = str(b[0])
    rng1 = doc.Bookmarks("Zadaniye_5_b").Range
    rng1.Text = str(b[1])
    rng1 = doc.Bookmarks("Zadaniye_5_v").Range
    rng1.Text = str(b[2])
    rng1 = doc.Bookmarks("Zadaniye_5_g").Range
    rng1.Text = str(b[3])

    x5 = a[usl]
    rng1 = doc.Bookmarks("Zadaniye_5_otvet").Range
    rng1.Text = str(x5)

    return


def f6():
    # границы распределения
    g1 = random.randint(1, 3)
    g2 = random.randint(4, 6)
    g3 = random.randint(7, 9)
    g4 = random.randint(10, 12)
    g = [g1, g2, g3, g4]

    rng1 = doc.Bookmarks("Zadaniye_6_usloviye_1").Range
    rng1.Text = str(g[0])
    rng2 = doc.Bookmarks("Zadaniye_6_usloviye_2").Range
    rng2.Text = str(g[1])
    rng3 = doc.Bookmarks("Zadaniye_6_usloviye_3").Range
    rng3.Text = str(g[2])
    rng4 = doc.Bookmarks("Zadaniye_6_usloviye_4").Range
    rng4.Text = str(g[3])

    # распределение вероятностей
    s1 = random.choice([0.02, 0.05, 0.06, 0.1, 0.12, 0.15, 0.16, 0.2, 0.22, 0.25, 0.26, 0.3, 0.32, 0.35, 0.36, 0.4])
    s2 = random.choice([0.03, 0.04, 0.08, 0.09, 0.13, 0.14, 0.18, 0.19, 0.23, 0.24, 0.28, 0.29, 0.33, 0.34, 0.38, 0.39])
    s3 = round(0.5 - s1, 2)
    s4 = round(0.5 - s2, 2)
    s = [s1, s2, s3, s4]

    rng5 = doc.Bookmarks("Zadaniye_6_usloviye_5").Range
    rng5.Text = str(s[0])
    rng6 = doc.Bookmarks("Zadaniye_6_usloviye_6").Range
    rng6.Text = str(s[1])
    rng7 = doc.Bookmarks("Zadaniye_6_usloviye_7").Range
    rng7.Text = str(s[2])
    rng8 = doc.Bookmarks("Zadaniye_6_usloviye_8").Range
    rng8.Text = str(s[3])

    # варианты ответа - все правильные, но для своих функций
    # z1 = P(g1 < X ≤ g4),    z2 = P(g1 ≤ X < g4), z3 = P(g3 ≤ X ≤ g4),  z4 = P(g1 < X < g4)
    # в z3 границы (g3;g4), т.к. при (g1;g4) = 1, а при (g2;g4) = z1
    z1 = round(s2 + s3 + s4, 3)
    z2 = round(s1 + s2 + s3, 3)
    z3 = round(s3 + s4, 3)
    z4 = round(s2 + s3, 3)
    z = [z1, z2, z3, z4]

    # рандомный выбор функции
    r = random.choice([0, 1, 2, 3])
    if r == 0:
        usl = "P(" + str(g1) + " < X ≤ " + str(g4) + ")"
    if r == 1:
        usl = "P(" + str(g1) + " ≤ X < " + str(g4) + ")"
    if r == 2:
        usl = "P(" + str(g3) + " ≤ X ≤ " + str(g4) + ")"
    if r == 3:
        usl = "P(" + str(g1) + " < X < " + str(g4) + ")"

    rng0 = doc.Bookmarks("Zadaniye_6_usloviye_9").Range
    rng0.Text = str(usl)

    # надо shuffl'ануть
    r = z[r]
    random.shuffle(z)

    rng9 = doc.Bookmarks("Zadaniye_6_a").Range
    rng9.Text = str(z[0])
    rng10 = doc.Bookmarks("Zadaniye_6_b").Range
    rng10.Text = str(z[1])
    rng11 = doc.Bookmarks("Zadaniye_6_v").Range
    rng11.Text = str(z[2])
    rng12 = doc.Bookmarks("Zadaniye_6_g").Range
    rng12.Text = str(z[3])

    a = ["а)", "б)", "в)", "г)"]
    for i in range(4):
        if z[i] == r:
            x6 = a[i]

    rng13 = doc.Bookmarks("Zadaniye_6_otvet").Range
    rng13.Text = str(x6)

    return


def f7():
    # границы распределения
    g1 = random.randint(1, 3)
    g2 = random.randint(4, 6)
    g3 = random.randint(7, 9)
    g4 = random.randint(10, 12)
    g5 = random.randint(13, 15)
    g = [g1, g2, g3, g4, g5]

    rng1 = doc.Bookmarks("Zadaniye_7_usloviye_1").Range
    rng1.Text = str(g[0])
    rng2 = doc.Bookmarks("Zadaniye_7_usloviye_2").Range
    rng2.Text = str(g[1])
    rng3 = doc.Bookmarks("Zadaniye_7_usloviye_3").Range
    rng3.Text = str(g[2])
    rng4 = doc.Bookmarks("Zadaniye_7_usloviye_4").Range
    rng4.Text = str(g[3])
    rng5 = doc.Bookmarks("Zadaniye_7_usloviye_5").Range
    rng5.Text = str(g[4])

    # распределение вероятностей
    s1 = random.choice([0.05, 0.07, 0.1, 0.15, 0.17, 0.2, 0.25, 0.27])
    s5 = random.choice([0.03, 0.04, 0.06, 0.08, 0.09, 0.12, 0.16, 0.18, 0.22, 0.23])

    rng6 = doc.Bookmarks("Zadaniye_7_usloviye_6").Range
    rng6.Text = str(s1)
    rng7 = doc.Bookmarks("Zadaniye_7_usloviye_7").Range
    rng7.Text = str(s5)

    znach = random.choice([0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7])

    rng8 = doc.Bookmarks("Zadaniye_7_usloviye_8").Range
    rng8.Text = str(g[0])
    rng9 = doc.Bookmarks("Zadaniye_7_usloviye_9").Range
    rng9.Text = str(g[2])
    rng10 = doc.Bookmarks("Zadaniye_7_usloviye_10").Range
    rng10.Text = str(znach)

    # znach = P(g1 ≤ X ≤ g3) = s1 + s2 + s3
    s4 = round(1 - znach - s5, 3)
    s2_plus_s3 = round(znach - s1, 3)
    s2 = round(s2_plus_s3 / 3 - 0.05, 3)
    s3 = round(s2_plus_s3 - s2, 3)
    s = [s1, s2, s3, s4, s5]

    # варианты ответов
    pravda = "a = " + str(s2) + " b = " + str(s3) + " c = " + str(s4)
    lozh1 = "a = " + str(s4) + " b = " + str(s2) + " c = " + str(s3)
    lozh2 = "a = " + str(s1) + " b = " + str(s2) + " c = " + str(s5)
    lozh3 = "a = " + str(s2) + " b = " + str(s3) + " c = " + str(s1)

    # shuffl'анём
    b = [pravda, lozh1, lozh2, lozh3]
    random.shuffle(b)

    a = ["а)", "б)", "в)", "г)"]
    for i in range(4):
        if b[i] == pravda:
            x7 = a[i]

    for i in range(4):
        b[i] = a[i] + b[i]

    rng11 = doc.Bookmarks("Zadaniye_7_a").Range
    rng11.Text = str(b[0])
    rng12 = doc.Bookmarks("Zadaniye_7_b").Range
    rng12.Text = str(b[1])
    rng13 = doc.Bookmarks("Zadaniye_7_v").Range
    rng13.Text = str(b[2])
    rng14 = doc.Bookmarks("Zadaniye_7_g").Range
    rng14.Text = str(b[3])

    rng15 = doc.Bookmarks("Zadaniye_7_otvet").Range
    rng15.Text = str(x7)

    return


def f8():
    # для 0 < X <= pi/6
    var1 = "C * cos(4x)"
    var2 = "C * cos(2x)"
    var3 = "C * sin(2x)"
    var4 = "C * sin(3x)"
    var5 = "C * sin(4x)"
    var6 = "C * sin(6x)"
    var7 = "C * cos(8x)"
    var8 = "C * sin(8x)"
    var = random.choice([var1, var2, var3, var4, var5, var6, var7, var8])

    rng1 = doc.Bookmarks("Zadaniye_8_usloviye").Range
    rng1.Text = str(var)

    if var == var1:
        answ = "8/√3"
    if var == var2:
        answ = "4/√3"
    if var == var3:
        answ = "4"
    if var == var4:
        answ = "3"
    if var == var5:
        answ = "8/3"
    if var == var6:
        answ = "3"
    if var == var7:
        answ = "-16/√3"
    if var == var8:
        answ = "16/3"

    a = ["а)", "б)", "в)", "г)"]
    wrong = ["√3/8", "√3/4", "1/2", "1/3", "3/8", "-√3/16", "3/16", "-π/2", "π/4", "-π/6", "√2/3", "-√2/4", "√2/6",
             "-√3/3"]
    wrong1 = random.choice(wrong)
    wrong.remove(wrong1)
    wrong2 = random.choice(wrong)
    wrong.remove(wrong2)
    wrong3 = random.choice(wrong)
    wrong.remove(wrong3)

    b = [answ, wrong1, wrong2, wrong3]
    random.shuffle(b)

    rng2 = doc.Bookmarks("Zadaniye_8_a").Range
    rng2.Text = str(b[0])
    rng3 = doc.Bookmarks("Zadaniye_8_b").Range
    rng3.Text = str(b[1])
    rng4 = doc.Bookmarks("Zadaniye_8_v").Range
    rng4.Text = str(b[2])
    rng5 = doc.Bookmarks("Zadaniye_8_g").Range
    rng5.Text = str(b[3])

    for i in range(4):
        if b[i] == answ:
            x8 = a[i]

    rng6 = doc.Bookmarks("Zadaniye_8_otvet").Range
    rng6.Text = str(x8)

    return


def f9():
    # для 1 < X < 4
    var1 = "3x^2"
    var1_1 = "64"  # 63/64
    var2 = "2x^2"  # 21/16
    var2_2 = "32"
    var3 = "x^3"  # 5/4
    var3_3 = "51"
    var4 = "7x^2"  # 49/10
    var4_4 = "30"
    var5 = "4x"  # 6/7
    var5_5 = "35"
    var6 = "4x^2"  # 12/5
    var6_6 = "35"
    var7 = "5x^2"  # 15/4
    var7_7 = "30"
    var8 = "5x^2"  # 63/32
    var8_8 = "28"

    var = random.randint(0, 7)
    var_var = [var1, var2, var3, var4, var5, var6, var7, var8]
    var_var_var = [var1_1, var2_2, var3_3, var4_4, var5_5, var6_6, var7_7, var8_8]
    answers = ["63/64", "21/16", "5/4", "49/10", "6/7", "12/5", "15/4", "63/32"]

    answ = answers[var]
    usl1 = var_var[var]
    usl2 = var_var_var[var]

    rng1 = doc.Bookmarks("Zadaniye_9_usloviye_1").Range
    rng1.Text = str(usl1)
    rng2 = doc.Bookmarks("Zadaniye_9_usloviye_2").Range
    rng2.Text = str(usl2)

    wrong = ["1/2", "34/35", "32/63", "31/56", "41/51", "15/19", "5/7", "11/5", "6/13", "7/2", "62/15", "11/23"]
    wrong1 = random.choice(wrong)
    wrong.remove(wrong1)
    wrong2 = random.choice(wrong)
    wrong.remove(wrong2)
    wrong3 = random.choice(wrong)
    wrong.remove(wrong3)

    a = ["а)", "б)", "в)", "г)"]
    b = [answ, wrong1, wrong2, wrong3]
    random.shuffle(b)

    rng3 = doc.Bookmarks("Zadaniye_9_a").Range
    rng3.Text = str(b[0])
    rng4 = doc.Bookmarks("Zadaniye_9_b").Range
    rng4.Text = str(b[1])
    rng5 = doc.Bookmarks("Zadaniye_9_v").Range
    rng5.Text = str(b[2])
    rng6 = doc.Bookmarks("Zadaniye_9_g").Range
    rng6.Text = str(b[3])

    for i in range(4):
        if b[i] == answ:
            x9 = a[i]

    rng7 = doc.Bookmarks("Zadaniye_9_otvet").Range
    rng7.Text = str(x9)

    return


def f10():
    g1 = random.randint(3, 9)
    g2 = g1 * g1
    x10 = "г)"

    rng0 = doc.Bookmarks("Zadaniye_10_otvet").Range
    rng0.Text = str(x10)

    rng1 = doc.Bookmarks("Zadaniye_10_usloviye_1").Range
    rng1.Text = str(g2)
    rng2 = doc.Bookmarks("Zadaniye_10_usloviye_2").Range
    rng2.Text = str(g1)
    rng3 = doc.Bookmarks("Zadaniye_10_usloviye_3").Range
    rng3.Text = str(g1)

    rng4 = doc.Bookmarks("Zadaniye_10_a_1").Range
    rng4.Text = str(g2)
    rng4 = doc.Bookmarks("Zadaniye_10_a_2").Range
    rng4.Text = str(g1)
    rng5 = doc.Bookmarks("Zadaniye_10_a_3").Range
    rng5.Text = str(g1)

    rng6 = doc.Bookmarks("Zadaniye_10_b_1").Range
    rng6.Text = str(g2)
    rng7 = doc.Bookmarks("Zadaniye_10_b_2").Range
    rng7.Text = str(g1)
    rng8 = doc.Bookmarks("Zadaniye_10_b_3").Range
    rng8.Text = str(g1)

    rng9 = doc.Bookmarks("Zadaniye_10_v_1").Range
    rng9.Text = str(g2)
    rng10 = doc.Bookmarks("Zadaniye_10_v_2").Range
    rng10.Text = str(g1)
    rng11 = doc.Bookmarks("Zadaniye_10_v_3").Range
    rng11.Text = str(g1)

    rng12 = doc.Bookmarks("Zadaniye_10_g_1").Range
    rng12.Text = str(g2)
    rng13 = doc.Bookmarks("Zadaniye_10_g_2").Range
    rng13.Text = str(g1)
    rng14 = doc.Bookmarks("Zadaniye_10_g_3").Range
    rng14.Text = str(g1)

    return


def f11():
    s1 = random.choice([0.15, 0.25, 0.3, 0.35, 0.4])
    s2 = 1 - s1
    x1 = random.randint(1, 5)
    x2 = random.randint(6, 9)

    rng1 = doc.Bookmarks("Zadaniye_11_usloviye_1").Range
    rng1.Text = str(x1)
    rng2 = doc.Bookmarks("Zadaniye_11_usloviye_2").Range
    rng2.Text = str(x2)

    znach = round(x1 * s1 + x2 * s2, 3)
    rng3 = doc.Bookmarks("Zadaniye_11_usloviye_3").Range
    rng3.Text = str(znach)

    r = random.randint(1, 2)
    if r == 1:
        st = "p1"
        answ = s1
    else:
        st = "p2"
        answ = s2

    rng4 = doc.Bookmarks("Zadaniye_11_usloviye_4").Range
    rng4.Text = str(st)

    wr1 = round(1 - answ, 3)
    wr2 = round(wr1 + 0.1, 3)
    wr3 = round(wr1 - 0.1, 3)
    a = ["а)", "б)", "в)", "г)"]
    b = [answ, wr1, wr2, wr3]
    random.shuffle(b)

    rng5 = doc.Bookmarks("Zadaniye_11_a").Range
    rng5.Text = str(b[0])
    rng6 = doc.Bookmarks("Zadaniye_11_b").Range
    rng6.Text = str(b[1])
    rng7 = doc.Bookmarks("Zadaniye_11_v").Range
    rng7.Text = str(b[2])
    rng8 = doc.Bookmarks("Zadaniye_11_g").Range
    rng8.Text = str(b[3])

    for i in range(4):
        if b[i] == answ:
            x11 = a[i]

    rng9 = doc.Bookmarks("Zadaniye_11_otvet").Range
    rng9.Text = str(x11)

    return


def f12():
    var = [64, 128, 69, 20, 32]
    inter = [4, 4, 5, 4, 4]
    otv = [2.2, 1.35, 3.93, 0, 2.4]

    wrong = [1.2, 2.7, 3.1, 1.75, 0.8, 1, 2, 3, 4, 2.36]
    wrong1 = random.choice(wrong)
    wrong.remove(wrong1)
    wrong2 = random.choice(wrong)
    wrong.remove(wrong2)
    wrong3 = random.choice(wrong)
    wrong.remove(wrong3)

    r = random.randint(0, 4)
    v = var[r]
    i = inter[r]
    answ = otv[r]

    rng1 = doc.Bookmarks("Zadaniye_12_usloviye_1").Range
    rng1.Text = str(v)
    rng2 = doc.Bookmarks("Zadaniye_12_usloviye_2").Range
    rng2.Text = str(i)
    rng3 = doc.Bookmarks("Zadaniye_12_usloviye_3").Range
    rng3.Text = str(i)

    a = ["а)", "б)", "в)", "г)"]
    b = [answ, wrong1, wrong2, wrong3]
    random.shuffle(b)

    rng4 = doc.Bookmarks("Zadaniye_12_a").Range
    rng4.Text = str(b[0])
    rng5 = doc.Bookmarks("Zadaniye_12_b").Range
    rng5.Text = str(b[1])
    rng6 = doc.Bookmarks("Zadaniye_12_v").Range
    rng6.Text = str(b[2])
    rng7 = doc.Bookmarks("Zadaniye_12_g").Range
    rng7.Text = str(b[3])

    for i in range(4):
        if b[i] == answ:
            x12 = a[i]

    rng8 = doc.Bookmarks("Zadaniye_12_otvet").Range
    rng8.Text = str(x12)

    return


def f13():
    s1 = random.randint(1, 8)
    s2 = s1 + 1

    rng1 = doc.Bookmarks("Zadaniye_13_usloviye_1").Range
    rng1.Text = str(s1)
    rng2 = doc.Bookmarks("Zadaniye_13_usloviye_2").Range
    rng2.Text = str(s2)

    o1 = 2 * (s1 * s1)
    o2 = 2 * (s2 * s2)
    r = random.randint(1, 4)
    if r == 1:
        a1 = b1 = s1
        a3, b3 = o2, o1
        v1 = g1 = s2
        v3, g3 = o1, o2
        a2 = b2 = v2 = g2 = s1
        x13 = "г)"

    if r == 2:
        a1 = b1 = s2
        a3, b3 = o2, o1
        v1 = g1 = s1
        v3, g3 = o1, o2
        a2 = b2 = v2 = g2 = s1
        x13 = "а)"

    if r == 3:
        a1 = b1 = s1
        a3, b3 = o1, o2
        v1 = g1 = s2
        v3, g3 = o2, o1
        a2 = b2 = v2 = g2 = s1
        x13 = "в)"

    if r == 4:
        a1 = b1 = s2
        a3, b3 = o1, o2
        v1 = g1 = s1
        v3, g3 = o1, o2
        a2 = b2 = v2 = g2 = s1
        x13 = "б)"

    rng1 = doc.Bookmarks("Zadaniye_13_a_1").Range
    rng1.Text = str(a1)
    rng2 = doc.Bookmarks("Zadaniye_13_a_2").Range
    rng2.Text = str(a2)
    rng3 = doc.Bookmarks("Zadaniye_13_a_3").Range
    rng3.Text = str(a3)

    rng2 = doc.Bookmarks("Zadaniye_13_b_1").Range
    rng2.Text = str(b1)
    rng1 = doc.Bookmarks("Zadaniye_13_b_2").Range
    rng1.Text = str(b2)
    rng2 = doc.Bookmarks("Zadaniye_13_b_3").Range
    rng2.Text = str(b3)

    rng2 = doc.Bookmarks("Zadaniye_13_v_1").Range
    rng2.Text = str(v1)
    rng1 = doc.Bookmarks("Zadaniye_13_v_2").Range
    rng1.Text = str(v2)
    rng2 = doc.Bookmarks("Zadaniye_13_v_3").Range
    rng2.Text = str(v3)

    rng2 = doc.Bookmarks("Zadaniye_13_g_1").Range
    rng2.Text = str(g1)
    rng1 = doc.Bookmarks("Zadaniye_13_g_2").Range
    rng1.Text = str(g2)
    rng2 = doc.Bookmarks("Zadaniye_13_g_3").Range
    rng2.Text = str(g3)


    rng0 = doc.Bookmarks("Zadaniye_13_otvet").Range
    rng0.Text = str(x13)

    return


# # main

#ввод числа вариантов
path = "C:/Users/Grechka/Desktop/VARIANTS/Variant"
print("Введите число вариантов")
n = int(input())

#чистка папки с (возможно) предыдущими вариантами
files = glob.glob('C:/Users/Grechka/Desktop/VARIANTS/*docx')
for f in files:
    os.remove(f)

for i in range(1, n+1):
    doc = wordApp.Documents.Open("C:/Users/Grechka/Desktop/template.docx")  # opening the template file
    rng1 = doc.Bookmarks("Variant_testa").Range
    rng1.Text = str(i)
    this_path = path + str(i) + ".docx"
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    f13()
    # важно - сохраняем в новый файл
    doc.SaveAs(this_path)

    #показ варианта, который генерится, тип загрузка
    show = "Генерируется вариант " + str(i)

wordApp.Quit()

