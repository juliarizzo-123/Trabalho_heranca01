from estudante import Student
from professor import Teacher
from empregado import Employee
from time import sleep

def msg_erro():
    print('login nao efetuado!')

op = 88
aluno = []
professor = []
ai=0
pi=0
a = []
b = []
c = []
p = []
sss = []
d = []
m = []
da = []
log = False

while op != 0:
    print("~"*30)
    print ('Bem vindo a UNIABCDE. \n O que deseja fazer: \n 1 - Cadastrar Aluno \n 2 - Cadastrar Professor \n 3 - Mostrar Informações \n 4 - Mostrar mensalidades \n 5 - Mostrar dias de trabalho \n 6 - Adicional de periculosidade \n 7 - Criar cadastro\n 8 - Efetuar login\n 0 - Sair do programa ')
    op = int(input('Qual é sua opção: '))
    
    if op == 1 and log == True:
        if ai < 2 :
            print("~"*30)
            print('Cadastrar um aluno: ')
            name = input('Digite o nome: ') 
            phone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            ar = input('Digite o RA: ')
            course = int(input(' 1- Engenharia \n 2- Direito \n 3- Pedagogia\n Digite o curso: '))
            sleep(1)
            a = [name,phone,email,ar,course]
            aluno.append(a)
            b = Student(name,phone,email,ar,course)
            mens = b.monthly_paymant(course,name)
            m.append(mens)
            if ai == 0:
                A = Student(name,phone,email,ar,course)

            elif ai == 1:
                x = Student(name,phone,email,ar,course)

            ai = ai+1

            #print(aluno)
        

        else:
            print(" Maximos de alunos cadastrados")




    elif op == 2 and log == True:
        if pi < 2:
            print("~"*30)
            print('Cadastrar professor: ')
            name = input('Digite o nome: ') 
            phone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            salary = int(input('Salario: '))
            print ('digite a data: ')
            ano= int(input('Ano de inicio: '))
            mes= int(input('Mes de inicio: '))
            dia= int(input('Dia de inicio: '))
            da = [ano, mes, dia]
            course = int(input(' 1- Engenharia \n 2- Direito \n 3- Pedagogia \n Digite o curso ministrado: '))
            c = [name,phone,email,salary,da,course]
            professor.append(c)
            p = Teacher(name,phone,email,salary,da,course)
            sala = p.additional_health_hazard(salary,course,name)
            sss.append(sala)
            dias = p.work_days( da, name)
            d.append(dias)
        
            if pi == 0:
                P = Teacher(name,phone,email,salary,da,course)
            
            elif pi == 1:
                p1 = Teacher(name,phone,email,salary,da,course)
            
            
                
            pi = pi+1
        else:
            print("Maximos de professores cadastrados")


    elif op == 3 and log == True :
        print("Mostrar Informações:")
        ec = int(input(' 1 - Mostrar Informações dos Alunos \n 2 - Mostrar Informações dos Professores \nQual sua opção: '))
        print("~"*30)
        if ec == 1:
            print(A.show_info( A.name, A.phone, A.email, A.ar, A.course))
            print(x.show_info( x.name, x.phone, x.email, x.ar, x.course))
            

        else:
            print('Mostrar Informações dos Professores:')
            print(P.show_info(P.name, P.phone, P.email, P.salary, P.da,P.course))
            print(p1.show_info(p1.name, p1.phone, p1.email, p1.salary, P.da,p1.course))

    elif op == 4 and log == True :
        print("\nAs mensaidades são:\n ")
        print(A.monthly_paymant( A.course, A.name))
        print(x.monthly_paymant( x.course, x.name ))
        #print(m)

    elif op == 5 and log == True :
        print("\nMostrar dias de trabalho:\n") 
        print(P.work_days( P.da, P.name))
        print(p1.work_days( p1.da, p1.name))

    elif op == 6 and log == True:
        print("\nAdicional de periculosidade:")
        print(P.additional_health_hazard(P.salary,P.course,P.name))
        print(p1.additional_health_hazard(p1.salary,p1.course,p1.name))
    
    elif op == 7:
        print('Criar cadastro: ')
        login = input('Qual o login: ')
        senha = input('Qual a senha: ')
        l=open('login.txt','w')
        l.write(login)
        l.close()
        sen=open('senha.txt','w')
        sen.write(senha)
        sen.close()
    
    elif op == 8:
        print('Efetuar cadastro:')
        login = input('Qual o login: ')
        senha = input('Qual a senha: ')
        l = open ('login.txt', 'r') 
        with open ('login.txt', 'r') as l:
            logar = l.readline()
        sen = open ('senha.txt', 'r') 
        with open ('senha.txt', 'r') as sen:
            comf= sen.readline()

        if login == logar and senha == comf:
            print('Login efetuado!')
            log = True

        else:
            print('login ou senha invalidos')
    
    elif op == 1 and log == False:
        msg_erro()

    elif op == 2 and log == False:
        msg_erro() 

    elif op == 3 and log == False:
        msg_erro()
    elif op == 4 and log == False:
        msg_erro()
    elif op == 5 and log == False:
        msg_erro()
    elif op == 6 and log == False:
        msg_erro()
    else:
        print("\n finalizando....\n")


    