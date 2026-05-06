from celery import shared_task
from .models import URL, ClickEvent

@shared_task
def log_click(short_code, ip):
    try:
        url = URL.objects.get(short_code=short_code)

        ClickEvent.objects.create(
            url=url,
            ip_address=ip
        )

    except URL.DoesNotExist:
        print("===============url not exits")
        pass
    except Exception as e:
        print("e===============", e)