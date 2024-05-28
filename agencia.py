from banco import Banco

class Agencia(Banco):
    
    def __init__(self, nome, endereco,numero) -> None:
        
        """
        super() é uma função especial em Python que permite acessar métodos e atributos de uma classe pai (superclasse).
        Neste caso, estamos utilizando super() para chamar o construtor da classe ItemCardapio,
        passando os parâmetros 'nome' e 'preco'. Isso inicializa esses atributos na classe ItemCardapio.
        
        Na prática, isso é similar a instanciar um objeto da classe ItemCardapio dentro da classe Banco.
        """
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self) -> str:
        return self._nome
    
    
    
    
if __name__ == '__main__':
    response = Agencia("Itaú","Rua antonio de santos moura",204)
    print(response)