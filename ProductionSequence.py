class ProductionSequence:
    def __init__(self, BobinNo, starttime, endtime, uzunluk, kalınlık, genislik, hrc_kalite, kalite, passType,
                    rtf_ort, rtf_max, rtf_min, kaplamatipi, yuzeygrup, oncelik, cglhız):
        self.BobinNo = BobinNo
        self.StartTime = starttime
        self.EndTime = endtime
        self.Uzunluk = uzunluk
        self.Kalınlık = kalınlık
        self.Genislik = genislik
        self.HRC_kalite = hrc_kalite
        self.Kalite = kalite
        self.Passivizasyon = passType
        self.RTF_Ort = rtf_ort
        self.RTF_Max = rtf_max
        self.RTF_Min = rtf_min
        self.Kaplama_Tipi = kaplamatipi
        self.YuzeyGrup = yuzeygrup
        self.Oncelik = oncelik
        self.CGL_hız = cglhız



