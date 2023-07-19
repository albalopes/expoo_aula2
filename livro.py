class Livro:
    def __init__(self, titulo, autor, anopublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anopublicacao = anopublicacao
    
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def info(self):
        print('Titulo: ', self.__titulo)
        print('Autor: ', self.__autor)
        print('Ano de Publicação: ', self.__anopublicacao)