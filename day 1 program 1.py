s1 = input("Enter S1 value:")
t1 = input("Enter t1 value:")
s2 = input("Enter S2 value:")
t2 = input("Enter t1 value:")

if len(s1) != len(t1) or len(s2) != len(t2):
    print(False)
else:
    mapping1 = {}
    mapped_chars1 = set()
    for i in range(len(s1)):
        if s1[i] not in mapping1:
            if t1[i] in mapped_chars1:
                print(False)
                break
            mapping1[s1[i]] = t1[i]
            mapped_chars1.add(t1[i])
        else:
            if mapping1[s1[i]] != t1[i]:
                print(False)
                break
    else:
        print(True)

mapping2 = {}
mapped_chars2 = set()
for i in range(len(s2)):
    if s2[i] not in mapping2:
        if t2[i] in mapped_chars2:
            print(False)
            break
        mapping2[s2[i]] = t2[i]
        mapped_chars2.add(t2[i])
    else:
        if mapping2[s2[i]] != t2[i]:
            print(False)
            break
else:
    print(True)
