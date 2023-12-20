class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitirSom(self):
        print("O animal emite um som.")

class Cao(Animal):
    def latir(self):
        print("O cão está latindo.")

class Gato(Animal):
    def miar(self):
        print("O gato está miando.")

def main():
    print("Digite o nome do animal:")
    nome = input()

    print("Digite o tipo do animal (cao/gato):")
    tipo = input()

    if tipo == 'cao':
        animal = Cao(nome)
    elif tipo == 'gato':
        animal = Gato(nome)
    else:
        print("Tipo de animal inválido. Tente novamente.")
        return

    animal.emitirSom()

    if isinstance(animal, Cao):
        animal.latir()
    elif isinstance(animal, Gato):
        animal.miar()

if __name__ == '__main__':
    main()