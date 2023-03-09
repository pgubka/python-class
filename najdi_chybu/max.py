print("Zadaj niekolko celych cisel oddelenych medzerou a ja najdem najvacsie z nich; ")
cisla_string = input()
cisla_list = [ int(a) for a in cisla_string.split() ]
print("Idem hladat maximum z cisel: ", cisla_list)
max_cislo=cisla_list[0]
for cislo in cisla_list:
    if cislo == max_cislo:
        cislo_max = cislo
print("Nasiel som maximalne cislo: ", cislo)
