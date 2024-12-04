from App.models import *
from django.utils.timezone import now
from datetime import timedelta

def run():
    today = now().date()
    wateja_list = WatejaWote2.objects.all()

    for mteja in wateja_list:
        time_elapsed =  mteja.time_left

        if time_elapsed == 4 and mteja.Ni_Mteja_Hai:
            mteja.Ni_Mteja_Hai = False
            mteja.save(update_fields=['Ni_Mteja_Hai'])
            self.send_email(mteja, "Ni Mteja Hai condition reached.")

        if time_elapsed == 3 and not mteja.Nje_Ya_Mkata_Leo:
            mteja.Nje_Ya_Mkata_Leo = True
            mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
            self.send_email(mteja, "Nje Ya Mkata Leo condition reached.")
            self.copy_to_nje_ya_mkataba_copies(mteja)

        if time_elapsed == 3 and mteja.Nje_Ya_Mkata_Leo:
            mteja.Nje_Ya_Mkata_Leo = False
            mteja.save(update_fields=['Nje_Ya_Mkata_Leo'])
            self.send_email(mteja, "Umetoka nje ya mkataba wa siku 30")

        if time_elapsed == 4 and not mteja.Nje_Ya_Mkata_Wote:
            mteja.Nje_Ya_Mkata_Wote = True
            mteja.save(update_fields=['Nje_Ya_Mkata_Wote'])
            self.send_email(mteja, "Nje Ya Mkata Wote condition reached.")
        
        print(f"Excuted: {mteja.JinaKamiliLaMteja}")
