from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Posts"
    link = "/posts/"
    description = "Most recently blog posts"

    def items(self):
        return Post.objects.order_by('created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # def item_link(self, item):
    #     return reverse('posts', args=[item.pk])
