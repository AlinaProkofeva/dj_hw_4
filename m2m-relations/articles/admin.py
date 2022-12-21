from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            dict_ = form.cleaned_data
            if dict_['is_main'] == True:
                counter += 1

        if counter == 0:
            raise ValidationError('Укажите основной раздел')
        if counter > 1:
            raise ValidationError('основным может быть только один раздел')

        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

