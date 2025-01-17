from dataclasses import dataclass
from abc import abstractmethod
import logging

@dataclass
class BaseClass:
    name: str
    size: int
    created_at: str
    owner: str

    @abstractmethod
    def save(self, name):
        logging.info(f'Сохраняет файл {self.name} в указанном хранилище.')
        """Сохраняет файл в указанном хранилище."""
        pass

    @abstractmethod
    def update_metadata(self, new_data: dict):
        print(f'Обновляет метаданные файла {self.name}.')
        """Обновляет метаданные файла."""
        pass

    @abstractmethod
    def delete(self, name):
        print(f'Удаляет файл {name} из хранилища.')
        """Удаляет файл из указанного хранилища."""
        pass

    @abstractmethod
    def extract_features(self) -> dict:
        return self.__dict__

    @abstractmethod
    def convert_to_format(self, target_format: str):
        print(f'Конвертирует файл в {target_format}.')

class AudioFile(BaseClass):
    pass

class VideoFile(BaseClass):
    pass

class PhotosFile(BaseClass):
    pass


audio = AudioFile("audio_file.mp3", 222, "2020-01-01 00:00:00", "owner")


audio.save("audio_file.mp3")
