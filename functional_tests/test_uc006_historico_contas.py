'''
UC006 - Geração, Consulta e Imutabilidade do Histórico de Contas

Objetivo: Garantir que o sistema rastreie automaticamente as alterações em contas e cobranças, permitindo a consulta estruturada em uma aba específica e assegurando a total imutabilidade dos registros.

Requisito Base:
[RF050304] - Histórico de alterações de contas e cobranças

Ator:
- Tesoureiro
- Sistema

Responsável:
- Luís Miguel Carvalho da Rocha
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O tesoureiro realiza uma ação rastreável em uma conta/cobrança (ex: cadastra, edita valor/vencimento, altera status para "Paga", valida comprovante ou remove a conta).
# 2. O sistema gera automaticamente os registros correspondentes no histórico da conta. [RN1]
# 3. O tesoureiro acessa a listagem de contas ou cobranças e seleciona a referida conta para ver os detalhes.
# 4. O tesoureiro clica na aba "Histórico". [RN4]
# 5. O sistema exibe uma lista cronológica contendo todos os registros de alteração daquela conta.
# 6. O tesoureiro visualiza a estrutura do registro gerado, e o sistema exibe corretamente: o campo alterado, o Valor Anterior, o Novo Valor, o Usuário responsável, a Data e a Hora da alteração. [RN2]


# 🟡 FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# [FA1] - TENTATIVA DE ALTERAÇÃO OU EXCLUSÃO DE LOG
# 1. No passo 4 do [FP], o tesoureiro (ou administrador) tenta encontrar opções para editar, mascarar ou excluir um registro de log existente.
# 2. O sistema não exibe nenhuma interface, botão ou atalho que permita a alteração dos registros (read-only).
# 3. A integridade do histórico é mantida. [RN3]

# [FA2] - CONSULTA DE HISTÓRICO DE CONTA REMOVIDA
# 1. O tesoureiro realiza a remoção lógica ou o cancelamento definitivo de uma conta no sistema.
# 2. O sistema gera o registro final de remoção/cancelamento.
# 3. O tesoureiro (ou auditor) acessa os registros da conta removida.
# 4. O sistema mantém o histórico da conta removida intacto e permanentemente disponível para auditoria. [RN3]


# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] EVENTOS RASTREADOS: 
# Toda criação, edição, mudança de status, validação de comprovante e remoção de conta/cobrança deve, obrigatoriamente, disparar a geração de um registro de log. Em caso de edição de múltiplos dados, o sistema deve registrar exatamente qual campo foi alterado.

# [RN2] ESTRUTURA DO REGISTRO: 
# Cada registro no histórico deve exibir de forma padronizada e obrigatória: 
# - O campo alterado;
# - O valor anterior;
# - O novo valor;
# - O nome do usuário que realizou a ação;
# - A data e a hora da ocorrência.

# [RN3] IMUTABILIDADE: 
# O registro gerado no histórico é estritamente imutável. Nenhum usuário do sistema (incluindo administradores) pode editar, mascarar ou deletar um log. Históricos de contas canceladas ou removidas devem ser preservados intactos para auditoria.

# [RN4] LOCALIZAÇÃO NA INTERFACE: 
# O histórico deve ser posicionado e exibido exclusivamente dentro de uma aba específica, localizada no detalhe da conta ou cobrança.