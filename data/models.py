from django.db import models

# 在setting里设置连接mysql数据库djangodata
# 执行python manage.py inspectdb 命令，生成的数据库里所有表格对应的models，复制到这里
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Tboxdata(models.Model):
    id = models.IntegerField(db_column='key', blank=True, primary_key=True)
    tbox_data = models.TextField(db_column='TBOX_data', blank=True, null=True)  # Field name made lowercase.
    # sdata = models.TextField(blank=True, null=True)
    vin = models.TextField(db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)
    sid = models.TextField(db_column='SID', blank=True, null=True)  # Field name made lowercase.
    detail = models.TextField(db_column='detail', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbox_data'


class BorgwardEngineDiagnostics(models.Model):
    problem_description = models.TextField(blank=True, null=True)
    parts = models.CharField(max_length=255, blank=True, null=True)
    performance = models.TextField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    vehicle_system = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borgward_engine_diagnostics'

    def as_dict(self):
        return {
            "problem_description": self.problem_description,
            "parts": self.parts,
            "performance": self.performance,
            "solution": self.solution,
            "vehicle_system": self.vehicle_system
        }


class EngineDiagnosticsRecord(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    vin = models.CharField(max_length=255, blank=True, null=True)
    engine = models.CharField(max_length=255, blank=True, null=True)
    fault_code = models.CharField(max_length=255, blank=True, null=True)
    fault_phenomenon = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_diagnostics_record'


class EngineFaultCode(models.Model):
    fault_code = models.CharField(max_length=255, blank=True, null=True)
    interpretation = models.CharField(max_length=255, blank=True, null=True)
    fault_cause = models.CharField(max_length=255, blank=True, null=True)
    diagnostic_scheme = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_fault_code'

    def engine_fault_code_dict(self):
        return {
            "fault_code": self.fault_code,
            "interpretation": self.interpretation,
            "fault_cause": self.fault_cause,
            "diagnostic_scheme": self.diagnostic_scheme
        }


class EngineFaultPhenomenon(models.Model):
    fault_phenomenon = models.CharField(max_length=255, blank=True, null=True)
    fault_cause = models.CharField(max_length=255, blank=True, null=True)
    diagnostic_scheme = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_fault_phenomenon'

