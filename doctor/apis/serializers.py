from rest_framework import serializers
from doctor.models import Doctor, Department
from rest_framework_simplejwt.tokens import RefreshToken

class DepartmentSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = Department
        fields = ('name',)

class DoctorSerializer (serializers.ModelSerializer) : 
    has_counter = False
    department = DepartmentSerializer()    

    class Meta:
        model = Doctor
        fields = ('id','picture','full_name','department')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if self.has_counter :
            # return client analytics with data
            pass

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