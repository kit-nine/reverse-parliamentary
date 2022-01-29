def lawmaking():
    import random
    # voting system here, take the output and each time it needs to run the lawmaking system
    # leg makes a law that is on its side of the spectrum
    # temporary voting system
    # these are basically constants in this code but i have to manually change them for testing.
    LEG = 0
    EXE = 7
    # def and some variables
    vetoed = False
    continue_current_law = True
    # the code first  has to determine whether this is an A scenario or a B scenario
    # to make this simpler:
    if LEG >= 0 and LEG <= 4:
        type = "A"
    elif LEG >= 5 and LEG <= 9:
        type = "B"
    # now the code knows the scenario and can refer to that instead of computing
    # the scenario out each time.
    previous_law = 10
    law = 10
    def law_func():
        nonlocal type
        nonlocal vetoed
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
            for i in range(535):            # each person in the legislature
                law_vote_4 = random.randint(0,1)    # votes either 0 or 1
                if law_vote_4.count(0) > law_vote_4.count(1):   # if there are more votes for 0 than for 1
                    law = 4                 # they make a law that is 4
                else:                       # if there are not more votes for 0 than for 1
                    law = 5                 # they make a law that is 5
                    continue_current_law = False    # and they wont make another law based on this one
        elif previous_law == 4:             # if the previous law was 4
            for i in range(535):            # each person in the legislature
                law_vote_5 = random.randint(0,1)    # votes either 0 or 1
                if law_vote_5.count(0) > law_vote_5.count(1):   # if there are more votes for 0 than for 1
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
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "VETOED") # prints the law, the EXE pos, and that it was vetoed
                vetoed = True                                           # sets vetoed = True
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "PASSED") # prints the law, the EXE pos, and that it was passed
                vetoed = False                                          # sets vetoed = False
        else:                                                           # if LEG is not 0 through 4 (and therefore is 5 through 9)
            if law >= exe_line:                                         # and the law is lower than the deciding line
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "VETOED") # prints the law, the EXE pos, and that it was vetoed
                vetoed = True                                           # sets vetoed = True
            else:                                                       # if LEG is 0 through 4 but the law is not lower than the deciding line
                print("Law: ", law, "\n", "EXE: ", EXE, "\n", "PASSED") # prints the law, the EXE pos, and that it was passed
                vetoed = False                                          # sets vetoed = False
    def jud_func():
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
            law_func()                                   # they'll make a new law with the previous one in mind
            print("unconstitutional")               # prints "unconstitutional"
        else:                                       # if vote is not unconsititutional
            print("law constitutional")             # prints "constitutional"
    # runs the function law
    law_func()
    # legislative votes on the veto
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
                law_func()                               # they'll make a new law with the previous one in mind
                print("new law should be made now")
    else:                                           # if the law was not vetoed
        jud_func()
lawmaking()
