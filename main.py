# Created by Michael Buyanin.

import random

def initialize_classes():
    # Some champions fit under multiple categories. I used personal experience and tried to place each champion in their STRONGEST position. For instance, while tank malphite exists, in ARAM burst malphite is a lot stronger and a lot more popular.

    # Controllers are people that primarily focus on ccing in an aram match.
    controller = ["Fiddlesticks", "Kennen", "Bard", "Blitzcrank", "Rakan", "Thresh", "Twisted Fate", "Veigar", "Amumu", "Leona", "Rell", "Renata Glasc", "Morgana"]

    # Enchanters are usually there to either buff a team in general, pocket someone to carry, or heal a team.
    enchanter = ["Janna", "Karma", "Lulu", "Nami", "Seraphine", "Sona", "Soraka", "Taric", "Yuumi", "Ivern"]

    # Fighters are not tanky enough to be classified as tanks, and they do a decent amount of damage
    fighter = ["Gnar", "Graves", "Camille", "Hecarim", "Jarvan IV", "Lee Sin", "Olaf", "Pantheon", "Rek'Sai", "Renekton", "Vi", "Warwick", "Wukong", "Xin Zhao", "Aatrox", "Darius", "Garen", "Illaoi", "Mordekaiser", "Nasus", "Sett", "Trundle", "Udyr", "Urgot", "Yorick", "Sylas", "Viego", "Irelia", "Gwen", "Kled", "Riven", ]
    # For Graves, since his life steal is so strong I decided to classify him as a fighter. Should this ever be nerfed, he may be moved to the slayer position.
    # For Irelia and Gwen, they both play in a way that can be described as a fighter playstyle or a slayer playstyle. I have decided to place them in fighter; however, should it feel awkward in terms of team composition, they may be moved to the slayer position.

    # Mages are champions that rely on utilizing their abilities to do a large amount of damage. This group primarily includes burst mages and battle mages.
    mage = ["Teemo", "Zilean", "Heimerdinger", "Neeko", "Zyra", "Anivia", "Aurelion Sol", "Cassiopeia", "Karthus", "Malzahar", "Rumble", "Ryze", "Swain", "Taliyah", "Viktor", "Vladimir", "Ahri", "Annie", "Brand", "Lissandra", "Orianna", "Syndra", "Vex", "Malphite"]
    # Zilean can be classified as either a mage or an enchanter. I placed him here because I feel that most Zileans are built to be a mage.
    # Anivia and Neeko can both be classified as a controller due to their ultimates. I placed them here; however, it is up to user discretion.

    # Poke mages so extremely strong in ARAM that I decided to classify them in their own tier. These mages utilize poke at long distances to do a large amount of damage.
    poke_mage = ["Shyvana", "Jayce", "Lux", "Varus", "Vel'Koz", "Xerath", "Ziggs", "Nidalee", "Ashe", "Kai'Sa", "Ezreal", "Corki", "Kog'Maw", "Zoe", "Lillia", "Maokai"]
    # Lillia is an interesting champion. She can be classified as a poke mage (e), fighter (q w and speed), or controller (ultimate). For now I decided to place her here since her e can do a lot of damage late game; however, this is up to user discretion.

    # Marksmen typically classify those who rely on autoattacking to do majority of their damage.
    marksman = ["Azir", "Kayle", "Quinn", "Jhin", "Senna", "Akshan", "Aphelios", "Caitlyn", "Draven", "Jinx", "Kalista", "Kindred", "Lucian", "Miss Fortune", "Samira", "Tristana", "Twitch", "Vayne", "Zeri", "Xayah"] 
    # Vayne possibly move to fighter? She plays more like a fighter than a marksman. Similar for Samira
    # AP Miss Fortune in my eyes around the same power as AD Lethality Miss Fortune. While AP has more poke, AD in general does more damage in a team fight. As such I believe it is fine that MF is classified as a Marksman since she can be flexed. If AP becomes too strong in the future, move her to Mage/Poke Mage.

    # Slayers emcompass assassins and skirmishers. These champions generally do more damage and are less tanky than a fighter.
    slayer = ["Pyke", "Elise", "Rengar", "LeBlanc", "Sivir", "Akali", "Ekko", "Diana", "Evelynn", "Fizz", "Kassadin", "Katarina", "Kha'Zix", "Nocturne", "Qiyana", "Shaco", "Talon", "Yone", "Zed", "Fiora", "Jax", "Kayn", "Master Yi", "Gangplank", "Tryndamere", "Yasuo"]
    # I placed Sivir here because her lethality build does not really feel like a marksmen build. As such I moved her here. Caitlyn would also be moved here if her lethality build was more popular.

    # Tanks are meatshields that generally have a lot of hp or resistances and are capable of withstanding a large amount of damage.
    tank = ["Cho'Gath", "Singed", "Skarner", "Volibear", "Dr. Mundo", "Alistar", "Gragas", "Nautilus", "Nunu & Willump", "Ornn", "Rammus", "Sejuani", "Sion", "Zac", "Braum", "Galio", "Poppy", "Shen", "Tahm Kench"]
    # Nunu & Willump is kinda in the middle of a tank or a mage depending on their build. I've placed them in Tank; however, it is up to user discretion.

    return controller, enchanter, fighter, mage, poke_mage, marksman, slayer, tank

def initialize_sides():
    blue_side = {"Controllers" : [], "Enchanters": [], "Fighters" : [], "Mages" : [], "Poke Mages" : [], "Marksmen" : [], "Slayers" : [], "Tanks" : []}
    red_side =  {"Controllers" : [], "Enchanters": [], "Fighters" : [], "Mages" : [], "Poke Mages" : [], "Marksmen" : [], "Slayers" : [], "Tanks" : []}
    return blue_side, red_side

def number_of_classes(mirror, class_c, class_e, class_f, class_m, class_p, class_ma, class_s, class_t):

    # Possible Breakdowns:
        # 2 Tanks 1 Controller 2 Enchanter 2 Fighters 3 Mages 1 Poke Mage 2 Marksmen 2 Slayers
        # 2 Tanks 2 Controller 1 Enchanter 2 Fighters 3 Mages 1 Poke Mage 2 Marksmen 2 Slayers
        # 2 Tanks 1 Controller 1 Enchanter 3 Fighters 3 Mages 1 Poke Mage 3 Marksmen 1 Slayers
        # 2 Tanks 2 Controller 2 Enchanter 2 Fighters 2 Mages 1 Poke Mage 2 Marksmen 2 Slayers

    val = input("Default composition composes of 2 controllers, 2 enchanters, 2 fighters, 2 mages, 1 poke mage, 2 marksmen, 2 slayers, and 2 tanks.\nWould you like to customize the team composition? (Y/N): ")
    if val.lower() == 'n':
        return {"Controllers" : 2, "Enchanters": 2, "Fighters" : 2, "Mages" : 2, "Poke Mages" : 1, "Marksmen" : 2, "Slayers" : 2, "Tanks" : 2}
    elif val.lower() == 'y':
        print("Please be aware that it is recommended that you have the sum of all options add up to AT LEAST 15.")
        control = input("Insert the number of controllers: ")
        enchant = input("Insert the number of enchanters: ")
        fight = input("Insert the number of fighters: ")
        mage = input("Insert the number of mages: ")
        poke = input("Insert the number of poke mages: ")
        marksmen = input("Insert the number of marksmen: ")
        slayer = input("Insert the number of slayers (Assassins/Skirmishers): ")
        tank = input("Insert the number of tanks: ")

        if not control.isdigit() or not enchant.isdigit() or not fight.isdigit() or not mage.isdigit() or not poke.isdigit() or not marksmen.isdigit() or not slayer.isdigit() or not tank.isdigit():
            print("[ERROR] One of the types returned a value that is not an int. Please try again.")
            return {}
        else:
            if not mirror and (int(control) > len(class_c)/2 or int(enchant) > len(class_e)/2 or int(fight) > len(class_f)/2 or int(mage) > len(class_m)/2 or int(poke) > len(class_p)/2 or int(marksmen) > len(class_ma)/2 or int(slayer) > len(class_s)/2 or int(tank) > len(class_t)/2):
                print("[ERROR] The number of selections for a certain class per team covers more than half the roster of that class AND you have selected no mirror matchups. Please try again.")
                return {}
            if int(control) + int(enchant) + int(fight) + int(mage) + int(poke) + int(marksmen) + int(slayer) + int(tank) < 15:
                print("[WARNING] All classes do not add up to at least 15. Be aware that this is below the recommended amount of picks for ARAM.")
            else:
                return {"Controllers" : int(control), "Enchanters": int(enchant), "Fighters" : int(fight), "Mages" : int(mage), "Poke Mages" : int(poke), "Marksmen" : int(marksmen), "Slayers" : int(slayer), "Tanks" : int(tank)}
    else:
        print("[ERROR] Input not registered, please try again.")
        return {}

def selection_process(blue_side, red_side, mirror, controller, enchanter, fighter, mage, poke_mage, marksman, slayer, tank, team_composition):
    blue_side["Controllers"] = random.sample(controller, team_composition["Controllers"])
    blue_side["Enchanters"] = random.sample(enchanter, team_composition["Enchanters"])
    blue_side["Fighters"] = random.sample(fighter, team_composition["Fighters"])
    blue_side["Mages"] = random.sample(mage, team_composition["Mages"])
    blue_side["Poke Mages"] = random.sample(poke_mage, team_composition["Poke Mages"])
    blue_side["Marksmen"] = random.sample(marksman, team_composition["Marksmen"])
    blue_side["Slayers"] = random.sample(slayer, team_composition["Slayers"])
    blue_side["Tanks"] = random.sample(tank, team_composition["Tanks"])

    # This removes the already selected champions from the pool.
    if not mirror:
        for y in blue_side:
            for x in blue_side[y]:
                if x in controller:
                    controller.remove(x)
                elif x in enchanter:
                    enchanter.remove(x)
                elif x in fighter:
                    fighter.remove(x)
                elif x in mage:
                    mage.remove(x)
                elif x in poke_mage:
                    poke_mage.remove(x)
                elif x in marksman:
                    marksman.remove(x)
                elif x in slayer:
                    slayer.remove(x)
                else:
                    tank.remove(x)

    red_side["Controllers"] = random.sample(controller, team_composition["Controllers"])
    red_side["Enchanters"] = random.sample(enchanter, team_composition["Enchanters"])
    red_side["Fighters"] = random.sample(fighter, team_composition["Fighters"])
    red_side["Mages"] = random.sample(mage, team_composition["Mages"])
    red_side["Poke Mages"] = random.sample(poke_mage, team_composition["Poke Mages"])
    red_side["Marksmen"] = random.sample(marksman, team_composition["Marksmen"])
    red_side["Slayers"] = random.sample(slayer, team_composition["Slayers"])
    red_side["Tanks"] = random.sample(tank, team_composition["Tanks"])

def display(blue_side, red_side):
    blue_composition = "```~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n/TEAM ONE/\n"
    for y in blue_side:
        for x in blue_side[y]:
            blue_composition += x + "\n"

    red_composition = ""
    for y in red_side:
        for x in red_side[y]:
            red_composition += x + "\n"
    print(blue_composition + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n/TEAM TWO/\n" + red_composition + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```")

def main():
    class_controller, class_enchanter, class_fighter, class_mage, class_poke_mage, class_marksman, class_slayer, class_tank = initialize_classes()
    blue_team, red_team = initialize_sides()
    while True:
        mirror_string = input("Would you like mirrored matchups? (Y/N): ")
        if mirror_string.lower() == 'y':
            mirror_true = True
            break
        elif mirror_string.lower() == 'n':
            mirror_true = False
            break
        else:
            print("[ERROR] Please try again.")

    composition = {}
    while not bool(composition):
        composition = number_of_classes(mirror_true, class_controller, class_enchanter, class_fighter, class_mage, class_poke_mage, class_marksman, class_slayer, class_tank)
    
    selection_process(blue_team, red_team, mirror_true, class_controller, class_enchanter, class_fighter, class_mage, class_poke_mage, class_marksman, class_slayer, class_tank, composition)
    display(blue_team, red_team)
    
if __name__ == "__main__":
    main()