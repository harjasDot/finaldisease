from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import breastCancer,diabetes,heart,liver,malaria,pneumonia,kidney

#class breastCancerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 #   ...

#admin.site.register(breastCancer,breastCancerAdmin)
admin.site.register(breastCancer)
admin.site.register(diabetes)
admin.site.register(heart)
admin.site.register(liver)
admin.site.register(malaria)
admin.site.register(pneumonia)
admin.site.register(kidney)