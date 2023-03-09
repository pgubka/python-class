print("Zadaj niekolko celych cisel oddelenych medzerou a ja najdem najmensie z nich; ")
cisla_string = input()
cisla_list = [ int(a) for a in cisla_string.split() ]
print("Idem hladat minimum z cisel: ", cisla_list)
min_cislo=cisla_list[0]
for cislo in cisla_list:
    if cislo > min_cislo:
        cislo_min = cislo
print("Nasiel som minimalne cislo: ", min_cislo)
