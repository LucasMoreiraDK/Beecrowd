s = int(input())

m = s//60
s=s-(60*m)

h = m//60
m = m-(60*h)

print("{}:{}:{}".format(h,m,s))


