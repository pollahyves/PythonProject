# Generated by Django 4.0 on 2023-01-09 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reunion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id_candidat', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Candidat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id_election', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('heure_election', models.TimeField()),
                ('temps_renouvelable', models.IntegerField()),
            ],
            options={
                'db_table': 'Election',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fond',
            fields=[
                ('id_fond', models.AutoField(primary_key=True, serialize=False)),
                ('type_fond', models.CharField(max_length=25)),
                ('nom_fond', models.CharField(blank=True, max_length=25, null=True)),
                ('montant', models.IntegerField()),
                ('objectif', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Fond',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id_membre', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(blank=True, max_length=25, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=15, null=True)),
                ('adresse', models.CharField(max_length=15)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_naissance', models.DateField()),
                ('profession', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Membre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id_poste', models.AutoField(primary_key=True, serialize=False)),
                ('nom_poste', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Poste',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id_pret', models.AutoField(primary_key=True, serialize=False)),
                ('nom_pret', models.CharField(blank=True, max_length=25, null=True)),
                ('date_pret', models.DateField()),
                ('montant', models.IntegerField()),
                ('date_remboursement', models.DateField()),
                ('interet', models.IntegerField()),
                ('sanction', models.IntegerField()),
                ('raison', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Pret',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id_reunion', models.AutoField(primary_key=True, serialize=False)),
                ('date_reunion', models.DateField()),
                ('beneficiare', models.IntegerField()),
                ('lieu', models.CharField(max_length=25)),
                ('heure', models.TimeField()),
                ('regle', models.CharField(blank=True, max_length=1000, null=True)),
                ('motif', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Reunion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tontine',
            fields=[
                ('id_tontine', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('date_creation', models.DateField()),
                ('slogan', models.CharField(blank=True, max_length=100, null=True)),
                ('regle', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Tontine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppartenirTontine',
            fields=[
                ('id_membre', models.OneToOneField(db_column='id_membre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.membre')),
                ('statut', models.CharField(blank=True, max_length=30, null=True)),
                ('nbr_parts', models.IntegerField()),
            ],
            options={
                'db_table': 'Appartenir_tontine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContribuerFond',
            fields=[
                ('id_fond', models.OneToOneField(db_column='id_fond', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.fond')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'Contribuer_fond',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id_tontine', models.OneToOneField(db_column='id_tontine', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.tontine')),
                ('nom_cotisation', models.CharField(max_length=25)),
                ('montant', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('cycle', models.IntegerField()),
                ('nb_participant', models.IntegerField()),
                ('taux_interet', models.IntegerField()),
            ],
            options={
                'db_table': 'Cotisation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cotiser',
            fields=[
                ('id_membre', models.OneToOneField(db_column='id_membre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.membre')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'Cotiser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipantReunion',
            fields=[
                ('id_reunion', models.OneToOneField(db_column='id_reunion', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.reunion')),
            ],
            options={
                'db_table': 'Participant_Reunion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id_membre', models.OneToOneField(db_column='id_membre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='reunion.membre')),
            ],
            options={
                'db_table': 'Vote',
                'managed': False,
            },
        ),
    ]
