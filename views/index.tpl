% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">画像一覧</h1>

    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>タイトル</th>
                <th>ファイル名</th>
                <th>画像</th>
                <th>緯度</th>
                <th>経度</th>
                <th></th>
            </tr>
            </thead>
            <tbody>

            % for image in images:
            <tr>
                <td>{{image.id}}</td>
                <td><a href="/images/{{image.id}}/edit">{{image.title}}</a></td>
                <td>{{image.file}}</td>
                <td><img src="/static/image/{{image.file}}" alt="Sample" height="100"></td>
                <td>{{image.lat}}</td>
                <td>{{image.lon}}</td>
                <td>
                    <form action="/images/{{image.id}}/delete" method="post">
                        <p><input value="削除する" type="submit"/></p>
                    </form>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>