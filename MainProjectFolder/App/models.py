from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser
import random
from datetime import timedelta
# Create your models here.



class AinaZaKuku(models.Model):
    
    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=100, blank=False,null=False)

    #hivi ni vipindi vya chakula vinavyoanza mpk vinapoishia
    #na vinachukua interval gani na kwa wiki ngapi kulingana
    #na aina ya kuku
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)

    #hizi ni total percentages required kwa kila aina ya
    #kipindi cha chakula ambazo hizi kule kwenye model
    #ya vyakula wkt wa kukokotoa baada ya kupata total
    #percentage ya kila kirutubisho tunakuja kukompare na
    #hii km ni ndogo tunampa ushauri,
    #ila hapa tunatumia makundi 3 tu ya virutubisho mengine
    #tunaachana nayo
    TotalCPPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)

    TotalMEPercentageRequired_Starter = models.CharField(max_length=300,verbose_name="Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Starter - Kcal/kg", default=0, blank=True,null=True)
    TotalMEPercentageRequired_Grower = models.CharField(max_length=300,verbose_name="Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Grower - Kcal/kg", default=0, blank=True,null=True)
    TotalMEPercentageRequired_Layer = models.CharField(max_length=300,verbose_name="Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Layer - Kcal/kg", default=0, blank=True,null=True)
    TotalMEPercentageRequired_Finisher = models.CharField(max_length=300,verbose_name="Kiwango Cha Jumla Cha ME Kwenye Kipindi  Cha Finisher - Kcal/kg", default=0, blank=True,null=True)

    PichaYaKuku = models.ImageField(verbose_name="Picha Ya Kuku", upload_to='media/PichaZaKuku/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Aina Za Kuku"

class AinaZaNdege(models.Model):
    
    AinaYaNdege = models.CharField(verbose_name="Aina Ya Ndege",max_length=100, blank=False,null=False)
    SikuKamiliZaKuatamia = models.IntegerField(verbose_name="Siku Kamili Za Kuatamia", blank=True,null=True)
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)

    PichaYaNdege = models.ImageField(verbose_name="Picha Ya Ndege", upload_to='media/PichaZaKuku/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaNdege}"
    
    class Meta:
        verbose_name_plural = "Aina Za Ndege"




class SlidingInformations(models.Model):
    
    MainTitle = models.CharField(verbose_name="Main Title",max_length=200, blank=True,null=True)
    MinorTitle = models.CharField(verbose_name="Minor Title",max_length=200, blank=True,null=True)
    Description = models.TextField(verbose_name="Maelezo",max_length=500, blank=True,null=True)
    phone = models.CharField(verbose_name="Namba Ya Simu",max_length=13, blank=True,null=True)
    IconName = models.CharField(verbose_name="Icon Name",max_length=200, blank=True,null=True)
    BackgroundColor = models.CharField(verbose_name="Background Color",max_length=200, blank=True,null=True)
    MainTitleColor = models.CharField(verbose_name="Main Title Color",max_length=200, blank=True,null=True)
    MinorTitleColor = models.CharField(verbose_name="Minor Title Color",max_length=200, blank=True,null=True)
    DescriptionColor = models.CharField(verbose_name="Description Color",max_length=200, blank=True,null=True)
    IconColor = models.CharField(verbose_name="Icon Color",max_length=200, blank=True,null=True)


    PichaYa1 = models.ImageField(verbose_name="Picha Ya 1", upload_to='media/SlidingImages/',blank=True,null=True)
    # PichaYa2 = models.ImageField(verbose_name="Picha Ya 2", upload_to='media/SlidingImages/',blank=True,null=True)
    # PichaYa3 = models.ImageField(verbose_name="Picha Ya 3", upload_to='media/SlidingImages/',blank=True,null=True)
    # PichaYa4 = models.ImageField(verbose_name="Picha Ya 4", upload_to='media/SlidingImages/',blank=True,null=True)
    # PichaYa5 = models.ImageField(verbose_name="Picha Ya 5", upload_to='media/SlidingImages/',blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.MainTitle}"
    
    class Meta:
        verbose_name_plural = "Sliding Informations"



class Mikoa(models.Model):
    
    JinaLaMkoa = models.CharField(verbose_name="Jina La Mkoa",max_length=100, blank=False,null=False)
    Kanda = models.CharField(verbose_name="Kanda",max_length=500, blank=True,null=True) 
    #Chakula = models.ForeignKey('Vyakula', verbose_name="Aina Ya Chakula",on_delete=models.PROTECT, blank=True,null=True)
    #price = models.FloatField(verbose_name="Bei Ya Chakula", blank=True,null=True) 
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaMkoa}"
    
    class Meta:
        verbose_name_plural = "Mikoa"




class NotepadMikoa(models.Model):
    
    JinaLaMkoa = models.CharField(verbose_name="Jina La Mkoa",max_length=100, blank=True,null=True)
    NambaYaMkoa = models.IntegerField(verbose_name="Namba Ya Mkoa", blank=True,null=True)

    Kanda = models.CharField(verbose_name="Kanda",max_length=500, blank=True,null=True) 
    #Chakula = models.ForeignKey('Vyakula', verbose_name="Aina Ya Chakula",on_delete=models.PROTECT, blank=True,null=True)
    #price = models.FloatField(verbose_name="Bei Ya Chakula", blank=True,null=True) 
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaMkoa}"
    
    class Meta:
        verbose_name_plural = "Notepad Mikoa"


class NotepadMatatizo(models.Model):
    
    Tatizo = models.CharField(verbose_name="Jina La Tatizo",max_length=100, blank=True,null=True)
    NambaYaTatizo = models.IntegerField(verbose_name="Namba Ya Tatizo", blank=True,null=True)

    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Tatizo}"
    
    class Meta:
        verbose_name_plural = "Notepad Matatizo"







class MatatizoYaWateja(models.Model):
     
    JinaLaMteja = models.CharField(verbose_name="Jina La Mteja",max_length=100, blank=True,null=True)
    phone = models.CharField(verbose_name="Namba Ya Simu",max_length=13, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    JinaLaTatizo = models.CharField(verbose_name="Jina La Tatizo",max_length=1000, blank=True,null=True)
    Mkoa = models.CharField(verbose_name="Mkoa",max_length=100, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=100, blank=True,null=True)

    Message = models.TextField(max_length=10000, blank=True,null=True)

    is_checked = models.BooleanField(blank=True,null=True, default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.JinaLaMteja}"
    
    class Meta:
        verbose_name_plural = "Matatizo Ya Wateja"









class LevelZaWafugaji(models.Model):
    
    Level = models.CharField(verbose_name="Level Ya Mfugaji",max_length=100, blank=False,null=False)
    Nyota = models.CharField(verbose_name="Kanda",max_length=500, blank=True,null=True) 
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Level}"
    
    class Meta:
        verbose_name_plural = "LevelZaWafugaji"


class UserStatus(models.Model):
    
    Status = models.CharField(verbose_name="Status",max_length=100, blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Status}"
    
    class Meta:
        verbose_name_plural = "Status Za Wafugaji"

class UserRole(models.Model):
    
    Role = models.CharField(verbose_name="Aina Ya User",max_length=100, blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Role}"
    
    class Meta:
        verbose_name_plural = "User Role"



# class SikuZaKusafishaBanda(models.Model):
    
#     Siku = models.IntegerField(verbose_name="Siku ?", blank=False,null=False)
#     Wiki = models.IntegerField(verbose_name="Wiki ? (Usijaze)", blank=True,null=True)
#     Mwezi = models.IntegerField(verbose_name="Mwezi ? (Usijaze)", blank=True,null=True)
#     Created = models.DateTimeField(auto_now_add=True)
#     Updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Siku {self.Siku}, Wiki {self.Wiki}"
    
#     class Meta:
#         verbose_name_plural = "Siku Za Kusafisha Banda"





class MudaWaKumbushoUsafishajiBanda(models.Model):
    
    Muda = models.CharField(verbose_name="Jina La Muda",max_length=100, blank=False,null=False)
    StartingTime = models.TimeField(auto_now_add=False, verbose_name="Muda Wa Kuanza", blank=False,null=False)
    EndingTime = models.TimeField(auto_now_add=False, verbose_name="Muda Wa Kuisha", blank=False,null=False)
    
    def __str__(self):
        return f"{self.Muda} Kuanzia {self.StartingTime} Mpaka {self.EndingTime}"
    
    class Meta:
        verbose_name_plural = "Muda Wa Kumbusho Usafishaji Banda"



class KumbushoUsafishajiBanda(models.Model):
    SikuZaKukumbushwa = models.IntegerField(verbose_name="Ukumbushwe Baada Ya Siku ?", blank=True,null=True)   
    Muda = models.ForeignKey(MudaWaKumbushoUsafishajiBanda, verbose_name="Muda Wa Kukumbushwa", blank=True,null=True,on_delete=models.PROTECT)

    Awamu_Choices = (
            ('Ijirudie', 'Ijirudie'),
            ('Maramoja tu', 'Maramoja tu'),

        )
    Awamu = models.CharField(choices=Awamu_Choices, verbose_name="Awamu Za Ukumbushwaji",max_length=100, blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    SikuZaKukumbushwaDisplayedValue = models.IntegerField(verbose_name="Ukumbushwe Baada Ya Siku (TunayotumiaKudisplay- Usijaze) ?", blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} Siku {self.SikuZaKukumbushwa}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Usafishaji Banda"


#hizi ni calculation za kupatahizo field mbili za juu ambazo tutazitumia kwenye
#templates kumuindicate admin user yupi anapaswa kukumbushwa, kwa yule mwenye
#background nyekundi anapaswa kukumbushwa
    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        # print(f"Time Now: {timezone.now()}")
        # print(f"Time Since {time_elapsed} days")
        # print(f"Siku Za Kukumbushwa {self.SikuZaKukumbushwa} days")
        
        # Assuming SikuZaKukumbushwa is the number of days, directly subtract time_elapsed
        remaining_days = self.SikuZaKukumbushwa - time_elapsed
        #print(f"Time Left: {remaining_days} days")

        # Update day_is_reached to True if remaining_days is equal to 1
        if remaining_days == 1 and not self.day_is_reached:
            self.day_is_reached = True
            self.save(update_fields=['day_is_reached'])

        return remaining_days

    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 1













class MyUserManager(BaseUserManager):
    def create_user(self, email, username,phone,expo_push_token=None, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")

        


        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            expo_push_token=expo_push_token,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,
            expo_push_token=None  # Superuser doesn't require expo_push_token
            

        )
        user.is_admin=True
        user.is_staff=True
        user.is_customer=False
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name",blank=True,null=True, max_length=500, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=10)
    Location=models.CharField(verbose_name="Mahali", max_length=200, blank=True, null=True)
    Mkoa = models.ForeignKey(Mikoa, verbose_name="Mkoa",on_delete=models.PROTECT, blank=True,null=True)
    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku",on_delete=models.PROTECT, blank=True,null=True)
    Role = models.ForeignKey(UserRole, verbose_name="Aina Ya User",on_delete=models.PROTECT, blank=True,null=True)
    #hizi mbili zinakuwa approved by admin
    Level = models.ForeignKey(LevelZaWafugaji, verbose_name="Level Ya Mfugaji",on_delete=models.PROTECT, blank=True,null=True)
    Tick_choises = (
        ('Ndio Anastahili', 'Ndio Anastahili'),
        ('Hapana Hastahili', 'Hapana Hastahili')

    )
    Tick = models.CharField(choices=Tick_choises,max_length=100, verbose_name="Anastahili Tiki ?", blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    OmbaNyota = models.TextField(max_length=10000, blank=True,null=True)
    PichaYaLeseni = models.ImageField(upload_to='media/',verbose_name="Picha Ya Leseni", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    #phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mtu", blank=True, null=True)
    #profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mtu", blank=True, null=True, default='mtu.jpg')
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)

    hide_email = models.BooleanField(default=True)

    expo_push_token = models.CharField(max_length=255, blank=True, null=True)

    


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Method to update push token
    def update_push_token(self, token):
        self.expo_push_token = token
        self.save()






class OTP(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.otp:
            self.otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)

    def is_valid(self):
        from django.utils import timezone
        return self.created_at >= timezone.now() - timezone.timedelta(minutes=10)


class SampleModel(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    











class Notification(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='notifications')
    PostOwner = models.CharField(verbose_name="Mmiliki Wa Posti: ", max_length=200, blank=True,null=True)
    username = models.CharField(verbose_name="Aliye Like Ni: ", max_length=200, blank=True,null=True)
    duka_lako = models.CharField(verbose_name="Post Aliyo Like: ", max_length=1000, blank=True,null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #hii ni picha ya mtu aliyelike
    Photo = models.ImageField(upload_to='media/',verbose_name="Picha Ya Aliye Like", blank=True, null=True)

    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    PichaYaPost = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post", blank=True, null=True)
    PichaYaPost2 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 2", blank=True, null=True)
    PichaYaPost3 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 3", blank=True, null=True)
    PichaYaPost4 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 4", blank=True, null=True)
    PichaYaPost5 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 5", blank=True, null=True)
    
    #-------hizi ni taarifa za aliyelike
    phone = models.CharField(verbose_name="Namba Yake ya Simu",max_length=13, blank=True,null=True)  
    email = models.EmailField(verbose_name="Email Yake",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali Anapoishi",max_length=200, blank=True,null=True)
    #Likes = models.IntegerField(verbose_name="Post Likes",default=0, blank=True,null=True)
    #liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_dukalako', blank=True)


    def __str__(self):
        return f"Notification for {self.username} - {self.duka_lako}"




class DukaLako(models.Model):
    YouTubeLink = models.URLField(verbose_name="YouTube Video Link", max_length=5000, blank=True, null=True)
    Title = models.CharField(verbose_name="Kinahusiana Na ?", max_length=500, blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=False,null=False)
    PichaYaPost = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post", blank=True, null=True)
    PichaYaPost2 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 2", blank=True, null=True)
    PichaYaPost3 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 3", blank=True, null=True)
    PichaYaPost4 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 4", blank=True, null=True)
    PichaYaPost5 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 5", blank=True, null=True)

    Status = models.ForeignKey(UserStatus, verbose_name="Status",on_delete=models.PROTECT, blank=True,null=True)
    
    TickStatus = models.CharField(verbose_name="Tick Status",max_length=500, blank=True,null=True)
    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    UserRole = models.CharField(verbose_name="Aina Ya Mtumiaji",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Yako", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    Likes = models.IntegerField(verbose_name="Post Likes",default=0, blank=True,null=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_dukalako', blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    expo_push_token = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} - {self.Title}"
    
    class Meta:
        verbose_name_plural = "Duka Lako"



class Wanunuzi(models.Model):
    Message = models.TextField(max_length=10000, blank=True,null=True)
    Mkoa = models.ForeignKey(Mikoa, verbose_name="Mkoa",on_delete=models.PROTECT, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=100, blank=True,null=True)
    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=100, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Yako", blank=True, null=True)
    is_checked = models.BooleanField(blank=True,null=True, default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Wanunuzi"







class WazalishajiWaHuduma(models.Model):
    
    phone = models.CharField(verbose_name="Namba Simu Ya Mzalishaji",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina La Mzalishaji",max_length=100, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yake",max_length=200, blank=True,null=True)
    #Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yake",max_length=500, blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    Mkoa = models.ForeignKey(Mikoa, verbose_name="Mkoa",on_delete=models.PROTECT, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=100, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mzalishaji", blank=True, null=True)
    #is_checked = models.BooleanField(blank=True,null=True, default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Wazalishaji Wa Huduma"




class HudumazaWazalishaji(models.Model):
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=500, blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    Mzalishaji = models.ForeignKey(WazalishajiWaHuduma, verbose_name="Jina La Mtoa Huduma",on_delete=models.PROTECT, blank=True,null=True)
    TotalPrice = models.IntegerField(verbose_name="Bei Ya Jumla Ya Bidhaa", default=0, blank=True,null=True)
    PichaYaHuduma = models.ImageField(upload_to='media/',verbose_name="Picha Ya Huduma", blank=True, null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.JinaLaHuduma} Inatolewa na {self.Mzalishaji.username}"
    
    class Meta:
        verbose_name_plural = "Huduma Za Wazalishaji"





class WatejaWote(models.Model):
    JinaLaMteja = models.CharField(verbose_name="Jina La Mteja",max_length=200, blank=True,null=True)
    phoneYaMteja = models.CharField(verbose_name="Namba Ya Simu Ya Mteja",max_length=13, blank=True,null=True)  
    emailYaMteja = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    MkoaWaMteja = models.ForeignKey(Mikoa, verbose_name="Mkoa",on_delete=models.PROTECT, blank=True,null=True)
    WilayaYaMteja = models.CharField(verbose_name="Wilaya",max_length=100, blank=True,null=True)
    PichaYaMteja = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mteja", blank=True, null=True)
    is_checked = models.BooleanField(blank=True,null=True, default=False)

    Kiasi_Au_Idadi = models.CharField(verbose_name="Unit",max_length=100, blank=True,null=True)

    IdadiYaJumla = models.IntegerField(verbose_name="Idadi", default=1, blank=True,null=True)

    TotalAmount = models.IntegerField(verbose_name="Kiasi Cha Jumla", default=0, blank=True,null=True)

    PaidAmount = models.IntegerField(verbose_name="Kiasi Alicholipa", default=0, blank=True,null=True)
    RemainedAmount = models.IntegerField(verbose_name="Kiasi Anachodaiwa", default=0, blank=True,null=True)
    SikuYaKupokea = models.IntegerField(verbose_name="Siku Ya Kupokea Bidhaa", default=0, blank=True,null=True)
    SikuYaKupokea_Displayed = models.IntegerField(verbose_name="Siku Ya Kupokea Bidhaa", default=0, blank=True,null=True)
    OngezaOda = models.IntegerField(verbose_name="Peleka Oda Mbele Kwa Siku ?", default=0, blank=True,null=True)


    phone = models.CharField(verbose_name="Namba Simu Ya Mzalishaji",max_length=13, blank=True,null=True)
    Mzalishaji = models.CharField(verbose_name="Jina La Mzalishaji",max_length=100, blank=True,null=True)
    JinaLaHuduma = models.CharField(verbose_name="Huduma Anayohitaji",max_length=100, blank=True,null=True)

    email = models.EmailField(verbose_name="Email Yake",max_length=200, blank=True,null=True)
    #Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yake",max_length=500, blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    Mkoa = models.CharField(verbose_name="Mkoa",max_length=100, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=100, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mzalishaji", blank=True, null=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)


    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.JinaLaMteja} Simu {self.phoneYaMteja}"
    
    class Meta:
        verbose_name_plural = "Wateja"



    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        
        
        Siku_Ya_Kupokea = int(self.SikuYaKupokea)
            
        # Assuming SikuZaKukumbushwa is the number of days, directly subtract time_elapsed
        remaining_days = Siku_Ya_Kupokea - time_elapsed
        

        # Update day_is_reached to True if remaining_days is equal to 1
        if remaining_days == 5 and not self.day_is_reached:
            self.day_is_reached = True
            self.save(update_fields=['day_is_reached'])

        return remaining_days

    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 5










class Maoni(models.Model):
    Maoni = models.TextField(max_length=10000, blank=False,null=False)
    
    
    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=200, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Yako", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} - {self.Maoni}"
    
    class Meta:
        verbose_name_plural = "Maoni"












class Huduma(models.Model):
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Huduma"

class MgawanjoWaHuduma(models.Model):
    Category = models.ForeignKey(Huduma, verbose_name="Category",on_delete=models.PROTECT, blank=True,null=True)
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Mgawanjo Wa Huduma"



class IdadiYaKuku(models.Model):
    
    IdadiYaKuku = models.IntegerField(verbose_name="Idadi Ya Kuku", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Kuku {self.IdadiYaKuku}"
    
    class Meta:
        verbose_name_plural = "Idadi Ya Kuku"


class IdadiYaKilos(models.Model):
    
    IdadiYaKilos = models.IntegerField(verbose_name="Idadi Ya Kilos", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Kilos {self.IdadiYaKilos}"
    
    class Meta:
        verbose_name_plural = "Idadi Ya Kilos"


class UmriWaKuku(models.Model):
    
    UmriKwaWiki = models.IntegerField(verbose_name="Wiki ?", blank=False,null=False)
    UmriKwaSiku = models.IntegerField(verbose_name="Siku ? (Usijaze)", blank=True,null=True)
    Interval = models.CharField(verbose_name="Interval",max_length=100, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.UmriKwaWiki}, Siku {self.Interval}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"



@receiver(pre_save, sender=UmriWaKuku)
def set_UmriKwaSiku(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.UmriKwaSiku = instance.UmriKwaWiki * 7



class Siku(models.Model):
    
    Siku = models.IntegerField(verbose_name="Siku ?", blank=False,null=False)
    Wiki = models.IntegerField(verbose_name="Wiki ? (Usijaze)", blank=True,null=True)
    Mwezi = models.IntegerField(verbose_name="Mwezi ? (Usijaze)", blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Siku {self.Siku} - Wiki {self.Wiki}  - Mwezi {self.Mwezi}"
    
    class Meta:
        verbose_name_plural = "Siku"


@receiver(pre_save, sender=Siku)
def set_Wiki(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        if instance.Siku < 7:
            instance.Wiki = 0
        instance.Wiki = int(instance.Siku / 7)

@receiver(pre_save, sender=Siku)
def set_Mwezi(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        if instance.Siku < 28:
            instance.Mwezi = 0
        instance.Mwezi = int(instance.Wiki / 4)







class MaktabaYaLisheCategories(models.Model):

    CategoryName = models.CharField(max_length=500,verbose_name="Category", blank=False,null=False)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Makundi Ya Maktaba Ya Lishe"

    def __str__(self):
        return self.CategoryName


class MaktabaYaLisheContents(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.PROTECT, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ndani Ya Makundi Maktaba Ya Lishe"

    def __str__(self):
        return self.Title



class MuongozoWaLishe(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    #CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.PROTECT, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Muongozo Wa Lishe"

    def __str__(self):
        return self.Title


class MatumiziSahihiYaIndibata(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    #CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.PROTECT, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    YoutubeLinkVideo = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Matumizi Sahihi Ya Indibata"

    def __str__(self):
        return self.Title





class JamiiYaMfugajiCategories(models.Model):

    CategoryName = models.CharField(max_length=500,verbose_name="Category", blank=False,null=False)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Makundi Ya Jamii Ya Mfugaji"

    def __str__(self):
        return self.CategoryName






class JamiiYaMfugajiContents(models.Model):

    FullName = models.CharField(max_length=100,verbose_name="Jina Kamili", blank=False,null=False)
    Location = models.CharField(max_length=100,verbose_name="Mahali", blank=True,null=True)
    Title = models.CharField(max_length=5000,verbose_name="Title", blank=True,null=True)
    CategoryName = models.ForeignKey(JamiiYaMfugajiCategories, verbose_name="Category",on_delete=models.PROTECT, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    #Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Email = models.EmailField(max_length=100,blank=True,null=True)
    Phone = models.CharField(default="+255", max_length=13,blank=True,null=True)
    #Github = models.CharField(default="https://github.com/dimosojunior/", max_length=1000,blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)
    WhatsappLink = models.CharField(max_length=1000,blank=True,null=True)
    FaceBook = models.CharField(max_length=1000,blank=True,null=True)
    Instagram = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ndani Ya Jamii Ya Mfugaji"

    def __str__(self):
        return self.FullName + " " + self.Title






class UnitZaVyakula(models.Model):
    
    Unit = models.CharField(verbose_name="Unit", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Unit
    
    class Meta:
        verbose_name_plural = "Unit Za Vyakula"


class MakundiYaVyakula(models.Model):
    
    Jina = models.CharField(verbose_name="Jina", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Jina
    
    class Meta:
        verbose_name_plural = "Makundi Ya Vyakula"

class VipindiVyaKuku(models.Model):
    
    Kipindi = models.CharField(verbose_name="Kipindi", max_length=500,blank=False,null=False)
    Muda = models.CharField(verbose_name="Muda",default="0-2", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Jina
    
    class Meta:
        verbose_name_plural = "Makundi Ya Vyakula"

class Vyakula(models.Model):
    
    
    product_name = models.CharField(verbose_name="Jina La Chakula", max_length=100,blank=False,null=False)
    FoodGroup = models.ForeignKey(MakundiYaVyakula, verbose_name="Kundi La Chakula",on_delete=models.PROTECT, blank=True,null=True)
    ProductDescription = models.TextField(verbose_name="Maelezo", max_length=10000,blank=True,null=True)
    InitialPrice = models.IntegerField(verbose_name="Bei Ya Mwanzo Ya Chakula", blank=True,null=True)
    price = models.FloatField(verbose_name="Bei Ya sasa Ya Chakula (Usijaze)", blank=True,null=True)   
    #ProductUnit = models.CharField(verbose_name="Product Unit", max_length=100,blank=True,null=True)
    ProductQuantity = models.FloatField(verbose_name="Kiasi - KG (Usijaze)",default=1, blank=True,null=True)
    #InitialProductQuantity = models.FloatField(verbose_name="Kiasi Cha Mwanzo Store-KG (Usijaze)",blank=True,null=True)    
    Unit = models.ForeignKey(UnitZaVyakula, verbose_name="Unit Ya Chakula",on_delete=models.PROTECT, blank=True,null=True)
    ProductImage = models.ImageField(verbose_name="Picha Ya Chakula", upload_to='media/PichaZaVyakula/',blank=True,null=True)

    

    #----------------MWANZO WA VIRUTUBISHO---------------------
    ME = models.FloatField(verbose_name="Kiwango Cha ME - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    CP = models.FloatField(verbose_name="Kiwango Cha CP - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Wanga = models.FloatField(verbose_name="Kiwango Cha Wanga - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Mafuta = models.FloatField(verbose_name="Kiwango Cha Mafuta - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    DCP = models.FloatField(verbose_name="Kiwango Cha DCP - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    PREMIX = models.FloatField(verbose_name="Kiwango Cha PREMIX - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Lysin  = models.FloatField(verbose_name="Kiwango Cha Lysin  - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    METH = models.FloatField(verbose_name="Kiwango Cha METH - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Tryptophan = models.FloatField(verbose_name="Kiwango Cha Tryptophan - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    UngaWaMifupa = models.FloatField(verbose_name="Kiwango Cha UngaWaMifupa - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Chumvi = models.FloatField(verbose_name="Kiwango Cha Chumvi - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)


    #----------------PERCENTAGE YA KILA CHAKULA KWENYE MCHANGANYIKO---
    #hizi ni percentage ya kila chakula kinavyohitajika kwenye
    #mchanganyiko fulani wa chakula ambazo ni constant ila
    #zinabadilika kutokana na aina ya vipindi vya chakula
    #mfano percentage ya mahindi inayohitajika kwenye mchanganyiko
    #wa chakula kipindi cha starter ni tofauti na ile ya kipindi
    #cha grower kwahiyo zimekuwa categorized kwa magroup
    TotalPercentageRequired_Starter = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Starter - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Grower = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Grower - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Layer = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Layer - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Finisher = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Finisher - %", default=0, blank=True,null=True)
    
    

    #Hutakiwi kujaza Hizi
    # Protini_In_1Kg = models.FloatField(verbose_name="Kiwango Cha Protini - % Kwenye 1Kg Ya Chakula", blank=True,null=True)

    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Vyakula"
        
    
    def __str__(self):
        return f" {self.product_name} "


# @receiver(pre_save, sender=ProductsStores)
# def Products__initial_quantity(sender, **kwargs):
#     Initial_qty = kwargs['instance']
#     Initial_qty.InitialProductQuantity = Initial_qty.ProductQuantity
#     # total_cart_items = CartItems.objects.filter(user = cart_items.user )
#     # cart = Cart.objects.get(id = cart_items.cart.id)
#     # cart.total_price = cart_items.price
#     # cart.save()

#@receiver(pre_save, sender=Vyakula)
# def set_initial_quantity(sender, instance, **kwargs):
#     # Check if the instance is new (i.e., it doesn't have a primary key yet)
#     if instance._state.adding:
#         instance.InitialProductQuantity = instance.ProductQuantity

@receiver(pre_save, sender=Vyakula)
def set_price_from_initial_price(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.price = instance.InitialPrice








class VyakulaCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(verbose_name="Jumla Ya Bei", default=0)
    total_Kilos = models.FloatField(verbose_name="Jumla Ya Kilos", default=0)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula  Cart"

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
         


class VyakulaCartItems(models.Model):
    cart = models.ForeignKey(VyakulaCart, on_delete=models.PROTECT) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey(Vyakula,on_delete=models.PROTECT)
    price = models.FloatField(default=0)
    #Customer = models.ForeignKey(ProductsCustomers,on_delete=models.PROTECT,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    #table = models.ForeignKey(ProductsTables,on_delete=models.PROTECT,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula  Cart Items"
    
    def __str__(self):
        return f" {self.product.product_name}"
        
    

@receiver(pre_save, sender=VyakulaCartItems)
def Vyakula__correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Vyakula.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user = cart_items.user )
    # cart = Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()







class VyakulaOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,blank=True, null=True)
    cart = models.ForeignKey(VyakulaCart, on_delete=models.PROTECT, blank=True, null=True)
    # orderItems = models.ManyToManyField('ProductsOrderItems')
    total_price = models.FloatField(verbose_name="Jumla Ya Bei")
    total_Kilos = models.FloatField(verbose_name="Jumla Ya Kilos")

    TotalFoodMixerPercentage = models.FloatField(verbose_name="Jumla Ya Percentage Ya Vyakula Vyote (Variables Food) - %", default=0, null=True, blank=True)
    
    TotalConstantFoodMixerPercentage = models.FloatField(verbose_name="Jumla Ya Percentage Ya Vyakula Vyote (constant Food) - %", default=0, null=True, blank=True)
    TotalMixerKios_ForConstantFoodGroups = models.FloatField(verbose_name="Jumla Ya Kiasi Ya Vyakula Vyote Vilivyochagualiwa kutoka kwenye (constant Food Groups) - Kg", default=0, null=True, blank=True)

    #-----------ZOTE ZINAJIADD AUTOMATIC-----------------
    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=200, blank=True,null=True)
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)
    UmriKwaSiku = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku", default=0, null=True, blank=True)
    UmriKwaWiki = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Wiki", default=0, null=True, blank=True)
    Interval = models.CharField(verbose_name="Interval",max_length=100, blank=True,null=True)

    TotalFoodAmount = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Chakula - Kg", default=0, null=True, blank=True)
    TotalCPPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha CP Kwenye Chakula - %", default=0, null=True, blank=True)
    TotalWangaPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Wanga Kwenye Chakula - %", default=0, null=True, blank=True)
    TotalMafutaPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Mafuta Kwenye Chakula - %", default=0, null=True, blank=True)
    TotalMEPercentageRequired = models.CharField(verbose_name="Jumla Ya  Kiasi Cha ME Kwenye Chakula - Kg/kca", default=0,max_length=300, null=True, blank=True)

    #CategoryId = models.IntegerField(verbose_name="Category ID",blank=True,null=True)
    #closed_order_state = models.BooleanField(verbose_name="Is Order Closed ?", default=False,blank=True,null=True)
    Customer = models.CharField(max_length=500, verbose_name="Imewekwa Na:",blank=True,null=True)

    # table_number = models.CharField(max_length=500, verbose_name="Table Number",blank=True,null=True)

    #order_status = models.BooleanField(verbose_name="Status", default=False,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vyakula Orders"

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class VyakulaOrderItems(models.Model):
    order = models.ForeignKey(VyakulaOrder, on_delete=models.PROTECT) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey(Vyakula,on_delete=models.PROTECT)
    price = models.FloatField(default=0)
    # Customer = models.ForeignKey(ProductsCustomers,on_delete=models.PROTECT,blank=True,null=True)
    #order_status = models.BooleanField(verbose_name="Status", default=False,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    # table = models.ForeignKey(ProductsTables,on_delete=models.PROTECT,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula Orders Items"

    def __str__(self):
        return f" {self.product.product_name}" 








class Virutubisho(models.Model):
    JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.PROTECT, blank=True,null=True)  
    Protini = models.IntegerField(verbose_name="Kiwango Cha Protini- %", blank=False,null=False)
    Cabohydrate = models.IntegerField(verbose_name="Kiwango Cha Cabohydrate- %", blank=False,null=False)
    Wanga = models.IntegerField(verbose_name="Kiwango Cha Wanga- %", blank=False,null=False)
    Fati = models.IntegerField(verbose_name="Kiwango Cha Fati- %", blank=False,null=False)
    Vitamini = models.IntegerField(verbose_name="Kiwango Cha Vitamini- %", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.JinaLaChakula.product_name}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"












class AinaZaChanjo(models.Model):
    
    JinaLaChanjo = models.CharField(verbose_name="Jina La Chanjo",max_length=200, blank=False,null=False)
    Kutolewa = models.IntegerField(verbose_name="Hutolewa Siku Ya Ngapi ?",blank=True,null=True)
    MaelezoYaChanjo = models.TextField(verbose_name="Maelezo Ya Chanjo",max_length=10000, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaChanjo} Siku Ya {self.Kutolewa}"
    
    class Meta:
        verbose_name_plural = "Aina Za Chanjo"











class KumbushoLaMabadilikoYaLishe(models.Model):
      
    
    #--------HIZI ZINZJIJAZA ZENYEWE KWENYE VIEW------------------
    MudaWaKumbusho_Choices = (
            ('12:00 asubuhi -> 6:00 mchana', '12:00 asubuhi -> 6:00 mchana'),
            ('6:00 mchana -> 12:00 jioni', '6:00 mchana -> 12:00 jioni'),

        )
    MudaWaKumbusho = models.CharField(choices=MudaWaKumbusho_Choices, verbose_name="Muda Wa Kukumbushwa ?",max_length=500, blank=True,null=True)
    Lengo_Choices = (
            ('Kwaajili Ya Mayai', 'Kwaajili Ya Mayai'),
            ('Kwaajili Ya Nyama', 'Kwaajili Ya Nyama'),

        )
    LengoLaKufuga = models.CharField(choices=Lengo_Choices, verbose_name="Lengo La Kufuga Hao Kuku ?",max_length=500, blank=True,null=True)
    MfumoWaKufuga_Choices = (
            ('Shadidi (mfumo wa ndani tu)', 'Shadidi (mfumo wa ndani tu)'),
            ('Nusu huria (mfumo wa ndani na nje)', 'Nusu huria (ndani na nje)'),
            ('Huria (mfumo wa nje)', 'Huria (mfumo wa nje)')

        )
    MfumoWaKufuga = models.CharField(choices=MfumoWaKufuga_Choices, verbose_name="Mfumo Wa Kufuga Unaotumia ?",max_length=500, blank=True,null=True)
    KundiLaKukuWake = models.CharField(verbose_name="Kundi La Kuku Wake",max_length=500, blank=True,null=True)

    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=500, blank=True,null=True)
    UmriWaKukuKwaSiku = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku", blank=True,null=True)
    UmriWaKukuKwaWiki = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Wiki", blank=True,null=True)

    UmriWaKukuKwaSiku_KwaMahesabuTu = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku Kwa Mahesabu Tu", blank=True,null=True)
    UmriWaKukuKwaWiki_KwaMahesabuTu = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Wiki Kwa Mahesabu Tu", blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} Lengo: {self.LengoLaKufuga}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Mabadiliko Ya Lishe"


    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        AinaYaKuku = self.AinaYaKuku
        UmriWaKukuKwaWiki = self.UmriWaKukuKwaWiki_KwaMahesabuTu
        UmriWaKukuKwaSiku = self.UmriWaKukuKwaSiku_KwaMahesabuTu
        Remained_Days_Per_Period = 0
        remaining_days = 0

        #-------------KUKU MWENYE WIKI 1------------

        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7):
            Remained_Days_Per_Period = 21 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #--------------------------KUKU WA WIKI 2---------------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14):
            Remained_Days_Per_Period = 14 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #------------------------KUKU WA WIKI 3----------------
        #--------------------------KUKU WA WIKI 3---------------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------KUKU WA WIKI 4--------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #---------------KUKU WA WIKI 5------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35):
            Remained_Days_Per_Period = 84 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #--------------KUKU WA WIKI 6---------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42):
            Remained_Days_Per_Period = 77 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 7---------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49):
            Remained_Days_Per_Period = 70 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #----------------KUKU WA WIKI 8------------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56):
            Remained_Days_Per_Period = 63 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 9-------------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63):
            Remained_Days_Per_Period = 56 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 10------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70):
            Remained_Days_Per_Period = 49 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-----------------KUKU WA WIKI 11-----------------
        #-------------------KUKU WA WIKI 11------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77):
            Remained_Days_Per_Period = 42 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------KUKU WA WIKI 12----------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84):
            Remained_Days_Per_Period = 35 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #----------------KUKU WA WIKI 13-----------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91):
            Remained_Days_Per_Period = 28 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-------------KUKU WA WIKI 14---------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98):
            Remained_Days_Per_Period = 21 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #--------------KUKU WA WIKI 15-----------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105):
            Remained_Days_Per_Period = 14 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #---------------------KUKU WA WIKI 16--------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-------------KUKU WA WIKI 17------------
        if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #--------------KUKU WA WIKI 18---------------
        # if (AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126):
        #     Remained_Days_Per_Period = 42 #28-7=21
        #     remaining_days = Remained_Days_Per_Period - time_elapsed
        #     print(f"remaining_days: {remaining_days}")

        #     # Update day_is_reached to True if remaining_days is equal to 1
        #     if remaining_days == 0 and not self.day_is_reached:
        #         self.day_is_reached = True
        #         self.save(update_fields=['day_is_reached'])


        #     return remaining_days





        #---------------------MWISHO WA KUKU HUYO AISHIA WIKI YA 17 (YANI CHAKULA CHA GROWER)










        #------------------MWANZO WA KUKU MWINGINE-----------------(BROILA)


        #--------------------KUKU WA WIKI 1---------------
        if (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #----------------KUKU WA WIKI 2-----------------
        if (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #------------------KUKU WA WIKI 3------------------
        if (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #--------------------KUKU WA WIKI 4-------------------
        if (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days






        #------------------------MWISHO WA KUKU (BROILA) TUNAENDA KWA WIKI 4------




        #---------------------MWANZO WA KUKU MWINGINE--------------------

        #--------------KUKU WA WIKI 1-----------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7)):
            Remained_Days_Per_Period = 35 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #---------------KUKU WA WIKI 2-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14)):
            Remained_Days_Per_Period = 28 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #---------------KUKU WA WIKI 3------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21)):
            Remained_Days_Per_Period = 21 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------KUKU WA WIKI 4-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28)):
            Remained_Days_Per_Period = 14 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #----------------KUKU WA WIKI 5------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35)):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-------------------KUKU WA WIKI 6------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42)):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-----------------KUKU WA WIKI 7--------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49)):
            Remained_Days_Per_Period = 98 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 8-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56)):
            Remained_Days_Per_Period = 91 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #------------------KUKU WA Wiki 9------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63)):
            Remained_Days_Per_Period = 84 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #------------------KUKU WA WIKI 10---------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70)):
            Remained_Days_Per_Period = 77 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 11--------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77)):
            Remained_Days_Per_Period = 70 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #----------------KUKU WA WIKI 12-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84)):
            Remained_Days_Per_Period = 63 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------KUKU WA WIKI 13--------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91)):
            Remained_Days_Per_Period = 56 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #---------------KUKU WA WIKI 14-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98)):
            Remained_Days_Per_Period = 49 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #--------------------KUKU WA WIKI 15--------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105)):
            Remained_Days_Per_Period = 42 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------------KUKU WA WIKI 16----------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112)):
            Remained_Days_Per_Period = 35 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        #-----------------KUKU WA WIKI 17-------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119)):
            Remained_Days_Per_Period = 28 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------WIKI YA 18-----------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126)):
            Remained_Days_Per_Period = 21 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #---------------KUKU WA WIKI 19------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 127 and UmriWaKukuKwaSiku <= 133)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 127 and UmriWaKukuKwaSiku <= 133)):
            Remained_Days_Per_Period = 14 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-----------------KUKU WA WIKI 20---------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 134 and UmriWaKukuKwaSiku <= 140)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 134 and UmriWaKukuKwaSiku <= 140)):
            Remained_Days_Per_Period = 7 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days

        #-------------KUKU WA WIKI 21--------------
        if ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 141 and UmriWaKukuKwaSiku <= 147)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 141 and UmriWaKukuKwaSiku <= 147)):
            Remained_Days_Per_Period = 1 #28-7=21
            remaining_days = Remained_Days_Per_Period - time_elapsed
            print(f"remaining_days: {remaining_days}")

            # Update day_is_reached to True if remaining_days is equal to 1
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])


            return remaining_days


        

        

    @property
    def is_red(self):
        # Will return True if any of the selected chanjo's remaining days is 1
        return self.time_left == 0




class KumbushoLaChanjo(models.Model):
      
    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku", blank=True,null=True,on_delete=models.PROTECT)
    #UmriWaKuku = models.ForeignKey(UmriWaKuku, verbose_name="Umri Wa Kuku", blank=False,null=False,on_delete=models.PROTECT)
    AinaYaChanjo = models.ManyToManyField(AinaZaChanjo, verbose_name="Aina Ya Chanjo", blank=True)

    #--------HIZI ZINZJIJAZA ZENYEWE KWENYE VIEW------------------
    UmriWaKukuKwaSiku = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku", blank=True,null=True)
    UmriWaKukuKwaWiki = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Wiki", blank=True,null=True)
    KundiLaKukuWake = models.CharField(verbose_name="Kundi La Kuku Wake",max_length=200, blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Chanjo"


    
    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Updated).days

        username = self.username
        UmriWaKukuKwaSiku = int(self.UmriWaKukuKwaSiku)

        #ili kuapdate umri wa kuku
        #UmriWaKukuKwaSiku_UpadteValue = time_elapsed - UmriWaKukuKwaSiku


        selected_chanjo = self.AinaYaChanjo.filter(
            Kutolewa__gt=UmriWaKukuKwaSiku  # Use double underscores for field lookups
        ).first()


        if selected_chanjo:
            print(f"selected Chanjos: {selected_chanjo}, username: {username}")
            
            chanjo_name = selected_chanjo.JinaLaChanjo
            Hutolewa_Siku = int(selected_chanjo.Kutolewa)
            remaining_days_1 = Hutolewa_Siku - UmriWaKukuKwaSiku

            remaining_days = remaining_days_1 - time_elapsed

            print(f"{self.username}, chanjo_name: {chanjo_name}, time_elapsed:{time_elapsed}, Hutolewa_Siku: {Hutolewa_Siku}, remaining_days: {remaining_days}")

            # Check if remaining days is 1 and set day_is_reached if not already set
            if remaining_days == 0 and not self.day_is_reached:
                self.day_is_reached = True
                self.save(update_fields=['day_is_reached'])

            # Return the remaining days for the first match (for display)
            return remaining_days

        # If no matching chanjo
        return 0

    @property
    def is_red(self):
        # Will return True if any of the selected chanjo's remaining days is 1
        return self.time_left == 0







class KumbushoLaUatamiajiWaMayai(models.Model):
    KiasiChaMayai = models.IntegerField(verbose_name="Kiasi Cha Mayai", blank=False,null=False)
    SikuYaNgapiTokaKuatamiwa = models.IntegerField(verbose_name="Siku Ya Ngapi Tangu Kuatamiwa", blank=False,null=False)
    AinaYaNdege = models.CharField(verbose_name="Aina Ya Ndege",max_length=200, blank=True,null=True)
    SikuKamiliZaKuatamia = models.IntegerField(verbose_name="Siku Zake kamili za Ndege Kuatamia", blank=True,null=True)

    #AinaYaNdege = models.ForeignKey(AinaZaNdege, verbose_name="Aina Ya Ndege", blank=True,null=True,on_delete=models.PROTECT)
    JinaLaUlipoYatoaMayai = models.CharField(verbose_name="Jina La UlipoYatoa Mayai au Alama",max_length=200, blank=True,null=True)
    NambaYakeYaSimu = models.CharField(verbose_name="Namba yake Ya Simu",max_length=13, blank=True,null=True)
    Kifaa_Choices = (
            ('Incubator', 'Incubator'),
            ('Ndege Mwenyewe', 'Ndege Mwenyewe'),

        )
    Kifaa = models.CharField(choices=Kifaa_Choices, verbose_name="Unatumia nini Kuatamia ?",max_length=100, blank=True,null=True)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    SikuKamiliZaKuatamiaDisplayed = models.IntegerField(verbose_name="Siku Zake kamili za Ndege Kuatamia (TunayotumiaKudisplay -Usijaze)", blank=True,null=True)
        
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Uatamiaji Wa Mayai"




    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        print(f"Time Since: {time_elapsed}")
        # print(f"Time Since {time_elapsed} days")
        # print(f"Siku Za Kukumbushwa {self.SikuZaKukumbushwa} days")
        kumbusho_la_mwisho = self.SikuYaNgapiTokaKuatamiwa
        siku_kamili_za_kuatamia_ndege = self.SikuKamiliZaKuatamia

        siku_tatu_kabla = siku_kamili_za_kuatamia_ndege - 3

        differ_days = siku_tatu_kabla - kumbusho_la_mwisho
        
        # Assuming SikuZaKukumbushwa is the number of days, directly subtract time_elapsed
        remaining_days = differ_days - time_elapsed
        print(f"Siku Ya Mwisho: {kumbusho_la_mwisho}, Siku Kamili: {siku_kamili_za_kuatamia_ndege}, Differ: {differ_days}, Time Left: {remaining_days} days")

        # Update day_is_reached to True if remaining_days is equal to 1
        if remaining_days == 0 and not self.day_is_reached:
            self.day_is_reached = True
            self.save(update_fields=['day_is_reached'])

        return remaining_days

    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 0










class EmailSendCount_Wanunuzi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    JinaLaMnunuzi = models.CharField(verbose_name="Jina La Mnunuzi",max_length=500, blank=True,null=True)
    NambaYaSimuYaMnunuzi = models.CharField(verbose_name="Namba Ya Simu Ya Mnunuzi",max_length=13, blank=True,null=True)
    Mkoa = models.CharField(verbose_name="Mkoa",max_length=500, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho Wanunuzi"



class HistoriaZaJumbeZaWanunuzi(models.Model):
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    JinaLaMnunuzi = models.CharField(verbose_name="Jina La Mnunuzi",max_length=500, blank=True,null=True)
    NambaYaSimuYaMnunuzi = models.CharField(verbose_name="Namba Ya Simu Ya Mnunuzi",max_length=13, blank=True,null=True)
    Mkoa = models.CharField(verbose_name="Mkoa",max_length=500, blank=True,null=True)
    Wilaya = models.CharField(verbose_name="Wilaya",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.JinaLaMnunuzi} - {self.NambaYaSimuYaMnunuzi}"

    class Meta:
        verbose_name_plural = "Historia Za Jumbe Za Wanunuzi"





class EmailSendCount_KumbushoLaUatamiajiWaMayai(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Uatamiaji Wa Mayai"

class EmailSendCount_Maoni(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    ApprovedUser = models.CharField(verbose_name="Mtu Aliyetoa Maoni",max_length=500, blank=True,null=True)
    ApprovedMaelezoUser = models.CharField(verbose_name="Maoni Aliyohakiki",max_length=1000, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Maoni"

class EmailSendCount_MyUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    ApprovedUser = models.CharField(verbose_name="Mtumiaji  Aliyeomba Kuidinishwa",max_length=500, blank=True,null=True)
    ApprovedMaelezoUser = models.CharField(verbose_name="Maelezo Ya Mtumiaji  Aliyeomba Kuidinishwa",max_length=1000, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Users"







class EmailSendCount_DukaLako(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    ApprovedPost = models.CharField(verbose_name="Posti Aliyohakiki",max_length=500, blank=True,null=True)
    ApprovedMaelezoPost = models.CharField(verbose_name="Maelezo Ya Posti Aliyohakiki",max_length=1000, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Duka Lako"


class EmailSendCount_KumbushoUsafishajiBanda(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Usafishaji Banda"



class EmailSendCount_KumbushoLaMabadilikoYaLishe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Mabadiliko Ya Lishe"






class EmailSendCount_KumbushoLaChanjo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Chanjo"











class TaarifaZaKuku(models.Model):

    # Hapa utajaza kila aina ya kuku na kwa kila Chakula na kwa kila wiki
    # Eg: AinaYaKuku: Stata
    #     UmriKwaWiki: Wiki 1
    #     JinaLaChakula: Mahindi
    #     KiwangoChaProtini_In_1Kg: 80%
    #     KiwangoChaWanga_In_1Kg: 80%, etc


    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku",on_delete=models.PROTECT, blank=True,null=True)
    #UmriKwaWiki = models.ForeignKey(UmriWaKuku, verbose_name="Umri Wa Kuku - Wiki ?",on_delete=models.PROTECT, blank=True,null=True)
    #Kipindi = models.ForeignKey(VipindiVyaKuku, verbose_name="Kipindi",on_delete=models.PROTECT, blank=True,null=True)
    #JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.PROTECT, blank=True,null=True)


    #--kiasi cha chakula KWA WIKI kulingana na umri wa kuku-----------------
    KiasiChaChakulaKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 1 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 2 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 3 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 4 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 5 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 6 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 7 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 8 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 9 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 10 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 11 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 12 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 13 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 14 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 15 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 16 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 17 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 18 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 19 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 20 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 21 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 22 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 23 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 24 - KG", default=0, blank=True,null=True)


    

    

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaKuku.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Taarifa Za Kuku"














#-------------------CHAT DUKALAKO----------------------
class ChatMessage(models.Model):
    MyPostID = models.IntegerField(verbose_name="ID Ya Post", blank=True,null=True)
    post = models.ForeignKey(DukaLako, related_name='chat_messages', on_delete=models.CASCADE)
    #sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(verbose_name="Sender Name",max_length=200, blank=True,null=True)

    SenderImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Sender", blank=True, null=True)
    SenderPhone = models.CharField(verbose_name="Namba Ya Sender",max_length=13, blank=True,null=True)
    SenderEmail = models.EmailField(verbose_name="Email Ya Sender",max_length=200, blank=True,null=True)
    SenderWilaya = models.CharField(verbose_name="Wilaya Ya Sender",max_length=200, blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    replyTo = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self):
        return f"Message by {self.sender} on {self.post.Title}"




class InformUsers(models.Model):
    Title = models.CharField(verbose_name="Ujumbe unahusiana na ?", max_length=1000, blank=True, null=True)
    SentMessage = models.TextField(max_length=10000, verbose_name="Ujumbe", blank=True, null=True)     
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.SentMessage 

    class Meta:
        verbose_name_plural = "InformUsers"











class WatejaWote2(models.Model):
    #reg_no= models.CharField(max_length=100000, default=generated_reg_no, unique=True, editable=False,blank=True,null=True)
    
    
    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500,blank=True,null=True)
    #JinaLaKituo = models.ForeignKey(VituoVyote, on_delete=models.PROTECT, blank=True,null=True) 

    SimuYaMteja = models.IntegerField(verbose_name="Namba Ya Simu Ya Mteja", blank=True,null=True)
    SimuYaMzaminiWa1 = models.IntegerField(verbose_name="Namba Ya Simu Ya Mzamini Wa 1", blank=True,null=True)
    SimuYaMzaminiWa2 = models.IntegerField(verbose_name="Namba Ya Simu Ya Mzamini Wa 2", blank=True,null=True)
    JinaLaMzaminiWa1 = models.CharField(verbose_name="Jina Kamili La Mzamini Wa 1", max_length=500,blank=True,null=True)
    JinaLaMzaminiWa2 = models.CharField(verbose_name="Jina Kamili La Mzamini Wa 2", max_length=500,blank=True,null=True)

    EmailYaMteja = models.EmailField(verbose_name="Email Ya Mteja", max_length=500,blank=True,null=True)
    Mahali = models.CharField(verbose_name="Mahali Anapoishi", max_length=500,blank=True,null=True)
    MaelezoYaMteja = models.TextField(verbose_name="Maelezo Ya Mteja", max_length=10000,blank=True,null=True)

    KiasiAnachokopa = models.IntegerField(verbose_name="Kiasi Kiasi Anachokopa", blank=True,null=True, default=0)
    KiasiAlicholipa = models.IntegerField(verbose_name="Kiasi Alicholipa Mpaka Sasa", blank=True,null=True, default=0)
    RejeshoKwaSiku = models.IntegerField(verbose_name="Rejesho Kwa Siku", blank=True,null=True, default=0)
    JumlaYaDeni = models.IntegerField(verbose_name="Jumla Ya Deni Analodaiwa", blank=True,null=True, default=0)
    Riba = models.IntegerField(verbose_name="Riba", blank=True,null=True, default=0)

    AmesajiliwaNa = models.CharField(verbose_name="Amesajiliwa Na ?", max_length=500,blank=True,null=True)
    Amerejesha_Leo = models.BooleanField(default=False, blank=True, null=True)
    
    PichaYaMteja = models.ImageField(verbose_name="Picha Ya Mteja", upload_to='media/PichaZaVyakula/',blank=True,null=True)

    #if created is greater than 30 inakuwa false
    Ni_Mteja_Hai = models.BooleanField(default=True, blank=True, null=True)

    Nje_Ya_Mkata_Wote = models.BooleanField(default=False, blank=True, null=True)
    Nje_Ya_Mkata_Leo = models.BooleanField(default=False, blank=True, null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Up_To = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    JumlaYaFainiZote = models.IntegerField(verbose_name="JumlaYaFainiZote", blank=True,null=True, default=0)

    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)

    
    
    class Meta:
        verbose_name_plural = "Wateja Wote"
        
    
    def __str__(self):
        return f" {self.JinaKamiliLaMteja} "

    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        #print(f"Time Since: {time_elapsed}")
    
        # Update day_is_reached to True if remaining_days is equal to 1

        

        # if time_elapsed == 30 and not self.Nje_Ya_Mkata_Leo:
        #     self.Nje_Ya_Mkata_Leo = True
        #     self.save(update_fields=['Nje_Ya_Mkata_Leo'])

        # if time_elapsed == 31 and self.Ni_Mteja_Hai:
        #     self.Ni_Mteja_Hai = False
        #     self.Nje_Ya_Mkata_Leo = False
        #     self.save(update_fields=['Ni_Mteja_Hai','Nje_Ya_Mkata_Leo'])

        # if time_elapsed == 31 and self.Nje_Ya_Mkata_Leo:
        #     self.Nje_Ya_Mkata_Leo = False
        #     self.save(update_fields=['Nje_Ya_Mkata_Leo'])

        # if time_elapsed == 31 and not self.Nje_Ya_Mkata_Wote:
        #     self.Nje_Ya_Mkata_Wote = True
        #     self.save(update_fields=['Nje_Ya_Mkata_Wote'])

        return time_elapsed



    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 4





class MarejeshoCopies(models.Model):
    #reg_no = models.CharField(verbose_name="Namba Ya Mteja", max_length=100000, blank=True, null=True)

    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.CharField(verbose_name="Jina La Kituo Cha Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.ForeignKey(VituoVyote, on_delete=models.PROTECT, blank=True, null=True)
    SimuYaMteja = models.IntegerField(verbose_name="Namba Ya Simu Ya Mteja", blank=True, null=True)
    EmailYaMteja = models.EmailField(verbose_name="Email Ya Mteja", max_length=500, blank=True, null=True)
    Mahali = models.CharField(verbose_name="Mahali Anapoishi", max_length=500, blank=True, null=True)
    KiasiAnachokopa = models.IntegerField(verbose_name="Kiasi Anachokopa", blank=True, null=True, default=0)
    KiasiAlicholipa = models.IntegerField(verbose_name="Kiasi Alicholipa", blank=True, null=True, default=0)
    RejeshoKwaSiku = models.IntegerField(verbose_name="Rejesho Kwa Siku", blank=True, null=True, default=0)
    JumlaYaDeni = models.IntegerField(verbose_name="Jumla Ya Deni Analodaiwa", blank=True, null=True, default=0)
    Riba = models.IntegerField(verbose_name="Riba", blank=True, null=True, default=0)
    RejeshoLililoPokelewaLeo = models.IntegerField(verbose_name="Rejesho Lililo Pokelewa Leo", blank=True, null=True, default=0)
    FainiKwaSiku = models.IntegerField(verbose_name="Faini Kwa Siku", blank=True, null=True, default=0)

    AmesajiliwaNa = models.CharField(verbose_name="Amesajiliwa Na ?", max_length=500, blank=True, null=True)
    PichaYaMteja = models.ImageField(verbose_name="Picha Ya Mteja", upload_to='media/PichaZaVyakula/', blank=True, null=True)
    Ni_Mteja_Hai = models.BooleanField(default=True, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Up_To = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Marejesho Copies"

    def __str__(self):
        return f"{self.JinaKamiliLaMteja}"


    


class NjeYaMkatabaCopies(models.Model):
    #reg_no = models.CharField(verbose_name="Namba Ya Mteja", max_length=100000, blank=True, null=True)

    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.CharField(verbose_name="Jina La Kituo Cha Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.ForeignKey(VituoVyote, on_delete=models.PROTECT, blank=True, null=True)
    SimuYaMteja = models.IntegerField(verbose_name="Namba Ya Simu Ya Mteja", blank=True, null=True)
    EmailYaMteja = models.EmailField(verbose_name="Email Ya Mteja", max_length=500, blank=True, null=True)
    Mahali = models.CharField(verbose_name="Mahali Anapoishi", max_length=500, blank=True, null=True)
    KiasiAnachokopa = models.IntegerField(verbose_name="Kiasi Anachokopa", blank=True, null=True, default=0)
    KiasiAlicholipa = models.IntegerField(verbose_name="Kiasi Alicholipa", blank=True, null=True, default=0)
    RejeshoKwaSiku = models.IntegerField(verbose_name="Rejesho Kwa Siku", blank=True, null=True, default=0)
    JumlaYaDeni = models.IntegerField(verbose_name="Jumla Ya Deni Analodaiwa", blank=True, null=True, default=0)
    Riba = models.IntegerField(verbose_name="Riba", blank=True, null=True, default=0)
    RejeshoLililoPokelewaLeo = models.IntegerField(verbose_name="Rejesho Lililo Pokelewa Leo", blank=True, null=True, default=0)
    FainiKwaSiku = models.IntegerField(verbose_name="Faini Kwa Siku", blank=True, null=True, default=0)

    AmesajiliwaNa = models.CharField(verbose_name="Amesajiliwa Na ?", max_length=500, blank=True, null=True)
    PichaYaMteja = models.ImageField(verbose_name="Picha Ya Mteja", upload_to='media/PichaZaVyakula/', blank=True, null=True)
    Ni_Mteja_Hai = models.BooleanField(default=True, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Up_To = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Nje Ya Mkataba Copies"

    def __str__(self):
        return f"{self.JinaKamiliLaMteja}"



class MalipoYaFainiCopies(models.Model):
    #reg_no = models.CharField(verbose_name="Namba Ya Mteja", max_length=100000, blank=True, null=True)
    
    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.CharField(verbose_name="Jina La Kituo Cha Mteja", max_length=500, blank=True, null=True)
    #JinaLaKituo = models.ForeignKey(VituoVyote, on_delete=models.PROTECT, blank=True, null=True)
    SimuYaMteja = models.IntegerField(verbose_name="Namba Ya Simu Ya Mteja", blank=True, null=True)
    EmailYaMteja = models.EmailField(verbose_name="Email Ya Mteja", max_length=500, blank=True, null=True)
    Mahali = models.CharField(verbose_name="Mahali Anapoishi", max_length=500, blank=True, null=True)
    KiasiAnachokopa = models.IntegerField(verbose_name="Kiasi Anachokopa", blank=True, null=True, default=0)
    KiasiAlicholipa = models.IntegerField(verbose_name="Kiasi Alicholipa", blank=True, null=True, default=0)
    RejeshoKwaSiku = models.IntegerField(verbose_name="Rejesho Kwa Siku", blank=True, null=True, default=0)
    JumlaYaDeni = models.IntegerField(verbose_name="Jumla Ya Deni Analodaiwa", blank=True, null=True, default=0)
    Riba = models.IntegerField(verbose_name="Riba", blank=True, null=True, default=0)
    FainiIliyoPokelewaLeo = models.IntegerField(verbose_name="Faini Iliyopokelewa Leo", blank=True, null=True, default=0)
    FainiKwaSiku = models.IntegerField(verbose_name="Faini Kwa Siku", blank=True, null=True, default=0)

    AmesajiliwaNa = models.CharField(verbose_name="Amesajiliwa Na ?", max_length=500, blank=True, null=True)
    PichaYaMteja = models.ImageField(verbose_name="Picha Ya Mteja", upload_to='media/PichaZaVyakula/', blank=True, null=True)
    Ni_Mteja_Hai = models.BooleanField(default=True, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Up_To = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Malipo Ya Faini Copies"

    def __str__(self):
        return f"{self.JinaKamiliLaMteja}"

