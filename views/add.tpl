% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">登録</h1>

    <div class="col-md-5">

        <form action="/images/add" method="post">

            <div class="form-group">
                <label for="title">タイトル</label>
                <input id="title" name="title" type="text" class="form-control" maxlength="100" placeholder="タイトルを入力">
            </div>

            <div class="form-group">
                <label for="file">ファイル名</label>
                <input id="file" name="file" type="text" class="form-control" maxlength="10" placeholder="ファイル名を入力">
            </div>

            <input type="submit" class="btn btn-default" value="登録する"/>

        </form>
    </div>
</div>