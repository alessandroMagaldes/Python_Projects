pesos = [int(input(f"Digite o peso do Lutador {i+1}: ")) for i in range(2)]

def solution(resultado):
        if 5 >= abs(pesos[0] - pesos[1]) >= -5:
            print('PODEM LUTAR')
        else:
            print('Não podem lutar')
            pesos = [int(input(f"Digite o peso do Lutador {i+1}: ")) for i in range(2)]
                
                
        
