from rest_framework import serializers
from .models import Friends
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'

    # def restore_object(self, attrs, instance=None):
    #     """
    #     Create or update a new snippet instance, given a dictionary
    #     of deserialized field values.
    #
    #     Note that if we don't define this method, then deserializing
    #     data will simply return a dictionary of items.
    #     """
    #     if instance:
    #         # Update existing instance
    #         instance.title = attrs.get('name', instance.name)
    #         instance.code = attrs.get('first_met', instance.first_met)
    #         instance.linenos = attrs.get('home_town', instance.home_town)
    #         instance.language = attrs.get('status', instance.status)
    #         instance.style = attrs.get('type', instance.type)
    #         return instance
    #
    #     # Create new instance
    #     return Friends(**attrs)