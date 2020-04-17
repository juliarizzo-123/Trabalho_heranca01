from estudante import Student
from professor import Teacher
from empregado import Employee
op = 88
aluno = []
professor = []
ai=0
pi=0
a = []
b = []
c = []
p = []
s = []
d = []
m = []

while op != 0:

    print ('Bem vindo a UNIABCDE. \n O que deseja fazer: \n 1 - Cadastrar Aluno \n 2 - Cadastrar Professor \n 3 - Mostrar Informações \n 4 - Mostrar mensalidades \n 5 - Mostrar dias de trabalho \n 6 - Adicional de periculosidade \n 0 - Sair do programa ')
    op = int(input('Qual é sua opção: '))
    if op == 1:
        if ai < 2:

            print('cadastrar um aluno: ')
            name = input('Digite o nome: ') 
            phone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            ar = input('Digite o RA: ')
            course = int(input(' 1- Engenharia \n 2- Direito \n 3- Pedagogia\n Digite o curso: '))
            a = [name,phone,email,ar,course]
            aluno.append(a)
            b = Student(name,phone,email,ar,course)
            mens = b.monthly_paymant(course)
            m.append(mens)
            ai = ai+1
            #print(aluno)
         

        else:
            print(" Maximos de alunos cadastrados")




    elif op == 2:
        if pi < 2:
            print('Cadastrar professor: ')
            name = input('Digite o nome: ') 
            phone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            salary = int(input('Salario: '))
            start_day = print ('digite a data: ')
            ano= int(input('Ano de inicio: '))
            mes= int(input('Mes de inicio: '))
            dia= int(input('Dia de inicio: '))
            course = int(input(' 1- Engenharia \n 2- Direito \n 3- Pedagogia \n Digite o curso ministrado: '))
            c = [name,phone,email,salary,start_day,course]
            professor.append(c)
            p = Teacher(name,phone,email,salary,start_day,course)
            sala = p.additional_health_hazard(salary,course)
            s.append(sala)
            dias = p.work_days( ano , mes, dia)
            d.append(dias)
            pi = pi+1
        else:
            print("Maximos de professores cadastrados")


    elif op == 3:
        print("Mostrar Informações:")
        ec = int(input(' 1 - Mostrar Informações dos Alunos \n 2 - Mostrar Informações dos Professores \nQual sua opção: '))
            
        if ec == 1:
            print (aluno)

        else:
            print('Mostrar Informações dos Professores:')
            print(professor)
           


    elif op == 4:
        print("Mostrar messalidades:")
        print(m)

    elif op == 5:
        print("Mostrar dias de trabalho:")
        print(d)



    elif op == 6:
        print("Adicional de periculosidade:")
        print(s)
        
    else:
        print("finalizando....")

