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


# 1 задание
a = []  # список с ответами на задания
#s1, answer1, x1 = f1()
#a.append(x1)
#print(s1, answer1, x1, "\n")

# 2 задание
s2, answer2, x2 = f2()
a.append(x2)
print(s2, "\n", answer2, x2)