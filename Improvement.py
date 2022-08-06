
import random
import Sequence_Cost
import copy
import math
import CostParameters
random.seed(9001)


def group_two_opt(best_schedule, iteration_limit):
    mincost = 0
    Totalcost = 0
    galva_sorted = []
    reverse_galva = []
    opt_best_schedule = []
    for i in range(len(best_schedule)):
        if len(best_schedule[i]) > 0:
            mincost += Sequence_Cost.Process_Cost(best_schedule[i])

    Totalcost = mincost
    opt_best_schedule = copy.copy(best_schedule)
    try:
        for i in range(iteration_limit):
            mincost = 0
            for j in range(len(best_schedule)):

                if len(best_schedule[j]) > 2:
                    random_numbers = random.sample(range(0, len(best_schedule[j])), 2)
                    random_numbers.sort()
                    random_num1 = random_numbers[0]
                    random_num2 = random_numbers[1]
                    if random_num1 == 0:
                        reverse_galva = best_schedule[j][random_num1:random_num2]
                        reverse_galva = reverse_galva[::-1]
                        galva_sorted = reverse_galva + best_schedule[j][random_num2:]
                    else:
                        reverse_galva = best_schedule[j][random_num1:random_num2]
                        reverse_galva = reverse_galva[::-1]
                        galva_sorted = best_schedule[j][:random_num1] + reverse_galva + best_schedule[j][random_num2:]
                    best_schedule[j] = copy.copy(galva_sorted)

            for k in range(len(best_schedule)):
                mincost += Sequence_Cost.Process_Cost(best_schedule[k])
            if mincost < Totalcost:
                Totalcost = mincost
                opt_best_schedule = copy.copy(best_schedule)


 #           print("min", mincost, Totalcost)
 #       print(Totalcost, "---", best_schedule)

    except:
        print("---")
    # for j in range(Group_Num):
    #     for i in range(len(BobinListeGroup)):
    #         print(BobinListeGroup[j][i].roll_id, BobinListeGroup[j][i].thickness, BobinListeGroup[j][i].width)
    return opt_best_schedule

def two_opt(best_schedule, iteration_limit):
    mincostTO = 0
    TotalcostTO = 0
    galva_sortedTO = []
    reverse_galvaTO = []
    FinalListTO = []
    MalIter = []
    sonn = []
    # for rolls in best_schedule:
    #     FinalList += [x for x in rolls]
    mincostTO = Sequence_Cost.Process_Cost(best_schedule)

    TotalcostTO = mincostTO
    try:
        for i in range(iteration_limit):

            random_numbers = random.sample(range(0, len(best_schedule)), 2)
            random_numbers.sort()
            random_num1 = random_numbers[0]
            random_num2 = random_numbers[1]

            if random_num1 == 0:
                reverse_galvaTO = best_schedule[random_num1:random_num2]
                reverse_galvaTO = reverse_galvaTO[::-1]
                galva_sortedTO = reverse_galvaTO + best_schedule[random_num2:]
            else:
                reverse_galvaTO = best_schedule[random_num1:random_num2]
                reverse_galvaTO = reverse_galvaTO[::-1]
                galva_sortedTO = best_schedule[:random_num1] + reverse_galvaTO + best_schedule[random_num2:]
#            best_schedule = copy.copy(galva_sortedTO)

            mincostTO = Sequence_Cost.Process_Cost(galva_sortedTO)

            if mincostTO < TotalcostTO:
                best_schedule = copy.copy(galva_sortedTO)
                TotalcostTO = mincostTO
                sonn = [mincostTO, i]
                MalIter.append(sonn)



 #       print(Totalcost, "---", best_schedule)

    except:
        print("two-opt----")
    # for j in range(Group_Num):
    #     for i in range(len(BobinListeGroup)):
    #         print(BobinListeGroup[j][i].roll_id, BobinListeGroup[j][i].thickness, BobinListeGroup[j][i].width)
    return best_schedule

def destroy_repair(best_schedule, iteration_limit, no_improvement_iteration_limit, destroy_percentage):
        # print("Destroy-Repair Process Started")
#        best_roll_list = []
#        active_roll_list = []
    MalIter = []
    sonn = []
    cand_roll_list = []
    best_roll_list = copy.copy(best_schedule)
    active_roll_list = copy.copy(best_roll_list)
    best_solution_cost = Sequence_Cost.Process_Cost(best_roll_list)

    no_of_rolls_to_be_picked = max(int(len(best_roll_list) * destroy_percentage/100), 1)
    iteration = 1
    no_improvement_iteration = 0
    while iteration <= iteration_limit:
        rolls_to_be_added = []
        for i in range(0, no_of_rolls_to_be_picked + 1):
            try:
                roll = random.choice(active_roll_list)
            except:
                break
            active_roll_list.remove(roll)
            rolls_to_be_added.append(roll)
        rolls_to_be_added = sorted(rolls_to_be_added, key=lambda rolls_to_be_added: rolls_to_be_added.Kalınlık, reverse=False)
        AA = len(rolls_to_be_added)
        for i in range(0, len(rolls_to_be_added)):
        #i = 0
#        while len(rolls_to_be_added) > 0:
            roll = rolls_to_be_added[i]
#            rolls_to_be_added.remove(roll)
            temp_solution_cost = math.inf
            for position in range(len(active_roll_list)):
                temp_roll_list = copy.copy(active_roll_list)
                temp_roll_list.insert(position, roll)
                if Sequence_Cost.Process_Cost(temp_roll_list) < temp_solution_cost:
                    temp_solution_cost = Sequence_Cost.Process_Cost(temp_roll_list)
                    cand_roll_list = copy.copy(temp_roll_list)

            active_roll_list = copy.copy(cand_roll_list)
            #i = i + 1
#            print(len(active_roll_list))
#        print(best_solution_cost)

        if Sequence_Cost.Process_Cost(active_roll_list) < best_solution_cost:
            best_solution_cost = Sequence_Cost.Process_Cost(active_roll_list)
            best_roll_list = copy.copy(active_roll_list)
            sonn = [best_solution_cost, iteration]
            MalIter.append(sonn)
            no_improvement_iteration = 0
        else:
            no_improvement_iteration += 1

        iteration += 1
        if no_improvement_iteration >= no_improvement_iteration_limit:
            break
    return best_roll_list

def group_destroy_repair(best_schedule, iteration_limit, no_improvement_iteration_limit, destroy_percentage):
    mincost = 0
    Totalcost = 0
    galva_sorted = []
    reverse_galva = []
    for i in range(len(best_schedule)):
        if len(best_schedule[i]) > 0:
            mincost += Sequence_Cost.Process_Cost(best_schedule[i])

    Totalcost = mincost
    best_roll_list = []
    active_roll_list = []
    cand_roll_list = []
    try:

        for j in range(len(best_schedule)):
            best_roll_list = copy.copy(best_schedule[j])
            active_roll_list = copy.copy(best_roll_list)
            best_solution_cost = Sequence_Cost.Process_Cost(best_roll_list)

            no_of_rolls_to_be_picked = max(int(len(best_roll_list) * destroy_percentage / 100), 1)
            iteration = 1
            no_improvement_iteration = 0
            while iteration <= iteration_limit:
                rolls_to_be_added = []
                for i in range(0, no_of_rolls_to_be_picked + 1):
                    try:
                        roll = random.choice(active_roll_list)
                    except:
                        break
                    active_roll_list.remove(roll)
                    rolls_to_be_added.append(roll)
                while len(rolls_to_be_added):
                    roll = random.choice(rolls_to_be_added)
                    rolls_to_be_added.remove(roll)
                    temp_solution_cost = math.inf
                    for position in range(len(active_roll_list) + 1):
                        temp_roll_list = copy.copy(active_roll_list)
                        temp_roll_list.insert(position, roll)

                        if Sequence_Cost.Process_Cost(temp_roll_list) < temp_solution_cost:
                            temp_solution_cost = Sequence_Cost.Process_Cost(temp_roll_list)
                            cand_roll_list = copy.copy(temp_roll_list)
                    active_roll_list = copy.copy(cand_roll_list)

                if Sequence_Cost.Process_Cost(active_roll_list) < best_solution_cost:
                    best_solution_cost = Sequence_Cost.Process_Cost(active_roll_list)
                    best_roll_list = copy.copy(active_roll_list)
                    no_improvement_iteration = 0
                else:
                    no_improvement_iteration += 1

                iteration += 1
                if no_improvement_iteration >= no_improvement_iteration_limit:
                    break
            best_schedule[j] = copy.copy(best_roll_list)
    except:
        print("---")

    return best_schedule

def multi_opt(best_schedule, iteration_limit):
    mincostTO = 0
    TotalcostTO = 0
    galva_sortedTO = []
    reverse_galvaTO = []
    reverse_galvaTO2 = []
    reverse_galvaTO3 = []
    FinalListTO = []
    MalIter = []
    sonn = []
    # for rolls in best_schedule:
    #     FinalList += [x for x in rolls]
    mincostTO = Sequence_Cost.Process_Cost(best_schedule)
    TotalcostTO = mincostTO
    try:
        for i in range(iteration_limit):

            random_numbers = random.sample(range(0, len(best_schedule)), 4)
            random_numbers.sort()
            random_num1 = random_numbers[0]
            random_num2 = random_numbers[1]
            random_num3 = random_numbers[2]
            random_num4 = random_numbers[3]
            prt1 = best_schedule[:random_num1]
            prt2 = best_schedule[random_num1:random_num2]
            prt3 = best_schedule[random_num2:random_num3]
            prt4 = best_schedule[random_num3:random_num4]
            prt5 = best_schedule[random_num4:]
            ###############################
            ##     prt leri random birleştir
            prt = [prt1, prt2, prt3, prt4, prt5]
            random_number_arr = random.sample(range(0, 5), 3)
            random_number_arr.sort()
            if random_number_arr[0] == 0:
                if random_number_arr[2] == 2:
                    galva_sortedTO = prt1[::-1] + prt2[::-1] + prt3[::-1] + prt4 + prt5
                elif random_number_arr[2] == 3:
                    if random_number_arr[1] == 1:
                        galva_sortedTO = prt1[::-1] + prt2[::-1] + prt3 + prt4[::-1] + prt5
                    if random_number_arr[1] == 2:
                        galva_sortedTO = prt1[::-1] + prt2 + prt3[::-1] + prt4[::-1] + prt5
                elif random_number_arr[2] == 4:
                    if random_number_arr[1] == 1:
                        galva_sortedTO = prt1[::-1] + prt2[::-1] + prt3 + prt4 + prt5[::-1]
                    elif random_number_arr[1] == 2:
                        galva_sortedTO = prt1[::-1] + prt2 + prt3[::-1] + prt4 + prt5[::-1]
                    elif random_number_arr[1] == 3:
                        galva_sortedTO = prt1[::-1] + prt2 + prt3 + prt4[::-1] + prt5[::-1]
            elif random_number_arr[0] == 1:
                if random_number_arr[2] == 3:
                    galva_sortedTO = prt1 + prt2[::-1] + prt3[::-1] + prt4[::-1] + prt5
                    if random_number_arr[2] == 4:
                        if random_number_arr[1] == 2:
                            galva_sortedTO = prt1 + prt2[::-1] + prt3[::-1] + prt4 + prt5[::-1]
                        if random_number_arr[1] == 3:
                            galva_sortedTO = prt1 + prt2[::-1] + prt3 + prt4[::-1] + prt5[::-1]
            else:
                galva_sortedTO = prt1 + prt2 + prt3[::-1] + prt4[::-1] + prt5[::-1]


#            best_schedule = copy.copy(galva_sortedTO)

            mincostTO = Sequence_Cost.Process_Cost(galva_sortedTO)
            if mincostTO < TotalcostTO:
                best_schedule = copy.copy(galva_sortedTO)
                TotalcostTO = mincostTO
                sonn = [mincostTO, i]
                MalIter.append(sonn)

 #           print("min", mincost, Totalcost)
 #       print(Totalcost, "---", best_schedule)

    except:
        print("--")
    # for j in range(Group_Num):
    #     for i in range(len(BobinListeGroup)):
    #         print(BobinListeGroup[j][i].roll_id, BobinListeGroup[j][i].thickness, BobinListeGroup[j][i].width)
    return best_schedule


def lastRepair(best_schedule, iteration_limit, no_improvement_iteration_limit):

    # if best_schedule[1].bobin_category == "Galvaneal":
    Paramkalinlikgecis = CostParameters.CostParametersGA.kalinlikgecis
    Paramgenislikgecis = CostParameters.CostParametersGA.genislikgecis
    # elif best_schedule[1].bobin_category == "Zcampain":
    #      Paramkalinlikgecis = CostParameters.CostParametersZ.kalinlikgecis
    #      Paramgenislikgecis = CostParameters.CostParametersZ.genislikgecis
    # elif best_schedule[1].bobin_category == "Xcampain":
    #      Paramkalinlikgecis = CostParameters.CostParametersX.kalinlikgecis
    #      Paramgenislikgecis = CostParameters.CostParametersX.genislikgecis
    # elif best_schedule[1].bobin_category == "DPcampain":
    #      Paramkalinlikgecis = CostParameters.CostParametersDP.kalinlikgecis
    #      Paramgenislikgecis = CostParameters.CostParametersDP.genislikgecis
    # elif best_schedule[1].bobin_category == "ZPAR":
    #      Paramkalinlikgecis = CostParameters.CostParametersZPAR.kalinlikgecis
    #      Paramgenislikgecis = CostParameters.CostParametersZPAR.genislikgecis
    # else:
    #      Paramkalinlikgecis = CostParameters.CostParametersX.kalinlikgecis
    #      Paramgenislikgecis = CostParameters.CostParametersX.genislikgecis


    cand_roll_list = []
    rolls_to_be_added = []
    temp_roll_list = []


    MalIter = []
    sonn = []
    best_roll_list = copy.copy(best_schedule)

    iteration = 1
    no_improvement_iteration = 0
    while iteration <= iteration_limit:

        best_solution_cost = Sequence_Cost.Process_Cost(best_roll_list)
        active_roll_list = copy.copy(best_roll_list)
        rolls_to_be_added = []
        for i in range(1, len(best_schedule)):

            perthick = 0
            widechange = 0
            perthick = abs(((best_roll_list[i].Kalınlık - best_roll_list[i - 1].Kalınlık) /
                            max(best_roll_list[i - 1].Kalınlık, best_roll_list[i].Kalınlık)) * 100)
            widechange = abs(best_roll_list[i].Genislik - best_roll_list[i - 1].Genislik)
            if ((perthick > Paramkalinlikgecis) or (widechange > Paramgenislikgecis)):
                roll = best_roll_list[i]
                active_roll_list.remove(roll)
                rolls_to_be_added.append(roll)

        rolls_to_be_added = sorted(rolls_to_be_added, key=lambda rolls_to_be_added: rolls_to_be_added.Kalınlık,
                                   reverse=False)
        AA = len(rolls_to_be_added)
        for i in range(0, len(rolls_to_be_added)):
            # i = 0
            #        while len(rolls_to_be_added) > 0:
            roll = rolls_to_be_added[i]
            #            rolls_to_be_added.remove(roll)
            temp_solution_cost = math.inf
            for position in range(len(active_roll_list)):
                temp_roll_list = copy.copy(active_roll_list)
                temp_roll_list.insert(position, roll)
                if Sequence_Cost.Process_Cost(temp_roll_list) < temp_solution_cost:
                    temp_solution_cost = Sequence_Cost.Process_Cost(temp_roll_list)
                    cand_roll_list = copy.copy(temp_roll_list)
            active_roll_list = copy.copy(cand_roll_list)

        if Sequence_Cost.Process_Cost(active_roll_list) < best_solution_cost:
            best_solution_cost = Sequence_Cost.Process_Cost(active_roll_list)
            best_roll_list = copy.copy(active_roll_list)
            no_improvement_iteration = 0
            sonn = [best_solution_cost, iteration]
            MalIter.append(sonn)
        else:
            no_improvement_iteration += 1

        iteration += 1
        if no_improvement_iteration >= no_improvement_iteration_limit:
            break


    return best_roll_list