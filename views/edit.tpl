% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">

    % if request.path == "/images/add":
        <h1 class="page-header">登録</h1>
    % else:
        <h1 class="page-header">編集</h1>
    % end

    <div class="col-md-5">

        % if request.path == "/images/add":
            <form action="/images/add" method="post">
        % else:
            <form action="/images/{{image.id}}/edit" method="post">
        % end

        <div class="form-group">
            {{ !form.title.label }}
            {{ !form.title(class_="form-control", placeholder=u"タイトルを入力", maxlength="100") }}

           % if form.title.errors:
                <div class="errors">
                % for error in form.title.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        <div class="form-group">
            {{ !form.file.label }}
            {{ !form.file(class_="form-control", placeholder=u"ファイル名を入力", maxlength="100") }}

           % if form.file.errors:
                <div class="errors">
                % for error in form.file.errors:
                    <p class="text-danger">{{ error }}</p>
                % end
                </div>
            % end

        </div>

        % if request.path == "/images/add":
            <input type="submit" class="btn btn-default" value="作成する"/>
        % else:
            <input type="submit" class="btn btn-default" value="更新する"/>
        % end

        </form>
    </div>
</div>