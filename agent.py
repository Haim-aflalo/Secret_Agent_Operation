class Agent:

    def __init__(self,code_name,clearance_level = 0):
        self.code_name = code_name
        self._clearance_level = clearance_level

    def get_clearance_level(self):
        return self._clearance_level

    def set_clearance_level(self,level):
        if 0 < level < 11:
            self._clearance_level = level

    def report(self):
        return f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}"


