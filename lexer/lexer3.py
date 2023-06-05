import ply.lex as lex

file = open('./prueba2.txt')

# Lista de tokens
tokens = [
    'DOCTYPE','COMIENZO_SIMPARA','FIN_SIMPARA','COMIENZO_EMPHASIS','FIN_EMPHASIS','LINK','SIMPARA_ID_COMIENZO','CONTENIDO','SALTO_DE_LINEA',
    'ARTICLE_COMIENZO','ARTICLE_FIN','INFO_COMIENZO','INFO_FIN','TITLE_COMIENZO','TITLE_FIN','OB_COMIENZO','OB_FIN','OP_COMIENZO',
    'OP_FIN','ITEMIZEDLIST_COMIENZO','ITEMIZEDLIST_FIN','LISTITEM_COMIENZO', 'LISTITEM_FIN', 'IMPORTANT_COMIENZO','IMPORTANT_FIN',
    'PARA_COMIENZO','PARA_FIN','SIMPARA_COMIENZO','SIMPARA_FIN','ADDRESS_COMIENZO','ADDRESS_FIN','MEDIAOBJECT_COMIENZO',
    'MEDIAOBJECT_FIN','INFORMALTABLE_COMIENZO','INFORMALTABLE_FIN','COMMENT_COMIENZO','COMMENT_FIN','ABSTRACT_COMIENZO',
    'ABSTRACT_FIN','FIRSTNAME_COMIENZO','FIRSTNAME_FIN','SURNAME_COMIENZO','SURNAME_FIN','STREET_COMIENZO','STREET_FIN',
    'CITY_COMIENZO','CITY_FIN','STATE_COMIENZO','STATE_FIN','PHONE_COMIENZO','PHONE_FIN','EMAIL_COMIENZO', 'EMAIL_FIN',
    'DATE_COMIENZO','DATE_FIN','YEAR_COMIENZO','YEAR_FIN','HOLDER_COMIENZO','HOLDER_FIN','SECTION_COMIENZO','SECTION_FIN',
    'SIMPLESEC_COMIENZO','SIMPLESEC_FIN','ROW_COMIENZO','ROW_FIN','ENTRYTBL_COMIENZO','ENTRYTBL_FIN','ENTRY_COMIENZO',
    'ENTRY_FIN','HEAD_COMIENZO','HEAD_FIN','COLSPEC_COMIENZO','COLSPEC_FIN','TRMARGIN_COMIENZO','TRMARGIN_FIN','GRMARGIN_COMIENZO',
    'GRMARGIN_FIN','LRMARGIN_COMIENZO','LRMARGIN_FIN','LINK_COMIENZO','LINK_FIN','FOOTER_COMIENZO','FOOTER_FIN','IMG_COMIENZO',
    'SALTO__LINEA'
]

# Expresiones regulares para los tokens
t_DOCTYPE = r'\<\?(.*?)\?\>'
t_COMIENZO_SIMPARA = r'<simpara\s*>'
t_FIN_SIMPARA = r'</simpara\s*>'
t_COMIENZO_EMPHASIS = r'<emphasis\s*>'
t_FIN_EMPHASIS = r'</emphasis\s*>'
t_LINK = r'<link\s+xlink:href="[^"]+"\s*/>'
t_SIMPARA_ID_COMIENZO = r'<simpara\s+id="[^"]+"\s*>'
t_CONTENIDO = r'[^<]+'
t_SALTO_DE_LINEA = r'\n'
t_ARTICLE_COMIENZO = r'<!DOCTYPE\s+article>'
t_ARTICLE_FIN = r'</article>'
t_INFO_COMIENZO = r'<info>'
t_INFO_FIN = r'</info>'
t_TITLE_COMIENZO = r'<title>'
t_TITLE_FIN = r'</title>'
t_OB_COMIENZO = r'<OB>'
t_OB_FIN = r'</OB>'
t_OP_COMIENZO = r'<OP>'
t_OP_FIN = r'</OP>'
t_ITEMIZEDLIST_COMIENZO = r'<itemizedlist>'
t_ITEMIZEDLIST_FIN = r'</itemizedlist>'
t_LISTITEM_COMIENZO = r'<listitem>'
t_LISTITEM_FIN = r'</listitem>'
t_IMPORTANT_COMIENZO = r'<important>'
t_IMPORTANT_FIN = r'</important>'
t_PARA_COMIENZO = r'<para>'
t_PARA_FIN = r'</para>'
t_SIMPARA_COMIENZO = r'<simpara>'
t_SIMPARA_FIN = r'</simpara>'
t_ADDRESS_COMIENZO = r'<address>'
t_ADDRESS_FIN = r'</address>'
t_MEDIAOBJECT_COMIENZO = r'<mediaobject>'
t_MEDIAOBJECT_FIN = r'</mediaobject>'
t_INFORMALTABLE_COMIENZO = r'<informaltable>'
t_INFORMALTABLE_FIN = r'</informaltable>'
t_COMMENT_COMIENZO = r'<comment>'
t_COMMENT_FIN = r'</comment>'
t_ABSTRACT_COMIENZO = r'<abstract>'
t_ABSTRACT_FIN = r'</abstract>'
t_FIRSTNAME_COMIENZO = r'<firstname>'
t_FIRSTNAME_FIN = r'</firstname>'
t_SURNAME_COMIENZO = r'<surname>'
t_SURNAME_FIN = r'</surname>'
t_STREET_COMIENZO = r'<street>'
t_STREET_FIN = r'</street>'
t_CITY_COMIENZO = r'<city>'
t_CITY_FIN = r'</city>'
t_STATE_COMIENZO = r'<state>'
t_STATE_FIN = r'</state>'
t_PHONE_COMIENZO = r'<phone>'
t_PHONE_FIN = r'</phone>'
t_EMAIL_COMIENZO = r'<email>'
t_EMAIL_FIN = r'</email>'
t_DATE_COMIENZO = r'<date>'
t_DATE_FIN = r'</date>'
t_YEAR_COMIENZO = r'<year>'
t_YEAR_FIN = r'</year>'
t_HOLDER_COMIENZO = r'<holder>'
t_HOLDER_FIN = r'</holder>'
t_SECTION_COMIENZO = r'<section>'
t_SECTION_FIN = r'</section>'
t_SIMPLESEC_COMIENZO = r'<simplesec>'
t_SIMPLESEC_FIN = r'</simplesec>'
t_ROW_COMIENZO = r'<row>'
t_ROW_FIN = r'</row>'
t_ENTRYTBL_COMIENZO = r'<entrytbl>'
t_ENTRYTBL_FIN = r'</entrytbl>'
t_ENTRY_COMIENZO = r'<entry>'
t_ENTRY_FIN = r'</entry>'
t_HEAD_COMIENZO = r'<head>'
t_HEAD_FIN = r'</head>'
t_COLSPEC_COMIENZO = r'<colspec>'
t_COLSPEC_FIN = r'</colspec>'
t_TRMARGIN_COMIENZO = r'<trmargin>'
t_TRMARGIN_FIN = r'</trmargin>'
t_GRMARGIN_COMIENZO = r'<grmargin>'
t_GRMARGIN_FIN = r'</grmargin>'
t_LRMARGIN_COMIENZO = r'<lrmargin>'
t_LRMARGIN_FIN = r'</lrmargin>'
t_LINK_COMIENZO = r'<link>'
t_LINK_FIN = r'</link>'
t_FOOTER_COMIENZO = r'<footer>'
t_FOOTER_FIN = r'</footer>'
t_IMG_COMIENZO = r'<img\s+src="[^"]+"\s*/>'


# Función de salto de linea
def t_SALTO__LINEA(t):
    r'\n'
    t.lexer.lineno += 1
    print('')
    return t


# Función de manejo de errores
def t_error(t):
    t.lexer.skip(1) 
    print("\033[91mERROR TOKEN NO VALIDO\033[0m " )
      
lexer = lex.lex()


lex.input(file.read())

while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value)," -->> se encontro el token  ",str(tok.type))
    
file.close()



