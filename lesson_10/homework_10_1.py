class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
       # self.programming_language = programming_language
        self.team_size = team_size


team_lead = TeamLead("Slava", 7000, "IT", "Python", 8)
print(TeamLead.__mro__)
print()

# version 1
print("----- version 1", "-"*35)
print("attribute 'name':", hasattr(team_lead, "name"))
print("attribute 'salary':", hasattr(team_lead, "salary"))
print("attribute 'department':", hasattr(team_lead, "department"))
print("attribute 'programming_language':", hasattr(team_lead, "programming_language"))
print("attribute 'team_size':", hasattr(team_lead, "team_size"))
print("attribute 'prog_lang':", hasattr(team_lead, "prog_lang"))
print("-"*50)
print("team_lead is an instance of the Employee class:", isinstance(team_lead, Employee))
print("team_lead is an instance of the Manager class:", isinstance(team_lead, Manager))
print("team_lead is an instance of the Developer class:", isinstance(team_lead, Developer))
print("team_lead is an instance of the TeamLead class:", isinstance(team_lead, TeamLead))
print("-"*50)
print()

# version 2
print("----- version 2", "-"*35)
assert hasattr(team_lead, "name")
assert hasattr(team_lead, "salary")
assert hasattr(team_lead, "department")
assert hasattr(team_lead, "programming_language")
assert hasattr(team_lead, "team_size")
assert isinstance(team_lead, Employee)
assert isinstance(team_lead, Manager)
assert isinstance(team_lead, Developer)
assert isinstance(team_lead, TeamLead)
print("All tests passed!")
print("-"*50)
print()

# version 3
print("----- version 3", "-"*35)
attributes = {
    "name": "Employee",
    "salary": "Employee",
    "department": "Manager",
    "programming_language": "Developer",
    "team_size": "TeamLead"
}

for attribute, class_name in attributes.items():
    print(f"{attribute}: {getattr(team_lead, attribute)} - attribute of {class_name} class")

