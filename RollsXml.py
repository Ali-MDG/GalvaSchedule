import xml.dom.minidom
import datetime
import Roll
import math

class RollsXml:


    def __init__(self):
        self.job_list = []
        self.programs = []

    def process_xml_file(self, line):
        try:
            self.xml_file = xml.dom.minidom.parse("rolls.xml")
            self.schedule_tables = self.xml_file.getElementsByTagName("ScheduleTable")
        except:
            return False
        for item in self.schedule_tables:
            try:
                temp_BobinNo = item.getElementsByTagName("BatchNumber")[0].childNodes[0].data
                temp_BobinNo = temp_BobinNo.strip()
            except:
                temp_BobinNo = ""
            try:
                temp_weight = float(item.getElementsByTagName("Weight")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_weight = math.nan
            try:
                temp_thickness = float(item.getElementsByTagName("Thickness")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_thickness = math.nan
            try:
                temp_width = float(item.getElementsByTagName("Width")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_width = math.nan
            try:
                temp_real_thickness = float(item.getElementsByTagName("A373_B")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_real_thickness = math.nan

            try:
                temp_program_order = int(item.getElementsByTagName("ProgramOrder")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_program_order = 255
            try:
                temp_program_number = int(item.getElementsByTagName("ProgramNumber")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_program_number = 255
            try:
                temp_batch_order = int(item.getElementsByTagName("BatchOrder")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_batch_order = 255
            try:
                temp_status = int(item.getElementsByTagName("Status")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_status = 0
            try:
                temp_entry_time = str(item.getElementsByTagName("EntryTime")[0].childNodes[0].data.replace(",", "."))
                temp_entry_time = datetime.datetime.strptime(temp_entry_time, "%Y-%m-%d %H:%M:%S")
            except:
                temp_entry_time = math.nan
            try:
                temp_Loading_Time = str(item.getElementsByTagName("LoadingTime")[0].childNodes[0].data.replace(",", "."))
                temp_Loading_Time = datetime.datetime.strptime(temp_Loading_Time, "%Y-%m-%d %H:%M:%S")
            except:
                temp_Loading_Time = math.nan
            try:
                temp_last_process_time = str(item.getElementsByTagName("A453_B")[0].childNodes[0].data.replace(",", "."))
                temp_last_process_time = datetime.datetime.strptime(temp_last_process_time, "%Y-%m-%d %H:%M:%S")
            except:
                temp_last_process_time = math.nan

            try:
                temp_length = float(item.getElementsByTagName("A366_B")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_length = 1
            try:
                temp_pasivization_type = item.getElementsByTagName("A011_H")[0].childNodes[0].data
            except:
                temp_pasivization_type = ""
            try:
                temp_inner_diameter = float(item.getElementsByTagName("A308_H")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_inner_diameter = math.nan
            try:
                temp_surface_group = int(item.getElementsByTagName("A007_H")[0].childNodes[0].data)
            except:
                temp_surface_group = math.nan

            try:
                temp_priority = int(item.getElementsByTagName("A489_H")[0].childNodes[0].data)
            except:
                temp_priority = math.nan
            try:
                temp_cover_type = item.getElementsByTagName("A008_H")[0].childNodes[0].data
            except:
                temp_cover_type = ""
            try:
                temp_quality = item.getElementsByTagName("A004_H")[0].childNodes[0].data
            except:
                temp_quality = ""

            try:
                temp_avarage_speed = float(item.getElementsByTagName("A112_H")[0].childNodes[0].data.replace(",", "."))
                if temp_avarage_speed == 0:
                    temp_avarage_speed = 95
            except:
                temp_avarage_speed = math.nan
            try:
                temp_rtf_min = float(item.getElementsByTagName("A559_H")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_rtf_min = math.nan
            try:
                temp_rtf_ortalama = float(item.getElementsByTagName("A120_H")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_rtf_ortalama = math.nan
            try:
                temp_rtf_max = float(item.getElementsByTagName("A560_H")[0].childNodes[0].data.replace(",", "."))
            except:
                temp_rtf_max = math.nan
            try:
                temp_capacity_suitability = str(item.getElementsByTagName("A607_H")[0].childNodes[0].data)
            except:
                temp_capacity_suitability = ""
            try:
                temp_SPM_Status = str(item.getElementsByTagName("A018_H")[0].childNodes[0].data)
            except:
                temp_SPM_Status = ""
            try:
                temp_Lokasyon = str(item.getElementsByTagName("A510_B")[0].childNodes[0].data)
            except:
                temp_Lokasyon = ""

            temp_roll = Roll.Roll(temp_BobinNo, temp_weight, temp_thickness, temp_real_thickness, temp_width,
                                  temp_program_order,
                                  temp_program_number, temp_batch_order, temp_status, temp_entry_time, temp_Loading_Time, temp_last_process_time,
                                  temp_length, temp_pasivization_type, temp_inner_diameter, temp_surface_group,
                                  temp_priority, temp_cover_type, temp_quality, temp_avarage_speed, temp_rtf_min,
                                  temp_rtf_max, temp_rtf_ortalama,temp_capacity_suitability, temp_SPM_Status, temp_Lokasyon)
            self.job_list.append(temp_roll)
        #self.set_fix_positions()
        return True


