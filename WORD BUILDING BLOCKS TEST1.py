import pyperclip as pc

def printLine():
    print("---------------------------------")

no=input("nom: ")
printLine()
ad=str(input("adresse: "))
printLine()
da=str(input("date: "))
printLine()
re=input("revocation? (oui/non): ")
printLine()
noLi1=input("nom du liquidateur: ")
printLine()
adLi1=str(input("adresse du lquidateur: "))
printLine()

deLi=input("deuxieme liquidateur? (oui/non): ")
printLine()
if deLi=="oui":
    deLi2=str(input("delais de deces liquidateur: "))
    printLine()
    noLi2=input("nom liquidateur 2: ")
    printLine()
    adLi2=str(input("adresse liquidateur 2: "))
else:
    pass

printLine()

poLi=input("pouvoir de liquidateur? (oui/non): ")
printLine()
if poLi=="oui":
    moPaLi=str(input("montant paiement du liquidateur: "))
else:
    pass

printLine()

lePa=input("legataire particullier? (oui/non): ")
printLine()
if lePa=="oui":
    noLe1=input("nom du legataire 1: ")
    biLe1=str(input("biens legues a legataire 1: "))
    printLine()
    noLe2=input("nom du legataire 2: ")
    biLe2=str(input("biens legues a legataire 2: "))
else:
    pass

printLine()

leUn=input("legataire universel? (oui/non): ")
printLine()
if leUn=="oui":
    noLeUn=input("nom du legataire universel: ")
else:
    pass

printLine()
noTe1=input("nom du temoin 1: ")
noTe2=input("nom du temoin 2: ")
printLine()
ocTe1=input("emploi du temoin 1: ")
ocTe2=input("emploi du temoin 2: ")
printLine()
adTe1=str(input("adresse du temoin 1: "))
adTe2=str(input("adresse du temoin 2: "))
printLine()

create_file = open("testament_"+no+".txt", "a")
create_file.write("TESTAMENT:\n\nDE: "+no+"\nDate: "+da+"\n\nTestament\n\nCeci est le testament du (de la) soussigné(e), "+no+" ,domicilié(e) et résidant au"+adLi1+", province de Quebec, fait ce "+da+".")

if re=="oui":
    create_file.write("\n\n\nJE RÉVOQUE tous les testaments, codicilles et dispositions testamentaires que j’ai faits antérieurement au présent testament.")
else:
    pass

create_file.write("\n\nJE NOMME "+noLi1+", domicilié et résidant au adresse du liquidateur province de Québec, à titre de liquidateur de ma succession.")

if deLi=="oui":
    create_file.write("\n\nCEPENDANT, si le liquidateur ainsi désigné devait refuser d’agir, décéder avant moi ou décéder dans un délai de "+deLi2+" jours après mon décès, ALORS JE NOMME "+noLi2+", domicilié et résidant au "+adLi2+", province de Québec, pour agir comme remplaçant.")
else:
    pass

if poLi=="oui":
    create_file.write("\n\nPOUVOIRS. Le liquidateur est chargé de voir à l’exécution de mon testament et à la liquidation de ma succession. Il est par les présentes investi de tous les pouvoirs requis pour ce faire. Il aura droit au remboursement des dépenses qu’il encourra pour l’exercice de cette charge et à une rémunération globale de "+moPaLi+"$.")
else:
    pass

create_file.write("\n\nJE CHARGE mon liquidateur de payer et d’acquitter toutes mes dettes, dépenses funéraires et testamentaires, mes droits ou impôts sur les successions, le cas échéant, et toutes les dépenses normales qui en découlent et ce aussitôt qu’il conviendra de le faire après mon décès.")

if lePa=="oui":
    create_file.write("JE FAIS les legs suivants, à titre particulier :\n\nÀ "+noLe1+", je lègue: "+biLe1+"\n\nÀ "+noLe2+", je lègue: "+biLe2)
else:
    pass

if leUn=="oui":
    create_file.write("\n\nJ'INSTITUE "+noLeUn+" légataire universel résiduaire de l’ensemble de mes biens.\nOU")
else:
    pass

create_file.write("\n\n\nEN FOI DE QUOI j’ai signé à la date mentionnée au début des présentes.\n\n\n_________________________\n(Signature)\n\n\nCette page a été signée et chacune des pages précédentes a été paraphée par le (la) testateur (trice) qui présente et déclare le présent document comme étant son testament en présence de chacun de nous réunis au même moment et qui, à sa demande et en sa présence et en la présence l’un de l’autre, avons signé ci-après comme témoins et paraphé chacune des pages précédentes.\n\n\nNom "+noTe1+" Nom "+noTe2+"\n\nOccupation "+ocTe1+" Occupation "+ocTe2+"\n\nAdresse "+adTe1+" Adresse "+adTe2+"\n\n\n_________________________\n"+noTe1+"\n_________________________\n"+noTe2)
create_file.close()