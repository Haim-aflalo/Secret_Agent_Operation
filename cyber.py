from agent import Agent


class CyberAgent(Agent):
    def __init__(self,code_name,clearance_level,speciality):
        super().__init__(code_name,clearance_level)
        self.speciality = speciality

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._Agent__clearance_level}. Speciality: {self.speciality}")
