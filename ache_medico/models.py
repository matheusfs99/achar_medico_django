from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Especialidade(models.Model):
    ESPECIALIDADE = [
        ('ACUPUNTURA', 'ACUPUNTURA'), ('ALERGIA E IMUNOLOGIA', 'ALERGIA E IMUNOLOGIA'), ('ANESTESIOLOGIA', 'ANESTESIOLOGIA'),
        ('ANGIOLOGIA', 'ANGIOLOGIA'), ('CANCEROLOGIA CLÍNICA', 'CANCEROLOGIA CLÍNICA'), ('CANCEROLOGIA CIRÚRGICA', 'CANCEROLOGIA CIRÚRGICA'),
        ('CANCEROLOGIA PEDIÁTRICA', 'CANCEROLOGIA PEDIÁTRICA'), ('CARDIOLOGIA', 'CARDIOLOGIA'), ('CIRURGIA CARDIOVASCULAR', 'CIRURGIA CARDIOVASCULAR'),
        ('CIRURGIA DE CABEÇA E PESCOÇO', 'CIRURGIA DE CABEÇA E PESCOÇO'), ('CIRURGIA DO APARELHO DIGESTIVO', 'CIRURGIA DO APARELHO DIGESTIVO'),
        ('CIRURGIA GERAL', 'CIRURGIA GERAL'), ('CIRURGIA PEDIÁTRICA', 'CIRURGIA PEDIÁTRICA'), ('CIRURGIA PLÁSTICA', 'CIRURGIA PLÁSTICA'),
        ('CIRURGIA TORÁCICA', 'CIRURGIA TORÁCICA'), ('CIRURGIA VASCULAR', 'CIRURGIA VASCULAR'), ('CLÍNICA MÉDICA', 'CLÍNICA MÉDICA'),
        ('COLOPROCTOLOGIA', 'COLOPROCTOLOGIA'), ('DERMATOLOGIA', 'DERMATOLOGIA'), ('ENDOCRINOLOGIA', 'ENDOCRINOLOGIA'),
        ('ENDOSCOPIA', 'ENDOSCOPIA'), ('GASTROENTEROLOGIA', 'GASTROENTEROLOGIA'), ('GENÉTICA MÉDICA', 'GENÉTICA MÉDICA'),
        ('GERIATRIA', 'GERIATRIA'), ('GINECOLOGIA E OBSTETRÍCIA', 'GINECOLOGIA E OBSTETRÍCIA'), ('HEMATOLOGIA E HEMOTERAPIA', 'HEMATOLOGIA E HEMOTERAPIA'),
        ('HOMEOPATIA', 'HOMEOPATIA'), ('INFECTOLOGIA', 'INFECTOLOGIA'), ('MASTOLOGIA', 'MASTOLOGIA'),
        ('MEDICINA DE FAMÍLIA E COMUNIDADE', 'MEDICINA DE FAMÍLIA E COMUNIDADE'), ('MEDICINA DO TRABALHO', 'MEDICINA DO TRABALHO'),
        ('MEDICINA DO TRÁFEGO', 'MEDICINA DO TRÁFEGO'), ('MEDICINA ESPORTIVA', 'MEDICINA ESPORTIVA'),
        ('MEDICINA FÍSICA E REABILITAÇÃO', 'MEDICINA FÍSICA E REABILITAÇÃO'), ('MEDICINA INTENSIVA', 'MEDICINA INTENSIVA'),
        ('MEDICINA LEGAL', 'MEDICINA LEGAL'), ('MEDICINA NUCLEAR', 'MEDICINA NUCLEAR'), ('MEDICINA PREVENTIVA E SOCIAL', 'MEDICINA PREVENTIVA E SOCIAL'),
        ('NEFROLOGIA', 'NEFROLOGIA'), ('NEUROCIRURGIA', 'NEUROCIRURGIA'), ('NEUROLOGIA', 'NEUROLOGIA'), ('NUTROLOGIA', 'NUTROLOGIA'),
        ('OFTALMOLOGIA', 'OFTALMOLOGIA'), ('ORTOPEDIA e TRAUMATOLOGIA', 'ORTOPEDIA e TRAUMATOLOGIA'), ('OTORRINOLARINGOLOGIA', 'OTORRINOLARINGOLOGIA'),
        ('PATOLOGIA', 'PATOLOGIA'), ('PATOLOGIA CLÍNICA/MEDICINA LABORATORIAL', 'PATOLOGIA CLÍNICA/MEDICINA LABORATORIAL'),
        ('PEDIATRIA', 'PEDIATRIA'), ('PNEUMOLOGIA', 'PNEUMOLOGIA'), ('PSIQUIATRIA', 'PSIQUIATRIA'),
        ('RADIOLOGIA E DIAGNÓSTICO POR IMAGEM', 'RADIOLOGIA E DIAGNÓSTICO POR IMAGEM'), ('DIAGNÓSTICO POR IMAGEM', 'DIAGNÓSTICO POR IMAGEM'),
        ('RADIOTERAPIA', 'RADIOTERAPIA'), ('REUMATOLOGIA', 'REUMATOLOGIA'), ('UROLOGIA', 'UROLOGIA')
    ]

class Plano_Saude(models.Model):
    PLANO = [
        ('Bradesco Saúde', 'Bradesco Saúde'),
        ('Amil', 'Amil'),
        ('NotreDame Intermédica (GNDI)', 'NotreDame Intermédica (GNDI)'),
        ('Porto Seguro', 'Porto Seguro'),
        ('SulAmérica Saúde', 'SulAmérica Saúde'),
        ('Care Plus', 'Care Plus'),
        ('Prevent Senior', 'Prevent Senior'),
        ('Allianz Saúde', 'Allianz Saúde'),
        ('Hapvida', 'Hapvida'),
        ('Sompo Saúde', 'Sompo Saúde'),
        ('Omint', 'Omint'),
        ('AMEPE CAMPE', 'AMEPE CAMPE'),
        ('BANCO CENTRAL (Bancen)', 'BANCO CENTRAL (Bancen)'),
        ('CASSI (Banco do Brasil)', 'CASSI (Banco do Brasil)'),
        ('CONAB', 'CONAB'),
        ('EMBRATEL', 'EMBRATEL'),
        ('FACHESF', 'FACHESF'),
        ('FUNCEF (Saúde Caixa)', 'FUNCEF (Saúde Caixa)'),
        ('GAMA SAÚDE', 'GAMA SAÚDE'),
        ('MEDIAL SAÚDE', 'MEDIAL SAÚDE'),
        ('PLANASSIST MINIST.PUB. TRABALHO', 'PLANASSIST MINIST.PUB. TRABALHO'),
        ('PLANASSIST MINIST.PUB. MILITAR', 'PLANASSIST MINIST.PUB. MILITAR'),
        ('PETROBRAS DISTRIBUIDORA', 'PETROBRAS DISTRIBUIDORA'),
        ('PROASA', 'PROASA'),
        ('UNAFISCO SAÚDE', 'UNAFISCO SAÚDE'),
        ('UNIMED', 'UNIMED'),
        ('AERONÁUTICA', 'AERONÁUTICA'),
        ('CAMED SAÚDE', 'CAMED SAÚDE'),
        ('COMPESASAUDE', 'COMPESASAUDE'),
        ('POSTAL SAÚDE (Correios)', 'POSTAL SAÚDE (Correios)'),
        ('ESTALEIRO ATLÂNTICO SUL (EAS)', 'ESTALEIRO ATLÂNTICO SUL (EAS)'),
        ('FIO SAÚDE', 'FIO SAÚDE'),
        ('FUSEX', 'FUSEX'),
        ('GEAP', 'GEAP'),
        ('MEDISERVICE', 'MEDISERVICE'),
        ('PLANASSIST MINIST. PUB. FEDERAL', 'PLANASSIST MINIST. PUB. FEDERAL'),
        ('OMIINT/SKILL', 'OMIINT/SKILL'),
        ('PETROB. PETROLEO', 'PETROB. PETROLEO'),
    ]

class Sexo(models.Model):
    SEXO = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    ]

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=50, choices=Especialidade.ESPECIALIDADE)
    sexo = models.CharField(max_length=10, choices=Sexo.SEXO)
    data_nascimento = models.DateField()
    telefone = models.BigIntegerField()
    planos_aceitos = MultiSelectField(choices=Plano_Saude.PLANO, null=True, blank=True)
    classificacao = models.FloatField(default=0)
    bio = models.TextField(max_length=500, null=True, blank=True)
    local_de_atendimento = models.TextField(max_length=300)
    foto = models.ImageField(upload_to='medicos_imgs/', blank=True, null=True)