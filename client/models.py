from django.db import models
from doctor.models import Doctor
from uuid import uuid4


GENDER_CHOICES = (
    ('male','male'),
    ('female','female'),
)

class Client (models.Model) : 
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4,db_index=True)
    picture = models.ImageField(upload_to='clients-pics/',default='default.png')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    def __str__(self) : 
        return self.full_name
    
class Ticket (models.Model) : 
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4,db_index=True)
    doctor = models.ForeignKey(Doctor,related_name='doc_ticket',on_delete=models.SET_NULL,null=True)
    client = models.ForeignKey(Client,related_name='client_ticket',on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self) : 
        return f"{self.doctor.full_name} | {self.client.full_name}"
