from rest_framework import serializers
from .models import Koyla

class KoylaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Koyla
		fields = ('word','la','comment')
