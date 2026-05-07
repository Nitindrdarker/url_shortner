from celery import shared_task
from .models import URL, ClickEvent

@shared_task(bind=True, max_retires = 3)
def log_click(self, short_code, ip, request_id):
    try:

        if ClickEvent.objects.filter(request_id=request_id).exists():
            return
        url = URL.objects.get(short_code=short_code)

        ClickEvent.objects.create(
            url=url,
            ip_address=ip,
            request_id=request_id
        )

    except URL.DoesNotExist:
        print("===============url not exits")
        pass
    except Exception as e:
        raise self.retry(exc=e, countdown = 5)