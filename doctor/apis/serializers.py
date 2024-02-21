from rest_framework import serializers
from client.models import Ticket
from client.apis.serializer import ClientSerializer
from doctor.models import Doctor, Department
from rest_framework_simplejwt.tokens import RefreshToken

class DepartmentSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = Department
        fields = ('name',)

class DoctorSerializer (serializers.ModelSerializer) : 
    has_counter = False
    has_clients = False
    department = DepartmentSerializer()    

    class Meta:
        model = Doctor
        fields = ('id','picture','full_name','department')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        

            
        if self.has_counter :
            ticket = Ticket.objects.filter(doctor=instance)
            data['checked_clients'] = ticket.filter(checked=True).count()
            data['unchecked_clients'] = ticket.filter(checked=False).count()
        
        if self.has_clients :
            clients = [i.get_client_for_doc() for i in Ticket.objects.filter(doctor=instance,checked=False)]
            data['clients'] = clients

        return data

class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()
    tokens = {}
    
    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            doc = Doctor.objects.get(email=email)
        except Doctor.DoesNotExist :
            raise serializers.ValidationError({
                'message' : "invalid email"
            },code=403)
        
        if not doc.check_password(password) : 
            raise serializers.ValidationError({
                'message' : "invalid password"
            },code=403)
        
        token = RefreshToken.for_user(doc)

        self.tokens = {
            'refresh' : str(token),
            'access' : str(token.access_token)
        }

        return attrs