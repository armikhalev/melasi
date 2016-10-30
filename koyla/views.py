from rest_framework import generics
from .serializers import KoylaSerializer
from .models import Koyla

class KoylaSet(generics.ListAPIView):
	queryset = Koyla.objects.all()
	serializer_class = KoylaSerializer

	def get_queryset(self):
		word = self.kwargs['word']
		return Koyla.objects.filter(word=word)

class EngSet(KoylaSet):
	pass

class MelaSet(KoylaSet):
	def get_queryset(self):
		la = self.kwargs['la']
		return Koyla.objects.filter(la=la)
