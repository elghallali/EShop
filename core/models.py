from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('PE', 'Petit electromenager'),
    ('GE', 'Gros electromenager'),
    ('EM', 'Entretien de la maison'),
    ('TPV', 'TV-Photo-Video'),
    ('I', 'Informatique'),
)

STATE_CHOICES = (
    ("TAN-TET-HOC", "Tanger-Tétouan-Al Hoceïma"),
    ("ORI", "L'Oriental"),
    ("FE-MEK", "Fès-Meknès"),
    ("RAB-SAL-KEN", "Rabat-Salé-Kénitra"),
    ("BMEL-KHEN", "Béni Mellal-Khénifra"),
    ("CASA-SET", "Casablanca-Settat"),
    ("MAR-SAF", "Marrakech-Safi"),
    ("DRA-TAF", "Drâa-Tafilalet"),
    ("SOU-MAS", "Souss-Massa"),
    ("GUE-ONOU", "Guelmim-Oued Noun"),
    ("LAA-SAK", "Laâyoune-Sakia El Hamra"),
    ("DAK-OED", "Dakhla-Oued Ed-Dahab"),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to ='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class PostMessageContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    #items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    #shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    #billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
'''
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total
'''