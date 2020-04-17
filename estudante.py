from pessoa import Person
class Student(Person):
    def __init__(self,name, phone, email,ar, course):
        self.ar = ar
        self.course = course
        super().__init__(name, phone, email)

    def monthly_paymant(self,course):
        self.course=course
        if self.course ==1:
            curso=" Engenharia : R$2000,00"
        elif self.course==2:
            curso=" Direito : R$1500,00"
        elif self.course==3:
            curso=" Pedagogia : R$500,00"
        return curso

    def show_info(self, name, phone, email, ar, course, aluno):
        print(aluno)
        #return[self.name, self.phone, self.email, self.ar, self.course]

