# coding=utf-8


def get_remote_addr(request):
    addr = request.META.get('REMOTE_ADDR')
    if not addr:
        addr = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[-1:][0].strip()
    return addr
