
class Weather:
    """docstring for Weather"""
    def __init__(self, weatherdict):
    	working_dictionary = weatherdict.get('currently')
    	self.temperature = working_dictionary.get('temperature')
        # self.temperature = weatherdict.get('temperature')
        # self.condition = weatherdict.get('summary')
        # self.icon = weatherdict.get('icon')