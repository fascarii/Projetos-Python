print('Descubra quanta tinta você irá precisar. \n')

lar_par = float(input('Qual a largura da parede que deseja pintar? '))
alt_par = float(input('Qual a altura da parede? '))

area = lar_par * alt_par
rend = area / 2
rend_ml = rend * 1000
qtde_tinta = rend_ml
lata = qtde_tinta // 18000
galaorest = qtde_tinta % 18000
galao = galaorest // 3600
litros = galaorest % 3600
lataquarto = litros // 900

if qtde_tinta >= 18000:
    print(
        'Para uma area de {:.2f} m²você precisará {:.0f}  latas de 18 litros.'.
        format(area, lata))

elif qtde_tinta > 3600 and qtde_tinta < 18000:
    print(
        'Para uma área de {:.2f} m² você precisará de {:.0f} galões de 3,6 litros.'
        .format(area, galao))

elif qtde_tinta >= 1800 and qtde_tinta < 3600:
    print(
        'Para uma área de {:.2f} m² você precisará de {:.0f} latas de 900ml.'.
        format(area, lataquarto))

elif qtde_tinta >= 900 and qtde_tinta < 3600:
    print('Para uma área de {:.2f} m² você precisará de {:.0f} lata de 900ml.'.
          format(area, lataquarto))
