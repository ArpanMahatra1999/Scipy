from scipy import integrate, special

i = integrate.quad(lambda x: special.exp10(x), 0, 1)
print(i)
