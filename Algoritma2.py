# from AutomaticUpload import AutomaticUpload
from RollsXml import RollsXml
# import pandas as pd
import InitialCons
import Improvement
import Sequence_Cost
# import WriteReport
import CostParameters
import random
import copy
import math
import CostParameters
import datetime
# AutomaticUpload.get_roll_list("GALVA1")
#deneme = RollsXml()
#deneme.process_xml_file('GALVA1')
class Algorithm:
    def __init__(self, roll_list):
        self.roll_list = roll_list

    def algorithm2(self):

        # new_report = WriteReport.TotalResult('result.xlsx')
        # new_reportb = WriteReport.TotalResult('resultB.xlsx')

        iter_count = 0
        iter_count2 = 0
        iter_count3 = 0
        solution_cost = 0
        solution_cost2 = 0
        solution_cost_GTO = 0
        solution_cost_first = 0
        solution_cost_first11 = 0
        output_InitOpt = []
        output_GTOOpt = []
        output_TOOpt = []
        GroupTwoOut = []
        GroupTwoOut2 = []
        best_schedule = []
        best_schedule_GTO = []
        best_schedule_TO = []
        best_schedule_MTO = []
        best_schedule_DR = []
        best_schedule_GDR = []
        TOIMPRO = []
        MTOIMPRO = []
        DRIMPRO = []
        last_solution = []
        best_scheduleBAS = []
        ## Initial solution
        best_schedule = InitialCons.InitialCons(self.roll_list)
        best_schedule, grouped_best_schedule = best_schedule.Initial_Sequence()




        # new_report.CreateNewSheet(best_schedule, "Initial")
        # new_reportb.CreateNewSheet(best_schedule, "Initial")

        Costs = Sequence_Cost.Process_Cost_2(best_schedule)
        solution_cost = Sequence_Cost.Process_Cost(best_schedule)
        print("Initial ", Costs)
        print("Initial ", solution_cost)
       # initial solution

        best_schedule_GTO = Improvement.group_two_opt(grouped_best_schedule, 50)
        best_schedule_GDR = Improvement.group_destroy_repair(best_schedule_GTO, 50, 10, 10)
        for rolls in best_schedule_GDR:
            GroupTwoOut += [x for x in rolls]

        Costs = Sequence_Cost.Process_Cost_2(GroupTwoOut)
        solution_cost = Sequence_Cost.Process_Cost(GroupTwoOut)
        print("GDR", Costs)


        while iter_count2 < 3:
            improving = True
            noimprove = 0
            int_sol_cost = 0
            iter_count = 0
            while improving and iter_count < 6:
                sol_TO_init = Sequence_Cost.Process_Cost(GroupTwoOut)
                best_schedule_TO = Improvement.two_opt(GroupTwoOut, 30)
                TOIMPRO = Sequence_Cost.Process_Cost_2(best_schedule_TO)
                sol_TO_out = Sequence_Cost.Process_Cost(best_schedule_TO)
                best_schedule_MTO = Improvement.multi_opt(best_schedule_TO, 50)
                MTOIMPRO = Sequence_Cost.Process_Cost_2(best_schedule_MTO)
                sol_MTO_out = Sequence_Cost.Process_Cost(best_schedule_MTO)
                best_schedule_DR = Improvement.destroy_repair(best_schedule_MTO, ((iter_count2+1)*10), 3, 10)
                sol_DR_out = Sequence_Cost.Process_Cost(best_schedule_DR)
                DRIMPRO = Sequence_Cost.Process_Cost_2(best_schedule_DR)
                int_sol_cost = Sequence_Cost.Process_Cost(best_schedule_DR)
                if int_sol_cost < solution_cost:
                    solution_cost = int_sol_cost
                    GroupTwoOut = copy.copy(best_schedule_DR)
                    noimprove = 0
                else:
                    noimprove = noimprove + 1
                    if noimprove > 3:
                        improving = False
                iter_count += 1

                improving = True
            iter_count2 += 1

        for i in range(len(best_schedule_DR)):
            print(best_schedule_DR[i].BobinNo, "---", best_schedule_DR[i].Kalınlık, "---", best_schedule_DR[i].Genislik, "---", best_schedule_DR[i].Oncelik,best_schedule_DR[i].RTF_Min,"---", best_schedule_DR[i].RTF_Max,"---",best_schedule_DR[i].RTF_Ort, "---", best_schedule_DR[i].CGL_hız)



        last_solution = Improvement.lastRepair(best_schedule_DR, 20, 3)
        solution_DR1 = Sequence_Cost.Process_Cost_2(last_solution)
        solution_lastMT = Sequence_Cost.Process_Cost(best_schedule_MTO)
        solution_last = Sequence_Cost.Process_Cost(last_solution)
        solution_DR = Sequence_Cost.Process_Cost(best_schedule_DR)
        print("sonucÖnceMT =", solution_lastMT)
        print("sonucÖnceDR =", solution_DR)
        print("sonuc =", solution_last)
        print("MES liste:", len(self.roll_list), "Two opt:", len(output_TOOpt), "Destroy Repair:", len(GroupTwoOut))
        for i in range(len(last_solution)):
            print(last_solution[i].BobinNo, "---", last_solution[i].Kalınlık, "---", last_solution[i].Genislik, "---", last_solution[i].Oncelik,last_solution[i].RTF_Min,"---", last_solution[i].RTF_Max,"---",last_solution[i].RTF_Ort, "---", last_solution[i].CGL_hız)

        #################### DR and two opt geçiş bobinleri yazdır
        #####Geçis bobinleri X campanyasından seç Galvaneal,DP, yediyüzey ve Z kampanya için

        # new_report.CreateNewSheet(GroupTwoOut, "Destroy_Repair")
        groupgecisinitial = []
        for i in range(1, len(last_solution)):
            perthick = 0
            widechange = 0
            perthick = abs(((last_solution[i].Kalınlık - last_solution[i - 1].Kalınlık) /
                            max(last_solution[i - 1].Kalınlık, last_solution[i].Kalınlık)) * 100)
            widechange = abs(last_solution[i].Genislik - last_solution[i - 1].Genislik)
            if (perthick > CostParameters.CostParametersGA.kalinlikgecis) or (widechange > CostParameters.CostParametersGA.genislikgecis):
                print("thick change:", perthick, last_solution[i - 1].Kalınlık,last_solution[i].Kalınlık, "widechange:", widechange, last_solution[i - 1].Genislik, last_solution[i].Genislik)
                print(last_solution[i - 1].BobinNo, "--arası--", last_solution[i].BobinNo)
                groupgecisinitial.append(last_solution[i - 1])
                # new_report.CreateNewSheet(groupgecisinitial, "DR-optGecis")
            groupgecisinitial = []

            #########################

        # new_report.xlsx_file.save()
        # new_reportb.xlsx_file.save()
