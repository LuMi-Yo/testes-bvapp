'''
CT003 - Visualização de Comprovantes Anexados

Objetivo: Validar que o tesoureiro consegue acessar e conferir os arquivos enviados.

Requisitos: 
- 28889 (US - Visualizar solicitações de novos comprovantes)

Ator:
- Tesoureiro

Responsável:
- Luís Miguel
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a aba "Solicitações de Novos Comprovantes".

# O sistema exibe uma tabela com os comprovantes pendentes. [RN1]

# O ator clica no botão "Visualizar Anexo" de um registro.

# O sistema abre o comprovante (PDF ou Imagem) em um modal sobreposto à tela. [A1]

# O ator visualiza o nome do cooperado, a parcela e o valor lado a lado com o arquivo.


# 🟠 [A1] - ERRO DE CARREGAMENTO
# ---------------------------------------------------------------
# Durante a abertura do modal, se o arquivo não for encontrado no storage da nuvem.

# O sistema exibe um placeholder visual e a mensagem: "Erro ao carregar o arquivo".


# 🟣 [RN1] LISTAGEM DE COMPROVANTES
# ---------------------------------------------------------------
# Apenas comprovantes vinculados a faturas com status "Em Análise" devem 
# aparecer nesta listagem principal.