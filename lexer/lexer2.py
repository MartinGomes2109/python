import ply.lex as lex

file = open('./prueba.txt')

tokens = ['COMA','NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMA = r','

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Token desconocido -->> '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6 , comaasd")

lex.input(file.read())

while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value)," -->> se encontro el token ",str(tok.type))
    
file.close()