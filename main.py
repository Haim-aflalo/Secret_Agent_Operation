from cyber import CyberAgent
from special_agent import FieldAgent
from agent import Agent
squad = [FieldAgent("david",5,"galil"),
         CyberAgent("gad",9,"hacking")]

def show_reports(lst):
    for i in range(len(lst)):
        lst[i].report()

show_reports(squad)

