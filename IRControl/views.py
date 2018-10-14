from django.http import HttpResponse

from subprocess import call


def ir_command(request):
    device = request.GET.get('device')
    command = request.GET.get('command')
    if device is not None and command is not None:
        call(["irsend", "send_once", "Vizio", "KEY_POWER"])
    return HttpResponse(status=204)
