# Simulação do Paradoxo de Monty Hall


[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://jp-linux.github.io)
![Python](https://img.shields.io/badge/Python-3.0+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto contém uma simulação computacional do famoso Paradoxo de Monty Hall, demonstrando por que trocar de porta aumenta suas chances de vitória.

## O Paradoxo de Monty Hall
No problema baseado no programa de TV *Let's Make a Deal*:
- Existem 3 portas: 1 com um prêmio e 2 vazias
- Você escolhe uma porta inicialmente
- O apresentador (Monty Hall) abre uma porta vazia das restantes
- Você tem a opção de manter sua escolha original ou trocar

**Paradoxo**: Estatisticamente, trocar de porta dobra suas chances de ganhar (de 1/3 para 2/3), o que vai contra a intuição inicial de muitas pessoas.

## Como a Simulação Funciona
O código Python (`monty_hall.py`) simula o problema 1 milhão de vezes, sempre utilizando a estratégia de trocar de porta. O processo:

1. Sorteia aleatoriamente a porta premiada
2. Escolhe uma porta aleatoriamente como palpite inicial
3. O apresentador abre uma porta vazia restante
4. O jogador **sempre troca** para a porta fechada restante
5. Registra se a troca resultou em vitória ou derrota

## Resultados das Simulações
Foram realizados múltiplos testes com 1.000.000 de simulações cada:

### Teste 1
```
Vitórias: 666426 (66.64%)
Derrotas: 333574 (33.36%)
```

### Teste 2
```
Vitórias: 666820 (66.68%)
Derrotas: 333180 (33.32%)
```

### Teste 3
```
Vitórias: 666443 (66.64%)
Derrotas: 333557 (33.36%)
```

## Conclusão
Os resultados confirmam consistentemente:
- **Taxa de vitórias**: ~66.67% 
- **Taxa de derrotas**: ~33.33%

Isso comprova matematicamente que a estratégia de **sempre trocar de porta** dobra suas chances de ganhar o prêmio, confirmando a solução do paradoxo.

## Como Executar
1. Tenha Python 3 instalado
2. Execute o script:
```bash
python monty_hall.py
```

## Requisitos
- Bibliotecas Python: `random`
- Nenhuma instalação adicional necessária

## 👤 Autor

**Jorge Paulo Santos**  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JP-Linux)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jorgepsan7@gmail.com)

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

