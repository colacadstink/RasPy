from django.http import HttpResponse

from envs import env

from wakeonlan import send_magic_packet


MAC_TABLE = env('MAC_TABLE', default={}, var_type='dict')

def wake(request):
    device = request.GET.get('device')
    if device is not None:
        mac = MAC_TABLE.get(device)
        if mac is not None:
            send_magic_packet(mac)
    return HttpResponse(status=204)
