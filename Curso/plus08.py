# Informe Altura, Largura e Aera para saber quantos m² faz com 1l de tinta sendo que 1l faz 2m²
altura = int(input('Informe a altura: '))
largura = int(input('Informe a lagura: '))
area = altura*largura

print(f'\n Se Áera=Altura*Largura, logo Área é = {area}M²\n Com base nisso, 1l de tinta pinta 2m², então vamos precisar de {area/2}L de tinta')