#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

import bottle
from bottle import static_file
from bottle import route, get, post, run
from bottle import request, template, redirect
from bottle import HTTPError
from sqlalchemy import create_engine, Column, Integer, Unicode, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

from bottle.ext import sqlalchemy

from wtforms.form import Form
from wtforms import validators
from wtforms import StringField, IntegerField, TextAreaField, FileField

from PIL import Image
from PIL.ExifTags import TAGS

from app_tools import get_GPS

Base = declarative_base()

# メモリ上でDBのデータを管理する
# engine = create_engine('sqlite:///:memory:', echo=True)
# 特定のファイルでDBのデータを管理する
engine = create_engine('sqlite:///images.sqlite', echo=True)

# bottle-sqlalchemyの設定
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',  # 関数内で挿入される場合の変数名
    create=True,  # テーブルを作成するか
    commit=True,  # 関数終了時にコミットするか
    use_kwargs=False
)

# プラグインのインストール
bottle.install(plugin)

# Imageクラスの定義
class Image(Base):
    # imagesテーブル
    __tablename__ = 'images'

    # カラムの定義
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    file = Column(Unicode(100), nullable=False)
    lat = Column(Unicode(100))
    lon = Column(Unicode(100))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Image('%s','%s','%s','%s','%s')>" % (self.title, self.file, self.lat, self.lon, self.created_at)

# ImageFormクラスの定義：入力フォームのオブジェクト
class ImageForm(Form):
    title = StringField(u'タイトル', [
        validators.required(message=u"入力してください"),
        validators.length(min=1, max=100, message=u"100文字以下で入力してください")
    ])
    file = StringField(u'ファイル名', [
        validators.required(message=u"入力してください"),
        validators.length(min=1, max=100, message=u"100文字以下で入力してください")
    ])


# 画像リスト内のImageインスタンスの緯度(lat), 経度(lon), タイトル(title)をファイル出力する
import codecs

def geodump(images):
    fhand = codecs.open('static/locations.js','w', "utf-8")
    fhand.write("locations = [\n")
    count = 0
    sum_lat = 0
    sum_lon = 0
    for image in images:
        lat = image.lat
        lon = image.lon
        title = image.title

        try :
            print(title, lat, lon)

            count = count + 1
            if count > 1 : fhand.write(",\n")
            output = "["+str(lat)+","+str(lon)+", '"+title+"']"
            fhand.write(output)
            lat = float(lat)
            lon = float(lon)
            sum_lat = sum_lat + lat 
            sum_lon = sum_lon + lon
        except:
            continue

    fhand.write("\n];\n")
    if count > 0:
        fhand.write("center = [")
        ctr_lat = float(sum_lat/count)
        ctr_lat = float("{:.6f}".format(ctr_lat))
        ctr_lon = float(sum_lon/count)
        ctr_lon = float("{:.6f}".format(ctr_lon))
        output = str(ctr_lat)+","+str(ctr_lon)+"];"
        print("Center:", ctr_lat, ctr_lon)
        fhand.write(output)
        fhand.write("\n")
    fhand.close()

@route('/static/<file_path:path>')
def static(file_path):
    """
    静的ファイル専用のルーティング
    /static/* は静的ファイルが存在するものとして動く
    :param file_path:
    :return:
    """
    return static_file(file_path, root="./static")

@get('/images')
def index(db):
    # imagesテーブルから全件取得
    images = db.query(Image).all()

    # index.tplの描画
    return template('index', images=images, request=request)

@get('/images/add')
def new(db):
    form = ImageForm()

    # add.tplの描画
    return template('edit', form=form, request=request)

@post('/images/add')
def create(db):
    form = ImageForm(request.forms.decode())

    # フォームのバリデーション
    if form.validate():

        # Imageインスタンスの作成
        image = Image(
            title=form.title.data,
            file=form.file.data,
        )

        path = os.path.join(os.getcwd(),"static/image",image.file)
        image.lat, image.lon = get_GPS(path)

        # imageを保存
        db.add(image)

        # 一覧画面へリダイレクト
        redirect("/images")
    else:
        return template('edit', form=form, request=request)

@get('/images/<id:int>/edit')
def edit(db, id):
    # imageの検索
    image = db.query(Image).get(id)

    # Imageが存在しない(404を表示）
    if not image:
        return HTTPError(404, 'Image is not found.')

    # フォームを作成
    form = ImageForm(request.POST, image)

    # edit.tplを描画
    return template('edit', image=image, form=form, request=request)


@post('/images/<id:int>/edit')
def update(db, id):
    # Imageの検索
    image = db.query(Image).get(id)

    # Imageが存在しない(404を表示）
    if not image:
        return HTTPError(404, 'Image is not found.')

    form = ImageForm(request.forms.decode())

    if form.validate():
        # image情報を更新
        image.title = form.title.data
        image.file = form.file.data
        path = os.path.join(os.getcwd(),"static/image",image.file)
        image.lat, image.lon = get_GPS(path)

        # 一覧画面へリダイレクト
        redirect("/images")
    else:
        return template('edit', form=form, request=request)


@post('/images/<id:int>/delete')
def destroy(db, id):
    # Imageの検索
    image = db.query(Image).get(id)

    # Imageが存在しない(404を表示）
    if not image:
        return HTTPError(404, 'Image is not found.')

    # imageを削除
    db.delete(image)

    # 一覧画面へリダイレクト
    redirect("/images")

@get('/images/map')
def map(db):
    # map.tplの描画
    # imagesテーブルから全件取得
    images = db.query(Image).all()
    geodump(images)
    return template('map', request=request)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
