from tortoise import Model, fields

MAX_VERSION_LENGTH = 255


class Aerich(Model):
    version = fields.CharField(max_length=MAX_VERSION_LENGTH)
    app = fields.CharField(max_length=20)
    content = fields.TextField()

    class Meta:
        ordering = ["-id"]

from tortoise.models import Model
from tortoise import fields


class Albums(Model):
    userId = fields.IntField(null=False)
    id = fields.IntField(pk=True)
    title = fields.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(userId={self.userId}, id= {self.id}, title={self.title})"

    class Meta:
        table = "albums"


class Photos(Model):
    albumId = fields.ForeignKeyField('diff_models.Albums', related_name='photos')
    id = fields.IntField(pk=True)
    title = fields.TextField()
    url = fields.CharField(max_length=255)
    thumbnailUrl = fields.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(albumId={self.albumId}, id= {self.id}, title={self.title}, url={self.url}, " \
               f"thumbnailUrl= {self.thumbnailUrl})"

    class Meta:
        table = "photos"

