from pykkar import *

create_world("""
########
#      #
#      #
#  ^   #
#      #
#      #
########
""")

# eeldame, et robot alustab alati näoga põhjasuunas

# liigu põhjaseinani
while not is_wall():
    step()

# pööra läänesuunda
right()
right()
right()

# liigu lääneseinani
while not is_wall():
    step()

# pööra lõunasuunda
right()
right()
right()

# välimine tsükkel käib üle veergude (kaks veergu korraga, üks allaminnes,
# koos värvimisega ja teine üles tulles, ilma värvimiseta)
while True:

    # allaminek ja värvimine
    paint()
    while not is_wall():
        step()
        paint()

    # liigu järgmisele veerule (kui võimalik)
    right()
    right()
    right()

    if is_wall():
        # rohkem veerge pole
        break

    # kui jõudsime siia, siis on järelikult veel veerge
    step()
    # pööra nina põhjasuunda
    right()
    right()
    right()

    # liigu üles
    while not is_wall():
        step()

    # proovime liikuda järgmisele (värvitavale) veerule
    right()
    if is_wall():
        # pole rohkem veerge
        break

    step()
    # pöörame õigesse suunda
    right()
exitonclick()