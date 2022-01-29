import random

    # FIRST GENERATION OF PEOPLE
# these people will randomly choose a legislature between all 10 example parties
# then the code will calculate who won and have the people vote on the executive branch from the other side of the political spectrum.
# the code will finally print the parties who won each house.

    # SECOND GEN
# these people are either going to vote exactly like their parents did or exactly
# the opposite 3/4 of the time, the other 1/4 will vote randomly. this will be determined by a boolean decision to see if their parents
# were good or not.
# same things are printed out

    # THIRD GEN
# these people will have the same decision up there, but it will depend on whether
# their grandparents were bad too. if their grandparents were bad, then there is a 2 out
# of 3 chance that their parents will have been bad too.
# then the boolean of whether they are voting the same or the opposite of their parents
# same things are printed out

    # ADDITIONAL NOTES - may or may not actually implement
# the parents will survive 3 generations.
# the parents will have a 2 out of 3 chance of voting the same every generation.
#    otherwise they will randomly choose every time.
# media influence can skew the voting by a certain amount - manual input
# law creation is skewed toward the position of the legislative 
# another voting session or the VP instead of a randint for the tiebreaker
# a set amount of laws per generation - manual input or a set amount can be built in

    # IMPLEMENTED ADDITIONAL NOTES
# more_gens() will have parameter gens, set it equal to the number of gens to test minus one - manual input

people_not_voted = 100
leg_options = "0123456789"
exe_options_1 = "01234"
exe_options_2 = "56789"
leg_votes = []
leg_counts = []
exe_votes = []
exe_counts = []
gen_1_wins = []
choice = 0
gen_previous_parents = []
gen_parents = []
vetoed = False

    # GEN 1
def gen_1():
    global people_not_voted     # I know this is a code smell but I could not figure anything else out
    # this makes the people vote for the legislative branch
    while people_not_voted > 0:                     # while any amount of people havent voted
        choice = int(random.choice(leg_options))    # have them vote 0-9
        leg_votes.append(choice)                    # append their choice to the votes list
        people_not_voted -= 1                       # subtract one person because they just voted
    # this finds out how many people voted for each option
    for i in range(0, 9):           # for each option
        count = leg_votes.count(i)  # see how many people voted for that option
        leg_counts.append(count)    # append that to the list
    leg_max_val = max(leg_counts)   # finds the one they voted for the most
    global leg_max_val_index_1      # so the code can use leg_max_val_index_1 later
    leg_max_val_index_1 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]   # this indexes the maximum value(s), which i use to find what the largest vote was for
    # this narrows it down to one winner incase there's a tie
    for i in range(len(leg_max_val_index_1)):       # for the length of the list of max value(s)
        while len(leg_max_val_index_1) > 1:         # while it's more than one
            delete = bool(random.getrandbits(1))    # delete = True / False
            if delete == True:                      # if delete == True
                del leg_max_val_index_1[i]          # deletes the first value in the list
            else:                                   # if delete != True
                del leg_max_val_index_1[i - 1]      # deletes the last value in the list
    people_not_voted = 100      # resets the people for the next voting session
    # this makes the people vote for the executive branch
    while people_not_voted > 0:                         # while any amount of people havent voted
        if 4 < leg_max_val_index_1[0] < 9:              # if the legislative vote is 5 through 9
            choice = int(random.choice(exe_options_1))  # the people are only allowed to vote from exe_options_1
            exe_votes.append(choice)                    # appends their choice to the votes list
        elif 0 < leg_max_val_index_1[0] < 5:            # if the legislative vote is 0 through 4
            choice = int(random.choice(exe_options_2))  # the people are only allowed to vote from exe_options_2
            exe_votes.append(choice)                    # appends their choice to the votes list
        people_not_voted -= 1                           # subtract one person because they just voted
    # finds out how many people voted for each option without pesky '0's from the other half of the spectrum
    if 0 <= leg_max_val_index_1[0] <= 4:    # if the legislative vote is 0 through 4
        for i in range(5, 10):              # for each option (5 through 9)
            count = exe_votes.count(i)      # see how many people voted for that option
            exe_counts.append(count)        # append that to the list
    else:                                   # if the legislative vote isn't 0 through 4
        for i in range(0, 5):               # for each option (5 through 9)
            count = exe_votes.count(i)      # see how many people voted for that option
            exe_counts.append(count)        # append that to the list
    exe_max_val = max(exe_counts)           # finds the one they voted for most
    global exe_max_val_index_1              # so the code can use exe_max_val_index_1 later
    exe_max_val_index_1 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]   # this indexes the maximum value(s), which i use to find what the largest vote was for
    # this narrows it down to one winner incase there's a tie
    for i in range(len(exe_max_val_index_1)):       # for the length of the list of max value(s)
        while len(exe_max_val_index_1) > 1:         # while it's more than one
            delete = bool(random.getrandbits(1))    # delete = True / False
            if delete == True:                      # if delete == True
                del exe_max_val_index_1[i]          # deletes the first value in the list
            else:                                   # if delete != True
                del exe_max_val_index_1[i - 1]      # deletes the last value in the list
    # since the right side of the spectrum starts with 5, using the index doesn't work unless the code adds the 5 in here to correct it
    if 0 <= leg_max_val_index_1[0] <= 4:    # if the legislative vote is 0 through 4
        exe_max_val_index_1[0] += 5         # add 5 to the index
    # resets these lists so they can be reused
    leg_counts.clear()
    exe_counts.clear()
    return

    # GEN 2
def gen_2():
    global people_not_voted
    # since gen_2() votes differently, a for loop was simpler so i could be used for indexing
    for i in range(people_not_voted):           # for the number of people who havent yet voted
        normality = random.randint(0,3)         # determines whether the person will vote based on their parents or not
        if normality == 0 or 1 or 2:            # if normality == 0 or 1 or 2
            parent_score = random.randint(0, 1) # determines whether their relationship with their parent is good or not
            x = leg_votes[i]                    # finds the parent's vote
            if parent_score == 0:               # if the parent relationship was bad,
                choice = abs(x - 9)             # the choice is reversed of what the parent chose 
            else:                               # if the parent relationship was good,
                choice = x                      # the choice is what the parent chose
            gen_parents.append(parent_score)    # appends the parent relationship score so it can be used in future generations
        else:                                   # if normality != 0 or 1 or 2
            choice = random.choice(leg_options) # the person chooses randomly
    # everything from here out is exactly the same as gen_1(), refer to those comments for explanations
    for i in range(0, 9):
        count = leg_votes.count(i)
        leg_counts.append(count)

    leg_max_val = max(leg_counts)
    global leg_max_val_index_2
    leg_max_val_index_2 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]

    for i in range(len(leg_max_val_index_2)):
        while len(leg_max_val_index_2) > 1:
            delete = bool(random.getrandbits(1))
            if delete == True:
                del leg_max_val_index_2[i]
            else:
                del leg_max_val_index_2[i - 1]

    people_not_voted = 100

    while people_not_voted > 0: 
        if 4 < leg_max_val_index_2[0] < 9:
            choice = int(random.choice(exe_options_1))
            exe_votes.append(choice)
        elif 0 < leg_max_val_index_2[0] < 5:
            choice = int(random.choice(exe_options_2))
            exe_votes.append(choice)
        else:
            quit
        people_not_voted -= 1

    if 0 <= leg_max_val_index_2[0] <= 4:
        for i in range(5, 10):
            count = exe_votes.count(i)
            exe_counts.append(count)
    else:
        for i in range(0, 5):
            count = exe_votes.count(i)
            exe_counts.append(count)

    exe_max_val = max(exe_counts)
    global exe_max_val_index_2
    exe_max_val_index_2 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]

    for i in range(len(exe_max_val_index_2)):
        while len(exe_max_val_index_2) > 1:
            delete = bool(random.getrandbits(1))
            if delete == True:
                del exe_max_val_index_2[i]
            else:
                del exe_max_val_index_2[i - 1]

    if 0 <= leg_max_val_index_2[0] <= 4:
        exe_max_val_index_2[0] += 5
    leg_counts.clear()
    exe_counts.clear()
    leg_votes.clear()
    exe_votes.clear()
    return

    # GEN 3
def gen_3():
    global people_not_voted
    # gen_3() also votes a little differently, starting with this for loop that copies gen_parents into gen_previous_parents for the next iteration of gen_3() to work
    for i in gen_parents:               # for each parent
        gen_previous_parents.append(i)  # copies their relationship score into gen_previous_parents
    gen_parents.clear()                 # clears gen_parents for reuse
    
    # this part is very similar to the for loop in gen_2(), but gen_previous_parents is used to determine the parent_score of gen_parents
    #   this way the simulation takes into account the fact that children with bad relationships with their parents usually end up 
    #   passing bad parenting strategies from their parents onto their future children
    #   this makes the simulation more accurate in that more than just one future generation is effected by bad parenting
    
    for i in range(people_not_voted):
        normality = random.randint(0,3)
        if normality == 0 or 1 or 2:
            if gen_previous_parents[i] == 0:        # if the grandparents' relationship with the parents was bad
                parent_score = random.randint(0,2)  # the parent score has a 2/3, rather than a 1/2, chance to also have a bad relationship with their kids
            elif gen_previous_parents[i] == 1:        # if the grandparents' relationship with the parents was good
                parent_score = random.randint(0,2)  # the parent score has a 2/3, rather than a 1/2, chance to also have a good relationship with their kids
            x = leg_votes[i]                    # same from gen 2
            if parent_score == 0 or 1:
                choice = abs(x - 9)
            else:
                choice = x
            gen_parents.append(parent_score)
        else:
            choice = random.choice(leg_options)

    for i in range(0, 9):
        count = leg_votes.count(i)
        leg_counts.append(count)

    leg_max_val = max(leg_counts)
    global leg_max_val_index_3
    leg_max_val_index_3 = [i for i in range(len(leg_counts)) if leg_counts[i] == leg_max_val]

    for i in range(len(leg_max_val_index_3)):
        while len(leg_max_val_index_3) > 1:
            delete = bool(random.getrandbits(1))
            if delete == True:
                del leg_max_val_index_3[i]
            else:
                del leg_max_val_index_3[i - 1]

    people_not_voted = 100

    while people_not_voted > 0: 
        if 4 < leg_max_val_index_3[0] < 9:
            choice = int(random.choice(exe_options_1))
            exe_votes.append(choice)
        elif 0 < leg_max_val_index_3[0] < 5:
            choice = int(random.choice(exe_options_2))
            exe_votes.append(choice)
        else:
            quit
        people_not_voted -= 1

    if 0 <= leg_max_val_index_3[0] <= 4:
        for i in range(5, 10):
            count = exe_votes.count(i)
            exe_counts.append(count)
    else:
        for i in range(0, 5):
            count = exe_votes.count(i)
            exe_counts.append(count)

    exe_max_val = max(exe_counts)
    global exe_max_val_index_3
    exe_max_val_index_3 = [i for i in range(len(exe_counts)) if exe_counts[i] == exe_max_val]

    for i in range(len(exe_max_val_index_3)):
        while len(exe_max_val_index_3) > 1:
            delete = bool(random.getrandbits(1))
            if delete == True:
                del exe_max_val_index_3[i]
            else:
                del exe_max_val_index_3[i - 1]

    if 0 <= leg_max_val_index_3[0] <= 4:
        exe_max_val_index_3[0] += 5
    leg_counts.clear()
    exe_counts.clear()
    leg_votes.clear()
    exe_votes.clear()
    return

    # MORE GENS
def more_gens(gens):
    for i in range(gens):
        global generations
        gen_3()
        current_gen = i + 3
        # print("\nGEN",current_gen,":")
        # print(leg_max_val_index_3[0],", ",exe_max_val_index_3[0], "\n")
        lawmaking(LEG = leg_max_val_index_3[0], EXE = exe_max_val_index_3[0])
        fail_check()
        generations.append(current_gen)

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
                law = random.randint(0,4)   # they make a law that is 0 through 4
            else:                           # and if LEG is not 0 through 4
                law = random.randint(5,9)   # they make a law that is 5 through 9
        elif previous_law == 9:             # if the previous law was 9
            law = random.randint(5,8)       # they make a law that is 5 through 8
        elif previous_law == 8:             # if the previous law was 8
            law = random.randint(5,7)       # they make a law that is 5 through 7
        elif previous_law == 7:             # if the previous law was 7
            law = random.randint(5,6)       # they make a law that is 5 through 6
        elif previous_law == 6:             # if the previous law was 6
            law = 5                         # they make a law that is 5
        elif previous_law == 5:             # if the previous law was 5
            law_votes_4 = []                # makes a list for votes
            for i in range(535):            # each person in the legislature
                law_vote_4 = random.randint(0,1)    # votes either 0 or 1
                law_votes_4.append(law_vote_4)  # appends the vote to the list of votes
                if law_votes_4.count(0) > law_votes_4.count(1):   # if there are more votes for 0 than for 1
                    law = 4                 # they make a law that is 4
                else:                       # if there are not more votes for 0 than for 1
                    law = 5                 # they make a law that is 5
                    continue_current_law = False    # and they wont make another law based on this one
        elif previous_law == 4:             # if the previous law was 4
            law_votes_5 = []                # make a list for votes
            for i in range(535):            # each person in the legislature
                law_vote_5 = random.randint(0,1)    # votes either 0 or 1
                law_votes_5.append(law_vote_5)  # appends the vote to the list of votes
                if law_votes_5.count(0) > law_votes_5.count(1):   # if there are more votes for 0 than for 1
                    law = 5                 # they make a law that is 5
                else:                       # if there are not more votes for 0 than for 1
                    law = 4                 # they make a law that is 4
                    continue_current_law = False    # and they wont make another law based on this one
        elif previous_law == 3:             # if the previous law was 3
            law = 4                         # they make a law that is 4
        elif previous_law == 2:             # if the previous law was 2
            law = random.randint(3,4)       # they make a law that is 3 through 4
        elif previous_law == 1:             # if the previous law was 1
            law = random.randint(2,4)       # they make a law that is 2 through 4
        elif previous_law == 0:             # if the previous law was 0
            law = random.randint(1,4)       # they make a law that is 1 through 4
        # decides where EXE draws the line based on their position and draw_line
        exe_line = EXE + draw_line      # EXE position plus or minus 5
        # vetos or passes law based on exe_line
        if type == "A":                                                 # if LEG is 0 through 4
            if law <= exe_line:                                         # and the law is lower than the deciding line
                vetoed = True                                           # sets vetoed = True
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "VETOED") # prints the law, the EXE pos, and that it was vetoed
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                vetoed = False                                          # sets vetoed = False
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "PASSED") # prints the law, the EXE pos, and that it was passed
        else:                                                           # if LEG is not 0 through 4 (and therefore is 5 through 9)
            if law >= exe_line:                                         # and the law is lower than the deciding line
                vetoed = True                                           # sets vetoed = True
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "VETOED") # prints the law, the EXE pos, and that it was vetoed
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                vetoed = False                                          # sets vetoed = False
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "PASSED") # prints the law, the EXE pos, and that it was passed
        unveto()
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
    def unveto():
        global vetoed
        nonlocal previous_law
        if vetoed == True:                              # if the law was vetoed
            vote_time = random.randint(0,1)             # decides whether they're going to vote to unveto
            if vote_time == 0:                          # if it's 0, they'll vote to unveto
                unveto_votes = []                       # creates the list unveto_votes
                for i in range(535):                    # for each person in the legislative branch
                    unveto_vote = random.randint(0,1)   # they get 2 possible votes, for and against the unveto 
                    unveto_votes.append(unveto_vote)    # append that vote to unveto_votes
                if unveto_votes.count(0) >= 356:        # if more than 2/3 of the legislative vote for the unveto
                    vetoed = False                      # unvetoed
                    print("unvetoed")                   # prints "unvetoed"
                    jud_func()
            else:                                       # if it's not 0, they won't vote to unveto
                if continue_current_law == True:        # if they're supposed to continue with this law and make it again but more centrist
                    previous_law = law                  # this law becomes the previous law
                    print("new law should be made now")
                    law_func()                          # they'll make a new law with the previous one in mind
        else:                                           # if the law was not vetoed
            jud_func()                                  # continue onto the judicial branch
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
    constitutional = False                                                  # resets constitutional
    print("\nGEN 1 :")
    gen_1()                                                                 # runs gen_1()
    print(leg_max_val_index_1[0],", ",exe_max_val_index_1[0])
    lawmaking(LEG = leg_max_val_index_1[0], EXE = exe_max_val_index_1[0])   # passes constants LEG and EXE for this gen to lawmaking() and runs it
    print("\nGEN 2 :")
    fail_check()                                                            # runs fail_check() on gen_1() and its lawmaking()
    constitutional = False                                                  # resets constitutional
    gen_2()                                                                 # runs gen_2()
    print(leg_max_val_index_2[0],", ",exe_max_val_index_2[0])
    lawmaking(LEG = leg_max_val_index_2[0], EXE = exe_max_val_index_2[0])   # passes constants LEG and EXE for this gen to lawmaking() and runs it
    fail_check()                                                            # runs fail_check() on gen_2() and its lawmaking()
    constitutional = False                                                  # resets constitutional
    more_gens(gens = 998)                                                    # runs more_gens() for the manually inputted amount of times


    # FAIL CHECKER
def fail_check():
    global fails
    global successes
    if constitutional == True:  # if the law is constitutional
        successes.append(1)     # add a success
    else:                       # otherwise
        if vetoed == True:      # if the law has been vetoed (soon vetoed laws wont be allowed as the code should remake that law each generation)
            successes.append(1) # add a success
        else:                   # otherwise
            fails.append(1)     # add a failure

successes = []
fails = []
generations = [1, 2]
run()
print("Gens:", len(generations))
print("Fails:", len(fails))
print("Successes:", len(successes))
print("Successes are determined by seeing that all passed laws are deemed constitutional by the judicial branch.")