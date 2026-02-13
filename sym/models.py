from django.db import models

# Create your models here.
class Sym(models.Model):
    fever = models.BigIntegerField(blank=True, null=True)
    tiredness = models.IntegerField(blank=True, null=True)
    drycough = models.IntegerField(blank=True, null=True)
    difficultybreathing = models.IntegerField(blank=True, null=True)
    sorethroat = models.IntegerField(blank=True, null=True)
    nonesympton = models.IntegerField(blank=True, null=True)
    pains = models.IntegerField(blank=True, null=True)
    nasalcongestion = models.IntegerField(blank=True, null=True)
    runnynose = models.IntegerField(blank=True, null=True)
    diarrhea = models.IntegerField(blank=True, null=True)
    noneexperiencing = models.IntegerField(blank=True, null=True)
    age09 = models.IntegerField(blank=True, null=True)
    age1019 = models.IntegerField(blank=True, null=True)
    age2024 = models.IntegerField(blank=True, null=True)
    age2559 = models.IntegerField(blank=True, null=True)
    age60 = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    severitymild = models.IntegerField(blank=True, null=True)
    severitymoderate = models.IntegerField(blank=True, null=True)
    severitysevere = models.IntegerField(blank=True, null=True)
    contactyes = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'sym'

class China(models.Model):
    fever = models.BigIntegerField(blank=True, null=True)
    tiredness = models.IntegerField(blank=True, null=True)
    drycough = models.IntegerField(blank=True, null=True)
    difficultybreathing = models.IntegerField(blank=True, null=True)
    sorethroat = models.IntegerField(blank=True, null=True)
    nonesympton = models.IntegerField( blank=True, null=True)
    pains = models.IntegerField( blank=True, null=True)
    nasalcongestion = models.IntegerField( blank=True, null=True)
    runnynose = models.IntegerField( blank=True, null=True)
    diarrhea = models.IntegerField( blank=True, null=True)
    noneexperiencing = models.IntegerField( blank=True, null=True)
    age09 = models.IntegerField( blank=True, null=True)
    age1019 = models.IntegerField( blank=True, null=True)
    age2024 = models.IntegerField( blank=True, null=True)
    age2559 = models.IntegerField( blank=True, null=True)
    age60 = models.IntegerField( blank=True, null=True)
    gender = models.CharField( max_length=255, blank=True, null=True)
    severitymild = models.IntegerField( blank=True, null=True)
    severitymoderate = models.IntegerField( blank=True, null=True)
    severitysevere = models.IntegerField( blank=True, null=True)
    contactyes = models.IntegerField( blank=True, null=True)
    class Meta:
        db_table='China'

class sym_all(models.Model):
    id=models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255,null=True)
    allperson = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    fever = models.BigIntegerField(blank=True, null=True)
    tiredness = models.IntegerField(blank=True, null=True)
    drycough = models.IntegerField(blank=True, null=True)
    difficultybreathing = models.IntegerField(blank=True, null=True)
    sorethroat = models.IntegerField(blank=True, null=True)
    nonesympton = models.IntegerField(blank=True, null=True)
    pains = models.IntegerField(blank=True, null=True)
    nasalcongestion = models.IntegerField(blank=True, null=True)
    runnynose = models.IntegerField(blank=True, null=True)
    diarrhea = models.IntegerField(blank=True, null=True)
    noneexperiencing = models.IntegerField(blank=True, null=True)
    age09 = models.IntegerField(blank=True, null=True)
    age1019 = models.IntegerField(blank=True, null=True)
    age2024 = models.IntegerField(blank=True, null=True)
    age2559 = models.IntegerField(blank=True, null=True)
    age60field = models.IntegerField(blank=True, null=True)
    age091 = models.IntegerField(blank=True, null=True)
    age10191 = models.IntegerField(blank=True, null=True)
    age20241 = models.IntegerField(blank=True, null=True)
    age25591 = models.IntegerField(blank=True, null=True)
    age60field1 = models.IntegerField(blank=True, null=True)
    age090 = models.IntegerField(blank=True, null=True)
    age10190 = models.IntegerField(blank=True, null=True)
    age20240 = models.IntegerField(blank=True, null=True)
    age25590 = models.IntegerField(blank=True, null=True)
    age60field0 = models.IntegerField(blank=True, null=True)
    severitymild = models.IntegerField(blank=True, null=True)
    severitymoderate = models.IntegerField(blank=True, null=True)
    severitysevere = models.IntegerField(blank=True, null=True)
    contactor = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sym_all'

class France(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'france'


class Germany(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'germany'


class Iran(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iran'


class Italy(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'italy'

class RepublicOfKorean(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'republic of korean'


class Spain(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spain'

class Uae(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uae'
class Other(models.Model):
    fever = models.CharField(db_column='Fever', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiredness = models.CharField(db_column='Tiredness', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drycough = models.CharField(db_column='DryCough', max_length=255, blank=True, null=True)  # Field name made lowercase.
    difficultybreathing = models.CharField(db_column='DifficultyBreathing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sorethroat = models.CharField(db_column='SoreThroat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonesympton = models.CharField(db_column='NoneSympton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pains = models.CharField(db_column='Pains', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nasalcongestion = models.CharField(db_column='NasalCongestion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runnynose = models.CharField(db_column='RunnyNose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diarrhea = models.CharField(db_column='Diarrhea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noneexperiencing = models.CharField(db_column='NoneExperiencing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age09 = models.CharField(db_column='Age09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age1019 = models.CharField(db_column='Age1019', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2024 = models.CharField(db_column='Age2024', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age2559 = models.CharField(db_column='Age2559', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age60 = models.CharField(db_column='Age60', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymild = models.CharField(db_column='SeverityMild', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitymoderate = models.CharField(db_column='SeverityModerate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severitysevere = models.CharField(db_column='SeveritySevere', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactyes = models.CharField(db_column='Contactyes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'other'
class Sym0(models.Model):
    fever = models.BigIntegerField(blank=True, null=True)
    tiredness = models.IntegerField(blank=True, null=True)
    drycough = models.IntegerField(blank=True, null=True)
    difficultybreathing = models.IntegerField(blank=True, null=True)
    sorethroat = models.IntegerField(blank=True, null=True)
    nonesympton = models.IntegerField(blank=True, null=True)
    pains = models.IntegerField(blank=True, null=True)
    nasalcongestion = models.IntegerField(blank=True, null=True)
    runnynose = models.IntegerField(blank=True, null=True)
    diarrhea = models.IntegerField(blank=True, null=True)
    noneexperiencing = models.IntegerField(blank=True, null=True)
    age09 = models.IntegerField(blank=True, null=True)
    age1019 = models.IntegerField(blank=True, null=True)
    age2024 = models.IntegerField(blank=True, null=True)
    age2559 = models.IntegerField(blank=True, null=True)
    age60 = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    severitymild = models.IntegerField(blank=True, null=True)
    severitymoderate = models.IntegerField(blank=True, null=True)
    severitysevere = models.IntegerField(blank=True, null=True)
    contactyes = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'sym0'