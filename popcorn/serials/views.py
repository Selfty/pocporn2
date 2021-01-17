from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Epizoda, Serial, Topserials
from django.http import JsonResponse
from django.views.generic.base import View
import unidecode
#from django_ajax.decorators import ajax

from django.contrib.sitemaps import Sitemap

def post_list(request):
    serials = Serial.objects.order_by('title_cz')
    posts = Epizoda.objects.order_by('-created_date')[:12]
    toppost = Topserials.objects.first()
    return render(request, 'serials/post_list.html', {'menu_items' : serials,'posts' : posts, 'toppost' : toppost})

def post_detail(request, name, sn, en):

	#episode nebo 404
    serials = Serial.objects.order_by('title_cz')

    post = get_object_or_404(Epizoda, epizoda_serial__title_cz=name, cislo_serie=sn, cislo_epizoda=en)
    toppost = Topserials.objects.first()
	#next episode


    if Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie=sn,cislo_epizoda__gt=en).order_by('cislo_epizoda').first():
        next = Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie=sn,cislo_epizoda__gt=en).order_by('cislo_epizoda').first()
    elif Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie__gt=sn,cislo_epizoda__gte=1).order_by('cislo_serie','cislo_epizoda').first():
        next = Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie__gt=sn,cislo_epizoda__gte=1).order_by('cislo_serie','cislo_epizoda').first()
    else:
        next = None
	#prev cislo_epizoda

    if Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie=sn,cislo_epizoda__lt=en).order_by('-cislo_epizoda').first():
        prev = Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie=sn,cislo_epizoda__lt=en).order_by('-cislo_epizoda').first()
    elif Epizoda.objects.filter(epizoda_serial__title_cz = name,cislo_serie__lt=sn).order_by('-cislo_serie','-cislo_epizoda').first():
        prev = Epizoda.objects.filter(epizoda_serial__title_cz=name,cislo_serie__lt=sn).order_by('-cislo_serie','-cislo_epizoda').first()
    else:
        prev = None
	
	#serial
    serial = get_object_or_404(Serial, title_cz=name)
		
    return render(request, 'serials/post_detail.html', {'menu_items' : serials,'post' : post,'next' : next,'prev' : prev,'toppost' : toppost, 'serial' : serial})

def serials(request):
    serialss = Serial.objects.order_by('title_cz')

	#episode nebo 404

    serials = Serial.objects.all().order_by('title_cz')
    #episodes = get_object_or_404(Post, name=name)
    toppost = Topserials.objects.first()
    return render(request, 'serials/serials.html', {'menu_items' : serialss,'serials' : serials,'toppost' : toppost})

def serial(request, name):
    serials = Serial.objects.order_by('title_cz')

    series = []
    serial = get_object_or_404(Serial, title_cz=name)
    episodes = Epizoda.objects.filter(epizoda_serial=serial.id)
    episodes = episodes.values('cislo_serie').distinct().order_by('cislo_serie')
    
    for ep in episodes:
        series.append(Epizoda.objects.filter(epizoda_serial=serial.id, cislo_serie=ep['cislo_serie']).order_by('cislo_epizoda'))

    return render(request, 'serials/serial.html', {'menu_items' : serials,'serial' : serial, 'series' : series})
    
def dmca(request):
    serials = Serial.objects.order_by('title_cz')

    return render(request, 'serials/dmca.html',{'menu_items' : serials})


def get(request, uid):
    uid = unidecode.unidecode(uid)
    serial = Serial.objects.filter(vyhledavaci_pole__contains=uid).order_by('title_cz')[:3]
    serials_dict = []
    for serie in serial:
        serial_dict = {
             'name' : serie.title_cz,
	     'title' : serie.title_cz
	              }
        serials_dict.append(serial_dict)
    if serial :
        return JsonResponse(serials_dict, safe=False)
    else:
        return JsonResponse({'serial':''}, safe=False)


def gett(request):
    return JsonResponse({'serial' : ''}, safe = False)

class EpizodaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Epizoda.objects.all()

    def lastmod(self, obj):
        return obj.created_date

class SerialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Serial.objects.all()

    def lastmod(self, obj):
        return timezone.now()