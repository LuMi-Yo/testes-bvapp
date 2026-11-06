'''
CT002 - Aplicação Automática de Juros Diários

Objetivo: Verificar se a rotina diária identifica contas em atraso e aplica os juros.

Requisitos: 
- 25551 (US - Aplicação de juros)
- 23949 (CA01 - O sistema deve aplicar juros após X dias configurável)

Ator:
- Sistema (Job Automático)

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O relógio do servidor atinge 00:00 (virada do dia).

# O sistema busca todas as contas a pagar com status "Pendente" e vencimento 
# inferior à data atual.

# O sistema verifica que os dias de atraso superaram a carência configurada de "X dias". [A1]

# O sistema calcula o juros simples pro-rata die com base na taxa cadastrada.

# O sistema salva o "Valor Atualizado" da conta no banco de dados.


# 🟠 [A1] - CARÊNCIA NÃO ATINGIDA
# ---------------------------------------------------------------
# Se, durante a verificação, o atraso da conta for menor que os "X dias" de carência.

# O sistema ignora a conta e não aplica juros.


'''
CT004 - Validação de Limites de Taxa de Juros

Objetivo: Garantir que o sistema bloqueie taxas de juros inválidas inseridas pelo usuário.

Requisitos: 
- 29512 (CA02 - O sistema não deve permitir juros de 0% ou negativos)
- 29513 (CA03 - O sistema não deve permitir juros de 100% ou mais)

Ator:
- Administrador

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa o formulário de cadastro ou edição de uma conta a pagar.

# O ator insere um valor negativo no campo de taxa de juros (ex: -1%) e 
# tenta clicar em "Salvar".

# O sistema bloqueia a ação e exibe uma mensagem de erro na tela. [RN1]

# O ator altera o valor para 100% ou mais e tenta clicar em "Salvar".

# O sistema bloqueia a ação e exibe uma mensagem de erro na tela. [RN2]


# 🟣 [RN1] LIMITE INFERIOR
# ---------------------------------------------------------------
# O sistema não deve permitir juros de 0% ou negativos, exibindo mensagem: 
# "A taxa de juros deve ser maior que zero".

# 🟣 [RN2] LIMITE SUPERIOR
# ---------------------------------------------------------------
# O sistema não deve permitir juros de 100% ou mais, exibindo mensagem:
# "A taxa de juros deve ser inferior a 100%".


'''
CT010 - Alteração de Taxa de Juros em Contas Atrasadas

Objetivo: Validar o recálculo retroativo do saldo ao editar a taxa de uma conta atrasada.

Requisitos: 
- 29514 (CA04 - Taxa editada atualiza pagamentos em atraso)

Ator:
- Administrador

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a edição de uma conta a pagar que já está atrasada há vários dias.

# O ator altera a taxa de juros (ex: de 2% para 5%) e clica em "Salvar".

# O sistema descarta o cálculo de juros anterior.

# O sistema aplica a nova taxa 

# O sistema exibe o novo valor atualizado na tela de detalhes da conta.

