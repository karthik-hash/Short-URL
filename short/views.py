from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .models import URL

def homeview(request):
    if request.method == 'POST':
        url = request.POST['url']
        if url[:4].lower() != "http":
                url = "http://" + url
        exists = URL.objects.filter(url = url).exists()
        if exists:
            obj = URL.objects.get(url = url)
            obj.count += 1
            obj.save()
        else:
            obj, created = URL.objects.get_or_create(url=url)

        content = {
            'count' : URL.objects.get(url=url).count,
            'url' : url,
            'short' : URL.objects.get(url=url).shortcode,
            'shortcode' : "https://pin-ly.herokuapp.com/"+URL.objects.get(url=url).shortcode
        }
        request.session['content'] = content
        return redirect(success)
    return render(request, 'home.html')

def success(request):
    try:
        content = request.session['content']
    except:
        raise Http404("First Generate Short URL.")
    return render(request, 'success.html', content)

def redir(request, shortcode=None):
    obj = URL.objects.get(shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
