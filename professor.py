from empregado import Employee
class Teacher(Employee):
       def __init__(self,name,phone,email,salary,da,course):
              self.course = course
              super().__init__(name,phone,email,salary,da)
       
       
       def  additional_health_hazard(self, salary,course,name):
              
              if  self.course == 1:
                     self.adicional = self.salary*0.3

              elif self.course == 2:
                     self.adicional = self.salary*0.05
            
              else:
                     self.adicional = self.salary*0.15
              
              self.professor = ("Professor: "+name+ " \nAdicional de periculosidade "+str( self.adicional )+"\n")
              return self.professor
              
              
       def show_info(self,name, phone, email, salary,da, course): 
              self.professor = ("Nome do professor: "+name+ "\nTelefone de contato: "+str(phone)+ "\nEmail: "+str(email)+ "\nsalario: "+str(salary)+"\nDias de trabalho: "+str(da)+"\nCurso: "+str(course)+"\n")
              return self.professor        