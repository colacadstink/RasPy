from django.http import HttpResponse

import serial


def input_switch(request):
    input = request.GET.get('input', "+")

    with serial.Serial('/dev/ttyUSB0', 19200) as ser:
        ser.write(b'sw '+bytes(input)+b'\n')

    return HttpResponse(status=204)
