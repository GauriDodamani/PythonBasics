#Skip numbers divisible by 3, from (0,100)

for i in range(0,101):
    if i % 3 == 0:
        continue
    print(f"{i} is the number")


# for i in range(0, 101):
#     if i % 3 == 0:
#         continue  # skip numbers divisible by 3
#     print(i)