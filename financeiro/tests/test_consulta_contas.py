'''
CT005 - Manter Cobranças

Objetivo: Garantir a gestão completa (criar, consultar, atualizar, excluir) das cobranças.

Requisitos: 
- 25925 (US - Consulta de Cobranças organizada por mês)
- 29482 (US - Adicionar juros à cobranças)
- 25931 (US - Visualização detalhada de Cobrança)

Ator:
- Administrador / Tesoureiro

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a página "Cobranças" e seleciona "Nova Cobrança".

# O ator preenche os campos com os dados (Cliente, Valor, Vencimento, Taxa) e clica em Salvar.

# O sistema verifica os dados, gera a cobrança com status "Aguardando Pagamento" e
# exibe mensagem de sucesso.

# O ator seleciona 'Consultar' e visualiza o detalhamento para checar o link de pagamento.

# O ator clica em 'Editar', altera a data de vencimento e salva. [A1]

# O sistema salva os dados e recalcula/atualiza o link de pagamento. [RN1]

# O ator seleciona 'Excluir' na cobrança, confirma a exclusão no modal e o 
# sistema remove a cobrança.


# 🟠 [A1] - COBRANÇA LIQUIDADA
# ---------------------------------------------------------------
# Se o ator tentar editar ou excluir uma cobrança que já possui o status "Paga".

# O sistema bloqueia a ação de exclusão e edição de valor/vencimento.


# 🟣 [RN1] ATUALIZAÇÃO DE LINK
# ---------------------------------------------------------------
# Ao alterar o vencimento ou valor, o link/boleto de pagamento deve ser regenerado
# automaticamente pela integração financeira.


'''
CT006 - Paginação da Listagem Geral

Objetivo: Validar se o sistema respeita o limite de registros por página.

Requisitos: 
- 25922 (US - Consulta Geral de Contas e Cobranças)

Ator:
- Usuário Autenticado

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a listagem de Contas a Pagar (que possui mais de 20 registros no banco).

# O sistema carrega apenas os primeiros 20 registros na tabela. [RN1]

# O ator rola até o final da página e clica no botão "Próximo" ou "Página 2".

# O sistema processa a requisição e exibe os registros da posição 21 a 40.


# 🟣 [RN1] ORDENAÇÃO E LIMITE
# ---------------------------------------------------------------
# O limite padrão da paginação é de 20 itens. A ordenação padrão (mais recentes 
# primeiro) deve ser mantida ao navegar pelas páginas.


'''
CT007 - Agrupamento Mensal de Contas a Pagar

Objetivo: Validar se o sistema exibe as contas agrupadas visualmente por mês.

Requisitos: 
- 25924 (US - Consulta de Contas a Pagar organizada por mês)

Ator:
- Usuário Autenticado

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a tela de Contas a Pagar.

# O sistema processa o agrupamento cronológico de todas as contas no backend.

# O sistema renderiza a tela exibindo seções (acordeões) com o nome do mês e ano. [A1]

# O ator clica no título de um mês e visualiza as contas específicas daquele período. [RN1]


# 🟠 [A1] - MÊS SEM CONTAS
# ---------------------------------------------------------------
# Se não houver nenhum registro de conta vencendo em um mês específico (ex: Janeiro).

# O sistema não deve gerar a seção/acordeão de Janeiro na interface.


# 🟣 [RN1] ORDENAÇÃO DOS MESES
# ---------------------------------------------------------------
# A ordenação das seções de meses deve ser decrescente, exibindo o mês mais 
# recente ou futuro no topo.


'''
CT008 - Exportação Unificada de Contas/Cobranças

Objetivo: Validar a geração de arquivo cruzando contas e cobranças com filtros.

Requisitos: 
- 27184 (US - Busca, Filtro e Exportação unificada)
- 28376 (US - Exportação visual unificada)

Ator:
- Administrador

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a tela de consulta unificada.

# O ator filtra os registros preenchendo um período de datas específico. [A1]

# O ator clica no botão "Exportar XLSX".

# O sistema compila os dados das duas naturezas e inicia o download do arquivo.

# O ator abre o arquivo e verifica que as colunas correspondem aos dados da tela. [RN1]


# 🟠 [A1] - FILTRO SEM RESULTADOS
# ---------------------------------------------------------------
# Se os filtros aplicados não retornarem nenhum dado na listagem da tela.

# O botão de "Exportar XLSX" deve ficar desabilitado (inativo) para clique.


# 🟣 [RN1] DIFERENCIAÇÃO NO ARQUIVO
# ---------------------------------------------------------------
# O arquivo gerado deve conter uma coluna obrigatória "Tipo", diferenciando 
# claramente se a linha é uma Entrada (Cobrança) ou Saída (Conta a Pagar).


'''
CT009 - Comportamento de Lista Vazia

Objetivo: Verificar a usabilidade do sistema quando não existem dados.

Requisitos: 
- 25922 (US - Consulta Geral de Contas e Cobranças)

Ator:
- Usuário Autenticado

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa uma listagem onde nenhum registro foi cadastrado no banco de dados.

# O sistema oculta a estrutura de tabela e cabeçalhos. [RN1]

# O sistema exibe um componente visual contendo a mensagem: 
# "Não há contas ou cobranças cadastradas". [A1]


# 🟠 [A1] - BUSCA SEM RESULTADOS
# ---------------------------------------------------------------
# Se o banco de dados tiver registros, mas o ator pesquisar por um termo inexistente.

# O sistema deve ocultar a tabela e exibir a mensagem: 
# "Nenhum resultado encontrado para a busca".


# 🟣 [RN1] ESTÉTICA DE EMPTY STATE
# ---------------------------------------------------------------
# A tabela padrão não deve ser renderizada vazia e quebrada; a interface deve 
# usar um "Empty State" amigável mantendo os menus operacionais.