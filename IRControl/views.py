from django.http import HttpResponse

from subprocess import call


def ir_command(request):
    device = request.GET.get('device', "Insignia")
    command = request.GET.get('command', "KEY_POWER")
    call(["irsend", "send_once", device, command])
    return HttpResponse(status=204)
