#gramatica

reserved = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'para': 'PARA',
    'funk': 'FUNK',
    'retorna': 'RETORNA',
    'ifsuldeminas': 'IFSULDEMINAS',
    'inicio': 'INICIO',
    'compiladores': 'COMPILADORES',
    'fim': 'FIM',
    'int': 'INT',
    'real': 'REAL',
    'bool': 'BOOLEANO',
    'texto': 'TEXTO',
}

# Define os nomes dos tokens
tokens = [

    'IFSULDEMINAS'
def p_ifsuldeminas(p):
    '''ifsuldeminas : IFSULDEMINAS'''

    'COMPILADORES'
def p_compiladores(p):
    '''compiladores : COMPILADORES'''

    'INICIO'
def p_inicio(p):
    '''inicio : INICIO'''

    'FIM'
def p_fim(p):
    '''fim : FIM'''

    'CODIGO'
def p_codigo_mais(p):
    '''codigos : codigos codigo'''

def p_codigo_simples(p):
    '''codigos : codigo'''

    'VAR'
def p_variavel(p):
    '''variavel : TIPO VAR 
                | TIPO VAR OP_ATRIB_IGUAL INTEIRO
                | TIPO VAR OP_ATRIB_IGUAL REAL
                | TIPO VAR OP_ATRIB_IGUAL CADEIA_CAR
                | TIPO VAR OP_ATRIB_IGUAL BOOLEANO 
                | TIPO VAR OP_ATRIB_IGUAL VAR
    '''

    'TIPO'
def p_tipo(p):
    '''tipo : INT
            | REAL
            | BOOLEANO
            | CADEIA_CAR
    '''

    'PARA'
def p_para(p):
    '''para : PARA ABRE_PAR VAR OP_ATRIB_IGUAL VAR PONTO_VIRG VAR OP_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | PARA ABRE_PAR VAR OP_RELA VAR PONTO_VIRG VAR OP_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | PARA ABRE_PAR VAR OP_ATRIB_IGUAL VAR PONTO_VIRG VAR OP_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | PARA ABRE_PAR VAR OP_RELA VAR PONTO_VIRG VAR OP_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV

            | PARA ABRE_PAR VAR OP_ATRIB_IGUAL INTEIRO PONTO_VIRG VAR OP_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | PARA ABRE_PAR VAR OP_RELA INTEIRO PONTO_VIRG VAR OP_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
    '''

    'SE' 'SENAO'
def p_condicional(p):
    '''condicional : SE ABRE_PAR VAR OP_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV

                   | SE ABRE_PAR VAR OP_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OP_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV
        '''

    'ENQUANTO'
def p_enquanto(p):
    '''enquanto : ENQUANTO ABRE_PAR VAR OP_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                | ENQUANTO ABRE_PAR VAR OP_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                | ENQUANTO ABRE_PAR VAR OP_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                | ENQUANTO ABRE_PAR VAR OP_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                | ENQUANTO ABRE_PAR VAR OP_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
    '''
    'RETORNO',
def p_retorno(p):
    '''retorno : RETORNO ABRE_PAR VAR FECHA_PAR
               | RETORNO INTEIRO
    '''

    'FUNK'
def p_definir_funk(p):
    '''funk : FUNK NOME_FUNK ABRE_PAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | FUNK NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | FUNK NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | FUNK NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
            | FUNK NOME_FUNK ABRE_PAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
    '''

def p_chamar_funk(p):
    '''funk : NOME_FUNK ABRE_PAR VAR FECHA_PAR
            | NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR
            | NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR
            | NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR
            | NOME_FUNK ABRE_PAR FECHA_PAR
    '''

#    'ESCREVA',
#    escreva(“Parabéns você acertou o nome”);
#    escreva(resultado);
#
#
#def p_escreva(t):
#    '''escreva : ESCREVA ABRE_PAR '''
#def p_statement_write(t):
#    '''write_statement : WRITE  list_expression '''
#    tmp=""
#    for element in t[2]:
#        tmp+=str(element)+" "
#    print ("In Exectution: "+tmp)
#
#
#def p_statement_read(t):
#    '''read_statement : READ variavel '''
#    t[3].value = raw_input(); 	
#
#    'LEIA',


    'STR_INCOMPLETA',
    'VAR_ERRO',
    'NUM_ERRO',
]+ list(reserved.values())

# Expressões regulares para cada token
t_INTEIRO = r'([+-])?\d+'
t_REAL = r'(([+-])?\d+)[.]\d+'
t_CADEIA_CAR = r'"[^"\n]*"'
t_ABRE_COLCH = r'\['
t_FECHA_COLCH = r'\]'
t_ABRE_CHAV = r'{'
t_FECHA_CHAV = r'}'
t_VIRG = r','
t_PONTO_VIRG = r';'
t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_OPER_RELA = r'(=|==|!=|<=|>=|<|>)'
t_OPER_MAT = r'(\+|\-|\*|\/|\%)'
t_ITERADORES = r'(ate|passo)'
t_NEGACAO = r'!'
t_OPER_LOG = r'(&&|\|\|)'
t_NOME_FUNK = r'[a-zA-Z_]\w*[ ][(].*?[)]'
t_STR_INCOMPLETA = r'"[^"]*'
t_VAR_ERRO = r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
t_NUM_ERRO = r'^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?[^0-9]*$'