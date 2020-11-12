# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print("="*80)
print("10 primeiros termos de uma PA (Progressão aritmética)")
print("="*80)

a1 = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão da PA: "))
an = a1 + (10 - 1) * r 

for n in range(a1, an + r, r):
    print(n, end="  → ")
print("Acabou.")
