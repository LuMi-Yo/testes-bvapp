'''
CT001 - Manter contas a pagar

Objetivo: Garantir que o usuário possa criar, consultar, atualizar e excluir contas a pagar no sistema.

Requisitos: 
- 25922 (US - Consulta Geral de Contas e Cobranças)
- 29505 (US - Adicionar juros à contas a pagar)
- 25926 (US - Visualização detalhada de Conta a Pagar)
- 27273 (US - Visualização de Conta a Pagar)

Ator:
- Administrador / Tesoureiro

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página "Contas a Pagar" e seleciona "Nova Conta". Ele observa
# que existem os campos:
# - Fornecedor
# - Valor
# - Vencimento
# - Taxa de Juros
# - Opções:
# -- Botão "Salvar"
# -- Botão "Cancelar"

# O ator preenche os campos com os dados da conta (ex: Energisa, R$ 500,00, 2%).

# Ao concluir o preenchimento, ele seleciona a opção "Salvar". 
 
# O sistema verifica que os dados estão corretos [RN1]

# O sistema exibe a página de listagem geral de contas novamente e exibe uma
# mensagem de sucesso informando que a conta foi cadastrada.

# O ator verifica que a conta cadastrada está na lista com status "Pendente".


# 🟠 [A1] - BUSCAR E CONSULTAR CONTA
# ---------------------------------------------------------------

# O ator necessita realizar uma busca pela conta cadastrada. 
# Ele acessa a página "Contas a Pagar".

# O sistema exibe a página de listagem.

# Ele seleciona o campo de busca e digita o nome do Fornecedor ("Energisa").

# O ator seleciona 'Pesquisar'.

# O sistema exibe a conta que corresponde ao termo.

# O ator clica na conta para visualizar os detalhes gravados e confirma os dados.


# 🟠 [A2] - EDITAR CONTA
# ---------------------------------------------------------------
# O ator executa [A1].

# O ator seleciona a conta na lista e clica no botão para editar. [A4]

# O sistema exibe a página de edição de contas com os campos preenchidos.

# O ator altera o valor da conta (ex: para R$ 550,00) e clica no botão para salvar.

# O sistema salva os dados e exibe a lista de contas.

# O ator verifica que o valor da conta foi atualizado na lista.


# 🟠 [A3] - EXCLUIR CONTA
# ---------------------------------------------------------------
# O ator decide excluir a conta e executa [A1]. 

# Ele visualiza a conta e seleciona a opção 'Excluir'.

# O sistema pergunta em um modal se o usuário realmente deseja excluir a conta.

# O ator confirma a exclusão.

# O sistema exclui a conta logicamente.

# O sistema exibe a lista de contas cadastradas.

# O ator verifica que a conta excluída não está mais na lista.


# 🟠 [A4] - EDIÇÃO DE CONTA JÁ PAGA
# ---------------------------------------------------------------
# Durante a execução do [A2], se o status da conta constar como "Paga".

# O sistema desabilita a edição dos campos de Valor e Vencimento.

# O ator pode apenas alterar anexos ou observações.


# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------
# Todas as informações são obrigatórias, exceto o campo 'Taxa de Juros' e anexos.