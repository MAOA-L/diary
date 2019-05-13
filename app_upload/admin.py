# from django.contrib import admin
# from .models import Sort, Label, Article
#
#
# @admin.register(Sort)
# class SortAdmin(admin.ModelAdmin):
#     list_display = ('sort_feature', 'sort_name')
#
#
# @admin.register(Label)
# class SortAdmin(admin.ModelAdmin):
#     list_display = ('label_feature', 'label_name')
#
#
# @admin.register(Article)
# class SortAdmin(admin.ModelAdmin):
#     list_display = ('article_feature', 'article_title', 'article_sort',
#                     'article_label', 'article_theory', 'article_html_short')
#
#     readonly_fields = ('article_feature', 'article_time', 'article_see')
#     fieldsets = [
#         ("概览", {"fields": ("article_feature", "article_time", "article_see")}),
#         ("文章", {"fields": ("article_sort", "article_label", "article_html")})
#     ]
#
#     def article_html_short(self, obj):
#         if len(obj.article_html) > 20:
#             return obj.article_html[:20]
#         else:
#             return obj.article_html
#     article_html_short.short_description = '文章内容'
#     # 届时将文章内容中文提取出来作为展示
# import xadmin
#
# from app_upload.models import Article
#
#
# class ArticleAdmin:
#     list_display = ('title', 'sort')
#     model_icon = 'fa fa-skype'
#
#
# xadmin.site.register(Article, ArticleAdmin)