call = 15
n = 0
an = 3
line =[]
poly = []

while True:
    if call>0:
        if call%2:
            line.append(str(call))
            poly = "".join(line)
    else:
        break
    call-=1
answer  = poly.count(str(an))

print(answer)

# %%





