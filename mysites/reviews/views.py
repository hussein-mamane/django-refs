from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Article
from django.shortcuts import render

from .forms import ReviewerForm, CustomReviewerForm


class IndexView(generic.ListView):
    # All of this have default django management
    # only mandatory thing in that case is
    # model = Review #you dont even need to create the template
    # In case you want your own template
    template_name = "reviews/index.html"
    # in case you want to overwrite default name
    context_object_name = "article_list"
    # In case you want to override get_queryset with maximum flexibility

    def get_queryset(self):
        """Return all the articles"""
        return Article.objects.all  # .order_by("-pub_date")[:5]
    # it is enough to just override queryset and give model
    # queryset = Article.objects.all.order_by("-pub_date")[:5]


def add_reviewer(request):
    if request.method == 'GET':
        # the model form, recommended
        # form = ReviewerForm()
        # the custom form, avoid frontend validation not needed most of the time
        form = CustomReviewerForm()  # instance= can be given to pass default data
        return render(request, "reviews/add_reviewer.html", {"form": form})
    if request.method == 'POST':
        # request.POST is a dict
        form = ReviewerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # You can still access the unvalidated data directly
            # from request.POST at this point, but the  validated
            # data is better.
            # process the data in form.cleaned_data as required
            cleaned = {
                "first_name": form.cleaned_data.get("first_name"),
                "last_name": form.cleaned_data.get("last_name"),
                "reviewer_email": form.cleaned_data.get("reviewer_email")
            }
        # ----------------------------------------------------------------------------------------------
            # Convert dictionary to query string
            query_string = urlencode(form.cleaned_data)
            # query_string = urlencode(cleaned)
            # Construct the redirect URL
            # redirect_url = reverse('reviews:thanks_args') + '?' + query_string
            # this works for moving data, but it is not encrypted, and seeable in the url, use Post with render() or the session
            # It is better to use query_strings only for research on the website, so user can bookmark & share
            # return HttpResponseRedirect(redirect_url)
        # ----------------------------------------------------------------------------------------------
        # This down will works if args is a type supported for path parameter(int,slug,str,...)
        # They are seen in url
            # return HttpResponseRedirect(reverse("reviews:thanks_with_args", kwargs=cleaned))
        # ----------------------------------------------------------------------------------------------
        # Render thanks_safe.html template and pass the form data securely
            # safe redirect in request body;no data seen in url
            # Ensure that you have appropriate HTTPS configuration in
            # your Django project to ensure secure transmission of data.
            # This typically involves configuring your web server
            # (such as Nginx or Apache) to serve your Django application over HTTPS.
            # Additionally, you may want to configure Django's settings (settings.py)
            # to enforce HTTPS by setting SECURE_SSL_REDIRECT = True
            # and SECURE_HSTS_SECONDS = 31536000 (to enforce HSTS).
            return render(request, "reviews/thanks_safe.html", {'first_name': form.cleaned_data.get("first_name"), 'last_name': form.cleaned_data.get("last_name"), 'reviewer_email': form.cleaned_data.get("reviewer_email")})
        else:
            # return HttpResponseRedirect("invalid")# path for reviews/invalid
            # using url name, redirect with no args
            return HttpResponseRedirect(reverse("reviews:invalid", args=()))


def thanks(request, **kwargs):
    if kwargs:
        # path or route parameters
        return render(request, "reviews/thanks_path.html", kwargs)
    else:
        return render(request, "reviews/thanks.html")


def thanks_args(request):
    # you can just use the thanks view if you want
    return render(request, "reviews/thanks.html")


def invalid(request):
    return render(request, "reviews/invalid.html")
