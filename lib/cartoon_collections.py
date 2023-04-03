def roll_call_dwarves(d_names):
    i=1
    for name in d_names:
        print(f'{i}. {name}')
        i+=1

def summon_captain_planet(calls):
    return [f'{el.capitalize()}!' for el in calls]

def long_planeteer_calls(calls):
    for el in calls:
        if (len(el) > 4):
            return True
    return False

def find_the_cheese(list): ##cheddar, gouda, camembert
    for el in list:
        if 'gouda' in el:
            return 'gouda'
        elif 'cheddar' in el:
            return 'cheddar'
        elif 'camembert' in el:
            return 'camembert'
    return None
