from django.conf.urls import patterns, url


urlpatterns = patterns('product.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug>[a-z-]+?)-(?P<product_id>[0-9]+)/$', 'details',
        name='details'),
)
