'''
UC003 - Juros por atraso

Objetivo: Verificar se a rotina diária identifica parcelas em atraso (de cobranças e contas a pagar) e aplica os juros (simples ou compostos) corretamente.

Requisito Base:
[RF050302] - Juros por atraso

Ator:
- Sistema (Rotina de Backend)

Autor: Luís Miguel Carvalho da Rocha
'''


# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. A rotina diária é acionada pelo sistema.
# 2. O sistema busca todas as parcelas de contas a pagar e cobranças com status "Atrasada".
# 3. O sistema verifica se os dias de atraso superaram o número de dias de carência configurado. [A1] [RN1]
# 4. O sistema calcula os juros do dia, aplicando o tipo de juros (simples ou composto) e a taxa percentual definida.
# 5. O sistema atualiza o "Valor Atualizado" da parcela somando os juros, preservando intacto o "Valor Original". [RN2]
# 6. O sistema disponibiliza ambos os valores (original e atualizado) para exibição. [RN3]

# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] INCIDÊNCIA DOS JUROS:
# Os juros passam a incidir após um número de dias de atraso configurável pelo tesoureiro.

# [RN2] RECÁLCULO E PRESERVAÇÃO:
# A rotina diária recalcula o valor atualizado de cada parcela atrasada, somando os juros do dia. O valor original é sempre preservado.

# [RN3] EXIBIÇÃO DE VALORES:
# O valor original e o valor atualizado são exibidos nas listagens e nos detalhes.