from restaurants.models import Restaurant,Products,Category
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = u'Opens a connection to Redis and listens for messages, and then whenever it gets one, sends the message onto a channel in the Django channel system'

    def __init__(self,*args,**kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def import_data(self):
        if not Restaurant.objects.all():
            r=Restaurant(name="Bizim Büfe")
            r.save()
            c= Category(name="FastFood")
            c.save()
            p = Products(name="Yengen", category=c, restaurants=r)
            p.save()
            p = Products(name="Dilli Kaşarlı", category=c, restaurants=r)
            p.save()
            p = Products(name="Goralı", category=c, restaurants=r)
            p.save()
            r=Restaurant(name="Harika Ev Yemekleri")
            r.save()
            c= Category(name="Ev Yemekleri")
            c.save()
            p = Products(name="Mercimek Çorbası", category=c, restaurants=r)
            p.save()
            p = Products(name="Pilav", category=c, restaurants=r)
            p.save()
            p = Products(name="Kuru Fasülye", category=c, restaurants=r)
            p.save()
            r=Restaurant(name="Süper Dönerci")
            r.save()
            c= Category(name="Döner/Kebap")
            c.save()
            p = Products(name="Döner", category=c, restaurants=r)
            p.save()
            p = Products(name="İskender", category=c, restaurants=r)
            p.save()
            p = Products(name="Etibol İskender", category=c, restaurants=r)
            p.save()



            u = User(username="Uğur Özi", email="uozy@yspt.com")
            u.save()
            u = User(username="Cenk Yaldız", email="cyaldiz@yspt.com")
            u.save()
            u = User(username="Selin Simge", email="ssimge@yspt.com")
            u.save()

    def handle(self, *args, **options):
        self.import_data()