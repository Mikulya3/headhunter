from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.feedback.models import Like, Favorite


class LikeMixin:
    @action(detail=True, methods=['POST'])
    def post(self, request, pk, *args, **kwargs):
        obj, _ = Like.objects.get_or_create(vacancy_id=pk, user=request.user)
        obj.like = not obj.like
        obj.save()
        status_ = 'Liked'
        if not obj.like:
            status_ = 'Unliked'
        return Response({'msg': status_})


class FavoriteMixin:
    @action(detail=True, methods=['POST'])
    def post(self, request, pk, *args, **kwargs):
        try:
            obj = Favorite.objects.get(vacancy_id=pk, user=request.user)
            obj.delete()
            status_ = 'Удалено из избранного'
        except Favorite.DoesNotExist:
            obj = Favorite.objects.get_or_create(vacancy_id=pk, user=request.user)
            status_ = 'Добавлено в избранное'
        return Response({'msg': status_})
