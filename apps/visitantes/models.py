from django.db import models

class Visitante(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO","Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIXADO", "Visita finalizada")
    ]

    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO"
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now_add=False,
        auto_now=False,
    )
     
    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada"
    ) 

    placa_veiculo = models.CharField(
        verbose_name="Placa de veículo",
        max_length=7,
        blank=True,
        null=True,
    )


    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True
    )

    resgistrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida

        return "Horário de saída não registrado"

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao

        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel

        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
        return "Veículo não registrado"

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            cpf_parte_1 = cpf[0:3]
            cpf_parte_2 = cpf[3:6]
            cpf_parte_3 = cpf[6:9]
            cpf_parte_4 = cpf[9:]

            cpf_formatado = f"{cpf_parte_1}.{cpf_parte_2}.{cpf_parte_3}-{cpf_parte_4}"
            return cpf_formatado

    class Meta:
        verbose_name = "visitante"
        verbose_name_plural ="Visitantes"
        db_table = "visitante"


    def __str__(self):
        return self.nome_completo