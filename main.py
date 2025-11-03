from cyber import CyberAgent
from special_agent import FieldAgent

squad = [FieldAgent("david",5,"galil"),
         CyberAgent("gad",9,"hacking")]

def show_reports(lst):
    for i in lst:
        i.report()

show_reports(squad)
