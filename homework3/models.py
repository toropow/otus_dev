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
    albumId = fields.ForeignKeyField('models.Albums', related_name='photos')
    id = fields.IntField(pk=True)
    title = fields.TextField()
    url = fields.TextField()
    thumbnailUrl = fields.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(albumId={self.albumId}, id= {self.id}, title={self.title}, url={self.url}, " \
               f"thumbnailUrl= {self.thumbnailUrl})"

    class Meta:
        table = "photos"
