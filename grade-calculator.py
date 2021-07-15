quantN = int(input('Quantas notas você quer colocar? '))

for c in range(quantN):
	notas = float(input(f'Digite sua {c} nota: '))
media = () / quantN

print(f'Sua media foi: {media:.1f}')

if media >= 6:
	print('Você foi APROVADO!')
else:
	print ('Você foi REPROVADO!')