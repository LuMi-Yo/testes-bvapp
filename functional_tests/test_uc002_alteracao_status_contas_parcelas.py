'''
UC002 - Alteração Manual de Status de Parcelas e Contas

Objetivo: Permitir que o tesoureiro realize baixas (pagamentos) ou cancelamentos de parcelas de forma manual, garantindo as regras de bloqueio e irreversibilidade.

Requisito Base:
[RF050301] - Status de parcelas e contas

Ator:
- Tesoureiro

Autor: Luís Miguel Carvalho da Rocha
'''


# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O tesoureiro acessa o sistema e seleciona uma conta.
# 2. O tesoureiro solicita a alteração do status de uma parcela para "Paga" ou "Cancelada".
# 3. O sistema valida se a conta/parcela não se encontra previamente cancelada. [RN4]
# 4. O sistema valida se não é uma tentativa de reverter uma parcela "Paga". [RN5]
# 5. O sistema atualiza o status da parcela conforme a ação do tesoureiro. [RN1]
# 6. O sistema reavalia as parcelas da conta e deriva automaticamente o novo status da Conta. [RN2]
# 7. O sistema exibe mensagem de sucesso e conclui a operação.


# 🟡 FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# [FA1] - TENTATIVA DE ALTERAÇÃO DE CONTA CANCELADA
# 1. No passo 3 do [FP], se o sistema identificar que a conta se encontra com status "Cancelada":
# 2. O sistema bloqueia a edição.
# 3. O sistema exibe uma mensagem informando o cancelamento da conta: "O status da conta selecionada não pode ser alterado".
# 4. O processo é encerrado sem salvar alterações.


# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] - STATUS DE PARCELAS (ATRIBUIÇÃO MANUAL):
# Os status "Paga" e "Cancelada" são de atribuição exclusiva pelo tesoureiro (ou validação sistêmica de recebimento). 

# [RN2] - STATUS DE CONTAS (DERIVADO):
# O status da conta deriva do status de suas parcelas:
# - Aberta: Nenhuma parcela foi paga e nenhuma está atrasada.
# - Parcial: Ao menos uma parcela está paga e as demais estão "Abertas".
# - Paga: Todas as parcelas estão pagas.
# - Cancelada: Cancelada pelo tesoureiro.

# [RN3] - RESPONSABILIDADE DE ATRIBUIÇÃO (TESOUREIRO):
# "Paga" e "Cancelada" são atribuídas EXCLUSIVAMENTE de forma manual pelo tesoureiro (ou por integração automática de recebimento em contas a receber).

# [RN4] - IRREVERSIBILIDADE DO CANCELAMENTO:
# O status "Cancelada" é permanente e irreversível, disparando o fluxo alternativo [FA1] em caso de tentativa de alteração.

# [RN5] - FLUXO DE PAGAMENTO DE PARCELAS:
# Uma parcela atrasada que é paga transita diretamente para o status "Paga". Uma parcela paga não pode, sob nenhuma hipótese, retornar para o status "Aberta" ou "Atrasada".