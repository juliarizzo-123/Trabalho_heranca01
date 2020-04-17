from empregado import Employee
class Teacher(Employee):
       def __init__(self,name,phone,email,salary,start_day,course):
              self.course = course
              super().__init__(name,phone,email,salary,start_day)
       
       
       def  additional_health_hazard(self, salary,course):
              
              if  course == 1:
                     salary = (self.salary + (salary*0.3))

              elif course == 2:
                     salary = (self.salary + (salary*0.05))
            
              else:
                     salary = (self.salary + (salary*0.15))

              return salary
              
       def show_info(self,name, phone, email, salary,start_day, course, professor): 
              print(professor)
              #return [self.name, self.phone, self.email, self.salary, self.start_date, self.course]
 