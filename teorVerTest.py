import random


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
    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + b[i] + "   "
        if b[i] == str5:
            x1 = a[i]

    return s, otvet, x1


def f2():
    form1 = "Найдите вероятность, что наудачу брошенная в круг точка окажется вне вписанного в него квадрата"
    form2 = "Найдите вероятность, что наудачу брошенная в круг точка окажется внутри вписанного в него правильного " \
            "треугольника "
    form3 = "Найдите вероятность, что наудачу брошенная в круг точка окажется ВНЕ вписанного в него правильного " \
            "треугольника "

    ans = ["1-2/pi", "3*sqrt(3)/4*pi", "1-3*sqrt(3)/4*pi"]  # правильные ответы
    a = ["а)", "б)", "в)", "г)"]
    s = random.choice([form1, form2, form3])

    # неправильные ответы
    notans = ["1-" + str(random.randint(1, 4)) + "/" + "pi", "1" + "/" + str(random.randint(2, 8)) + "pi",
              "pi" + "/" + str(random.randint(2, 38)),
              "sqrt(3)" + "/" + str(random.randint(1, 8))]
    vernOtvet = {
        form1: ans[0],
        form2: ans[1],
        form3: ans[2],
    }
    variant = []
    variant.append(str(vernOtvet[s]))
    variant = variant + (random.sample(notans, 3))
    random.shuffle(variant)
    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + variant[i] + "   "
        if variant[i] == vernOtvet[s]:
            x2 = str(a[i])

    return s, otvet, x2

def f3():
    p1 = random.choice([0.1, 0.2])
    p2 = random.choice([0.1, 0.2, 0.2, 0.3])
    p3 = random.choice([0.1, 0.1, 0.2, 0.2, 0.3, 0.4])

    znach = round(1 - ((1 - p1) * (1 - p2) * (1 - p3)), 3)
    z1 = round(znach - 0.05, 3)
    z2 = round(znach - 0.1, 3)
    z3 = round(znach + 0.15, 3)

    a = ["а)", "б)", "в)", "г)"]
    b = [znach, z1, z2, z3]
    random.shuffle(b)

    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + str(b[i]) + " "
        if b[i] == znach:
            x3 = a[i]

    return p1, p2, p3, otvet, x3

def f4():
    s1 = random.randint(30, 60)
    s2 = 100 - s1
    s3 = random.choice([0.1, 0.2, 0.3, 0.4])
    s4 = random.choice([0.05, 0.15, 0.25, 0.35])

    znach = round(1 - (((s1 / 100) * s3) + ((s2 / 100) * s4)), 3)
    z1 = round(1 - znach, 3)
    z2 = round(1 - znach / 2, 3)
    z3 = round(znach + 0.017, 3)

    a = ["а)", "б)", "в)", "г)"]
    b = [znach, z1, z2, z3]
    random.shuffle(b)

    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + str(b[i]) + " "
        if b[i] == znach:
            x4 = a[i]

    return s1, s2, s3, s4, otvet, x4

def f5():
    # расстановка котят в первой серии коробок
    # s1 специально имеет такие узкие значения, на основе него вычисляется s3
    # и мы не можем расположить котов в соотношении  1-9 или 9-1, т.к. текст условия станет некрасивым :/
    s1 = random.choice([2, 3, 4, 6, 7, 8])
    s2 = 10 - s1
    # расстановка котят во второй серии коробок
    # важно - она должна быть другой, иначе вероятности для серий коробок будут одинаковыми
    # считаю, что s3 достаточно вариативен и продуман.
    ne_peresekayet = []
    for i in range(2, 8):
        if i != s1 and i != s2 and i != 5:
            ne_peresekayet.append(i)

    s3 = random.choice(ne_peresekayet)
    s4 = 10 - s3

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

    # всегда в первой серии 4 коробки, во второй 6, всего 100 котят
    # s1, s3 - белые, s2, s4 - черные
    # shuffle не нужен, т.к. номер правильного ответа зависит от usl, которое случайное
    a = ["а)", "б)", "в)", "г)"]
    b1 = round(((4 * s1) / 100) / ((4 * s1 + 6 * s3) / 100), 3)
    b2 = round(((4 * s2) / 100) / ((4 * s4 + 6 * s3) / 100), 3)
    b3 = round(((6 * s1) / 100) / ((4 * s1 + 6 * s3) / 100), 3)
    b4 = round(((6 * s1) / 100) / ((4 * s2 + 6 * s4) / 100), 3)
    b = [str(b1), str(b2), str(b3), str(b4)]

    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + str(b[i]) + "   "
    x5 = a[usl]
    return s1, s2, s3, s4, usl1, usl2, otvet, x5


def f6():
    # границы распределения
    g1 = random.randint(1, 3)
    g2 = random.randint(4, 6)
    g3 = random.randint(7, 9)
    g4 = random.randint(10, 12)
    g = [g1, g2, g3, g4]

    # распределение вероятностей
    s1 = random.choice([0.02, 0.05, 0.06, 0.1, 0.12, 0.15, 0.16, 0.2, 0.22, 0.25, 0.26, 0.3, 0.32, 0.35, 0.36, 0.4])
    s2 = random.choice([0.03, 0.04, 0.08, 0.09, 0.13, 0.14, 0.18, 0.19, 0.23, 0.24, 0.28, 0.29, 0.33, 0.34, 0.38, 0.39])
    s3 = round(0.5 - s1, 2)
    s4 = round(0.5 - s2, 2)
    s = [s1, s2, s3, s4]

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
        usl = "P(" + str(g1) + " < X ≤ " + str(g4)
    if r == 1:
        usl = "P(" + str(g1) + " ≤ X < " + str(g4)
    if r == 2:
        usl = "P(" + str(g3) + " ≤ X ≤ " + str(g4)
    if r == 3:
        usl = "P(" + str(g1) + " < X < " + str(g4)

    # надо shuffl'ануть
    r = z[r]
    random.shuffle(z)

    a = ["а)", "б)", "в)", "г)"]
    otvet = ""
    for i in range(4):
        otvet = otvet + a[i] + str(z[i]) + "   "
        if z[i] == r:
            x6 = a[i]

    return g, s, usl, otvet, x6

    print(s)


# 1 задание
a = []  # список с ответами на задания
#s1, answer1, x1 = f1()
#a.append(x1)
#print(s1, answer1, x1, "\n")

# 2 задание
#s2, answer2, x2 = f2()
#a.append(x2)
#print(s2, "\n", answer2, x2)

# 3 задание

#s3_1, s3_2, s3_3, answer3, x3 = f3()
#a.append(x3)
#print(s3_1, s3_2, s3_3, answer3, x3)

# 4 задание
#s4_1, s4_2, s4_3, s4_4, answer4, x4 = f4()
#a.append(x4)
#print(s4_1, s4_2, s4_3, s4_4, answer4, x4)

# # 5 задание
# s5_1, s5_2, s5_3, s5_4, s5_usl1, s5_usl2, answer5, x5 = f5()
# a.append(x5)
# print(s5_1, s5_2, s5_3, s5_4, s5_usl1, s5_usl2, answer5, x5)

# 6 задание
g6, s6, s6_usl, answer6,  x6 = f6() # в массивах удобнее
a.append(x6)
print(g6, s6, s6_usl, answer6,  x6)