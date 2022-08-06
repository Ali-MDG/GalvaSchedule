import pandas as pd
import numpy as np
import Roll
#import exception
import ntpath

class readfile:

    def __init__(self, job_list):
        self.job_list = job_list


    def read_schedule_file(self, file_path, line):
        new_read_exception = Exception.Exception()
        xls = pd.ExcelFile(file_path)
        df = xls.parse(xls.sheet_names[0])
        df = df.replace(",", ".", regex=True)
        head, tail = ntpath.split(file_path)
        file_name = "\"" + tail + "\""
        for index, row in df.iterrows():
            try:
                temp_roll_id = str(row["Bobin No"])
                temp_roll_id = temp_roll_id.strip()
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Bobin No")
                break
            try:
                temp_entry_time = row["Başlama Zamanı"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Başlama Zamanı")
                break
            try:
                temp_end_time = row["Bitiş Zamanı"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Bitiş Zamanı")
                break
            try:
                temp_length = row["Uzunluk"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Uzunluk")
                break

            try:
                temp_thickness = row["Kalınlık[B] (MM)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Kalınlık[B] (MM)")
                break
            try:
                temp_width = row["Genişlik[B] (MM)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Genişlik[B] (MM)")
                break

            try:

                temp_Quality= row["Kalite[B]"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Kalite[B]")
                break
            try:
                temp_pasivization_type = row["Pas. Tipi[B]"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Pas. Tipi[B]")
                break
            try:
                temp_RTF_Ortalama = row["RTF Ort. Sıc.[B] (GC)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "RTF Ort. Sıc.[B] (GC)")
                break
            try:
                temp_RTF_Max = row["RTF Maksimum.  (°C)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "RTF Maksimum.  (°C)")
                break
            try:
                temp_RTF_Min = row["RTF Minumum.  (°C)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "RTF Minumum.  (°C)")
                break
            try:
                temp_cover_type = str(row["Kaplama Tipi[H]"])
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Kaplama Tipi[H]")
                break
            try:
                temp_surface_group = row["yüzey gr.[H]"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "yüzey gr.[H]")
                break
            try:
                temp_priority = row["Öncelik[H]"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "Öncelik[H]")
                break
            try:
                temp_avarage_speed = row["CGL Maks. Hız[H] (m/dk)"]
            except LookupError:
                new_read_exception.raise_lookup_exception(file_name, "CGL Maks. Hız[H] (m/dk)")
                break

            temp_roll = Roll.Roll(temp_roll_id, temp_entry_time, temp_end_time, temp_length, temp_thickness,temp_width,
                                  temp_Quality, temp_pasivization_type,temp_RTF_Ortalama,temp_RTF_Max,temp_RTF_Min,temp_cover_type,
                                  temp_surface_group,temp_priority,temp_avarage_speed)
            self.job_list.append(temp_roll)
        return new_read_exception.read_file_error
