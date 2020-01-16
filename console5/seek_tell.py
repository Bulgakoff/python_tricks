
with open('t1.txt', 'w') as ff:
    content = 'Strings Strings Strings Strings '
    ff.write(content)

f = open('t1.txt')
print(f.read(3))
print('текущая позиция',f.tell())
f.seek(0)
print(f.read())
f.close()
