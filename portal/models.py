from django.db import models

class faq(models.Model):
	question = models.CharField(max_length=300)
	answer = models.TextField()

        class Meta:
                verbose_name_plural = "Faq"
	
	def __unicode__(self):
		return self.question
	
	
jadwal_STATUS = (
    ('Selesai', 'Selesai'),
    ('Belum', 'Belum'),
)
		
class jadwal(models.Model):
	kegiatan = models.CharField(max_length=300)
	tempat = models.CharField(max_length=300)
	tanggal = models.DateField()
	pembicara = models.CharField(max_length=20)
	status = models.CharField(max_length=30, choices=jadwal_STATUS)
	
	
	def __unicode__(self):
		return self.kegiatan
	
	class Meta:
		verbose_name_plural = "Jadwal Kegiatan"
		
class sponsor_and_partner(models.Model):
	by = models.CharField(max_length=30)
	website = models.URLField(blank=True,help_text="kosong jika tidak ada")
	about_sponsor = models.TextField()
#        gambar = models.ImageField(upload_to='upload')
	def __unicode__(self):
		return self.by
	

class daftar(models.Model):
	daftar = models.TextField()
	
	def __unicode__(self):
		return self.daftar		
		
KELAS_PENGINAPAN = (
	("bh", "bawah"),
	("tg", "tengah"),
	("at", "atas"),
	)


class penginapan(models.Model):
	kelas = models.CharField(max_length=2, choices=KELAS_PENGINAPAN)	
	penginapan = models.CharField(max_length=30)
	harga = models.TextField()
	Alamat = models.CharField(max_length=300)
	website = models.URLField(blank=True,help_text="kosong jika tidak ada")
	
	def __unicode__(self):
		return self.penginapan
		
	class Meta:
		verbose_name_plural ="Penginapan"			
				
					
class informasi(models.Model):
	informasi = models.TextField()
	
	def __unicode__(self):
		return self.informasi
		
	class Meta:
		verbose_name_plural = "Informasi"	
		
						
