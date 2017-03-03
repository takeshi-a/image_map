% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">地図</h1>
    <div class="col-md-5">
        <div id="map"></div>
        <script src="/static/locations.js"></script>
        <script>
          function initMap() {
            // 画像リストの位置中心を記録する
            var myLatLng = {lat: center[0], lng: center[1]};

            // 東京駅を中心とするマップを作成する
            var map = new google.maps.Map(document.getElementById('map'), {
              center: myLatLng,
              scrollwheel: false,
              zoom: 11
            });

            // locations.jsから位置情報を読み取り、マーカーを作成する
            for (pos in locations) {
                var row = locations[pos];
                var newLatlng = new google.maps.LatLng(row[0], row[1]);
                var marker = new google.maps.Marker({
                    position: newLatlng,
                    map: map,
                    title: row[2]
                });
            }
          }
        </script>
        <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
            async defer></script>
    </div>
</div>