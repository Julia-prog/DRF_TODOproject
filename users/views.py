from rest_framework.viewsets import ModelViewSet
from users.models import User
from DRF_todo2022.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
