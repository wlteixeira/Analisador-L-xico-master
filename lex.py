import ply.lex as lex
import ply.yacc as yacc
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

errors = []
reserved_funk = ['fatorial']

reserved = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'para': 'PARA',
    'funk': 'FUNK',
    'retorno': 'RETORNO',
    'ifsuldeminas': 'IFSULDEMINAS',
    'inicio': 'INICIO',
    'compiladores': 'COMPILADORES',
    'fim': 'FIM',
    'int': 'INT',
    'real': 'REAL',
    'bool': 'BOOLEANO',
    'texto': 'CADEIA_CAR',
}

# Define os nomes dos tokens
tokens = [
    'VAR',
    'TIPO',
    'INTEIRO',
    'ABRE_CHAV',
    'FECHA_CHAV',
    'VIRG',
    'PONTO_VIRG',
    'ABRE_PAR',
    'FECHA_PAR',
    'OPER_RELA',
    'OPER_MAT',
    'OPER_ATRIB_IGUAL',
    'ITERADORES',
    'OPER_LOG',
    'NOME_FUNK',
    #'STR_INCOMPLETA',
    #'VAR_ERRO',
    #'NUM_ERRO'
]+ list(reserved.values())

# Expressões regulares para cada token
t_INTEIRO = r'([+-])?\d+'
t_BOOLEANO = r'(true|false)'
t_REAL = r'(([+-])?\d+)[.]\d+'
t_CADEIA_CAR = r'"[^"\n]*"'
t_ABRE_CHAV = r'{'
t_FECHA_CHAV = r'}'
t_VIRG = r','
t_PONTO_VIRG = r';'
t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_OPER_RELA = r'(=|==|!=|<=|>=|<|>)'
t_OPER_MAT = r'(\+|\-|\*|\/|\%)'
t_OPER_ATRIB_IGUAL = r'='
t_ITERADORES = r'(ate|passo)'
t_OPER_LOG = r'(&&|\|\|)'
t_NOME_FUNK = r'[a-zA-Z_]\w*[ ][(].*?[)]'
#t_STR_INCOMPLETA = r'"[^"]*'
#t_VAR_ERRO = r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
#t_NUM_ERRO = r'^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?[^0-9]*$'

def p_programa(p):
    ''' programa : ifsuldeminas compiladores inicio codigos fim'''

def p_ifsuldeminas(p):
    '''ifsuldeminas : IFSULDEMINAS'''

def p_compiladores(p):
    '''compiladores : COMPILADORES'''

def p_inicio(p):
    '''inicio : INICIO'''

def p_fim(p):
    '''fim : FIM'''

def p_codigo_mais(p):
    '''codigos : codigos codigo'''

def p_codigo_simples(p):
    '''codigos : codigo'''
    

def p_variavel(p):
    '''codigo : TIPO VAR 
                | TIPO VAR OPER_ATRIB_IGUAL INTEIRO
                | TIPO VAR OPER_ATRIB_IGUAL REAL
                | TIPO VAR OPER_ATRIB_IGUAL CADEIA_CAR
                | TIPO VAR OPER_ATRIB_IGUAL BOOLEANO 
                | TIPO VAR OPER_ATRIB_IGUAL VAR
    '''
def p_variavel_matematica(p):
    ''' varmat : VAR INTEIRO
               | VAR REAL
    '''
def p_operacao_mat(p):
    ''' operacao : INTEIRO OPER_MAT INTEIRO
                 | varmat OPER_MAT varmat
                 | varmat OPER_MAT INTEIRO
                 | INTEIRO OPER_MAT varmat

                 | REAL OPER_MAT REAL
                 | varmat OPER_MAT REAL
                 | REAL OPER_MAT varmat
    '''

def p_matematica(p):
    '''codigo : operacao
              | operacao operacao'''

def p_tipo(p):
    '''codigo : INT
              | REAL
              | BOOLEANO
              | CADEIA_CAR
    '''

def p_logico(p):
    '''logico : VAR OPER_LOG VAR
              | VAR OPER_LOG CADEIA_CAR
              | VAR OPER_LOG INTEIRO
              | VAR OPER_LOG REAL
    '''

def p_relacional(p):
    '''relacional :  VAR OPER_RELA VAR
                    | VAR OPER_RELA INTEIRO
                    | VAR OPER_RELA REAL
                    | VAR OPER_RELA CADEIA_CAR
    '''

def p_expressao_interna(p):
    '''expinterna : ABRE_CHAV codigos FECHA_CHAV'''

def p_para(p):
    '''codigo : PARA ABRE_PAR relacional PONTO_VIRG relacional PONTO_VIRG VAR ITERADORES FECHA_PAR expinterna'''


def p_condicional(p):
    '''codigo : SE ABRE_PAR relacional FECHA_PAR expinterna
              | SE ABRE_PAR logico FECHA_PAR expinterna

              | SE ABRE_PAR relacional FECHA_PAR expinterna SENAO expinterna
              | SE ABRE_PAR logico FECHA_PAR expinterna SENAO expinterna
        '''


def p_enquanto(p):
    '''codigo : ENQUANTO ABRE_PAR relacional FECHA_PAR expinterna
              | ENQUANTO ABRE_PAR BOOLEANO FECHA_PAR expinterna
    '''

def p_retorno(p):
    '''codigo : RETORNO ABRE_PAR VAR FECHA_PAR
              | RETORNO INTEIRO
    '''

def p_parametro_vazio(p):
    '''param_vazio : '''

def p_parametro(p):
    '''parametro : INTEIRO
                 | REAL
                 | CADEIA_CAR
                 | VAR
    '''

def p_parametro_grupo(p):
    '''parametro : parametro VIRG parametro'''

def p_regra_funk(p):
    '''regrafunk : ABRE_PAR param_vazio FECHA_PAR
                  | ABRE_PAR parametro FECHA_PAR
    '''

def p_definir_funk(p):
    '''codigo : FUNK NOME_FUNK regrafunk expinterna'''

def p_chamar_funk(p):
    '''codigo : NOME_FUNK regrafunk'''

def p_escreva(p):
  '''codigo : ESCREVA ABRE_PAR CADEIA_CAR FECHA_PAR
            | ESCREVA ABRE_PAR CADEIA_CAR VAR FECHA_PAR
            | ESCREVA ABRE_PAR VAR FECHA_PAR
            | ESCREVA ABRE_PAR CADEIA_CAR INTEIRO FECHA_PAR
            | ESCREVA ABRE_PAR INTEIRO FECHA_PAR
            | ESCREVA ABRE_PAR CADEIA_CAR REAL FECHA_PAR
            | ESCREVA ABRE_PAR REAL FECHA_PAR

  '''

def p_leia(p):
  '''codigo : LEIA ABRE_PAR VAR FECHA_PAR'''


# Ignora espaços em branco e tabulações
t_ignore = ' \t'

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print("ERRO: ",p)

parser = yacc.yacc()

#Chamada do Algoritmo em si começa aqui
erros = 0

#função padrão para adicionar as classificações dos tokens para ser impressa pelo compilador
def add_lista_saida(t,notificacao):
    saidas.append((t.lineno,t.lexpos,t.type,t.value, notificacao))

saidas = []

def t_VAR(t):
    r'([a-zA-Z_]+)\d*\w*'
    if t.value in reserved:# verifica se é uma palavra reservada
        t.type = reserved[t.value]
    elif t.value in reserved_funk:# verifica se é uma Função
        t.type = 'NOME_FUNK'
    return t


# Ignora comentários
def t_COMMENT(t):
    r'\//(.*?)\//'
    pass


def analyze_text():
    global errors
    input_string = text_input.get('1.0', tk.END)
    if errors:
        errors = []
    tokenize(input_string)
    
# Tratamento de erros
def t_error(t):
    line = t.lexer.lineno
    error_message = f"Caracter Invalido {t.value[0]!r} linha {line}"
    errors.append(error_message)
    t.lexer.skip(1)
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Cria o analisador léxico
lexer = lex.lex()

# Define a função para exibir os tokens
def tokenize(input_string):
    output_string = ''
    lexer.input(input_string)
    num_lines = input_string.count('\n')
    for token in lexer:
        output_string += 'Token: {}, valor: {}, linha: {}, coluna: {}\n'.format(token.type, token.value, token.lineno, token.lexpos - input_string.rfind("\n", 0, token.lexpos))

        if token.type == "STR_INCOMPLETA":
            error_message = f"String Mal formada {token.value!r} linha {token.lineno}"
            errors.append(error_message)
        if token.type == "VAR_ERRO":
            error_message = f"Variavel Mal formada {token.value!r} linha {token.lineno}"
            errors.append(error_message)
        if token.type == "NUM_ERRO":
            error_message = f"Número Mal formado {token.value!r} linha {token.lineno}"
            errors.append(error_message)
        if token.type == "INTEIRO":
            max = (len(str(token.value)))
            if (max > 10):
                error_message = f"Entrada maior que a suportada linha {token.lineno}"
                errors.append(error_message)
                
    output_string += f'\nNúmero de linhas: {num_lines}'
    error_message = lexer.token()
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert('1.0', output_string)
    if errors:
        text_output.insert(tk.END, "\n\nErros encontrados:\n")
        for error in errors:
            text_output.insert(tk.END, error + "\n")
    text_output.configure(state='disabled')
    lexer.lineno = 1
    


# Define a função para abrir o arquivo
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            file_contents = f.read()
        text_input.delete('1.0', tk.END)
        text_input.insert('1.0', file_contents)
        analyze_text()

# Cria a janela principal da interface gráfica
root = tk.Tk()
root.title("BR Script")

style = ttk.Style()
style.configure("TButton", background="gray25", foreground="black", font=("Helvetica", 12))
style.configure("TLabel", background="gray25", foreground="black", font=("Helvetica", 16))


# Cria um campo para digitar o texto
text_input = tk.Text(root, font=("Helvetica", 14),width=70, height=10)
text_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Cria um botão para abrir o arquivo
btn_open = ttk.Button(root, text="Abrir Arquivo", command=open_file)
btn_open.grid(row=1, column=0, padx=10, pady=10)

# Cria um botão para analisar o texto
btn_analyze = ttk.Button(root, text="Analisar Texto", command=analyze_text)
btn_analyze.grid(row=1, column=1, padx=10, pady=10)

btn_quit = ttk.Button(root, text="Sair", command=root.quit)
btn_quit.grid(row=1, column=2, padx=10, pady=10)


# Cria um campo para exibir o resultado
text_output = tk.Text(root, height=10, font=("Helvetica", 14), width=70)
text_output.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Inicia a interface gráfica
root.mainloop()