from recicle_apis_consume.recicle_atlas.libs.recicle_atlas import RecicleAtlas
from rest_framework.response import Response
from rest_framework.views import APIView


class RecicleMaterialsView(APIView):
    def get(self, request):
        object = RecicleAtlas()
        object.extract_information_about_recicles()
        object.treat_data_state()
        return Response(object.by_state.values())
