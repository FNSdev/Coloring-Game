class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def get_color(cls, color_code):
        if color_code == 'P':
            return cls.PINK
        elif color_code == 'B':
            return cls.BLUE
        elif color_code == 'G':
            return cls.GREEN
        elif color_code == 'Y':
            return cls.YELLOW
        elif color_code == 'R':
            return cls.RED
        else:
            raise ValueError('Color code is not correct')
