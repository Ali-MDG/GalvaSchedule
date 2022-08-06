import CostParameters
def CalStartEnd(Sequence):
    try:
        Sequence[0].StartTime = CostParameters.CostParameters.ScheduleStartTime
        Sequence[0].EndTime = Sequence[0].StartTime + Sequence[0].processTime
    except:
        for i in range(1, len(Sequence)):
            try:
                Sequence[i].StartTime = Sequence[i - 1].EndTime
                Sequence[i].EndTime = Sequence[i].StartTime + Sequence[i].processTime
            except:
                pass
