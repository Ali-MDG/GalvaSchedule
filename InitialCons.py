import CostParameters
import math
class InitialCons:
    def __init__(self, roll_list):
        self.roll_list = roll_list

    def Initial_Sequence(self):
        InitialProcessSeq = []
        BobinListeGroup = []
        BobinListe_P99 = []
        BobinListe_rest = []
        Group_Num = 0
        BobinListe_P99 = [x for x in self.roll_list if x.Oncelik == 99]
        BobinListe_rest = [x for x in self.roll_list if x.Oncelik != 99]

        Group_Num = math.ceil(
            (max([i.Genislik for i in BobinListe_rest]) - min(
                [i.Genislik for i in BobinListe_rest])) / CostParameters.wide_diff)
        for j in range(Group_Num):
            BobinListeGroup.append([x for x in BobinListe_rest if
                                    (max([i.Genislik for i in
                                          BobinListe_rest]) - CostParameters.wide_diff * j) >= x.Genislik > (
                                            max([i.Genislik for i in BobinListe_rest]) - CostParameters.wide_diff * (
                                                j + 1))])
        if len(BobinListe_P99) != 0:
            BobinListe_P99 = sorted(BobinListe_P99, key=lambda BobinListe_P99: BobinListe_P99.Kalınlık, reverse=False)
            BobinListe_P99 = [BobinListe_P99]

        for j in range(Group_Num):
            BobinListeGroup[j].sort(key=lambda x: x.Kalınlık, reverse=False)
        if len(BobinListe_P99) != 0:
            InitialProcessSeq = BobinListe_P99 + BobinListeGroup
        else:
            InitialProcessSeq = BobinListeGroup

        FinalList = []
        for rolls in InitialProcessSeq:
            FinalList += [x for x in rolls]
        return FinalList, InitialProcessSeq