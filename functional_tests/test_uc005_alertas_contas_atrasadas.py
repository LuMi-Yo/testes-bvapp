'''
UC005 - Alertas de Vencimento e de Atraso na Página Inicial

Objetivo: Notificar cooperados e tesoureiros sobre parcelas próximas do vencimento ou já em atraso diretamente na página inicial, visando evitar a inadimplência e facilitar o controle financeiro.

Requisito Base:
[RF050303] - Alertas de vencimento e de atraso

Atores:
- Cooperado
- Tesoureiro
- Sistema (Rotina de Backend)

Autor: Luís Miguel Carvalho da Rocha
'''


# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O sistema executa a rotina diária, sinalizando parcelas vencidas como "Atrasadas" e mapeando as parcelas que vencem dentro da antecedência padrão (7 dias corridos). [RN1] [RN5]
# 2. O ator (Cooperado ou Tesoureiro) realiza login e acessa a página inicial da plataforma.
# 3. O sistema verifica que o ator possui a opção de receber notificações habilitada no perfil. [RN2]
# 4. O sistema identifica que o ator possui parcelas elegíveis para alerta (próximas ao vencimento em dia útil ou já em atraso).
# 5. O sistema exibe um pop-up amarelo no canto superior direito da tela. [RN3]
# 6. O ator visualiza a mensagem padrão aplicável, contendo obrigatoriamente a identificação da conta, nome, valor original e data de vencimento. [RN3]


# 🟡 FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# [FA1] - NOTIFICAÇÕES DESABILITADAS PELO USUÁRIO
# 1. No passo 3 do [FP], o sistema verifica que o ator tem a opção de "receber notificações" DESABILITADA em seu perfil.
# 2. O sistema NÃO exibe nenhum pop-up de alerta (seja de proximidade ou atraso) na página inicial.

# [FA2] - VENCIMENTO CAI EM DIA NÃO ÚTIL (FIM DE SEMANA/FERIADO)
# 1. No passo 4 do [FP], se a parcela estiver próxima ao vencimento e a data cair em um dia não útil (sábado, domingo ou feriado):
# 2. O sistema exibe o pop-up com fundo amarelo padrão.
# 3. O sistema adiciona um destaque visual e textual obrigatório ao alerta informando essa condição (ex: "Atenção: O vencimento cai em um fim de semana ou feriado"). [RN4]

# [FA3] - CESSAÇÃO DO ALERTA (PARCELA PAGA OU CANCELADA)
# 1. O ator possuía uma conta que estava gerando alertas na página inicial (a vencer ou atrasada).
# 2. O status dessa parcela é alterado para "Paga" ou "Cancelada".
# 3. O ator acessa a página inicial da plataforma.
# 4. O sistema encerra as verificações para esta parcela e não repete a exibição do alerta. [RN6]


# 🟣 REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] VERIFICAÇÃO DIÁRIA E PROXIMIDADE:
# Diariamente, o sistema identifica parcelas não pagas. São elegíveis para notificação de proximidade as parcelas cujo vencimento ocorra dentro da antecedência configurada (padrão de 7 dias corridos).

# [RN2] PÚBLICO-ALVO E PERMISSÃO:
# O cooperado recebe alertas APENAS de suas próprias cobranças. O tesoureiro recebe alertas das contas a pagar da cooperativa. A exibição do pop-up depende de o usuário ter habilitado as notificações ativamente na plataforma.

# [RN3] PADRÃO VISUAL E CONTEÚDO DO ALERTA:
# O alerta deve ser um pop-up amarelo no canto superior direito. A mensagem padrão para proximidade é: "Sócio(a) [NOME], faltam [N] dias para o vencimento da conta [IDENTIFICAÇÃO]". Todo alerta deve exibir a identificação da conta, nome, valor original e data de vencimento.

# [RN4] TRATAMENTO DE DIAS NÃO ÚTEIS:
# A contagem de proximidade considera dias corridos. Se o vencimento exato cair em dia não útil, o alerta deve destacar essa condição na tela.

# [RN5] SINALIZAÇÃO DE ATRASO:
# Parcelas vencidas e não pagas passam a ser sinalizadas automaticamente como "Atrasadas" (RF05011) pela rotina diária e geram alerta de atraso ao acessar a home (para o respectivo cooperado ou tesoureiro).

# [RN6] CESSAÇÃO DE ALERTAS:
# O alerta de uma parcela não deve, sob nenhuma hipótese, ser repetido depois que a parcela for efetivamente paga ou cancelada.