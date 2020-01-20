from scipy import integrate, special

e = lambda x,y:x*y**2
f = lambda x:1
g = lambda x:-1

i = integrate.dblquad(e,0,2,f,g)
print(i)