from rest_framework import status, decorators
from rest_framework.response import Response
from doctor.apis.serializers import Doctor
from ..serializer import ClientSerializer



@decorators.api_view(['POST'])
def CreateClient (request, doc_id) : 
    try :
        
        try : 
            Doctor.objects.get(id=doc_id)
        except Doctor.DoesNotExist:
            return Response({
                'message' : f'doctor not found'
            },status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data.copy()
        data['doctor_id'] = doc_id

        serializer = ClientSerializer(data=data)
        
        if serializer.is_valid() : 
            response = serializer.save()
            return Response(response,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
    except Exception as error :
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)