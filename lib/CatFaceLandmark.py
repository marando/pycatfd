class CatFaceLandmark:
    CHIN = 0
    LEFT_EYE = 1
    LEFT_OF_LEFT_EAR = 2
    LEFT_OF_RIGHT_EAR = 3
    NOSE = 4
    RIGHT_EYE = 5
    RIGHT_OF_LEFT_EAR = 6
    RIGHT_OF_RIGHT_EAR = 7

    def __init__(self):
        pass

    @staticmethod
    def all():
        return [
            {
                'value': CatFaceLandmark.CHIN,
                'name': 'Chin'
            },
            {
                'value': CatFaceLandmark.LEFT_EYE,
                'name': 'Left Eye'
            },
            {
                'value': CatFaceLandmark.LEFT_OF_LEFT_EAR,
                'name': 'Left of Left Ear'
            },
            {
                'value': CatFaceLandmark.LEFT_OF_RIGHT_EAR,
                'name': 'Left of Right Ear'
            },
            {
                'value': CatFaceLandmark.NOSE,
                'name': 'Nose'
            },
            {
                'value': CatFaceLandmark.RIGHT_EYE,
                'name': 'Right Eye'
            },
            {
                'value': CatFaceLandmark.RIGHT_OF_LEFT_EAR,
                'name': 'Right of Left Ear'
            },
            {
                'value': CatFaceLandmark.RIGHT_OF_RIGHT_EAR,
                'name': 'Right of Right Ear'
            }
        ]
