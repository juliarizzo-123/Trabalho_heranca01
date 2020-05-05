from pessoa import Person
class Student(Person):
    def __init__(self,name, phone, email,ar, course):
        self.ar = ar
        self.course = course
        super().__init__(name, phone, email)

    def monthly_paymant(self,course,name):
        self.course=course
        if self.course ==1:
            curso=" Engenharia: R$2000,00"
        elif self.course==2:
            curso=" Direito: R$1500,00"
        elif self.course==3:
            curso=" Pedagogia: R$500,00"
        self.aluno = ("Aluno: "+name+ " Curso: "+str( curso )+"\n")
        return self.aluno

    def show_info(self, name, phone, email, ar, course):
        self.aluno = ("Nome do aluno: "+name+ "\nTelefone de contato: "+str(phone)+ "\nEmail: "+str(email)+ "\nRA: "+str(ar)+ "\nCurso: "+str(course)+"\n")
        return self.aluno