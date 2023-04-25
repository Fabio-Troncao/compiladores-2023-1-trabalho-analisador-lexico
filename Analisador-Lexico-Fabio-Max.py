import re

class AnalisadorLexico:
    
    palavra_reservada = ["int", "char", "long", "short", "float", "double", "void",
                        "if", "else", "for", "while", "do", "break", "continue", 
                        "struct", "switch", "case", "default", "return"]
    
    operadores = ["=", "+", "-", "*", "/", "++", "--", "!", "&", "%", "->", "==",
                 "!=", "", "&&", "+=", "-=", "*=", "/=", "<", ">", "<=", ">=","||"]
    
    delimitadores = ["(", ")", "[", "]", "{", "}", ";", ","]
    
    # Identificadores que começam com uma letra ou underscore, seguidos por letras, números ou underscores
    identificadores = '[a-zA-Z_]+[a-zA-Z0-9_]*' 

    # Números inteiros opcionais com um sinal de mais (+) ou menos (-) no início
    numeros_inteiros = '[+-]?\d+$'
    
    # Números flutuantes opcionais com um sinal de mais (+) ou menos (-) no início, seguidos por um ponto decimal e dígitos opcionais
    numeros_flutuantes = '[+-]?\d+\.\d+'

    # Cadeias de caracteres delimitadas por aspas duplas (") ou aspas simples (') que podem conter qualquer caractere, exceto aspas correspondentes
    constante_textual = '["\'][^"\']*["\']'

    regex = re.compile(r'\d+[a-zA-Z_]+\b|[a-zA-Z_]+[a-zA-Z0-9_]*[™]*|["\'][^"\']*["\']|[+-]?\d+\.\d+|[a-zA-Z_]+[a-zA-Z0-9_]*|->|&&|\|\||\-\-|\+\+|[-+*/%&=!><]=|[-+*/%&=!><|]|\||\(|\)|\[|\]|\{|\}|\.|,|;')
    
    def analisar(self):
        for token in self.tokens:
            if re.match(r'\d+[a-zA-Z_]+\b|[a-zA-Z_]+[a-zA-Z0-9_]*[™]+', token):
                print(f"Erro: token inválido -> {token}") 
                break  
            elif token in self.palavra_reservada:
                print(f"Palavra reservada -> {token}")
            elif token in self.operadores:
                print(f"Operador -> {token}")
            elif token in self.delimitadores:
                print(f"Delimitador -> {token}")
            elif re.match(self.numeros_inteiros, token):
                print(f"Inteiro -> {token}")      
            elif re.match(self.numeros_flutuantes, token):
                print(f"Ponto Flutuante -> {token}") 
            elif re.match(self.identificadores, token):
                print(f"Identificador -> {token}")
            elif re.match(self.constante_textual, token):
                print(f"Constante Textual -> {token}")




    def __init__(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            conteudo = re.sub('//.*', ' ', conteudo)  
            conteudo = re.sub('(/\*(.|\n)*?\*/)', ' ', conteudo)  
            self.tokens = self.regex.findall(conteudo)


while True:
    lista = ['teste1.c', 'teste2.c', 'teste3.c', 'teste4.c', 'teste5.c', 'teste6.c', 'teste7.c', 'teste8.c', 'teste-erro1.c', 'teste-erro2.c']
    escolha = input('Escolha entre 1 a 10: 1-teste1.c, 2-teste2.c, 3-teste3.c, 4-teste4.c, 5-teste5.c, 6-teste6.c, 7-teste7.c, 8-teste8.c, 9-teste-erro1.c, 10-teste-erro2.c -> ')
    escolha = int(escolha)
    analisador = AnalisadorLexico(lista[escolha-1])
    analisador.analisar()
    sair = input('Deseja escolher outro arquivo? [s]im ou [n]ão ').lower().startswith('n')

    if sair is True:
        break


"""
\d+[a-zA-Z_]+\b # Números seguidos por letras ou underscores, seguidos por uma borda de palavra
[a-zA-Z_]+[a-zA-Z0-9_]*[™]* # Identificadores que começam com uma letra ou underscore, seguidos por letras, números, underscores ou o caractere ™
["\'][^"\']*["\'] # Cadeias de caracteres delimitadas por aspas duplas (") ou aspas simples (') que podem conter qualquer caractere, exceto aspas correspondentes
[+-]?\d+(?:\.\d+)?| # Números inteiros ou flutuantes opcionais com um sinal de mais (+) ou menos (-) no início
[a-zA-Z_]+[a-zA-Z0-9_]* # Identificadores que começam com uma letra ou underscore, seguidos por letras, números ou underscores
&&|\|\||\-\-|\+\+|[-+*/%&=!><]= # Operadores lógicos (&&, ||) e operadores de incremento/decremento (++, --), bem como operadores de comparação e atribuição
[-+*/%&=!><|]|\| # Outros operadores aritméticos, de comparação, lógicos e de bit, bem como pipes (|)
\(|\)|\[|\]|\{|\}|\.|,|; # Parênteses, colchetes e chaves, bem como ponto (.), vírgula (,) e ponto-e-vírgula (;)
"""