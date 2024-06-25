from modelos.restaurante import Restaurante

restaurante_choes = Restaurante('Choes', 'Japonesa')
restaurante_choes.receber_avaliacao('Maral', 10)
restaurante_choes.receber_avaliacao('May', 10)
restaurante_choes.receber_avaliacao('Elvis', 5)
restaurante_choes.receber_avaliacao('Lui', 8)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

