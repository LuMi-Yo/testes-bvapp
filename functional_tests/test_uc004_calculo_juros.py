'''
UC004 - Atualização de Taxa de Juros e Aplicação nas Parcelas

Objetivo: Garantir que o sistema valide os limites da nova taxa de juros informada pelo tesoureiro e atualize corretamente os valores das parcelas, recalculando as atrasadas, congelando as pagas e preservando os valores originais.

Requisito Base:
[RF05014] - Como tesoureiro, gostaria de definir a taxa de juros aplicável a cada cobrança e a cada conta a pagar, para que o valor atualizado das parcelas atrasadas seja calculado automaticamente.

Ator:
- Tesoureiro

Responsável:
- Luís Miguel Carvalho da Rocha
'''


# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O tesoureiro acessa a edição de uma conta a pagar ou cobrança que já possui parcelas "Atrasadas" e parcelas "Pagas".
# 2. O tesoureiro insere uma nova taxa de juros válida (ex: alterando de 2% para 4%), confirma o tipo de juros (simples ou composto) e clica em "Salvar".
# 3. O sistema valida que a taxa está dentro dos limites permitidos. [RN1]
# 4. O sistema recalcula o "Valor Atualizado" das parcelas "Atrasadas", aplicando a nova configuração de juros retroativamente. [RN2]
# 5. O sistema mantém congelado o "Valor Atualizado" das parcelas "Pagas", ignorando a nova taxa para elas. [RN2]
# 6. O sistema preserva o "Valor Original" inalterado para todas as parcelas (atrasadas e pagas). [RN3]
# 7. O sistema salva as alterações, exibe mensagem de sucesso e atualiza as listagens e detalhes.


# 🟡 FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# [FA1] - TAXA DE JUROS IGUAL OU INFERIOR A 0%
# 1. No passo 2 do [FP], o tesoureiro insere uma taxa de juros igual ou inferior a 0% e tenta salvar.
# 2. O sistema bloqueia a ação de salvamento.
# 3. O sistema exibe a mensagem de erro: "A taxa de juros deve ser maior que zero". [RN1]
# 4. O processo é interrompido aguardando correção.

# [FA2] - TAXA DE JUROS IGUAL OU SUPERIOR A 100%
# 1. No passo 2 do [FP], o tesoureiro insere uma taxa de juros igual ou superior a 100% e tenta salvar.
# 2. O sistema bloqueia a ação de salvamento.
# 3. O sistema exibe a mensagem de erro: "A taxa de juros deve ser inferior a 100%". [RN1]
# 4. O processo é interrompido aguardando correção.


# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] REGRAS DE TAXA E TIPO:
# A taxa é informada em percentual e deve ser obrigatoriamente maior que 0% e menor que 100%. O tipo de juros é obrigatoriamente simples ou composto. Violações disparam os bloqueios e mensagens descritos nos fluxos alternativos.

# [RN2] ATUALIZAÇÃO RETROATIVA E CONGELAMENTO:
# Ao editar a taxa, o recálculo incide imediatamente sobre o "Valor Atualizado" das parcelas que já estão atrasadas. Parcela paga jamais sofre alteração, mantendo o "Valor Atualizado" rigorosamente congelado com base na data do pagamento efetivado.

# [RN3] PRESERVAÇÃO E EXIBIÇÃO:
# O "Valor Original" da parcela nunca é alterado por incidência de juros. Nas telas de listagem e detalhes, o sistema deve sempre exibir o valor original e o valor atualizado para garantir a rastreabilidade.