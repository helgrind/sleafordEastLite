#timetable = {}
#macros = []
#inputs = []
#outputs =[]


class Simulator:
    def __init__(self, app) -> None:
        self.app = app
        self.app.timetable = {}
        self.app.macros = []
        self.app.inputs = []
        self.app.outputs =[]
        
    def startup(self):
        """
        Initialise the simulator
        """
        pass #TODO Implement sim initialisation
