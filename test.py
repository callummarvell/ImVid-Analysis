test = ""
for i in "abc:1231234":
    try:
        if i == int(i):
            print(i)
            test.append(i)
    except Exception:
        continue
print(test)