
"""
neo.py

Author : Chris Azzara
Purpose : NEO Object to store and print data gathered from NASA's open API
"""


class Neo:
    
    def __init__(self, name, ref_id, approach_data, estimated_size, is_dangerous, url, magnitude):
        self.name = name
        self.ref_id = ref_id
        self.approach_data = approach_data
        self.estimated_size = estimated_size
        self.is_dangerous = is_dangerous
        self.url = url
        self.magnitude = magnitude

    def displayLineMetric(self):
        date = self.approach_data['close_approach_date']
        kms = self.approach_data['miss_distance']['kilometers']
        aus = self.approach_data['miss_distance']['astronomical']
        kph = self.approach_data['relative_velocity']['kilometers_per_hour']
        dia_meters = self.estimated_size['meters']['estimated_diameter_max']
        dia_kilometers = self.estimated_size['kilometers']['estimated_diameter_max']
        print("{:<20}{:<10}\t{:<20,.4f}\t{:<20.4f}{:<25,.4f}{:<25,.4f}{:<25,.4f}".format(self.name, date,  float(kms),\
                                                                                                       float(aus),  float(kph), \
                                                                                                       float(dia_meters),float(dia_kilometers)))
    def displayLineImperial(self):
        date = self.approach_data['close_approach_date']
        miles = self.approach_data['miss_distance']['miles']
        aus = self.approach_data['miss_distance']['astronomical']
        mph = self.approach_data['relative_velocity']['miles_per_hour']
        dia_feet = self.estimated_size['feet']['estimated_diameter_max']
        dia_miles = self.estimated_size['miles']['estimated_diameter_max']
        print("{:<20}{:<10}\t{:<20,.4f}\t{:<20.4f}{:<25,.4f}{:<25,.4f}{:<25,.4f}".format(self.name, date, float(miles), float(aus),\
                                                                                                       float(mph), float(dia_feet), float(dia_miles)))


    
