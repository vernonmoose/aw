from django.db import models
from datetime import datetime, timedelta

def drug_directory_path(instance, filename):
    return 'Drugs/drg_{0}/{1}'.format(instance.id, filename)

class Drug(models.Model):
    drug_name = models.CharField(max_length=150)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    best_use = models.TextField(max_length=1500)
    instructions = models.TextField(max_length=1500)
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()
    batch_no = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    manufacturing_country = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=drug_directory_path)

    def __str__(self):
        return f"{self.drug_name} {self.brand} {self.manufacturing_country}"
    
    def get_expiry_status(self):
        now = datetime.now().date()
        time_remaining = self.expiry_date - now
        
        if time_remaining < timedelta(days=0):
            return {
                "stqtus": "Expired",
                "days_left" : 0
            }   
        elif time_remaining < timedelta(days=30):
            return {
                "stqtus": "Expiring soon",
                "days_left" : time_remaining.days
            } 
        elif time_remaining < timedelta(days=30 * 5):  
            months_remaining = time_remaining.days // 30
            return {
                    "stqtus": f"Expires in {months_remaining} month{'s' if months_remaining > 1 else ''}",
                    "days_left" : months_remaining * 30
                }
        elif time_remaining < timedelta(days=365): 
            return {
                    "stqtus": f"Expires in less than a Year",
                    "days_left" : time_remaining.days
                }
        else:  
            years_remaining = time_remaining.days // 365
            return {
                    "stqtus": f"Expires in {years_remaining} year{'s' if years_remaining > 1 else ''}",
                    "days_left" : time_remaining.days
                }