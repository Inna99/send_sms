import logging

from .strategy import Context, FileProvider, PlugProvider


def send(payload):
    with open("sms.txt", "w") as f:
        f.write(str(payload))
    print(payload)


def some_func(payload):
    """
    * если отправка смс неуспешна, происходит автоматический повтор отправки, максимум попыток определяется для каждого
     провайдера отдельно. (для сохранения в файлы = 3, для заглушки = 1).
    промежуток между повторами определяется для каждого провайдера отдельно (по умолчанию 0.5 у каждого)
    * время ожидания ответа от сервера на любой запрос не должно превышать 1 секунды.
    """
    if "provider" in payload:
        provider = payload["provider"]
        if provider == "plug" or provider == "":
            Context(PlugProvider(payload))
            return None
        elif provider == "file":
            for _ in range(3):
                sms = Context(FileProvider(payload))
                success = sms.send_sms()
                if success:
                    return success
            return success
        else:
            logging.Logger("there is no such provider")


if __name__ == "__main__":  # pragma: no cover
    payload = {
        "uuid": 11,
        "body": "string",
        "provider": "file",
        "phone_number": "89516783430",
        "date_created": "2021-11-07",
    }

    print(some_func(payload))
