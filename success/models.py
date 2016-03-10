from django.db import models

# Create your models here.
class Variations(models.Model):
	v_id=models.IntegerField(default=0)
	hit=models.BigIntegerField(default=0)
	success=models.BigIntegerField(default=0)
	number=models.BigIntegerField(default=0)

	def __str__(self):
		return str(self.v_id)

class Percentage(models.Model):
	#p_id=models.IntegerField(default=0)
	percentage=models.CharField(max_length=100,default=0)
	no_users=models.BigIntegerField(default=0)
	def __str__(self):
		return str(self.percentage)