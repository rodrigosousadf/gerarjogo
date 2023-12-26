# Análise e Geração de Jogos da Mega Sena

Este repositório contém um script Python desenvolvido para analisar dados históricos da Mega Sena e gerar jogos com base em diferentes estratégias estatísticas.

## Visão Geral

O script `gerarmega.py` executa duas funções principais:

1. **Análise dos Resultados Históricos da Mega Sena**: O script analisa os resultados de jogos anteriores para identificar padrões, como a frequência de números sorteados.

2. **Geração de Jogos com Estratégias Balanceadas**: Com base na análise, o script gera jogos que levam em consideração combinações balanceadas de números pares e ímpares, além de evitar números comumente escolhidos (como datas).

## Metodologia

### Análise de Dados

- Os dados são carregados de um arquivo Excel contendo resultados históricos da Mega Sena.
- A análise de frequência identifica os números que mais apareceram nos últimos 10 jogos.
- Esta análise serve como base para a estratégia de geração de jogos.

### Estratégias de Geração de Jogos

- **Balanceamento de Pares e Ímpares**: Os jogos são gerados mantendo uma proporção específica entre números pares e ímpares.
- **Diversificação**: A estratégia busca diversificar os números escolhidos para evitar padrões comuns e aumentar a aleatoriedade.

## Considerações Importantes

- Este script é uma ferramenta para análise e geração de jogos de loteria para entretenimento.
- Não há garantia de aumento de chances de ganho na Mega Sena, já que os sorteios são eventos aleatórios e independentes.
- O jogo responsável é encorajado. Este script não deve ser visto como um meio de investimento financeiro.

## Como Usar

1. Garanta que o Python e as bibliotecas necessárias (Pandas, Numpy) estão instalados.
2. Coloque o arquivo de dados históricos no diretório correto.
3. Execute o script para gerar jogos.

## Licença

Este projeto está sob [inserir tipo de licença], veja o arquivo LICENSE para mais detalhes.
