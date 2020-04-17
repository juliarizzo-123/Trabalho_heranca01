from pessoa import Person
import time
class Employee(Person):
    def __init__(self,name, phone, email, salary, start_day):
        self.salary = salary
        self.start_date = start_day
        super().__init__(name, phone, email)
   
    def work_days(self, ano , mes, dia):
        
        import datetime

        datapadrao = datetime.date(ano, mes, dia)
        hoje = datetime.date.today()

        if datapadrao > hoje:
            delta = datapadrao - hoje

        elif datapadrao <= hoje:
            delta = hoje - datapadrao

        return delta.days