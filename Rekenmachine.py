getal1 = float(input("Voer je eerste getal in: "))
# float gebruiken voor getallen die een komma bevatten en grote getallen. Voor kleinere getallen gebruiken we integer
bewerking = input("Welke bewerking wenst je uit te voeren? ")
getal2 = float(input("Voer een tweede getal in: "))

if bewerking == "+":
    print(getal1 + getal2)
elif bewerking == "-":
    print(getal1 - getal2)
elif bewerking == "*":
    print(getal1 * getal2)
elif bewerking == "/":
    print(getal1 / getal2)
# if / elif  / else afsluiten met dubbele punt // inspringen dmv tab
