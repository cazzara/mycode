
"""
neo.py

Author : Chris Azzara
Purpose : NEO Object to store data gathered from NASA's open API
"""
AU_M = 149597870700

class Neo:
    
    def __init__(self, name, ref_id, approach_data, estimated_size, is_dangerous, url, magnitude):
        self.name = name
        self.ref_id = ref_id
        self.approach_data = approach_data
        self.estimated_size = estimated_size
        self.is_dangerous = is_dangerous
        self.url = url
        self.magnitude = magnitude

    def displayLine(self):
        miles = self.approach_data['miss_distance']['miles']
        kms = self.approach_data['miss_distance']['kilometers']
        aus = self.approach_data['miss_distance']['astronomical']
        lunar = self.approach_data['miss_distance']['lunar']
        mph = self.approach_data['relative_velocity']['miles_per_hour']
        kph = self.approach_data['relative_velocity']['kilometers_per_hour']
        kps = self.approach_data['relative_velocity']['kilometers_per_second']
        print("{:^20}\t{:<20,.4f}\t{:<20,.4f}\t{:<20.4f}{:<20.4f}{:<20,.4f}{:<20,.4f}{:<20.4f}".format(self.name,   float(miles),\
                                                                                                       float(kms),  float(aus), \
                                                                                                       float(lunar),float(mph), \
                                                                                                       float(kph),  float(kps)))

    def displayApproachInfo(self):
        print("Passing by {1} on {0}".format(self.approach_data['close_approach_date'], self.approach_data['orbiting_body']))
        print("\n**********Miss Distance**********")
        print("{:^20} {:^20} {:^20} {:^20}".format("Miles", "Kilometers", "Astronomical Units" , "Lunar Distance"))
        miles = self.approach_data['miss_distance']['miles']
        kms = self.approach_data['miss_distance']['kilometers']
        aus = self.approach_data['miss_distance']['astronomical']
        lunar = self.approach_data['miss_distance']['lunar']
        print("{:<20,.4f}\t{:<20,.4f}\t{:<20.4f}\t{:<20.4f}".format(float(miles), float(kms), float(aus), float(lunar)))
        print("\n**********Relative Distance**********")
        print("{:^20} {:^20} {:^20}".format("Miles per Hour", "Kilometers per Hour", "Kilometers per Sec"))
        mph = self.approach_data['relative_velocity']['miles_per_hour']
        kph = self.approach_data['relative_velocity']['kilometers_per_hour']
        kps = self.approach_data['relative_velocity']['kilometers_per_second']
        print("{:^20,.4f}\t{:<20,.4f}\t{:<20.4f}".format(float(mph), float(kph), float(kps)))

    def display(self):
        print("Name: {} ----- JPL REF ID: {}".format(self.name, self.ref_id))
        print("Threat To Humanity? - {}".format(self.is_dangerous))
        print("More Info At - {}".format(self.url))
        self.displayApproachInfo()
        #print(self.estimated_size)
    
