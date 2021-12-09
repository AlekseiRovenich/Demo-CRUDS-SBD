# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Antigen(models.Model):
    iantigenid = models.AutoField(db_column='iAntigenID', primary_key=True)  # Field name made lowercase.
    cantigen = models.CharField(db_column='cAntigen', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Antigen'


class Bloodtype(models.Model):
    ibloodtypeid = models.AutoField(db_column='iBloodTypeID', primary_key=True)  # Field name made lowercase.
    vbloodtype = models.CharField(db_column='vBloodType', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BloodType'


class Comorbility(models.Model):
    icomoborbility = models.IntegerField(db_column='iComoborbility', primary_key=True)  # Field name made lowercase.
    vriskfactor = models.CharField(db_column='vRiskFactor', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comorbility'


class DataAdmin(models.Model):
    idataadminid = models.AutoField(db_column='iDataAdminID', primary_key=True)  # Field name made lowercase.
    dadmitted = models.DateTimeField(db_column='dAdmitted', blank=True, null=True)  # Field name made lowercase.
    ddischarged = models.DateTimeField(db_column='dDischarged', blank=True, null=True)  # Field name made lowercase.
    vdescriptiondischarge = models.CharField(db_column='vDescriptionDischarge', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bensurance = models.BooleanField(db_column='bEnsurance')  # Field name made lowercase.
    iensuranceproviderid = models.ForeignKey('Ensuranceproviders', models.DO_NOTHING, db_column='iEnsuranceProviderID')  # Field name made lowercase.
    fensurancecoveragepercent = models.FloatField(db_column='fEnsuranceCoveragePercent', blank=True, null=True)  # Field name made lowercase.
    bpatientattention = models.ForeignKey('Patientattention', models.DO_NOTHING, db_column='bPatientAttention')  # Field name made lowercase.
    fadmininfoexam = models.FloatField(db_column='fAdminInfoExam')  # Field name made lowercase.
    fadminpharmainfo = models.FloatField(db_column='fAdminPharmaInfo')  # Field name made lowercase.
    fspecialistfee = models.FloatField(db_column='fSpecialistfee')  # Field name made lowercase.
    fsubtotalpatient = models.FloatField(db_column='fSubtotalPatient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Data_Admin'


class DataClinic(models.Model):
    idataclinicid = models.AutoField(db_column='iDataClinicID', primary_key=True)  # Field name made lowercase.
    vreasonconsult = models.CharField(db_column='vReasonConsult', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vinitialdx = models.CharField(db_column='vInitialDx', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vdifferentialdx = models.CharField(db_column='vDifferentialDx', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brequiresexam = models.BooleanField(db_column='bRequiresExam')  # Field name made lowercase.
    iexamid = models.ForeignKey('Exam', models.DO_NOTHING, db_column='iExamID', blank=True, null=True)  # Field name made lowercase.
    brequiresspecialist = models.BooleanField(db_column='bRequiresSpecialist')  # Field name made lowercase.
    ispecialistid = models.ForeignKey('Specialists', models.DO_NOTHING, db_column='iSpecialistID', blank=True, null=True)  # Field name made lowercase.
    brequiresprescription = models.BooleanField(db_column='bRequiresPrescription')  # Field name made lowercase.
    iprescriptionid = models.ForeignKey('Pharmacy', models.DO_NOTHING, db_column='iPrescriptionID', blank=True, null=True)  # Field name made lowercase.
    brequirescheckup = models.BooleanField(db_column='bRequiresCheckUp')  # Field name made lowercase.
    dcheckupdate = models.DateTimeField(db_column='dCheckUpDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Data_Clinic'


class Ensuranceproviders(models.Model):
    iensuranceproviderid = models.IntegerField(db_column='iEnsuranceProviderID', primary_key=True)  # Field name made lowercase.
    vprovidername = models.CharField(db_column='vProviderName', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EnsuranceProviders'


class Exam(models.Model):
    iexamid = models.IntegerField(db_column='iExamID', primary_key=True)  # Field name made lowercase.
    vclinicinfoexam = models.CharField(db_column='vClinicInfoExam', max_length=1000)  # Field name made lowercase.
    fadmininfoexam = models.FloatField(db_column='fAdminInfoExam', blank=True, null=True)  # Field name made lowercase.
    ddateofexam = models.DateTimeField(db_column='dDateOfExam', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exam'


class Health(models.Model):
    thealth = models.SmallIntegerField(db_column='tHealth', primary_key=True)  # Field name made lowercase.
    vhealthstatus = models.CharField(db_column='vHealthStatus', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Health'


class Patient(models.Model):
    ipatientid = models.AutoField(db_column='iPatientID', primary_key=True)  # Field name made lowercase.
    idataadminid = models.ForeignKey(DataAdmin, models.DO_NOTHING, db_column='iDataAdminID', blank=True, null=True)  # Field name made lowercase.
    idataclinicid = models.ForeignKey(DataClinic, models.DO_NOTHING, db_column='iDataClinicID', blank=True, null=True)  # Field name made lowercase.
    ipersonelid = models.ForeignKey('Personel', models.DO_NOTHING, db_column='iPersonelID', blank=True, null=True)  # Field name made lowercase.
    tage = models.SmallIntegerField(db_column='tAge', blank=True, null=True)  # Field name made lowercase.
    csex = models.CharField(db_column='cSex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    thealth = models.ForeignKey(Health, models.DO_NOTHING, db_column='tHealth', blank=True, null=True)  # Field name made lowercase.
    bpatientstatus = models.ForeignKey('Patientstatus', models.DO_NOTHING, db_column='bPatientStatus', blank=True, null=True)  # Field name made lowercase.
    vfullname = models.CharField(db_column='vFullName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ibloodtypeid = models.ForeignKey(Bloodtype, models.DO_NOTHING, db_column='iBloodTypeID', blank=True, null=True)  # Field name made lowercase.
    iantigenid = models.ForeignKey(Antigen, models.DO_NOTHING, db_column='iAntigenID', blank=True, null=True)  # Field name made lowercase.
    icomorbility = models.ForeignKey(Comorbility, models.DO_NOTHING, db_column='iComorbility', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'


class Patientattention(models.Model):
    bpatientattention = models.BooleanField(db_column='bPatientAttention', primary_key=True)  # Field name made lowercase.
    vtypeattention = models.CharField(db_column='vTypeAttention', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientAttention'


class Patientstatus(models.Model):
    bpatientstatus = models.BooleanField(db_column='bPatientStatus', primary_key=True)  # Field name made lowercase.
    vstatustext = models.CharField(db_column='vStatusText', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientStatus'


class Personel(models.Model):
    ipersonelid = models.IntegerField(db_column='iPersonelID', primary_key=True)  # Field name made lowercase.
    varea = models.CharField(db_column='vArea', max_length=50)  # Field name made lowercase.
    bspecialization = models.BooleanField(db_column='bSpecialization')  # Field name made lowercase.
    bpersonelstatus = models.BooleanField(db_column='bPersonelStatus')  # Field name made lowercase.
    vname = models.CharField(db_column='vName', max_length=100)  # Field name made lowercase.
    tstartshift = models.TimeField(db_column='tStartShift')  # Field name made lowercase.
    tendshift = models.TimeField(db_column='tEndShift')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personel'


class Pharmacy(models.Model):
    iprescriptionid = models.IntegerField(db_column='iPrescriptionID', primary_key=True)  # Field name made lowercase.
    vproductsold = models.CharField(db_column='vProductSold', max_length=15)  # Field name made lowercase.
    iunitssold = models.IntegerField(db_column='iUnitsSold')  # Field name made lowercase.
    fproductcost = models.FloatField(db_column='fProductCost')  # Field name made lowercase.
    fadminpharmainfo = models.FloatField(db_column='fAdminPharmaInfo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pharmacy'


class Specialists(models.Model):
    ispecialistid = models.IntegerField(db_column='iSpecialistID', primary_key=True)  # Field name made lowercase.
    varea = models.CharField(db_column='vArea', max_length=50)  # Field name made lowercase.
    bstatusonshift = models.BooleanField(db_column='bStatusOnShift')  # Field name made lowercase.
    vname = models.CharField(db_column='vName', max_length=100)  # Field name made lowercase.
    tstartshift = models.TimeField(db_column='tStartShift')  # Field name made lowercase.
    tendshift = models.TimeField(db_column='tEndShift')  # Field name made lowercase.
    fspecialistfee = models.FloatField(db_column='fSpecialistfee')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specialists'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
