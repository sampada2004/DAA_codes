#O(n^2)
def stable_match(men_prefs, women_prefs):
    # Initialize all men and women as free
    free_men = list(men_prefs.keys())
    engagements = {}
    # While there are free men
    while free_men:
        man = free_men.pop(0)
        # Get the preferences of the man
        man_pref = men_prefs[man]
        # Propose to the first woman in the man's preference list
        woman = man_pref.pop(0)
        fiance = engagements.get(woman)
        # If the woman is not engaged, engage her with the current man
        if not fiance:
            engagements[woman] = man
        else:
            # If the woman prefers the current man over her fiance
            if women_prefs[woman].index(man) < women_prefs[woman].index(fiance):
                engagements[woman] = man
                free_men.append(fiance)
            else:
                # The woman rejects the proposal
                free_men.append(man)
    return engagements

# Function to take user input for preferences
def take_input():
    men_prefs = {}
    women_prefs = {}
    
    # Input for men's preferences
    num_men = int(input("Enter the number of men: "))
    for i in range(1, num_men + 1):
        man = input(f"Enter name of man {i}: ")
        prefs = input(f"Enter preferences for {man} separated by spaces: ").split()
        men_prefs[man] = prefs
    
    # Input for women's preferences
    num_women = int(input("Enter the number of women: "))
    for i in range(1, num_women + 1):
        woman = input(f"Enter name of woman {i}: ")
        prefs = input(f"Enter preferences for {woman} separated by spaces: ").split()
        women_prefs[woman] = prefs
    
    return men_prefs, women_prefs

# Take input from the user
men_prefs, women_prefs = take_input()

# Perform stable matching
stable_matches = stable_match(men_prefs, women_prefs)

# Output the stable matches
print("\nStable Marriages:")
for woman, man in stable_matches.items():
    print(f"{man} is engaged to {woman}")
