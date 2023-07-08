s = input()

a = [ord(i) for i in s]

for i in range(len(a)):
    if a[i] <= 96:
        print(i+1)
        exit()