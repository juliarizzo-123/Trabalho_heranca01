from pessoa import Person
import time
class Employee(Person):
    def __init__(self,name, phone, email, salary, da):
        self.salary = salary
        self.da = da
        super().__init__(name, phone, email)
   
    def work_days(self, da, name):
        
        import datetime

        datapadrao = datetime.date(da[0], da[1], da[2])
        hoje = datetime.date.today()

        if datapadrao > hoje:
            delta = datapadrao - hoje

        elif datapadrao <= hoje:
            delta = hoje - datapadrao
        
        self.professor = ("Professor: "+name+ " \ndias de trabalho: "+str( delta )+"\n")
        
        return self.professor