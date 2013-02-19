from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from composer.models import Post, Page


def shorternUrl(url):
	API_KEY = "AIzaSyCmJI4LgXgNH8eItZUC--ExD8n6IXs-zCY"
	apiUrl = 'https://www.googleapis.com/urlshortener/v1/url'
	longUrl = url
	headers = {"Content-type": "application/json"}
	data = {"longUrl": longUrl}
	import httplib2
	h = httplib2.Http('.cache')
	try:
		import json
		headers, response = h.request(apiUrl, "POST", json.dumps(data), headers)
		result = json.loads(response)
		#print result["id"]
		return result["id"]
	except Exception, e:
		print "unexpected error %s" % e
		return ''


def landing(request):
	return render_to_response('landing.html', {}, context_instance=RequestContext(request))


def home(request):
	if request.method == 'POST':
		content = request.POST['content']
		from time import gmtime, strftime
		pub_date=strftime("%Y-%m-%d %H:%M:%S")	
		post_obj = Page(content=content, pub_date=pub_date)		
		post_obj.save()	
		# url for development
		#urlness = "http://localhost:8000/posts/" + str(post_obj.id)
		# url for production
		urlness = "http://blnkpg.com/posts/" + str(post_obj.id)
		# URL shortener call
		urlness = shorternUrl(urlness)
		post_obj.url = urlness
		post_obj.save()
		import markdown
		markdownhtml = markdown.markdown(post_obj.content)
		return render_to_response('post.html', {'post_detail': post_obj, 'markdownhtml': markdownhtml}, context_instance=RequestContext(request))
	else:
		return render_to_response('composer.html', {}, context_instance=RequestContext(request))


def posts(request):
	posts_list = Page.objects.all().order_by('-pub_date')
	return render_to_response('posts.html', {'posts_list': posts_list}, context_instance=RequestContext(request))


def post(request, post_id):
	post_detail = get_object_or_404(Page, pk=post_id)
	import markdown
	markdownhtml = markdown.markdown(post_detail.content)
	return render_to_response('post.html', {'post_detail': post_detail, 'markdownhtml': markdownhtml}, context_instance=RequestContext(request))


# Retired view
def publish(request):
	if request.method == 'POST':
		content = request.POST['content']
		print "content="+content
		from django.utils import timezone
		pub_date=timezone.now()
		print "pub_date="+ str(pub_date)
		post_obj = Post(content=content, pub_date=pub_date)		
		post_obj.save()
		print post_obj.id
		return render_to_response('composer.html', {}, context_instance=RequestContext(request))