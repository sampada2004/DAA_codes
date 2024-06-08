def gale_shapley(men_pref, women_pref):
    n = len(men_pref)
    men_engaged = {}
    women_engaged = {}
    free_men = set(men_pref.keys())
    while free_men:
        man = free_men.pop()
        preferences = men_pref[man]
        for woman in preferences:
            if woman not in women_engaged:
                men_engaged[man] = woman
                women_engaged[woman] = man
                break
            else:
                current_partner = women_engaged[woman]
                current_partner_pref = women_pref[woman]
                if current_partner_pref.index(current_partner) > current_partner_pref.index(man):
                    men_engaged[man] = woman
                    women_engaged[woman] = man
                    free_men.add(current_partner)
                    #free_men.remove(man)  # Remove man from free men as he's engaged now
                    break
    
    print("Final men engaged:", men_engaged)
    print("Final women engaged:", women_engaged)
    
    return men_engaged

men_pref = {0: [1, 2,0], 1: [1, 0, 2], 2: [0, 1, 2]}
women_pref = {0: [1, 0, 2], 1: [1, 0, 2], 2: [0, 1, 2]}

print(gale_shapley(men_pref, women_pref))
