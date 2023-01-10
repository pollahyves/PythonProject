from distutils.command.upload import upload
from email.policy import default
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_comissaire = models.BooleanField(default=False)
    is_president = models.BooleanField(default=False)
    is_secretaire = models.BooleanField(default=False)
    is_membre = models.BooleanField(default=True)

class AppartenirTontine(models.Model):
    id_membre = models.OneToOneField('Membre', models.DO_NOTHING, db_column='id_membre', primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    statut = models.CharField(max_length=30, blank=True, null=True)
    nbr_parts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Appartenir_tontine'
        unique_together = (('id_membre', 'id_tontine'),)


class Candidat(models.Model):
    id_candidat = models.AutoField(primary_key=True)
    id_membre = models.ForeignKey('Membre', models.DO_NOTHING, db_column='id_membre')
    id_election = models.ForeignKey('Election', models.DO_NOTHING, db_column='id_election')
    id_poste = models.ForeignKey('Poste', models.DO_NOTHING, db_column='id_poste')

    class Meta:
        managed = False
        db_table = 'Candidat'


class ContribuerFond(models.Model):
    id_fond = models.OneToOneField('Fond', models.DO_NOTHING, db_column='id_fond', primary_key=True)
    id_membre = models.ForeignKey('Membre', models.DO_NOTHING, db_column='id_membre')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'Contribuer_fond'
        unique_together = (('id_fond', 'id_membre', 'date'),)


class Cotisation(models.Model):
    id_tontine = models.OneToOneField('Tontine', models.DO_NOTHING, db_column='id_tontine', primary_key=True)
    nom_cotisation = models.CharField(max_length=25)
    montant = models.IntegerField()
    date_debut = models.DateField()
    cycle = models.IntegerField()
    nb_participant = models.IntegerField()
    taux_interet = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Cotisation'


class Cotiser(models.Model):
    id_membre = models.OneToOneField('Membre', models.DO_NOTHING, db_column='id_membre', primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'Cotiser'
        unique_together = (('id_membre', 'id_tontine', 'date'),)


class Election(models.Model):
    id_election = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    date = models.DateField()
    heure_election = models.TimeField()
    temps_renouvelable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Election'


class Fond(models.Model):
    id_fond = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    id_membre = models.ForeignKey('Membre', models.DO_NOTHING, db_column='id_membre')
    type_fond = models.CharField(max_length=25)
    nom_fond = models.CharField(max_length=25, blank=True, null=True)
    montant = models.IntegerField()
    objectif = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fond'


class Membre(models.Model):
    id_membre = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25, blank=True, null=True)
    e_mail = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    date_naissance = models.DateField()
    profession = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Membre'


class ParticipantReunion(models.Model):
    id_reunion = models.OneToOneField('Reunion', models.DO_NOTHING, db_column='id_reunion', primary_key=True)
    id_membre = models.ForeignKey(Membre, models.DO_NOTHING, db_column='id_membre')

    class Meta:
        managed = False
        db_table = 'Participant_Reunion'
        unique_together = (('id_reunion', 'id_membre'),)


class Poste(models.Model):
    id_poste = models.AutoField(primary_key=True)
    nom_poste = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Poste'


class Pret(models.Model):
    id_pret = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    id_membre = models.ForeignKey(Membre, models.DO_NOTHING, db_column='id_membre')
    nom_pret = models.CharField(max_length=25, blank=True, null=True)
    date_pret = models.DateField()
    montant = models.IntegerField()
    date_remboursement = models.DateField()
    interet = models.IntegerField()
    sanction = models.IntegerField()
    raison = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pret'


class Reunion(models.Model):
    id_reunion = models.AutoField(primary_key=True)
    id_tontine = models.ForeignKey('Tontine', models.DO_NOTHING, db_column='id_tontine')
    date_reunion = models.DateField()
    beneficiare = models.IntegerField()
    lieu = models.CharField(max_length=25)
    heure = models.TimeField()
    regle = models.CharField(max_length=1000, blank=True, null=True)
    motif = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reunion'


class Tontine(models.Model):
    id_tontine = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=15)
    date_creation = models.DateField()
    slogan = models.CharField(max_length=100, blank=True, null=True)
    regle = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tontine'


class Vote(models.Model):
    id_membre = models.OneToOneField(Membre, models.DO_NOTHING, db_column='id_membre', primary_key=True)
    id_election = models.ForeignKey(Election, models.DO_NOTHING, db_column='id_election')
    id_poste = models.ForeignKey(Poste, models.DO_NOTHING, db_column='id_poste')
    id_candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='id_candidat')

    class Meta:
        managed = False
        db_table = 'Vote'
        unique_together = (('id_membre', 'id_election', 'id_poste'),)
