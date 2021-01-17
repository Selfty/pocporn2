from django.db import models
from django.utils import timezone


class Zaner(models.Model):
	nazev = models.CharField(max_length=100)

	def __str__(self):
		return self.nazev

class Serial(models.Model):
	title_en = models.CharField(max_length=200, null=True)
	title_cz = models.CharField(max_length=200)
	title_sk = models.CharField(max_length=200, null=True, blank=True)
	vyhledavaci_pole = models.CharField(max_length=300, null=True,verbose_name="Pole pro vyhledavani(bez diakritiky, vsehny nazvy oddelene \";\")")
	popis = models.TextField(default='', null=True)
	url1 = models.CharField(default='', max_length=400, null=True, blank=True)
	url2 = models.CharField(default='', max_length=400, null=True, blank=True)
	image = models.CharField(max_length=200)
	start_yr = models.IntegerField(default=0, null=True)
	end_yr = models.IntegerField(default=0, null=True, blank=True)
	delka = models.CharField(max_length=20, null=True)
	zaner = models.ManyToManyField(Zaner, blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title_cz
   
 #   def get_absolute_url(self):
 #       return '/serial/{0}/'.format(self.name)

class Epizoda(models.Model):
	epizoda_serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
	cislo_serie = models.IntegerField()
	cislo_epizoda = models.IntegerField()
	popis_epizody = models.TextField( null=True, blank=True)
	url1 = models.TextField(default='', null=True, blank=True, verbose_name="1. Embed link")
	url1_cc = models.IntegerField(default=0, null=True, blank=True, verbose_name="nic = 0,titulky = 1, dabing = 2")
	url2 = models.TextField(default='', null=True, blank=True, verbose_name="2. Embed link")
	url2_cc = models.IntegerField(default=0, null=True, blank=True, verbose_name="nic = 0,titulky = 1, dabing = 2")
	url3 = models.TextField(default='', null=True, blank=True, verbose_name="3. Embed link")
	url3_cc = models.IntegerField(default=0, null=True, blank=True, verbose_name="nic = 0,titulky = 1, dabing = 2")
	created_date = models.DateTimeField(default=timezone.now, null=True, verbose_name="Čas nahrání")

	def publish(self):
		self.save()

	def __str__(self):
		return self.epizoda_serial.title_cz + " S" + str(self.cislo_serie) + " E" + str(self.cislo_epizoda) 
		
 #   def get_absolute_url(self):
  #      return '/{0}/{1}/{2}/'.format(self.name, self.serie, self.episode)


class Topserials(models.Model):
    serial = models.OneToOneField(Serial,on_delete=models.CASCADE,primary_key=True)
    image = models.CharField(max_length=200, default='brickleberry_small.jpg')

    def publish(self):
        self.save()

    def __str__(self):
        return self.serial.title_cz