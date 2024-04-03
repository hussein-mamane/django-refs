from django.db import models

"""
class Theme(models.Model):
    theme_name = models.CharField(max_length=40)
    theme_add_date = models.DateField()


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_add_date = models.DateField()
    # One category in many themes , one theme can be in many category
    # (like 'violence' theme can be in 'movie' category or 'videogame' category)
    # 'violence' have many category, but those categories have many themes also
    # I let django manage this one
    themes = models.ManyToManyField(Theme)
"""


class Reviewer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    # Validator can be given in parentheses
    reviewer_email = models.EmailField(max_length=40)


class Article(models.Model):
    pub_date = models.DateField()
    minimal_viewer_age = models.IntegerField()
    title = models.TextField()
    # 1 or more publishers (Reviewer), ManyToMany
    # This and the publication link table can be managed by django
    publishers = models.ManyToManyField(Reviewer,
                                        through="PublicationLink",
                                        through_fields=("article", "reviewer"),)
    # if you want django to manage this is enough
    # publishers = models.ManyToManyField(Reviewer)
    # themes = models.ForeignKey(
    #     Article, on_delete=models.SET_NULL, blank=True, null=True)


class PublicationLink(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('reviewer', 'article'),)
    # best to do than unique_together
    # UniqueConstraint(fields = ['reviewer', 'article'], name = 'whatever_meaningful')

    # The Image that represent the article, both on thumbnail and also
    # can be used in the article layout
    # thumbnail = models.OneToOneField(
    #     ImageOrVideo, on_delete=models.CASCADE, primary_key=True)
    # if it is not primary_key, another article can use this thumbnail


class Section(models.Model):
    title = models.TextField()
    content = models.TextField()
    # One article have many sections, one section in one article only
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class ImageOrVideo(models.Model):
    content = models.FileField()
    is_video = models.BooleanField(default=False)
    # belongs to one section in an article
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
