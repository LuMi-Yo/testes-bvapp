'''
UC001 - Atualização Automática de Status de Parcelas e Contas

Objetivo: Garantir a transição correta e automática do status de parcelas e contas para "Atrasada" quando o vencimento é ultrapassado sem pagamento.

Requisito Base:
[RF050301] - Status de parcelas e contas

Ator:
- Sistema (Rotina de Backend)

Autor: Luís Miguel Carvalho da Rocha
'''


# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O sistema executa a rotina diária de verificação de vencimentos.
# 2. O sistema identifica as parcelas com status "Aberta" cujo vencimento já passou e não possuem pagamento.
# 3. O sistema atualiza o status dessas parcelas automaticamente para "Atrasada". [RN1]
# 4. O sistema reavalia as parcelas da conta e atualiza o status da conta correspondente para "Atrasada". [RN2]


# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] - STATUS DE PARCELAS:
# Os status permitidos para parcelas são estritamente: Aberta, Atrasada, Paga e Cancelada. "Aberta" é o padrão ao ser criada (vencimento ainda não passou), e "Atrasada" ocorre quando o vencimento passou sem pagamento.

# [RN2] - STATUS DE CONTAS (DERIVADO):
# O status da conta é derivado exclusivamente do status de suas parcelas. Para ser "Atrasada", pelo menos uma de suas parcelas deve possuir o status "Atrasada". 

# [RN3] - RESPONSABILIDADE DE ATRIBUIÇÃO (SISTEMA):
# Os status "Aberta" e "Atrasada" são atribuídos EXCLUSIVAMENTE de forma automática por rotina diária do sistema.