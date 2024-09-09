tuple1 = (1, 7, 5, 6, 8, 2, 3, 4, 9)
tuple2 = (100, 700, 500, 600, 800, 200, 300, 400, 900)

product = ()

res = ()
for i in range(0, len(tuple1)):
    x = tuple1[i] * tuple2[i]
    res = res + (x, )
    
print (res)