from tortoise.models import Model
from tortoise import fields


class Album(Model):
    user_id = fields.IntField(null=False)
    id = fields.IntField(pk=True)
    title = fields.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(userId={self.user_id}, id= {self.id}, title={self.title})"

    class Meta:
        table = "albums"


class Photo(Model):
    album_id = fields.ForeignKeyField('models.Album', related_name='photos')
    id = fields.IntField(pk=True)
    title = fields.TextField()
    url = fields.TextField()
    thumbnail_url = fields.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(albumId={self.album_id}, id= {self.id}, title={self.title}, url={self.url}, " \
               f"thumbnailUrl= {self.thumbnail_url})"

    class Meta:
        table = "photos"


class TestMigration(Model):
    some_field = fields.IntField(null=True)
    id = fields.IntField(pk=True)
    text = fields.TextField(null=True)

    class Meta:
        table = "test_my"

