# views.py

from django.shortcuts import render, get_object_or_404, redirect
import qrcode
from io import BytesIO
from django.http import HttpResponse
from .models import QRData
from .forms import QRDataForm

def generate_qr(request, data_id):
    data = get_object_or_404(QRData, pk=data_id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data.data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer)
    response = HttpResponse(buffer.getvalue(), content_type="image/png")
    return response

def clear_data(request):
    QRData.objects.all().delete()
    return HttpResponse("All QRData objects deleted.")

def index(request):
    if request.method == 'POST':
        form = QRDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QRDataForm()

    data_list = QRData.objects.all()
    return render(request, 'index.html', {'data_list': data_list, 'form': form})
