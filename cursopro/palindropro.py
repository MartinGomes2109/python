def ispalindromo(string: str) -> bool:
     string  = string.replace(" ","").lower()
     return string == string[::-1]
#forma tipado duro: si o si tiene que ingresar una variable caracter y si o si devuelve un booleano
#lower(): colocar los caracteres en minusculas
# [::-1]: da vuelta la palabra o invite los caracteres para comparar si es palindromo

def run():
    valor = input("ingrese una palabla: ")
    print(ispalindromo(1000))
    
if __name__=='__main__':
    run()