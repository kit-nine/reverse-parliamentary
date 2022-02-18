import random

# FIRST GENERATION OF PEOPLE
#    these people will randomly choose a legislature between all 10 example parties
#    then the code will calculate who won and have the people vote on the executive branch from the other side of the political spectrum.
#    the code will finally print the parties who won each house.

# SECOND GEN
#    will vote like or against their parents 3/4 of the time, the other 1/4 will vote randomly. this will be determined by a boolean decision to see if the relationship with their parents was good or not.
#    same things are printed out

# THIRD GEN
#    these people will have the same decision as second gen, but it will depend on whether their grandparents were bad too. if their grandparents were bad, then there is a 2/3 chance that their parents will have been bad too.
#    then the boolean of whether they are voting the same or the opposite of their parents
#    same things are printed out

# LAWMAKING
#    the legislative makes a law aligning with their ideals, left or right
#    executive decides whether that law is close enough to their ideals, left or right
#    if vetoed, legislative decides whether to override or not
#    if the law has been vetoed and not overridden then legislative makes a new law, a little further from their own ideals
#    if the law has been either not vetoed or vetoed and then overridden, it goes to the judicial branch, who have a similar system to that of the executive, except their side is absolute centrist
#    if the law is constitutional, lawmaking ends
#    if it is unconstitutional, legislative has to make a new law

# ADDITIONAL NOTES - may or may not actually implement
#   - a set amount of laws per generation - manual input or a set amount can be built in
#   - go through entire legislative process rather than just simple voting
#   - full political compass; left-right and libertarian-authoritarian
#   - get rid of global variables

# IMPLEMENTED ADDITIONAL NOTES
#   - more_gens() will have parameter gens, set it equal to the number of gens to test minus one - manual input
#   - the parents will survive 2 generations.
#   - the parents will have a 2 out of 3 chance of voting the same every generation.
#   - otherwise they will randomly choose every time.
#   - media influence can skew the voting by a certain amount - manual input
#   - law creation is skewed toward the position of the legislative, not just random from their side

# IMPLEMENTING CURRENTLY
#   - another voting session instead of a randint for the tiebreaker

# media influence custom random function with skew
def skew(influence, range1, range2):    # influence should be a float between -1 and 1, including 0; type should be a string, either "bool" or "int", range1 and range2 should form the range that should be randomly picked from
    skew_int = random.randint(range1, range2)   # gets a random number in the range
    if influence > 0 and skew_int != range2:    # if the influence leans right
        skew_int += influence * (range2 - 1)    # multiply the influence times one less than the end of the range
    elif influence < 0 and skew_int != range1:  # otherwise, if the influence leans left
        skew_int += influence * (range1 + 1)    # multiply the influence times one more than the start of the range
    if skew_int < range1:                       # if this number is less than the smallest number in the range
        skew_int = range1                       # it becomes the smallest number in the range
    elif skew_int > range2:                     # otherwise, if this number is more than the largest number in the range
        skew_int = range2                       # it becomes the largest number in the range
    skew_int = int(skew_int)                    # rounds the float down
    return skew_int

people_not_voted = 100
leg_votes = []
leg_counts = []
exe_votes = []
exe_counts = []
gen_1_wins = []
new_leg_votes = []
new_exe_votes = []
gen_previous_parents = []
gen_parents = []
vetoed = False
current_gen = 0
leg_max_val_index_1 = []
exe_max_val_index_1 = []
leg_max_val_index_2 = []
exe_max_val_index_2 = []
leg_max_val_index_3 = []
exe_max_val_index_3 = []

    # GEN 1
def gen_1():
    global people_not_voted
    global exe_votes
    global leg_votes
    global gen_parents
    global gen_previous_parents
    global leg_max_val_index_1
    global exe_max_val_index_1
    # this makes the people vote for the legislative branch
    while people_not_voted > 0:                     # while any amount of people havent voted
        choice = skew(influence, 0, 9)       # have them vote 0-9
        leg_votes.append(choice)                    # append their choice to the votes list
        people_not_voted -= 1                       # subtract one person because they just voted
    # this finds out how many people voted for each option
    for i in range(0, 10):           # for each option
        count = leg_votes.count(i)  # see how many people voted for that option
        leg_counts.append(count)    # append that to the list
    leg_max_val = max(leg_counts)   # finds the one they voted for the most
    leg_max_val_index_1 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]   # this indexes the maximum value(s), which i use to find what the largest vote was for
    # this narrows it down to one winner if there's a tie
    while len(leg_max_val_index_1) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(leg_max_val_index_1)-1)
            tiebreaker.append(tie_vote)
        for i in range(0, len(leg_max_val_index_1)-1):
            tie_counts.append(tiebreaker.count(i))
        leg_max_val = max(tie_counts)
        leg_max_val_index_1 = [i for i in range(len(tie_counts)) if tie_counts[i] == leg_max_val]
        tiebreaker.clear()
        tie_counts.clear()
    people_not_voted = 100      # resets the people for the next voting session
    # this makes the people vote for the executive branch
    while people_not_voted > 0:                         # while any amount of people havent voted
        choice = skew(influence, 0, 4)           # the people vote for the executive 0 through 4
        if 0 < leg_max_val_index_1[0] < 5:              # if the legislative vote is 0 through 4
            choice += 5                                 # the people add 5 to their votes, making them actually vote for the executive 5 through 9
        exe_votes.append(choice)                        # appends their choice to the votes list
        people_not_voted -= 1                           # subtract one person because they just voted
    # finds out how many people voted for each option without pesky '0's from the other half of the spectrum
    if 0 <= leg_max_val_index_1[0] <= 4:    # if the legislative vote is 0 through 4
        for i in range(5, 10):              # for each option (5 through 9)
            count = exe_votes.count(i)      # see how many people voted for that option
            exe_counts.append(count)        # append that to the list
    else:                                   # if the legislative vote isn't 0 through 4
        for i in range(0, 5):               # for each option (0 through 4)
            count = exe_votes.count(i)      # see how many people voted for that option
            exe_counts.append(count)        # append that to the list
    exe_max_val = max(exe_counts)           # finds the one they voted for most
    exe_max_val_index_1 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]   # this indexes the maximum value(s), which i use to find what the largest vote was for
    # this narrows it down to one winner if there's a tie
    tiebreaker = []
    tie_counts = []
    while len(exe_max_val_index_1) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(exe_max_val_index_1)-1)
            tiebreaker.append(tie_vote)
        for i in range(0, len(exe_max_val_index_1)-1):
            tie_counts.append(tiebreaker.count(i))
        exe_max_val = max(tie_counts)
        exe_max_val_index_1 = [i for i in range(len(tie_counts)) if tie_counts[i] == exe_max_val]
        tiebreaker.clear()
        tie_counts.clear()
    # since the right side of the spectrum starts with 5, using the index doesn't work unless the code adds the 5 in here to correct it
    if 0 <= leg_max_val_index_1[0] <= 4:    # if the legislative vote is 0 through 4
        exe_max_val_index_1[0] += 5         # add 5 to the index
    leg_counts.clear()
    exe_counts.clear()
    people_not_voted = 100
    return leg_max_val_index_1, exe_max_val_index_1

    # GEN 2
def gen_2():
    global people_not_voted
    global exe_votes
    global leg_votes
    global gen_parents
    global gen_previous_parents
    global leg_max_val_index_2
    global exe_max_val_index_2
    normalities = []
    researchers = []
    # since gen_2() votes differently, a for loop was simpler so i could be used for indexing
    for i in range(people_not_voted):           # for the number of people who havent yet voted
        normality = random.randint(0,3)         # determines whether the person will vote based on their parents or not
        if normality == 0 or normality == 1 or normality == 2:  # if the person will vote based on their parents
            parent_score = random.randint(0, 1) # determines whether their relationship with their parent is good or not
            x = leg_votes[i]                    # finds the parent's vote
            if parent_score == 0:               # if the parent relationship was bad,
                choice = abs(x - 9)             # the choice is reversed of what the parent chose 
            else:                               # if the parent relationship was good,
                choice = x                      # the choice is what the parent chose
        else:                                   # if the person will not vote based on their parents
            choice = skew(influence, 0, 9)   # have them vote 0-9
            parent_score = random.randint(0, 1) # determines whether their relationship with their parent is good or not (makes indexing correct)
        normalities.append(normality)           # fills this list with normality scores
        new_leg_votes.append(choice)            # makes a list of the choices without resetting leg_votes
        gen_parents.append(parent_score)        # appends the parent relationship score for reuse

    # the parents are still alive so they also vote
    for i in range(len(gen_parents)):                   # for each parent
        research = random.randint(0,2)                  # determine whether they research their choice or just go with what they did last year
        if research == 0 or research == 1:              # if they will not research
            parent_choice = leg_votes[i]                # they vote for the same thing as they voted for last year
        else:                                           # otherwise if they will research
            parent_choice = skew(influence, 0, 9)       # have them vote 0-9
        new_leg_votes.append(parent_choice)             # appends their choice to new_leg_votes
        researchers.append(research)                    # fills this list with research scores
    leg_votes.clear()                                   # clears the old votes away
    for i in new_leg_votes:                             # for each item in the new votes list
        leg_votes.append(i)                             # appends it to the votes list

    for i in range(0, 9):
        count = leg_votes.count(i)
        leg_counts.append(count)

    leg_max_val = max(leg_counts)
    leg_max_val_index_2 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]

    while len(leg_max_val_index_2) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(leg_max_val_index_2)-1)
            tiebreaker.append(tie_vote)
        for i in range(0, len(leg_max_val_index_2)-1):
            tie_counts.append(tiebreaker.count(i))
        leg_max_val = max(tie_counts)
        leg_max_val_index_2 = [i for i in range(len(tie_counts)) if tie_counts[i] == leg_max_val]
        tiebreaker.clear()
        tie_counts.clear()

    people_not_voted = 100

    if 0 <= leg_max_val_index_2[0] <= 4:                # if the legislative is 0 through 4
        for i in range(people_not_voted):               # for the number of people who havent yet voted
            if normalities[i] == 0 or normalities[i] == 1 or normalities[i] == 2:   # if the person will vote based on their parents
                x = exe_votes[i]                        # finds the parent's vote
                if gen_parents[i] == 0:                   # if the parent relationship was bad,
                    if x >= 5:                          # if the parent vote was greater than 5
                        choice = abs(x - 14)            # choice is |x - 14| (|5 - 14| = 9, |6 - 14| = 8, |7 - 14| = 7)
                    else:                               # otherwise
                        choice = abs(x - 9)         # choice is opposite of their parents
                else:                                   # if the parent relationship was not bad,
                    choice = x                          # the choice is what the parent chose
            else:                                       # if the person will not vote based on their parents
                choice = skew(influence, 5, 9)   # the person chooses randomly
            new_exe_votes.append(choice)                    # makes a list of the choices without resetting leg_votes
        # the parents are still alive so they also vote
        for i in range(len(gen_parents)):                   # for each parent
            if researchers[i] == 0 or researchers[i] == 1:              # if they will not research
                parent_choice = exe_votes[i]                # they vote for the same thing as they voted for last year
            else:                                           # otherwise
                parent_choice = skew(influence, 5, 9)   # they vote randomly
            new_exe_votes.append(parent_choice)             # appends their choice to new_leg_votes
        exe_votes.clear()                                   # clears the old votes away
        for i in new_exe_votes:                             # for each item in the new votes list
            exe_votes.append(i)                             # appends it to the votes list
    else:                                               # if the legislative is not 0 through 4
        for i in range(people_not_voted):               # for the number of people who havent yet voted
            if normalities[i] == 0 or normalities[i] == 1 or normalities[i] == 2:   # if the person will vote based on their parents
                x = exe_votes[i]                        # finds the parent's vote
                if gen_parents[i] == 0:                 # if the parent relationship was bad,
                    if x >= 5:                          # if the parent vote was greater than 5
                        choice = abs(x - 4)             # choice is |x - 14| (|0 - 4| = 4, |1 - 4| = 3, |2 - 4| = 2)
                    else:                               # otherwise
                        choice = x + abs(x - 9)         # choice is opposite of their parents
                else:                                   # if the parent relationship was not bad,
                    choice = x                          # the choice is what the parent chose
            else:                                       # if the person will not vote based on their parents
                choice = skew(influence, 0, 4)  # the person chooses randomly
        new_exe_votes.append(choice)                    # makes a list of the choices without resetting leg_votes
        # the parents are still alive so they also vote
        for i in range(len(gen_parents)):                        # for each parent
            if research == 0 or 1:                          # if they will not research
                parent_choice = exe_votes[i]                # they vote for the same thing as they voted for last year
            else:                                           # otherwise
                parent_choice = skew(influence, 0, 4)   # they vote randomly
            new_exe_votes.append(parent_choice)             # appends their choice to new_leg_votes
        exe_votes.clear()                                   # clears the old votes away
        for i in new_exe_votes:                             # for each item in the new votes list
            exe_votes.append(i)                             # appends it to the votes list

    if 0 <= leg_max_val_index_2[0] <= 4:
        for i in range(5, 10):
            count = exe_votes.count(i)
            exe_counts.append(count)
    else:
        for i in range(0, 5):
            count = exe_votes.count(i)
            exe_counts.append(count)

    exe_max_val = max(exe_counts)
    exe_max_val_index_2 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]

    tiebreaker = []
    tie_counts = []
    while len(exe_max_val_index_2) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(exe_max_val_index_2)-1)
            tiebreaker.append(tie_vote)
        for i in range(0, len(exe_max_val_index_2)-1):
            tie_counts.append(tiebreaker.count(i))
        exe_max_val = max(tie_counts)
        exe_max_val_index_2 = [i for i in range(len(tie_counts)) if tie_counts[i] == exe_max_val]
        tiebreaker.clear()
        tie_counts.clear()

    if 0 <= leg_max_val_index_2[0] <= 4:
        exe_max_val_index_2[0] += 5
    leg_counts.clear()
    exe_counts.clear()
    new_leg_votes.clear()
    new_exe_votes.clear()
    people_not_voted = 100
    return

    # GEN 3
def gen_3():
    global people_not_voted
    global exe_votes
    global leg_votes
    global gen_parents
    global gen_previous_parents
    global leg_max_val_index_3
    global exe_max_val_index_3
    normalities = []
    researchers = []
    # gen_3() also votes a little differently, starting with this for loop that copies gen_parents into gen_previous_parents for the next iteration of gen_3() to work
    for i in gen_parents:               # for each parent
        gen_previous_parents.append(i)  # copies their relationship score into gen_previous_parents
    gen_parents.clear()
    for i in range(people_not_voted):
        normality = random.randint(0,3)
        if normality == 0 or normality == 1 or normality == 2:
            if gen_previous_parents[i] == 0:        # if the grandparents' relationship with the parents was bad
                parent_score = random.randint(0,3)  # the parent score has a 3/4, rather than a 1/2, chance to also have a bad relationship with their kids
            elif gen_previous_parents[i] == 1:      # if the grandparents' relationship with the parents was good
                parent_score = random.randint(2,5)  # the parent score has a 3/4, rather than a 1/2, chance to also have a good relationship with their kids
            x = leg_votes[i]
            if parent_score == 0 or parent_score == 1 or parent_score == 2:
                choice = abs(x - 9)
            elif parent_score == 3 or parent_score == 4 or parent_score == 5:
                choice = x
        else:
            parent_score = 6
            choice = skew(influence, 0, 9)
        normalities.append(normality)
        new_leg_votes.append(choice)
        gen_parents.append(parent_score)

    for i in range(len(gen_parents)):
        research = random.randint(0,2)
        if research == 0 or research == 1:
            parent_choice = leg_votes[i]
        else:
            parent_choice = skew(influence, 0, 9)
        new_leg_votes.append(parent_choice)
        researchers.append(research)
    leg_votes.clear()
    for i in new_leg_votes:
        leg_votes.append(i)
    for i in range(0, 9):
        count = leg_votes.count(i)
        leg_counts.append(count)

    leg_max_val = max(leg_counts)
    global leg_max_val_index_3
    leg_max_val_index_3 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]

    tiebreaker = []
    tie_counts = []
    while len(leg_max_val_index_3) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(exe_max_val_index_3)-1)
            tiebreaker.append(tie_vote)
        for i in range(0, len(exe_max_val_index_3)-1):
            tie_counts.append(tiebreaker.count(i))
        exe_max_val = max(tie_counts)
        exe_max_val_index_3 = [i for i in range(len(tie_counts)) if tie_counts[i] == exe_max_val]
        tiebreaker.clear()
        tie_counts.clear()

    people_not_voted = 100
                
    if 0 <= leg_max_val_index_3[0] <= 4:
        for i in range(people_not_voted):
            x = int(exe_votes[i])
            if gen_parents[i] == 0:
                if x >= 5:
                    choice = abs(x - 14)
                else:
                    choice = x + abs(x - 9)
            elif gen_parents[i] == 1:
                choice = x
            else:
                choice = skew(influence, 5, 9)
            new_exe_votes.append(choice)

        for i in range(len(gen_parents)):
            if researchers[i] == 0 or researchers[i] == 1:
                parent_choice = exe_votes[i]
            else:
                parent_choice = skew(influence, 5, 9)
            new_exe_votes.append(parent_choice)
        exe_votes.clear()
        for i in new_exe_votes:
            exe_votes.append(i)
    else:
        for i in range(people_not_voted):
            x = int(exe_votes[i])
            if gen_parents[i] == 0:
                if x >= 5:
                    choice = abs(x - 4)
                else:
                    choice = x + abs(x - 9)
            elif gen_parents[i] == 1:
                choice = x
            else:
                choice = skew(influence, 0, 4)
            new_exe_votes.append(choice)

        for i in range(len(gen_parents)):
            if researchers[i] == 0 or researchers[i] == 1:
                parent_choice = exe_votes[i]
            else:
                parent_choice = skew(influence, 0, 4)
            new_exe_votes.append(parent_choice)
        exe_votes.clear()
        for i in new_exe_votes:
            exe_votes.append(i)
        gen_parents.clear()

    if 0 <= leg_max_val_index_3[0] <= 4:
        for i in range(5, 10):
            count = exe_votes.count(i)
            exe_counts.append(count)
    else:
        for i in range(0, 5):
            count = exe_votes.count(i)
            exe_counts.append(count)

    exe_max_val = max(exe_counts)
    exe_max_val_index_3 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]

    tiebreaker = []
    tie_counts = []
    while len(exe_max_val_index_3) > 1:
        people_not_voted = 100
        for i in range(people_not_voted):
            tie_vote = skew(influence, 0, len(exe_max_val_index_3)-1)
            if 0 <= leg_max_val_index_3[0] <= 4:
                tiebreaker.append(tie_vote + 5)
        if 0 <= leg_max_val_index_3[0] <= 4:
            for i in range(5, 10):
                tie_counts.append(tiebreaker.count(i))
        else:
            for i in range(0, 5):
                tie_counts.append(tiebreaker.count(i))
        exe_max_val = max(tie_counts)
        exe_max_val_index_3 = [i for i in range(len(tie_counts)) if tie_counts[i] == exe_max_val]

    if 0 <= leg_max_val_index_3[0] <= 4:
        exe_max_val_index_3[0] += 5
    leg_counts.clear()
    exe_counts.clear()
    new_leg_votes.clear()
    new_exe_votes.clear()
    people_not_voted = 100
    return

    # MORE GENS
def more_gens(gens):
    global current_gen
    global generations
    global people_not_voted
    for i in range(gens - 2):
        gen_3()
        current_gen = i + 3
        print("\nGEN",current_gen,":")
        print(leg_max_val_index_3[0],", ",exe_max_val_index_3[0], "\n")
        lawmaking(LEG = leg_max_val_index_3[0], EXE = exe_max_val_index_3[0])
        fail_check()
        generations.append(current_gen)
        people_not_voted = 100

    # LAWMAKING
def lawmaking(LEG, EXE):
    global vetoed
    # functions
    def law_func():
        nonlocal type
        global vetoed
        nonlocal previous_law
        nonlocal continue_current_law
        nonlocal law
        # makes draw_line instead of having both -5 and +5 in the code, gets rid of some repetition
        if type == "A":
            draw_line = -5
        else:
            draw_line = 5
        # makes the law
        if previous_law == 10:              # if there is no previous law
            if type == "A":                 # and if LEG is 0 through 4
                law = skew((LEG-5)/10, 0, 4)    # they make a law that is 0 through 4 
            else:                           # and if LEG is not 0 through 4
                law = skew((LEG-5)/10, 5, 9)    # they make a law that is 5 through 9 
        elif previous_law == 9:             # if the previous law was 9
            law = skew((LEG-5)/10, 5, 8)       # they make a law that is 5 through 8
        elif previous_law == 8:             # if the previous law was 8
            law = skew((LEG-5)/10, 5, 7)       # they make a law that is 5 through 7
        elif previous_law == 7:             # if the previous law was 7
            law = skew((LEG-5)/10, 5, 6)       # they make a law that is 5 through 6
        elif previous_law == 6:             # if the previous law was 6
            law = 5                         # they make a law that is 5
        elif previous_law == 5:             # if the previous law was 5
            law_votes_4 = []                # makes a list for votes
            for i in range(535):            # each person in the legislature
                law_vote_4 = skew((LEG-5)/10, 0, 1)    # votes either 0 or 1
                law_votes_4.append(law_vote_4)  # appends the vote to the list of votes
                if law_votes_4.count(0) > law_votes_4.count(1):   # if there are more votes for 0 than for 1
                    law = 4                 # they make a law that is 4
                else:                       # if there are not more votes for 0 than for 1
                    law = 5                 # they make a law that is 5
                    continue_current_law = False    # and they wont make another law based on this one
        elif previous_law == 4:             # if the previous law was 4
            law_votes_5 = []                # make a list for votes
            for i in range(535):            # each person in the legislature
                law_vote_5 = skew((LEG-5)/10, 0, 1)    # votes either 0 or 1
                law_votes_5.append(law_vote_5)  # appends the vote to the list of votes
                if law_votes_5.count(0) > law_votes_5.count(1):   # if there are more votes for 0 than for 1
                    law = 5                 # they make a law that is 5
                else:                       # if there are not more votes for 0 than for 1
                    law = 4                 # they make a law that is 4
                    continue_current_law = False    # and they wont make another law based on this one
        elif previous_law == 3:             # if the previous law was 3
            law = 4                         # they make a law that is 4
        elif previous_law == 2:             # if the previous law was 2
            law = skew((LEG-5)/10, 3, 4)       # they make a law that is 3 through 4
        elif previous_law == 1:             # if the previous law was 1
            law = skew((LEG-5)/10, 2, 4)       # they make a law that is 2 through 4
        elif previous_law == 0:             # if the previous law was 0
            law = skew((LEG-5)/10, 1, 4)       # they make a law that is 1 through 4
        # decides where EXE draws the line based on their position and draw_line
        exe_line = EXE + draw_line      # EXE position plus or minus 5
        # vetos or passes law based on exe_line
        if type == "A":                                                 # if LEG is 0 through 4
            if law <= exe_line:                                         # and the law is lower than the deciding line
                vetoed = True                                           # sets vetoed = True
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                vetoed = False                                          # sets vetoed = False
        else:                                                           # if LEG is not 0 through 4 (and therefore is 5 through 9)
            if law >= exe_line:                                         # and the law is lower than the deciding line
                vetoed = True                                           # sets vetoed = True
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                vetoed = False                                          # sets vetoed = False
        if vetoed == False:
            print("Law: ", law, "\n", "EXE: ", EXE, "\n", "PASSED") # prints the law, the EXE pos, and that it was passed
        else:
            print("Law: ", law, "\n", "EXE: ", EXE, "\n", "VETOED") # prints the law, the EXE pos, and that it was vetoed
        override()

    def jud_func():
        global constitutional
        nonlocal previous_law
        jud_votes = []                              # judicial votes go here
        for i in range(9):                          # for each judge
            if law == 0 or law == 9:                # if the law is 0 or 9
                jud_vote = random.randint(0,5)      # picks from 0 to 5
                if jud_vote == 0 or jud_vote == 1 or jud_vote == 2 or jud_vote == 3 or jud_vote == 4:   # if it's 0, 1, 2, 3, or 4, giving a 5/6 chance,
                    jud_votes.append(0)             # vote is unconstitutional
                else:                               # if it isn't 0, 1, 2, 3, or 4, giving a 1/6 chance
                    jud_votes.append(1)             # vote is constitutional
            elif law == 1 or law == 8:              # if the law is 1 or 8
                jud_vote = random.randint(0,2)      # picks from 0 to 2
                if jud_vote == 0 or jud_vote == 1:  # if it's 0 or 1, giving a 2/3 chance,
                    jud_votes.append(0)             # vote is unconstitutional
                else:                               # if it isn't 0 or 1, giving a 1/3 chance,
                    jud_votes.append(1)             # vote is constitutional
            elif law == 2 or law == 7:              # if the law is 2 or 7
                jud_vote = random.randint(0,1)      # picks 0 or 1
                if jud_vote == 0:                   # if it's 0, giving a 1/2 chance,
                    jud_votes.append(0)             # vote is unconstitutional
                else:                               # if it isn't 0, giving a 1/2 chance,
                    jud_votes.append(1)             # vote is constitutional
            elif law == 3 or law == 6:              # if the law is 3 or 6
                jud_vote = random.randint(0,2)      # picks from 0 to 2
                if jud_vote == 0:                   # if it's 0, giving a 1/3 chance,
                    jud_votes.append(0)             # vote is unconstitutional
                else:                               # if it isn't 0, giving a 2/3 chance,
                    jud_votes.append(1)             # vote is constitutional
            elif law == 4 or law == 5:              # if the law is 4 or 5
                jud_vote = random.randint(0,5)      # picks from 0 to 5
                if jud_vote == 0:                   # if it's 0, giving a 1/6 chance,
                    jud_votes.append(0)             # vote is unconstitutional
                else:                               # if it isn't 0, giving a 5/6 chance,
                    jud_votes.append(1)             # vote is constitutional
        if jud_votes.count(0) > jud_votes.count(1): # if vote is unconstitutional
            previous_law = law                      # this law becomes the previous law
            constitutional = False
            print("unconstitutional")
            law_func()                              # they'll make a new law with the previous one in mind
        else:                                       # if vote is not unconsititutional
            constitutional = True
            print("law constitutional")

    def override():
        global vetoed
        nonlocal previous_law
        nonlocal continue_current_law
        if vetoed == True:                              # if the law was vetoed
            vote_time = random.randint(0,1)             # decides whether they're going to vote to unveto
            if vote_time == 0:                          # if it's 0, they'll vote to unveto
                unveto_votes = []                       # creates the list unveto_votes
                for i in range(535):                    # for each person in the legislative branch
                    unveto_vote = random.randint(0,1)   # they get 2 possible votes, for and against the unveto 
                    unveto_votes.append(unveto_vote)    # append that vote to unveto_votes
                if unveto_votes.count(0) >= 356:        # if more than 2/3 of the legislative vote for the unveto
                    vetoed = False                      # unvetoed
                    print("unvetoed")
                    jud_func()                          # continue on to the judicial branch
            if continue_current_law == True:            # if they're supposed to continue with this law and make it again but more centrist
                previous_law = law                      # this law becomes the previous law
                print("new law should be made now")
                law_func()                              # they'll make a new law with the previous one in mind
        else:                                           # if the law was not vetoed
            jud_func()                                  # continue on to the judicial branch
    # constants
    LEG = 0
    EXE = 7
    # variables
    vetoed = False
    continue_current_law = True
    previous_law = 10
    law = 10
    # the code first determines whether this is an A scenario or a B scenario to make calculations simpler
    if LEG >= 0 and LEG <= 4:
        type = "A"
    elif LEG >= 5 and LEG <= 9:
        type = "B"
    # now the code knows the scenario and can refer to that instead of computing it out each time
    law_func()  # runs the function law

    # RUN
def run():
    global constitutional
    global people_not_voted
    constitutional = False                                                  # resets constitutional
    print("\nGEN 1 :")
    gen_1()                                                                 # runs gen_1()
    print(leg_max_val_index_1[0],", ",exe_max_val_index_1[0])
    lawmaking(LEG = leg_max_val_index_1[0], EXE = exe_max_val_index_1[0])   # passes constants LEG and EXE for this gen to lawmaking() and runs it
    print("\nGEN 2 :")
    fail_check()                                                            # runs fail_check() on gen_1() and its lawmaking()
    constitutional = False                                                  # resets constitutional
    people_not_voted = 100                                                  # resets people
    gen_2()                                                                 # runs gen_2()
    print(leg_max_val_index_2[0],", ",exe_max_val_index_2[0])
    lawmaking(LEG = leg_max_val_index_2[0], EXE = exe_max_val_index_2[0])   # passes constants LEG and EXE for this gen to lawmaking() and runs it
    fail_check()                                                            # runs fail_check() on gen_2() and its lawmaking()
    constitutional = False                                                  # resets constitutional
    people_not_voted = 100                                                  # resets people
    more_gens(gens = 1000)                                                  # runs more_gens() for the manually inputted amount of times minus 2

    # FAIL CHECKER
def fail_check():
    global fails
    global successes
    if constitutional == True:  # if the law is constitutional
        successes.append(1)     # add a success
    else:                       # otherwise
        fails.append(current_gen)   # tells the position of the failure(s)

# starts the functions, prints out the info from the generation, lawmaking, and from fail_check
influence = 0
successes = []
fails = []
generations = [1, 2]
run()
print("Gens:", len(generations))
if len(fails) == 1:
    if fails[0] == 0:
        print("Fails:", "0")
    else:
        print("Fails:", len(fails))
else:
    print("Fails:", len(fails))
if len(fails) > 0:
    print("Generations that failed:", fails)
print("Successes:", len(successes))
print("Successes are determined by seeing that all passed laws are deemed constitutional by the judicial branch.")