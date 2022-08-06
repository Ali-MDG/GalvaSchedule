import CostParameters
import CalculateStartEndTime
#import datetime
#import Roll
from ProductionSequence import ProductionSequence


def Process_Cost(ProductionSequence):
    RTF_Ust_Lim = 0
    Thickness_Param_Pen = 0
    Width_Param_Pen = 0
    counteri = 0
    counterj = 0
    Interval_Param = 0
    Thickness_Param_Pos = 0
    Thickness_Param_Neg = 0
    RTF_Fark = 0
    RTF_Ort = 0
    Width_Param_Diff_Pos = 0
    Width_Param_Diff_Neg = 0
    RTFDiff_Param_Positive = 0
    RTFDiff_Param_Negative = 0
    RTFDiff_Param_Penalty = 0
    RTFDiff_Int_Param = 0
    RTF_Ust_Lim = 30
    Penalty_pri = 0
    process_cost_thick = 0
    process_cost_wide = 0
    Penalty_iccap = 0
    priority_cost = 0
    RTF_Fark_Cost = 0
    hız_fark_cost = 0
    overtime_cost = 0
    priority_cost = 0
    process_cost =0
    Pen_pasi = 0
    percent_thickness = 0
    percent_wide = 0
    overtimelimit = 16
    overtimepenalty = 10
    kalınlıkgecis = 0
    genislikgecis = 0
    hatgecis = 0
    StartEnd = []
    max_thickness = max([i.Kalınlık for i in ProductionSequence])
    min_thickness = min([i.Kalınlık for i in ProductionSequence])
    max_wide = max([i.Genislik for i in ProductionSequence])
    min_wide = min([i.Genislik for i in ProductionSequence])
    max_RTF = max([i.RTF_Max for i in ProductionSequence])
    min_RTF = min([i.RTF_Min for i in ProductionSequence])
    max_RTF_Ort = max([i.RTF_Ort for i in ProductionSequence])
    min_RTF_Ort = min([i.RTF_Ort for i in ProductionSequence])
    max_speed = max([i.CGL_hız for i in ProductionSequence])
    min_speed = min([i.CGL_hız for i in ProductionSequence])

    AA_thickness = 1000
    AA_width = 1000
    AA_RTF = 30
    AA_RTF_Ort = 850
    AA_speed = 100
    AA_pri = 10000
#    CalculateStartEndTime.CalStartEnd(Production_Sequence)


    # aa = (Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time)
    #
    # if (((Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time).total_seconds() / 3600) <= overtimelimit):
    #    overtime_cost = overtimepenalty * (abs(((Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time).total_seconds() / 3600) - overtimelimit))
    Thickness_Param_Pos = CostParameters.CostParametersGA.Thickness_Diff_Pos
    Thickness_Param_Neg = CostParameters.CostParametersGA.Thickness_Diff_Neg
    Thickness_Param_Pen = CostParameters.CostParametersGA.Thickness_Diff_Pen
    Width_Param_Diff_Pos = CostParameters.CostParametersGA.Width_Diff_Pos
    Width_Param_Diff_Neg = CostParameters.CostParametersGA.Width_Diff_Neg
    Width_Param_Pen = CostParameters.CostParametersGA.Width_Diff_Pen
    kalinlikgecis = CostParameters.CostParametersGA.kalinlikgecis
    hatgecis = CostParameters.CostParametersGA.hatgecis
    genislikgecis = CostParameters.CostParametersGA.genislikgecis
    hatgenisgec = CostParameters.CostParametersGA.hatgenisgec
    RTFDiff_Param_Positive = CostParameters.CostParametersGA.RTF_Diff_Pos
    RTFDiff_Param_Negative = CostParameters.CostParametersGA.RTF_Diff_Neg
    RTFDiff_Param_Penalty = CostParameters.CostParametersGA.RTF_Diff_Pen
    RTF_Ust_Lim = CostParameters.CostParametersGA.RTF_Ust_Lim
    Penalty_pri = CostParameters.CostParametersGA.Penalty_pri
    Penalty_iccap = CostParameters.CostParametersGA.Penalty_iccap
    Pen_pasi = CostParameters.CostParametersGA.Pen_pasi
    overtimelimit = CostParameters.CostParametersGA.overtimelim
    Deadtimelimit = CostParameters.CostParametersGA.DeadlineForPriority
    overtimepenalty = CostParameters.CostParametersGA.overtimepen

    for j in range(1, len(ProductionSequence)):




     

#        percent_thickness = (((Production_Sequence[j].thickness - Production_Sequence[j - 1].thickness) / Production_Sequence[j-1].thickness) * 100)
        percent_thickness = (((ProductionSequence[j].Kalınlık - ProductionSequence[j - 1].Kalınlık) /
                              max(ProductionSequence[j - 1].Kalınlık, ProductionSequence[j].Kalınlık)) * 100)
        if kalinlikgecis >= percent_thickness > 0:
            process_cost_thick += abs(Thickness_Param_Pos * (percent_thickness /AA_thickness))
        elif hatgecis >= percent_thickness > kalinlikgecis:
            process_cost_thick += abs(50 * Thickness_Param_Pos * (percent_thickness/AA_thickness))

        elif -kalinlikgecis < percent_thickness <= 0:
            process_cost_thick += abs(Thickness_Param_Neg * (percent_thickness/AA_thickness))
        elif -hatgecis < percent_thickness <= -kalinlikgecis:
            process_cost_thick += abs(50 * Thickness_Param_Neg * (percent_thickness/AA_thickness))

        else:
            process_cost_thick += abs(Thickness_Param_Pen * (percent_thickness/AA_thickness))

       #####################################wide change

#       if Production_Sequence[j].bobin_category == "GA" or Production_Sequence[j].bobin_category == "Zcampain" or Production_Sequence[j].bobin_category == "ZPAR":
#           genislikgecis = 100
#       else:
#           genislikgecis = 250
#       hatgenisgec = 300
        percent_wide = ProductionSequence[j].Genislik - ProductionSequence[j - 1].Genislik
#       print(Galvaneal_cizelgesiz[j].width, percent_wide, percent_thickness)
        if genislikgecis >= percent_wide > 0:
            process_cost_wide += abs(Width_Param_Diff_Pos * (percent_wide / AA_width))
        elif hatgenisgec >= percent_wide > genislikgecis:
            process_cost_wide += abs(5 * (Width_Param_Diff_Pos * (percent_wide / AA_width)))
        elif -genislikgecis <= percent_wide <= 0:
            process_cost_wide += abs(Width_Param_Diff_Neg * (percent_wide / AA_width))
        elif -hatgenisgec <= percent_wide < -genislikgecis:
            process_cost_wide += abs(5 * Width_Param_Diff_Neg * (percent_wide / AA_width))
        else:
            process_cost_wide += abs((Width_Param_Pen * (percent_wide / AA_width)))
#
# ############################################RTF Change
        if ((ProductionSequence[j-1].RTF_Max < ProductionSequence[j].RTF_Min)or(ProductionSequence[j].RTF_Max < ProductionSequence[j-1].RTF_Min)):
             Interval_Param = 0
        else:
             Interval_Param = 1

        RTF_Fark = (ProductionSequence[j-1].RTF_Ort - ProductionSequence[j].RTF_Ort)
        RTF_Ort = (ProductionSequence[j - 1].RTF_Ort + ProductionSequence[j].RTF_Ort)/2

        if 0 < RTF_Fark <= RTF_Ust_Lim:
            RTF_Fark_Cost += (RTFDiff_Param_Negative * RTF_Fark * RTF_Ort / (AA_RTF*AA_RTF_Ort))
        elif -RTF_Ust_Lim <= RTF_Fark <= 0:
            RTF_Fark_Cost += abs((RTFDiff_Param_Positive * RTF_Fark * RTF_Ort / (AA_RTF*AA_RTF_Ort)))
        else:
            RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTF_Fark * RTF_Ort/(AA_RTF*AA_RTF_Ort))

        if Interval_Param == 0:
            if ProductionSequence[j - 1].RTF_Max < ProductionSequence[j].RTF_Min:
                RTFDiff_Int_Param = abs(ProductionSequence[j].RTF_Min - ProductionSequence[j - 1].RTF_Max)
                RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTFDiff_Int_Param * RTF_Ort / (AA_RTF*AA_RTF_Ort))
            else:
                RTFDiff_Int_Param = abs(ProductionSequence[j - 1].RTF_Min - ProductionSequence[j].RTF_Max)
                RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTFDiff_Int_Param * RTF_Ort / (AA_RTF*AA_RTF_Ort))

# ###############################################Inner diam -passivizasyon değişimi
#
#         if (Production_Sequence[j].inner_diameter != Production_Sequence[j-1].inner_diameter):
#             counteri = counteri + 1
        if (ProductionSequence[j].Passivizasyon != ProductionSequence[j-1].Passivizasyon):
             counterj = counterj + 1
# ################################priority
        priority_cost = priority_cost + abs(ProductionSequence[j].Oncelik * CostParameters.Penalty_pri * j) / AA_pri
# #
# #
# #################################################3

        hız_fark_cost = hız_fark_cost + abs((ProductionSequence[j-1].CGL_hız - ProductionSequence[
           j].CGL_hız)) * CostParameters.Speed_Diff_Pos / AA_speed
# ######################################################## over time

#         if (((Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time).total_seconds())/3600) <= overtimelimit:
#             overtime_cost += overtimepenalty * (abs(((Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time).total_seconds() / 3600) - overtimelimit))
# #          print(overtime_cost, abs((Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time).total_seconds() / 3600 ))
#           print(Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time)
#           print(Production_Sequence[j-1].roll_id, Production_Sequence[j-1].StartTime, Production_Sequence[j-1].EndTime, Production_Sequence[j-1].processTime, "Soğumamış ")
           #



# ########################################################priority cost
#         for i in range(len(ProductionSequence)):
# #               print(StartEnd[i].StartTime, "----", StartEnd[i].EndTime)
#             if ProductionSequence[j].Oncelik == 99:
#                 if (((ProductionSequence[j].EndTime - ProductionSequence[0].StartTime).total_seconds())/3600) >= Deadtimelimit:
#                     priority_cost += (((ProductionSequence[j].EndTime - ProductionSequence[0].StartTime).total_seconds()/3600) - Deadtimelimit) * CostParameters.DeadlineForPriorityPen
# ########## Sıfırıncı bobin in overtime maliyeti
    # Costs = [process_cost_thick, process_cost_wide, RTF_Fark_Cost, priority_cost, hız_fark_cost, overtime_cost, \
    # counteri * abs(Penalty_iccap), counterj * abs(Pen_pasi)]
    process_cost = 0.2*process_cost_thick + 0.6*process_cost_wide + 0.1*RTF_Fark_Cost + 0.1*hız_fark_cost + counterj * abs(Pen_pasi) + priority_cost
    return process_cost


def Process_Cost_2(ProductionSequence):
    RTF_Ust_Lim = 0
    Thickness_Param_Pen = 0
    Width_Param_Pen = 0
    counteri = 0
    counterj = 0
    Interval_Param = 0
    Thickness_Param_Pos = 0
    Thickness_Param_Neg = 0
    RTF_Fark = 0
    RTF_Ort = 0
    Width_Param_Diff_Pos = 0
    Width_Param_Diff_Neg = 0
    RTFDiff_Param_Positive = 0
    RTFDiff_Param_Negative = 0
    RTFDiff_Param_Penalty = 0
    RTFDiff_Int_Param = 0
    RTF_Ust_Lim = 30
    Penalty_pri = 0
    process_cost_thick = 0
    process_cost_wide = 0
    Penalty_iccap = 0
    priority_cost = 0
    RTF_Fark_Cost = 0
    hız_fark_cost = 0
    overtime_cost = 0
    priority_cost = 0
    process_cost = 0
    Pen_pasi = 0
    percent_thickness = 0
    percent_wide = 0
    overtimelimit = 16
    overtimepenalty = 10
    kalınlıkgecis = 0
    genislikgecis = 0
    hatgecis = 0
    StartEnd = []
    max_thickness = max([i.Kalınlık for i in ProductionSequence])
    min_thickness = min([i.Kalınlık for i in ProductionSequence])
    max_wide = max([i.Genislik for i in ProductionSequence])
    min_wide = min([i.Genislik for i in ProductionSequence])
    max_RTF = max([i.RTF_Max for i in ProductionSequence])
    min_RTF = min([i.RTF_Min for i in ProductionSequence])
    max_RTF_Ort = max([i.RTF_Ort for i in ProductionSequence])
    min_RTF_Ort = min([i.RTF_Ort for i in ProductionSequence])
    max_speed = max([i.CGL_hız for i in ProductionSequence])
    min_speed = min([i.CGL_hız for i in ProductionSequence])

    AA_thickness = 1000
    AA_width = 1000
    AA_RTF = 30
    AA_RTF_Ort = 850
    AA_speed = 100
    AA_pri = 10000
    #    CalculateStartEndTime.CalStartEnd(Production_Sequence)

    # aa = (Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time)
    #
    # if (((Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time).total_seconds() / 3600) <= overtimelimit):
    #    overtime_cost = overtimepenalty * (abs(((Production_Sequence[0].StartTime - Production_Sequence[0].last_process_time).total_seconds() / 3600) - overtimelimit))
    Thickness_Param_Pos = CostParameters.CostParametersGA.Thickness_Diff_Pos
    Thickness_Param_Neg = CostParameters.CostParametersGA.Thickness_Diff_Neg
    Thickness_Param_Pen = CostParameters.CostParametersGA.Thickness_Diff_Pen
    Width_Param_Diff_Pos = CostParameters.CostParametersGA.Width_Diff_Pos
    Width_Param_Diff_Neg = CostParameters.CostParametersGA.Width_Diff_Neg
    Width_Param_Pen = CostParameters.CostParametersGA.Width_Diff_Pen
    kalinlikgecis = CostParameters.CostParametersGA.kalinlikgecis
    hatgecis = CostParameters.CostParametersGA.hatgecis
    genislikgecis = CostParameters.CostParametersGA.genislikgecis
    hatgenisgec = CostParameters.CostParametersGA.hatgenisgec
    RTFDiff_Param_Positive = CostParameters.CostParametersGA.RTF_Diff_Pos
    RTFDiff_Param_Negative = CostParameters.CostParametersGA.RTF_Diff_Neg
    RTFDiff_Param_Penalty = CostParameters.CostParametersGA.RTF_Diff_Pen
    RTF_Ust_Lim = CostParameters.CostParametersGA.RTF_Ust_Lim
    Penalty_pri = CostParameters.CostParametersGA.Penalty_pri
    Penalty_iccap = CostParameters.CostParametersGA.Penalty_iccap
    Pen_pasi = CostParameters.CostParametersGA.Pen_pasi
    overtimelimit = CostParameters.CostParametersGA.overtimelim
    Deadtimelimit = CostParameters.CostParametersGA.DeadlineForPriority
    overtimepenalty = CostParameters.CostParametersGA.overtimepen

    for j in range(1, len(ProductionSequence)):

        #        percent_thickness = (((Production_Sequence[j].thickness - Production_Sequence[j - 1].thickness) / Production_Sequence[j-1].thickness) * 100)
        percent_thickness = (((ProductionSequence[j].Kalınlık - ProductionSequence[j - 1].Kalınlık) /
                              max(ProductionSequence[j - 1].Kalınlık, ProductionSequence[j].Kalınlık)) * 100)
        if kalinlikgecis >= percent_thickness > 0:
            process_cost_thick += abs(Thickness_Param_Pos * percent_thickness /AA_thickness)
        elif hatgecis >= percent_thickness > kalinlikgecis:
            process_cost_thick += abs(50 * Thickness_Param_Pos * percent_thickness/AA_thickness)

        elif -kalinlikgecis < percent_thickness <= 0:
            process_cost_thick += abs(Thickness_Param_Neg * percent_thickness/AA_thickness)
        elif -hatgecis < percent_thickness <= -kalinlikgecis:
            process_cost_thick += abs(50 * Thickness_Param_Neg * percent_thickness/AA_thickness)

        else:
            process_cost_thick += abs(Thickness_Param_Pen * percent_thickness/AA_thickness)

        #####################################wide change

        #       if Production_Sequence[j].bobin_category == "GA" or Production_Sequence[j].bobin_category == "Zcampain" or Production_Sequence[j].bobin_category == "ZPAR":
        #           genislikgecis = 100
        #       else:
        #           genislikgecis = 250
        #       hatgenisgec = 300
        percent_wide = ProductionSequence[j].Genislik - ProductionSequence[j - 1].Genislik
        #       print(Galvaneal_cizelgesiz[j].width, percent_wide, percent_thickness)
        if genislikgecis >= percent_wide > 0:
            process_cost_wide += abs((Width_Param_Diff_Pos * percent_wide / AA_width))
        elif hatgenisgec >= percent_wide > genislikgecis:
            process_cost_wide += abs(5 * (Width_Param_Diff_Pos * percent_wide / AA_width))
        elif -genislikgecis <= percent_wide <= 0:
            process_cost_wide += abs(Width_Param_Diff_Neg * percent_wide / AA_width)
        elif -hatgenisgec <= percent_wide < -genislikgecis:
            process_cost_wide += abs(5 * Width_Param_Diff_Neg * percent_wide / AA_width)
        else:
            process_cost_wide += abs((Width_Param_Pen * percent_wide / AA_width))
        #
        # ############################################RTF Change
        if ((ProductionSequence[j - 1].RTF_Max < ProductionSequence[j].RTF_Min) or (
                ProductionSequence[j].RTF_Max < ProductionSequence[j - 1].RTF_Min)):
            Interval_Param = 0
        else:
            Interval_Param = 1

        RTF_Fark = (ProductionSequence[j - 1].RTF_Ort - ProductionSequence[j].RTF_Ort)
        RTF_Ort = (ProductionSequence[j - 1].RTF_Ort + ProductionSequence[j].RTF_Ort) / 2

        if 0 < RTF_Fark <= RTF_Ust_Lim:
            RTF_Fark_Cost += (RTFDiff_Param_Negative * RTF_Fark * RTF_Ort / (AA_RTF*AA_RTF_Ort))
        elif -RTF_Ust_Lim <= RTF_Fark <= 0:
            RTF_Fark_Cost += abs((RTFDiff_Param_Positive * RTF_Fark * RTF_Ort / (AA_RTF*AA_RTF_Ort)))
        else:
            RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTF_Fark * RTF_Ort/(AA_RTF*AA_RTF_Ort))

        if Interval_Param == 0:
            if ProductionSequence[j - 1].RTF_Max < ProductionSequence[j].RTF_Min:
                RTFDiff_Int_Param = abs(ProductionSequence[j].RTF_Min - ProductionSequence[j - 1].RTF_Max)
                RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTFDiff_Int_Param * RTF_Ort / (AA_RTF*AA_RTF_Ort))
            else:
                RTFDiff_Int_Param = abs(ProductionSequence[j - 1].RTF_Min - ProductionSequence[j].RTF_Max)
                RTF_Fark_Cost += abs(RTFDiff_Param_Penalty * RTFDiff_Int_Param * RTF_Ort / (AA_RTF*AA_RTF_Ort))

        ###############################################Inner diam -passivizasyon değişimi

        # if (ProductionSequence[j].inner_diameter != ProductionSequence[j-1].inner_diameter):
        #             counteri = counteri + 1
        if (ProductionSequence[j].Passivizasyon != ProductionSequence[j-1].Passivizasyon):
            counterj = counterj + 1
        # # ################################priority
        priority_cost = priority_cost + abs(ProductionSequence[j].Oncelik * CostParameters.Penalty_pri * j)/AA_pri
        #
        # #
        #################################################3

        hız_fark_cost = hız_fark_cost + abs((ProductionSequence[j - 1].CGL_hız - ProductionSequence[
            j].CGL_hız)) * CostParameters.Speed_Diff_Pos / AA_speed
    # ######################################################## over time

  # #          print(overtime_cost, abs((Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time).total_seconds() / 3600 ))
    #           print(Production_Sequence[j].StartTime - Production_Sequence[j].last_process_time)
    #           print(Production_Sequence[j-1].roll_id, Production_Sequence[j-1].StartTime, Production_Sequence[j-1].EndTime, Production_Sequence[j-1].processTime, "Soğumamış ")


    # ########################################################priority cost
    #     for i in range(len(ProductionSequence)):
    # #               print(StartEnd[i].StartTime, "----", StartEnd[i].EndTime)
    #         if ProductionSequence[j].Oncelik == 99:
    #             if(((ProductionSequence[j].EndTime - ProductionSequence[0].StartTime).total_seconds())/ 3600) >= Deadtimelimit:
    #                 priority_cost += (((ProductionSequence[j].EndTime - ProductionSequence[0].StartTime).total_seconds() / 3600) - Deadtimelimit) * CostParameters.DeadlineForPriorityPen
    # # # ########## Sıfırıncı bobin in overtime maliyeti
    Costs = [0.2*process_cost_thick, 0.6*process_cost_wide, 0.1*RTF_Fark_Cost, 0.1*hız_fark_cost, priority_cost, counterj * abs(Pen_pasi)]
    # process_cost = process_cost_thick + process_cost_wide + RTF_Fark_Cost + priority_cost + hız_fark_cost + overtime_cost + \
    #                counteri * abs(Penalty_iccap) + counterj * abs(Pen_pasi)

    return Costs
