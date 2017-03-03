from PIL import Image
from PIL.ExifTags import TAGS

def get_GPS(file):
    """
    指定した画像のEXIFデータからGPS_infoを取り出す
    lat: 緯度 -90<=lat<=90, float, 小数点以下6桁
    lon: 経度 -180<=lon<=180, float, 小数点以下6桁
    """
    im = Image.open(file)

    # Exif データを取得
    # 存在しなければそのまま終了 空の辞書を返す
    try:
        exif = im._getexif()
    except AttributeError:
        return {}

    # タグIDそのままでは人が読めないのでデコードして、テーブルに格納する
    exif_table = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    # 緯度latの読み取り。Nを正、Sを負として処理する。
    lat_dir = exif_table['GPSInfo'][1]
    lat = exif_table['GPSInfo'][2]

    if lat_dir[0] == "S":
        sgn = -1
    else:
        sgn = 1

    lat = sgn * (float(lat[0][0]) + float(lat[1][0])/60.0 + float(lat[2][0])/100.0/3600.0)
    lat = float("{:.6f}".format(lat))

    # 経度lonの読み取り。Eを正、Wを負として処理する。
    lon_dir = exif_table['GPSInfo'][3]
    lon = exif_table['GPSInfo'][4]

    if lon_dir[0] == "W":
        sgn = -1
    else:
        sgn = 1
        
    lon = sgn * (float(lon[0][0]) + float(lon[1][0])/60.0 + float(lon[2][0])/100.0/3600.0)
    lon = float("{:.6f}".format(lon))
    return lat, lon

if __name__ == '__main__':
    import glob
    path = r"static/image/*JPG"
    flist = glob.glob(path)
    f = flist[0]
    lat, lon = get_GPS(f)
    print(f)
    print("lat:", lat, "lon:", lon)


