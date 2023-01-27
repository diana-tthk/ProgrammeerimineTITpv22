from pykkar import *

def left():
    right()
    right()
    right()

def move_to_wall():
    while not is_wall():
        step()

def move_to_corner():
    move_to_wall()
    left()
    move_to_wall()


create_world("""
########
#      #
#      #
#  ^   #
#      #
#      #
########
""")

move_to_corner()
left()

# välimine tsükkel käib üle veergude (kaks veergu korraga, üks allaminnes,
# koos värvimisega ja teine üles tulles, ilma värvimiseta)
while True:

    # allaminek ja värvimine
    paint()
    while not is_wall():
        step()
        paint()

    # liigu järgmisele veerule (kui võimalik)
    left()
    if is_wall():
        # rohkem veerge pole
        break

    # kui jõudsime siia, siis on järelikult veel veerge
    step()
    # pööra nina põhjasuunda
    left()

    # liigu üles
    move_to_wall()

    # proovime liikuda järgmisele (värvitavale) veerule
    right()
    if is_wall():
        # pole rohkem veerge
        break

    step()
    # pöörame õigesse suunda
    right()
exitonclick()
