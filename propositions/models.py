import contextlib
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.


class Proposition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pops")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Proposition")
        verbose_name_plural = _("Propositions")

    def __str__(self):
        return self.title


class Upvote(models.Model):
    voter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="upvotes")
    proposition = models.ForeignKey(
        Proposition, on_delete=models.CASCADE, related_name="upvotes")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Upvote")
        verbose_name_plural = _("Upvotes")

    def __str__(self):
        return self.voter.username

    def save(self, *args,  **kwargs):
        try:
            Upvote.objects.get(
                voter=self.voter, proposition=self.proposition)
            jls_extract_var = Exception
            raise jls_extract_var(
                "This user has already upvoted this proposal")
        except Upvote.DoesNotExist:
            super().save(*args, **kwargs)


class Downvote(models.Model):
    voter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="downvotes")
    proposition = models.ForeignKey(
        Proposition, on_delete=models.CASCADE, related_name="downvotes")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Downvote")
        verbose_name_plural = _("Downvotes")

    def __str__(self):
        return self.voter.username

    def save(self, *args,  **kwargs):
        try:
            Downvote.objects.get(
                voter=self.voter, proposition=self.proposition)
            jls_extract_var = Exception
            raise jls_extract_var(
                "This user has already upvoted this proposal")
        except Downvote.DoesNotExist:
            super().save(*args, **kwargs)
