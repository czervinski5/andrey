#questao 1

def S(n):
  if n == 1: return 10
  if n >= 2: return S(n - 1) + 10

print(f"Questao 1) a) S(5) = {S(5)}")

def A(n):
  if n == 1: return 2
  if n >= 2: return 1/A(n - 1)

print(f"Questao 1) b) A(5) = {A(5)}")

def B(n):
  if n == 1: return 1
  if n >= 2: return B(n - 1) + n**2

print(f"Questao 1) c) B(5) = {B(5)}")

def P(n):
  if n == 1: return 1
  if n >= 2: return n**2 * P(n - 1) + n - 1

print(f"Questao 1) d) P(5) = {P(5)}")

def D(n):
  if n == 1: return 3
  if n == 2: return 5
  if n > 2: return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

print(f"Questao 1) e) D(5) = {D(5)}")

def W(n):
  if n == 1: return 2
  if n == 2: return 5
  if n > 2: return W(n - 1) * W(n - 2)

print(f"Questao 1) f) W(5) = {W(5)}")

def T(n):
  if n == 1: return 1
  if n == 2: return 2
  if n == 3: return 3
  if n > 3: return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)

print(f"Questao 1) g) T(5) = {T(5)}")

# questao 2

def geometrical_progression(a, r, n):
  if n == 1: return a
  if n >= 2: return geometrical_progression(a, r, n-1) * r

print(f"Questao 2) geometrical_progression(2, 2, 5) = {geometrical_progression(2, 2, 5)}")

# questao 3


def T3(n):
    if n == 2: return True
    elif n < 2: return False
    else: return T3(n - 3) or T3(n / 2)

numT = [6, 7, 19, 12]
for i in numT:
    if T3(i):
        print(f'{i} pertence a T')
    else:
        print(f'{i} não pertence a T')

# Questao 4
def M4(n):
  if n == 2 or n == 3: return True
  elif n < 2: return False
  else: 
     return M4(n / 2) or M4(n / 3)

numM = [6, 9, 16, 21, 26, 54, 72, 218]
for i in numM:
    if M4(i):
        print(f'{i} pertence a M')
    else:
        print(f'{i} não pertence a M')

#Questao 5

def S5(n):
    if n == "a" or n == "b":return True
    elif n[0] == "a":return S5(n[1:])
    elif n[0] == "b":return S5(n[1:])
    else:return False

array = ["a", "ab", "aba", "aaab", "bbbbb"]

for string in array:
    if S5(string):
        print(f'"{string}" pertence a S')
    else:
        print(f'"{string}" não pertence a S')



#Questao 6
def W6(n):
    if n == "a" or n == "b" or n == "c":return True
    elif n[0] == "a" and n[-1] == "c":return W6(n[1:-1])
    else:return False

array = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]

for string in array:
    if W6(string):
        print(f'"{string}" pertence a W')
    else:
        print(f'"{string}" não pertence a W')

#Questao 7
def binario_gerar(n, antes=""):
    if n == 0:
        if antes.count("0") % 2 != 0:
            print(antes)
    else:
        binario_gerar(n-1, antes + "0")
        binario_gerar(n-1, antes + "1")

binario_gerar(4)

#Questao 8
def oitoA(n):
    if n == 1:
        return 1
    else:
        return 3 * oitoA(n - 1)

def oitoB(n):
  if n == 1: 
    return 2
  else:
    return .5 * oitoB(n - 1)

def oitoC(n):
    if n == 1:
        return 'a'
    elif n == 2:
        return 'b'
    else:
        return oitoC(n-2) + oitoC(n-1)

print(oitoC(5))

def oitoD(n, p, q):
    if n == 1:
        return 'p'
    elif n == 2:
        return 'p - q'
    elif n % 2 == 0:
        return oitoD(n-1, p, q) + ' + {}q'.format((n-1) // 2)
    else:
        return oitoD(n-1, p, q) + ' - {}q'.format(n // 2)




#Questao 9
def pitagoras(n):
    if n == 1:
        return 1
    else:
        return n + pitagoras(n - 1)
    
print("\nPitagoras:",pitagoras(3))
# Questao 10
def bacterias(n, populacao):
    if populacao >= 200000:
        return n
    else:
        return bacterias(n+1, 3 * populacao)

leitura = bacterias(0, 50000)

print(f'\n questao 10 =\nExecucoes para ter mais de 200,000 bacterias: {leitura}\n')


#Questao 11
def Rotina(L, j):
    if j == 1:
        return L
  
    i = L.index(max(L[:j]))
    L[i], L[j-1] = L[j-1], L[i] 
    return Rotina(L, j-1)

L = [3, 7, 4, 2, 6]
resultado = Rotina(L, len(L))

print("\nlista final:\n", resultado)
