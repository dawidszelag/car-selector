from django.contrib.admin.views.decorators import staff_member_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render

from core.tasks import set_info_object, add_cars_data_to_database, add_cars_parameters_data_to_database

from core.models import UploadDataInfo


@staff_member_required
def import_data(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('data_file', None)
        fs = FileSystemStorage()
        filename = fs.save(upload_file.name, upload_file)  # saves the file to `media` folder
        file_path = fs.path(filename)
        if request.POST.get('type') == 'cars':
            add_cars_data_to_database.delay(file_path)
        elif request.POST.get('type') == 'parameters':
            add_cars_parameters_data_to_database.delay(file_path)
        set_info_object(lenght=1, current=0, message='Reading file...', status=2)
    return render(request, 'admin/data_importer.html')


@staff_member_required
def ajax_check_upload_data_status(request):
    upload_info, _ = UploadDataInfo.objects.get_or_create(pk=1)
    data = {
        'all_items': upload_info.all_items,
        'current_item': upload_info.current_item,
        'message': upload_info.message,
        'status': upload_info.status
    }
    return JsonResponse(data)
