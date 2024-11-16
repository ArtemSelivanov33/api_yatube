from rest_framework import serializers

from posts.models import Comment, Group, Post, User
#User получен в моделях через get_user_model(), я просто оттуда импортировал.
#Или надо получать в каждом файле через get_user_model()?


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователей."""
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='posts',
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели постов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели групп."""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
