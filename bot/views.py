# bot/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer

@api_view(['POST'])
def register_user(request):
    telegram_id = request.data.get('telegram_id')
    username = request.data.get('username')

    if not telegram_id:
        return Response({'error': 'telegram_id is required'}, status=400)

    user, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={'username': username}
    )

    if not created and user.username != username:
        user.username = username
        user.save()

    serializer = TelegramUserSerializer(user)
    return Response(serializer.data, status=200 if not created else 201)
