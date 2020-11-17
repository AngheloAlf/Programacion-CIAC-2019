def f1(estrellas, aliens):
  for polvo in estrellas:
    if aliens == polvo[0]:
      polvo[1] += 1
      return estrellas
  coso = [aliens, 1]
  estrellas.append(coso)
  return estrellas

def f2(cornios):
  coso = []
  for uni in cornios:
    coso = f1(coso, uni)
  return coso

magia = "alafa"
print(f2(magia))
