class Train:
    """docstring for Train"""
    line_colors = {
        'RD': 'Red',
        'OR': 'Orange',
        'YL': 'Yellow',
        'GR': 'Green',
        'BL': 'Blue',
        'SV': 'Silver',
    }

    def __init__(self, traindict):
        self.car = traindict.get('Car')
        self.destination_code = traindict.get('DestinationCode')
        self.destination_name = traindict.get('DestinationName')
        self.group = traindict.get('Group')
        self.line_code = traindict.get('Line')
        self.location_code = traindict.get('LocationCode')
        self.location_name = traindict.get('LocationName')
        self.minutes_to_train = traindict.get('Min')

    @property
    def line_name(self):
        return Train.line_colors.get(self.line_code, None)


        