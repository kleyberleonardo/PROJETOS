from tkinter import *
from tkinter import Tk ,  ttk
from tkinter import messagebox



# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"  # letra / letters
co5 = "#d3d3d3"  # instruções / cinza

# criação da janela ------------------

janela = Tk()
janela.title('CPF VALIDATOR')
janela.geometry('310x300')
janela.configure(background = co1)
janela.resizable(width=FALSE, height=FALSE)

# divisão da janela ------------------

parte_cima = Frame(janela , width=310 , height=50, bg=co1, relief='flat')
parte_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

parte_baixo = Frame(janela , width=310 , height=250, bg=co1, relief='flat')
parte_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando parte de cima ------------------

label_nome= Label(parte_cima, text='VALIDADOR DE CPF', anchor=NE, font=('Ivy 18'), bg=co1,fg=co4)
label_nome.place(x=37, y=5)

label_linha= Label(parte_cima, width=299, anchor=NW, font=('Ivy 1'), bg=co2,fg=co4)
label_linha.place(x=3, y=45)

# configurando ação ------------------


def verifica_cpf():
    
    cpf = ent_cpf.get()
    qnt_caract = int(len(cpf))
    if cpf.isnumeric() and qnt_caract ==11:
        pass
    else:
        messagebox.showwarning('ERRO', message = 'Caracteres ou Quantidade de Caracteres Inválidos\nVerifique e Tente Novamente!')
    cpfnovo = cpf[:9:1]
    listcpf = list(cpfnovo)  
    contagem = [10,9,8,7,6,5,4,3,2]
    listafinal = [int(i) for i in listcpf]
    n1,n2,n3,n4,n5,n6,n7,n8,n9 = listafinal
    d1,d2,d3,d4,d5,d6,d7,d8,d9 = contagem
    r1 = n1 * d1
    r2 = n2 * d2
    r3 = n3 * d3
    r4 = n4 * d4
    r5 = n5 * d5
    r6 = n6 * d6
    r7 = n7 * d7
    r8 = n8 * d8
    r9 = n9 * d9
    soma = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    elif digito1 < 9:
        digito1 = digito1
    listafinal.append(digito1)
    contagem2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = listafinal
    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 = contagem2
    z1 = m1 * s1
    z2 = m2 * s2
    z3 = m3 * s3
    z4 = m4 * s4
    z5 = m5 * s5
    z6 = m6 * s6
    z7 = m7 * s7
    z8 = m8 * s8
    z9 = m9 * s9
    z10 = m10 * s10
    soma2 = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10
    digito2 = 11 - (soma2 % 11)
    if digito2 > 9:
        digito2 = 0
    elif digito2 < 9:
        digito2 = digito2
    listafinal.append(digito2)
    listafinal = [str(i) for i in listafinal]
    listatotal = "".join(listafinal)
    if listatotal == cpf:
        messagebox.showinfo('SUCESS', message ='CPF Válido')
    else:
        messagebox.showwarning('ERROR', message ='CPF Inválido\nVerifique a numeração e tente novamente')
        

# configurando entrada de CPF ------------------

label_nome = Label(parte_baixo, text='Insira um CPF para validar', anchor=NW, font=('Arial 12 bold'), bg=co1,fg=co4)
label_nome.place(x=53, y=20)

ent_cpf = Entry (parte_baixo, width=25, justify ='left', font=("", 15), highlightthickness=1, relief='solid')
ent_cpf.place(x=15, y=50)

instrucao = Label(parte_baixo, text='INSIRA APENAS NÚMEROS', anchor=NW, font=('Arial 8 bold'), bg=co1,fg=co5)
instrucao.place(x=85, y=80)

# configurando botão de ação ------------------

button_ent = Button(parte_baixo, text='VERIFICAR', command = verifica_cpf,  width=27, height=1, anchor=CENTER, font=('Ivy 12 bold'), bg=co2,fg=co1, relief='raised', overrelief='ridge' )
button_ent.place(x=15, y=190)


janela.mainloop()

