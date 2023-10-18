from recicle_apis_consume.recicle_atlas.libs.recicle_atlas_class import RecicleAtlas
from django.shortcuts import render, redirect, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView


def RecicleMaterialsView(APIView):
	object_ = RecicleAtlas()
	object_.extract_information_about_recicles()
	object_.treat_data_state()
	object_.all_materials = [object_.by_state[state] for state in object_.by_state.keys()]
	return Response(object_.all_materials)