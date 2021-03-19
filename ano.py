
D = int(input())
Y = int(D/365)
D = int(D%365)
M = int(D/30)
D = D%30
print("%d ano(s)"%Y)
print("%d mes(es)"%M)
print("%d dia(s)"%D)