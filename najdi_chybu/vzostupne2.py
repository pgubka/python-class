print("Zadaj niekolko celych cisel oddelenych medzerou a ja ich zoradim vzostupme: ")
cisla_string = input()
cisla_list = [ int(a) for a in cisla_string.split() ]
print("Idem usporiadat cisla: ", cisla_list)
usporiadane_cisla = []
min_cislo=cisla_list[0]
dlzka_listu=len(cisla_list)
for i in range(dlzka_listu):
    for cislo in cisla_list:
        if cislo > min_cislo:
            min_cislo = cislo
    usporiadane_cisla.append(min_cislo)
    print("Min cislo", min_cislo)
    cisla_list.remove(min_cislo)
print("Usporiadane cisla: ", usporiadane_cisla)
