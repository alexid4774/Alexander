import random
def pswd():
    alph = "ABCDEFGHRJKLMNOPQRSTUVWXYZabcdefghrjklmnopqrstuvwxyz0123456789"
    res = ""
    for i in range(8):
        res += random.choice(alph)
    f1 = False
    f2 = False
    f3 = False
    for j in res:
        if j.isdigit():
            f1 = True
        if j in "ABCDEFGHRJKLMNOPQRSTUVWXYZ":
            f2 = True
        if j in "abcdefghrjklmnopqrstuvwxyz":
            f3 = True
    if f1 and f2 and f3:
        return res
    return pswd()

f = open("students.csv", encoding="utf8")
a = []
namme = f.readline().strip()
for i in f:
    a.append(i[:-1])
n = len(a) - 1
st = []



class Students:
    pass


for j in range(n):
    st.append(Students())

for i in range(n):
    s = a[i].split(",")
    svv = s[1].split()
    st[i].idd = s[0]
    st[i].name = s[1]
    st[i].tidd = s[2]
    st[i].clas = s[3]
    if s[4] == "None":
        st[i].score = s[4]
    else:
        st[i].score = int(s[4])
    st[i].login = svv[0] + "_" + svv[1][0] + svv[2][0]
    st[i].ps = pswd()

for i in st:
    s = 0
    k = 0
    if i.score == 'None':
        for j in st:
            if j.clas == i.clas and j.score != 'None':
                k += 1
                s += int(j.score)
        i.score = float(f'{s/k:.3f}')

f = open('students_new.csv', 'w')
print(namme, file=f)
for i in st:
    print(i.idd, ',', i.name, ',', i.tidd, ',', i.clas, ',', i.score, file=f)
f.close()

for i in range(n):
    if st[i].name == "Хадаров Владимир Валериевич":
        print("Ты получил:", st[i].score, "за проект -", st[i].tidd)
        break

for i in range(1, n):
    t = st[i]
    j = i - 1
    while j >= 0 and t.score > st[j].score:
        st[j + 1] = st[j]
        j -= 1
    st[j + 1] = t

k = 0
print("10 класс:")
for i in range(n):
    if st[i].clas[:-1] == "10":
        k += 1
        print(k, "место", st[i].name, st[i].score)
    if k == 3:
        break


Id = input()
while Id != "СТОП":
    for i in range(n):
        if st[i].tidd == Id:
            print("Проект №", st[i].idd, "делал(а):", st[i].name, ", он(а) получил(а) оценку -", st[i].score, ".")
    Id = input()

f1 = open('students_password.csv', 'w')
print(namme, ',', "login", ',', "password", file=f1)
for i in st:
    print(i.idd, ',', i.name, ',', i.tidd, ',', i.clas, ',', i.score, ',', i.login, ',', i.ps, file=f1)
f1.close()

