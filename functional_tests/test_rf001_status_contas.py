'''
UC001 -  Status de parcelas e contas

Objetivo: Garantir o controle e a consistência na transição de status de contas e suas respectivas parcelas, englobando tanto as rotinas automáticas do sistema
quanto as ações manuais do tesoureiro.

Requisito Base:
[RF050301] - Status de parcelas e contas

Atores:
- Sistema (Rotina de Backend)
- Tesoureiro

Autor: Luís Miguel Carvalho da Rocha
'''

# 🟢 FLUXOS PRINCIPAIS
# ---------------------------------------------------------------

# FP1 - ATUALIZAÇÃO AUTOMÁTICA DIÁRIA (SISTEMA)
# 1. O sistema executa a rotina diária de verificação de vencimentos.
# 2. O sistema identifica as parcelas com status "Aberta" cujo vencimento já passou e não possuem pagamento.
# 3. O sistema atualiza o status dessas parcelas automaticamente para "Atrasada".
# 4. O sistema atualiza o status da conta correspondente para "Atrasada".

# FP2 - ALTERAÇÃO MANUAL DE STATUS (TESOUREIRO)
# 1. O tesoureiro acessa o sistema e seleciona uma conta.
# 2. O tesoureiro solicita a alteração do status de uma parcela para "Paga" ou "Cancelada".
# 3. O sistema valida se a conta/parcela não se encontra previamente cancelada. [RN4]
# 4. O sistema valida se não é uma tentativa de reverter uma parcela "Paga". [RN5]
# 5. O sistema atualiza o status da parcela conforme a ação do tesoureiro.
# 6. O sistema reavalia as parcelas da conta e deriva automaticamente o novo status da Conta. [RN2]
# 7. O sistema exibe mensagem de sucesso e conclui a operação.

# 🟡 FLUXO ALTERNATIVO
# ---------------------------------------------------------------
# FA1 - TENTATIVA DE ALTERAÇÃO DE CONTA CANCELADA
# 1. No passo 3 do FP2, se o sistema identificar que a conta se encontra com status "Cancelada":
# 2. O sistema bloqueia a edição.
# 3. O sistema exibe uma mensagem informando o cancelamento da conta: "O status da conta selecionada não pode ser alterado".
# 4. O caso de uso é encerrado sem salvar alterações.

# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------

# [RN1] - STATUS DE PARCELAS:
# Os status permitidos para parcelas são estritamente:
# - Aberta: Padrão ao ser criada (vencimento ainda não passou).
# - Atrasada: Vencimento passou sem pagamento.
# - Paga: Atribuída pelo tesoureiro (ou decorrente de validação sistêmica, se a receber).
# - Cancelada: Atribuída pelo tesoureiro.

# [RN2] - STATUS DE CONTAS (DERIVADO):
# O status da conta é derivado exclusivamente do status de suas parcelas:
# - Aberta: Nenhuma parcela foi paga e nenhuma está atrasada.
# - Atrasada: Pelo menos uma de suas parcelas possui o status "Atrasada".
# - Parcial: Ao menos uma parcela está paga e as demais estão "Abertas".
# - Paga: Todas as parcelas estão pagas.
# - Cancelada: Cancelada pelo tesoureiro.

# [RN3] - RESPONSABILIDADE DE ATRIBUIÇÃO:
# - "Aberta" e "Atrasada" são atribuídas EXCLUSIVAMENTE de forma automática por rotina diária.
# - "Paga" e "Cancelada" são atribuídas EXCLUSIVAMENTE de forma manual pelo tesoureiro (ou validação sistêmica de recebimento).

# [RN4] - IRREVERSIBILIDADE DO CANCELAMENTO:
# O status "Cancelada" é permanente e irreversível.

# [RN5] - FLUXO DE PAGAMENTO DE PARCELAS:
# Uma parcela atrasada que é paga transita diretamente para o status "Paga". Uma parcela paga não pode, sob nenhuma hipótese, retornar para o status "Aberta" ou "Atrasada".