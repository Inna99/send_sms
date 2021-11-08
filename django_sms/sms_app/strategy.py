from abc import ABC, abstractmethod


class Order:
    def __init__(self, strategy=None) -> None:
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def send_sms(self) -> None:
        success = self._strategy.sending()
        return success

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
        return None


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
        if not int(self.payload["phone_number"][-1]) % 2:
            with open(
                f"sent_sms/{self.payload['date_created']}_{self.payload['phone_number']}.txt",
                "w",
            ) as f:
                f.write(self.payload["body"])
            return True
        else:
            return False
