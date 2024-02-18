from rest_framework import serializers
from ..models import Client, Ticket
from doctor.models import Doctor
import segno
from uuid import uuid4

class ClientSerializer (serializers.ModelSerializer): 
    doctor_id = serializers.CharField()

    class Meta : 
        model = Client
        fields = ('__all__')


    def save(self, **kwargs):
        doc_id = self.validated_data.pop('doctor_id')

        client = Client.objects.create(**self.validated_data)
        client.save()

        doctor = Doctor.objects.get(id=doc_id)

        ticket = Ticket.objects.create(
            client = client,
            doctor = doctor,
        )

        ticket.save()

        qr = segno.make_qr(f'{client.id}')

        qr_path = f"media/tickets/{uuid4()}.png"
        qr.save(qr_path,scale=6)

        context = {
            'qr' : f'/{qr_path}'
        }
        
        return context
