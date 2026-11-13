'''
UC002 - Juros por atraso

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

# CT004 - Validação das Regras e Limites da Taxa de Juros

# Objetivo: Garantir que o sistema valide corretamente a inserção da taxa percentual, bloqueando valores inválidos, e exija a seleção do tipo de juros.

# Requisito Base:
# [RF05014] - Como tesoureiro, gostaria de definir a taxa de juros aplicável a cada cobrança e a cada conta a pagar, para que o valor atualizado das parcelas atrasadas seja calculado automaticamente.

# Ator:
# - Tesoureiro

# Responsável:
# - Luís Miguel Carvalho da Rocha

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O tesoureiro acessa o formulário de cadastro ou edição de uma conta a pagar ou cobrança.
# 2. O tesoureiro insere uma taxa de juros inválida igual ou inferior a 0% e tenta salvar.
# 3. O sistema bloqueia a ação e exibe mensagem de erro. [RN1]
# 4. O tesoureiro insere uma taxa de juros inválida igual ou superior a 100% e tenta salvar.
# 5. O sistema bloqueia a ação e exibe mensagem de erro. [RN1]
# 6. O tesoureiro preenche uma taxa válida (ex: 5%), define o tipo de juros (simples ou composto), a carência e clica em "Salvar". [RN1]
# 7. O sistema processa e salva os dados com sucesso.

# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] REGRAS DE TAXA E TIPO:
# A taxa é informada em percentual e deve ser maior que 0% e menor que 100%. O tipo de juros é obrigatoriamente simples ou composto. Mensagens de erro devem ser exibidas caso os limites sejam violados ("A taxa de juros deve ser maior que zero" ou "A taxa de juros deve ser inferior a 100%").

# CT010 - Alteração de Taxa de Juros e Comportamento por Status da Parcela

# Objetivo: Validar que a edição da taxa de juros atualiza as parcelas já atrasadas, mas preserva os valores originais e o valor congelado das parcelas pagas.

# Requisito Base:
# [RF05014] - Como tesoureiro, gostaria de definir a taxa de juros aplicável a cada cobrança e a cada conta a pagar, para que o valor atualizado das parcelas atrasadas seja calculado automaticamente.

# Ator:
# - Tesoureiro

# Responsável:
# - Luís Miguel Carvalho da Rocha

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O tesoureiro acessa a edição de uma conta a pagar/cobrança que já possui parcelas "Atrasadas" e parcelas "Pagas".
# 2. O tesoureiro altera a taxa de juros (ex: de 2% para 4%) ou altera o tipo de juros e clica em "Salvar".
# 3. O sistema recalcula o "Valor Atualizado" das parcelas "Atrasadas", aplicando a nova configuração de juros. [RN1]
# 4. O sistema mantém congelado o "Valor Atualizado" das parcelas "Pagas", ignorando a nova taxa para elas. [RN1]
# 5. O sistema preserva o "Valor Original" inalterado para todas as parcelas (atrasadas e pagas).
# 6. O sistema atualiza as listagens e detalhes para exibir as mudanças.

# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] ATUALIZAÇÃO RETROATIVA E CONGELAMENTO:
# Se a taxa for editada, as parcelas já atrasadas passam a usar a nova taxa. Parcela paga mantém congelado o valor atualizado na data do pagamento.
