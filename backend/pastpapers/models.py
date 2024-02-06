from django.db import models

class subjects(models.Model):
    sub_id = models.AutoField(editable=False,auto_created=True,primary_key=True)
    sub_code = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255)
    class Meta():
        db_table = 'Subjects'
    def __str__(self) -> str:
        return self.sub_name
class years(models.Model):
    years_id = models.AutoField(primary_key=True,auto_created=True)
    sub_id = models.ForeignKey(subjects,on_delete=models.CASCADE)
    years = models.PositiveIntegerField()
    class Meta():
        db_table = 'Years'
    def __int__(self) -> int:
        return self.years
class papers(models.Model):
    year_id = models.ForeignKey(years,on_delete=models.CASCADE)
    paper_id = models.AutoField(primary_key=True,auto_created=True)    
    link = models.URLField(max_length=200)
    is_mid_i = models.BooleanField(blank = True)
    is_mid_ii = models.BooleanField(blank = True)
    is_finals = models.BooleanField(blank = True)
    is_lab_mid = models.BooleanField(blank = True)
    is_lab_finals = models.BooleanField(blank = True)

    class Meta():
        db_table = 'Papers'

    def save(self, *args, **kwargs):
        if not self.pk:  # Only on creation
            if self.is_mid_i:
                self.is_finals = False
                self.is_mid_ii = False
                self.is_lab_finals = False
                self.is_lab_mid = False
                return super().save(*args, **kwargs)
            if self.is_mid_ii:
                self.is_finals = False
                self.is_mid_i = False
                self.is_lab_finals = False
                self.is_lab_mid = False    
                return super().save(*args, **kwargs)
            if self.is_finals:
                self.is_mid_i = False
                self.is_mid_ii = False
                self.is_lab_finals = False
                self.is_lab_mid = False    
                return super().save(*args, **kwargs)
            if self.is_lab_finals:
                self.is_mid_i = False
                self.is_mid_ii = False
                self.is_lab_finals = False
                self.is_lab_mid = False    
                return super().save(*args, **kwargs)
            if self.is_lab_mid:
                self.is_mid_i = False
                self.is_mid_ii = False
                self.is_lab_finals = False
                self.is_finals = False    
                return super().save(*args, **kwargs)
            return
    def __str__(self) -> str:
        if self.is_mid_i:
            return "Mid i Papper " + str(self.paper_id) + "- " +str(self.year_id.years) 
        if self.is_mid_ii:
            return "Mid 2 Papper " + str(self.paper_id) + "- " +str(self.year_id.years)
        if self.is_finals:
            return "Final Papper " + str(self.paper_id) + "- " +str(self.year_id.years)
        if self.is_lab_finals:
            return "Lab final Papper " + str(self.paper_id) + "- " +str(self.year_id.years)
        if self.is_lab_mid:
            return "Lab mid Papper " + str(self.paper_id) + "- " +str(self.year_id.years)