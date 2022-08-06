import datetime
import CostParameters
class Roll:
    rollCount = 0

    def __init__(self, BobinNo,thickness, width,
                 entry_time, end_time, length, pasivization_type,surface_group, priority, cover_type,
                 Quality, avarage_speed ,RTF_Min, RTF_Max, RTF_Ortalama):
        self.BobinNo = BobinNo
        self.thickness = thickness
        self.width = width
        self.entry_time = entry_time
        self.end_time = end_time
        self.length = length
        self.pasivization_type = pasivization_type
        self.surface_group = surface_group
        self.priority = priority
        self.cover_type = cover_type
        self.Quality = Quality
        self.avarage_speed = avarage_speed
        self.RTF_Min = RTF_Min
        self.RTF_Max = RTF_Max
        self.RTF_Ortalama = RTF_Ortalama
        self.bobin_category = ""
        Roll.rollCount += 1