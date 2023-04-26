import os
import re

class AnalisadorLexico:
    
    palavra_reservada = ["int", "char", "long", "short", "float", "double", "void",
                        "if", "else", "for", "while", "do", "break", "continue", 
                        "struct", "switch", "case", "default", "return"]
    
    operadores = ["=", "+", "-", "*", "/", "++", "--", "!", "&", "%", "->", "==",
                 "!=", "", "&&", "+=", "-=", "*=", "/=", "<", ">", "<=", ">=","||"]
    
    delimitadores = ["(", ")", "[", "]", "{", "}", ";", ","]
    
    identificadores = '[a-zA-Z_]+[a-zA-Z0-9_]*' 

    inteiros = '[+-]?\d+'
    
    ponto_flutuante = '[+-]?\d+\.\d+'

    constante_textual = '["\'][^"\']*["\']'
   
    regex = re.compile(r'\d+[a-zA-Z_]+\b|[a-zA-Z_]+[a-zA-Z0-9_]*[™]+|["\'][^"\']*["\']|[+-]?\d+\.\d+|[a-zA-Z_]+[a-zA-Z0-9_]*|->|&&|\|\||\-\-|\+\+|[-+*/%&=!><]=|[-+*/%&=!><|]|\||\(|\)|\[|\]|\{|\}|\.|,|;')
    
    def analisar(self):
        for token in self.tokens:
            try:
                if re.match(r'\d+[a-zA-Z_]+\b|[a-zA-Z_]+[a-zA-Z0-9_]*[™]+', token):
                     raise Exception(f"Erro: token inválido -> {token}") 
                elif token in self.palavra_reservada:
                    print(f"Palavra reservada -> {token}")
                elif token in self.operadores:
                    print(f"Operador -> {token}")
                elif token in self.delimitadores:
                    print(f"Delimitador -> {token}")
                elif re.match(self.inteiros, token):
                    print(f"Inteiro -> {token}")      
                elif re.match(self.ponto_flutuante, token):
                    print(f"Ponto Flutuante -> {token}") 
                elif re.match(self.identificadores, token):
                    print(f"Identificador -> {token}")
                elif re.match(self.constante_textual, token):
                    print(f"Constante Textual -> {token}")
            except Exception as e: 
                print(str(e)) 
                break 
            
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
    sair = input('Deseja escolher outro arquivo? [s]im ou [n]ão ').lower()
    if sair.startswith('n'):
        break
    elif sair.startswith('s'):
        if os.name == 'nt':
            os.system('cls') 
        else:
            os.system('clear')
    else:
        print("Opção inválida.")
        break