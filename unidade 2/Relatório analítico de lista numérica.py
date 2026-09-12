lnum = []
par = []
impar = []
for i in range(10):
  num = (int(input('digite um numero: ')))
  lnum.append(num)
  if(num % 2 == 0):
    par.append(num)
  else:
    impar.append(num)
print(lnum)
print(par)
print(impar)
print(sum(lnum))
print(sum(lnum)/ 10)
print(max(lnum))
print(min(lnum))