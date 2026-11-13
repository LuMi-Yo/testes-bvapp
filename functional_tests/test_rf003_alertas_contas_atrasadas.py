'''
UC003 - Alertas de vencimento e de atraso

Objetivo: Notificar cooperados e tesoureiros sobre parcelas próximas do vencimento ou já em atraso diretamente na página inicial, visando evitar a inadimplência e facilitar o controle financeiro.

Requisito Base:
[RF050303] - Alertas de vencimento e de atraso

Atores:
- Cooperado
- Tesoureiro
- Sistema (Rotina de Backend)

Autor: Luís Miguel Carvalho da Rocha
'''

# 🟢 FLUXOS PRINCIPAIS
# ---------------------------------------------------------------

# FP1 - ALERTA DE PROXIMIDADE DE VENCIMENTO
# 1. O sistema executa a rotina diária e identifica parcelas não pagas que vencem dentro do período de antecedência configurado (padrão de 7 dias corridos). [RN1]
# 2. O ator (Cooperado ou Tesoureiro) realiza login e acessa a página inicial da plataforma.
# 3. O sistema verifica que o ator possui a opção de receber notificações habilitada. [RN2]
# 4. O sistema verifica que o vencimento cai em um dia útil. [A2]
# 5. O sistema exibe um pop-up amarelo no canto superior direito da tela.
# 6. O ator visualiza a mensagem padrão do alerta, contendo a identificação da conta, nome, valor original e data de vencimento. [RN3]

# FP2 - ALERTA DE PARCELA EM ATRASO
# 1. O sistema executa a rotina diária e identifica parcelas com o vencimento ultrapassado e não pagas.
# 2. O sistema sinaliza essas parcelas como "Atrasadas". [RN6]
# 3. O ator (Cooperado ou Tesoureiro) acessa a página inicial da plataforma.
# 4. O sistema verifica as permissões de notificação e exibe um alerta específico de atraso para o cooperado (suas cobranças) e para o tesoureiro (contas a pagar).

# 🟡 FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------

# A1 - NOTIFICAÇÕES DESABILITADAS PELO USUÁRIO
# 1. Durante o passo 3 do FP1 ou FP2, o sistema verifica que o ator tem a opção de "receber notificações" DESABILITADA em seu perfil.
# 2. O sistema NÃO exibe nenhum pop-up de alerta na página inicial.

# A2 - VENCIMENTO CAI EM DIA NÃO ÚTIL (FIM DE SEMANA/FERIADO)
# 1. Durante a verificação da rotina diária (Passo 4 do FP1), o sistema identifica que a parcela vence em um dia não útil (sábado, domingo ou feriado). [RN4]
# 2. O sistema exibe o pop-up com fundo amarelo padrão.
# 3. O sistema adiciona um destaque visual e textual ao alerta informando essa condição (ex: "Atenção: O vencimento cai em um fim de semana ou feriado").

# A3 - PARCELA PAGA OU CANCELADA
# 1. O ator possuía uma conta que estava gerando alertas (próxima ao vencimento ou atrasada).
# 2. A parcela correspondente é quitada ("Paga") ou "Cancelada". [RN5]
# 3. O ator acessa a página inicial da plataforma.
# 4. O sistema não repete a exibição do alerta para essa parcela.

# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------

# [RN1] VERIFICAÇÃO DIÁRIA E ELEGIBILIDADE:
# Diariamente, o sistema identifica parcelas não pagas. São elegíveis para notificação de proximidade as parcelas cujo vencimento ocorra dentro da antecedência configurada (padrão de 7 dias corridos).

# [RN2] PÚBLICO-ALVO E PERMISSÃO:
# O cooperado recebe alertas de suas próprias cobranças. O tesoureiro recebe alertas das contas a pagar da cooperativa. A exibição do pop-up na página inicial depende de o usuário ter habilitado as notificações na plataforma.

# [RN3] PADRÃO VISUAL E CONTEÚDO DO ALERTA (A VENCER):
# O alerta deve ser um pop-up amarelo no canto superior direito. A mensagem padrão obrigatória é: "Sócio(a) [NOME], faltam [N] dias para o vencimento da conta [IDENTIFICAÇÃO]". O alerta deve trazer a identificação da conta, nome do cooperado, valor original e data de vencimento.

# [RN4] TRATAMENTO DE DIAS NÃO ÚTEIS:
# A contagem considera dias corridos. Se o vencimento cair em dia não útil, o alerta deve obrigatoriamente destacar essa condição para o usuário.

# [RN5] CESSAÇÃO DE ALERTAS:
# O alerta de uma parcela não é repetido depois que o seu status for alterado para "Paga" ou "Cancelada".

# [RN6] SINALIZAÇÃO DE ATRASO:
# Parcelas vencidas e não pagas passam a ser sinalizadas automaticamente como atrasadas e devem gerar um alerta de atraso no acesso do respectivo cooperado e do tesoureiro.