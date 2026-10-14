# 30 if statements, no directions without instructions


# silver knight path

print( )
print("--------------------------------------------------------NEW-GAME------------------------------------------------------------")
print( )
print("The land is at WAR!\nThe dragons are invading the land from the north, the legion of dark warlocks are advancing on the west")
print("You are faced with a decision, join the silver knights in their efforts in the north, or join the red wizards in the west")
print( )
occupation = input("A. sliver knights\nB. red wizards\n: ")
if occupation == "A":
    print( )
    print("You march north with the silver knights, you are equipped with armor and a sword.")
    print("they teach you combat stretegies and how to use a sword.")
    print("You are headed toward the cavernous mountain where the dragons main forces are")
    print("The knights will raid the cave and try to gain information about the dragons strategies.")
    print( )
    decision_1 = input("Do you advance with the elite squadron of the silver knights to the cave,\nor do you stay back and pull security for the elite forces\n \nA. advance\nB. stay back\n: ")
    if decision_1 == "B":
        print( )
        print("The dragons ambush your scurity squad and because you lack the strength of the elite squadron you fight valiently but PERISH")
    if decision_1 == "A":
        print( )
        print("You and the elite squadron realize it was a trap and the security squadron was ambushed\n")
        decision_2 = input("The dragons are advancing fast, you can\n \nA. push toward the dragons and fight with the elite squad\nB. reateat into the cave\n: ")
        if decision_2 == "B":
            print( )
            print("You abandon you squad and reteat into the cave. you hear rumbling and see the large frame of the dragon queen")
            print("you try to escape but are engulfed in flames and PERISH")
        if decision_2 == "A":
            print( )
            print("You and the elite squadron push forward. the skill of the elite silver knights are no match for the dragons")
            print("You learn that the caves are mostly abandoned along with the surrounding area.")
            print("You take one last look at the mountain, and you are horrified with what you see.")
            print("Large flames erupt from all the enterances of the cave, you can feel the heat on your face.")
            print("The largest dragon you have ever seen emerges from the cave, it is the powerful dragon queen.")
            print("The leader of the squad yells to reteat, but you see a weak point on its neck that doesnt have scales")
            print("All the other knights are already retreating")
            print( )
            decision_3 = input("A. retreat with the knights\nB. charge toward the dragon\n: ")
            if decision_3 == "B":
                print("You charge toward the dragon, but are smacked by its tail and hit the side of the mountain and PERISH")
            if decision_3 == "A":
                print("")


# red wizard path

if occupation == "B":
    print( )
    print("You learn basic spells from the red wizards. they are very wise and powerful but so are the dark warlocks")
    print("You and the red wiards move west to defend the castle of the Sacred Tree. \nYou learn the red wizards have the ability to extract power from the tree so you must defend it")
    print("You and your forces set up defensive positions on the castle and await attack.")
    print("All of the sudden ten pitch balck sillouhetes appear, like a void of darkness in the daylight")
    print("You see them beginning to cast some kind of spell.")
    print( )
    decision_1 = input("A. wait to attack and hold the formation\nB. break the formation and cast a spell immediately\n:  ")
    if decision_1 == "A":
        print( )
        print("The dark warlocks finish summoning their spell uninterrupted and\nit overpowers the red wizards and vaporizes the castle, you PERISH")
    if decision_1 == "B":
        print( )
        print("Your quickly casted fireball spell broke up the formation of the dark warlocks and broke their spell.")
        print("Left vulnerable, the rest of the red wizards counterattack with all their might.")
        print("After the chaos of the counter attack, the dark warlocks are nowhere to be seen")
        print("Your decisiveness in battle is rewarded, but the fight isnt over.")
        print("The dark warlocks regroup and are now surrounding the castle")
        print( )
        decision_2 = input("A. cast a protection spell around the castle\nB. summon the mighty dwarves\n: ")
        if decision_2 == "A":
            print( )
            print("The dark warlocks advance too quicks and enter the castle before you finish casting the spell")
            print("They destroy the sacred tree, and with less power the red wizards cannot defeat the warlocks")
            print("the warlocks counterattack and while many red wizards escape, you PERISH")
        if decision_2 == "B":
            print( )
            print("You hear wild yelling and cheering. over the hill you see small rapidly moving specks.")
            print("As they come closer you see the mighty dwarves riding capybaras, weilding their battle hammers")
            print("the mighty dwarves rush at the warlocks, with little time to react, the warlocks are overrun.")
            print("The dwarves swing with their disproportianately large hammers and bash the warlocks.")
            print("With one final act of despiration, they set the tree on fire.")
            print("instantly weakened, the wizards and dwarves are forced to retreat.")
            print("You see a weakness in their positions and if you attack it you might turn the tide of the battle.")
            decision_3 = input("A. retreat with the wizards and regroup\nB. attack weakness in formation with ypur most powerful spell\n: ")
            if decision_3 == "B":
                print( )
                print("Your attack is quickly dismanteld in your weakened state, and without the support of the other wizards, you PERISH")
            if decision_3 == "A":
                print( )
                print("You retreat with the rest of the wizards and mighty dwarves, you recieve word that the silver knights were retreating.")
                print("The red wizards plan to regroup with the silver knights and join forces and focus on one front at a time")
                print("After falling back deeper into the kingdom, the wizards and mighty dwarves set up a camp and await the knights.")
                print("At night you all are about to sleep but you see something in the distance. five large figures with glowing purple staffs are approaching.")
                print("You sound the alarm and all the forces awaken. you quickly attack.")
                print( )
                decision_4 = input("A. cast fireball spell\nB. cast thunder bolt spell\n: ")
                if decision_4 == "A":
                    print("The powerful warlocks deflect your fireball spell back at you and you explode and PERISH")
                if decision_4 == "B":
                    print("The warlocks didnt have the time ro react to your spell and you see them stumble")
                    print("All the wizards begin casting fireball spells, if you too cast one it might overpower the warlocks.")
                    print( )
                    decision_4 = input("A. cast a protection spell onto the other forces\nB. cast fireball along with the other wizards\n: ")
                    if decision_4 == "B":
                        print( )
                        print("The warlocks absorb the onslaught of fireball spells and deflect them back, you are vaporized and PERISH")
                    if decision_4 == "A":
                        print( )
                        print("The warlocks deflect the fireballs back to the wizards, but your protection spell mitigates damage to them.")
                        print("The warlocks are advancing and seem to be summoning some kind of creature in the air.")
                        print("You then see that they are conveging the energy from their staffs to summon a glowing purple serpent in the air.")
                        print("It begins cutting through the air right towards you. The red wizards begin summoning a creature of their own.")
                        print("They sommon a large red falcon made of pure magical energy, it begins flying toward the serpent.")
                        print( )
                        decision_5 = input("A. add your own magical energy to the falcon to try to strengthen it\nB. command the mighty dwarves to flank the warlocks\n: ")
                        if decision_5 == "A":
                            print("You lakc experience compared to the other wizards and your addition of magic backfires and the falcon turns into a small magical pigeon.")
                            print("Without the powerful falcon, the serpent ignores the magical pigeon and blasts a powerful purple beam, you PERISH")
                        

