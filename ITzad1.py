f = open("students.csv", encoding="utf8")
a = []
for i in f:
    a.append(i[:-1])
n = len(a) - 1
st = []
a = a[1:]


class Students:
    pass


for j in range(n):
    st.append(Students())

for i in range(n):
    s = a[i].split(",")
    st[i].idd = s[0]
    st[i].name = s[1]
    st[i].tidd = s[2]
    st[i].clas = s[3]
    if s[4] == "None":
        s[4] = -1
    st[i].score = s[4]

for i in range(1, n):
    t = st[i]
    j = i - 1
    while j >= 0 and int(t.score) > int(st[j].score):
        st[j + 1] = st[j]
        j -= 1
    st[j + 1] = t

k = 0
print("10 класс:")
for i in range(n):
    if st[i].clas[:-1] == "10":
        k += 1
        print(k, "место", st[i].name)
    if k == 3:
        break

Id = input()
for i in range(n):
    if st[i].tidd == Id:
        print("Проект №", st[i].idd)