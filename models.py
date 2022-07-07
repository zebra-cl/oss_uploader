import os
from datetime import datetime

import peewee

db = peewee.SqliteDatabase(f"{os.environ['APPDATA']}/oss_uploader.db")


class Config(peewee.Model):
    name = peewee.CharField(primary_key=True)
    value = peewee.CharField()

    class Meta:
        database = db
        table_name = 'config'

    @staticmethod
    def get_conf(name) -> str:
        # 获取配置项
        try:
            conf = Config.get(Config.name == name)
        except peewee.DoesNotExist:
            return ''
        else:
            return conf.value

    @staticmethod
    def set_conf(name, value):
        # 设置配置项
        Config.insert(
            name=name, value=value
        ).on_conflict(
            conflict_target=[Config.name],
            update={Config.value: value}).execute()


class UploadHistory(peewee.Model):
    file = peewee.CharField()
    file_url = peewee.CharField()
    create_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'upload_history'


db.create_tables([Config, UploadHistory])
