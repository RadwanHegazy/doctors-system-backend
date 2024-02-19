from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ...models import Client, Ticket


@decorators.api_view(['PATCH'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CheckClientTicket(request, client_id) : 
    try :
        
        try : 
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist: 
            return Response({
                'message' : 'client not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        doctor = request.user

        ticket = Ticket.objects.get(doctor=doctor, client=client)

        ticket.checked = True
        ticket.save()

        return Response({
            'message' : "ticket updated sucessfully"
        },status=status.HTTP_200_OK)

    except Exception as erorr : 
        return Response({
            'message' : f'an error accoured : {erorr}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)