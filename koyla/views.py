from rest_framework import viewsets, generics
from .serializers import KoylaSerializer
from .models import Koyla

class KoylaSet(generics.ListAPIView):
	queryset = Koyla.objects.all()
	serializer_class = KoylaSerializer
	
	def get_queryset(self):
		word = self.kwargs['word']
		return Koyla.objects.filter(word=word)