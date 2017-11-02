from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import six
import tagulous.models

class Section(tagulous.models.TagTreeModel):
    class TagMeta:
        initial = [
            'Documentation/Report',
            'Research/Coding',
        ]
        space_delimiter = False
        autocomplete_view = 'log_section_autocomplete'

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(models.ForeignKey(User, on_delete=models.DO_NOTHING))
    date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.CharField(default="", max_length=5000)
    section = tagulous.models.TagField(
        Section, help_text="This field does not split on spaces",
    )
