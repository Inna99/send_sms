from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Context:
    """
    behavioral design pattern that lets you define a family of algorithms,
    put each of them into a separate class
    """

    def __init__(self, strategy=None) -> None:
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def send_sms(self) -> dict:
        return self._strategy.sending()

    def __repr__(self):
        return f"{self.send_sms()=}, strategy={self.strategy}"


class Strategy(ABC):
    @abstractmethod
    def sending(self):
        pass


class PlugProvider(Strategy):
    """
    провайдер "заглушка". который не будет ничего делать а просто принимать смс к отправке.
    Этот провайдер не поддерживает возможность узнать доставлена смс или нет.
    """

    def __init__(self, payload):
        self.payload = payload

    def sending(self):
        self.payload["amount_send"] -= 1
        return self.payload


class FileProvider(Strategy):
    """
    провайдер "файл". который вместо отправки будет сохранять тексты смс в папку "sent_sms"
    в виде файлов формата <датавремя в iso формате>_<телефон>.txt
    Если номер телефона четный - смс "доставится" через 10 секунд после отправки.
    Если нечетный - отправка неуспешна.
    """

    def __init__(self, payload):
        self.payload = payload

    def sending(self):
        self.payload["amount_send"] -= 1
        if not int(self.payload["phone_number"][-1]) % 2:
            date_created = datetime.strptime(
                self.payload["date_created"], "%Y-%m-%dT%H:%M:%S%z"
            )
            self.payload["date_created"] = (
                date_created + timedelta(seconds=10)
            ).isoformat()
            with open(
                f"sent_sms/{self.payload['date_created']}_{self.payload['phone_number']}.txt",
                "w",
            ) as f:
                f.write(self.payload["body"])
            self.payload["delivered"] = "sent"
        else:
            self.payload["delivered"] = "not sent"
        return self.payload
