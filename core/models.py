from django.db import models


class Colecao(models.Model):
    DEFAULT_PK = 1
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Coleções'
        verbose_name = 'Coleção'

    def __str__(self):
        return self.nome


class Amigo(models.Model):
    DEFAULT_PK = 1
    grupoAmigo_CHOICES = (
        ('PREDIO', 'Prédio'),
        ('ESCOLA', 'Escola'),
    )

    nome = models.CharField(max_length=50)
    nome_mae = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    grupo_amigo = models.CharField(max_length=50, choices=grupoAmigo_CHOICES)

    class Meta:
        verbose_name_plural = 'Amigos'
        verbose_name = 'Amigo'

    def __str__(self):
        return self.nome


class Caixa(models.Model):
    DEFAULT_PK = 1
    numero = models.IntegerField()
    etiqueta = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Caixas'
        verbose_name = 'Caixa'

    def __str__(self):
        return 'Caixa ' + str(self.cor)


class Revista(models.Model):
    DEFAULT_PK = 1
    colecao = models.ForeignKey(Colecao, default=Colecao.DEFAULT_PK, on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixa, default=Caixa.DEFAULT_PK, on_delete=models.CASCADE)
    numero_edicao = models.IntegerField()
    ano = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Revistas'
        verbose_name = 'Revista'

    def __str__(self):
        return 'Edição n° ' + str(self.numero_edicao)


class Emprestimo(models.Model):
    nome_do_amigo = models.ForeignKey(Amigo, default=Amigo.DEFAULT_PK, on_delete=models.CASCADE)
    numero_da_revista = models.ForeignKey(Revista, default=Revista.DEFAULT_PK, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    class Meta:
        verbose_name_plural = 'Emprestimos'
        verbose_name = 'Emprestimo'

    def __str__(self):
        return 'Emprestimo para ' + str(self.nome_do_amigo)