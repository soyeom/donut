var mapContainer = document.getElementById('map'),
    mapOption = {
        center: new kakao.maps.LatLng(36.5952730081064, 127.301825498491), // 지도의 중심 좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption);


var positions = [

    {
        content: '<div class="wrap">' +
            '    <div class="info">' +
            '        <div class="title">' +
            '            고려대학교 세종사회봉사단' +
            '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
            '        </div>' +
            '        <div class="body">' +
            '            <div class="img">' +
            '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
            '           </div>' +
            '            <div class="desc">' +
            '                <div class="ellipsis">조치원읍 서창리 208</div>' +
            '                <div class="jibun ellipsis">(우) 30019 (지번) 세종로 2511</div>' +
            '                <div><a href="https://sejong.korea.ac.kr/user/boardList.do?handle=108936&siteId=share&id=share_030100000000" target="_blank" class="link">홈페이지</a></div>' +
            '            </div>' +
            '        </div>' +
            '    </div>' +
            '</div>',
        latlng : new kakao.maps.LatLng(36.61109945, 127.2871618)
    },
    {
        content : '<div class="wrap">' +
        '    <div class="info">' +
        '        <div class="title">' +
        '            사회복지법인 세종중앙' +
        '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
        '        </div>' +
        '        <div class="body">' +
        '            <div class="img">' +
        '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
        '           </div>' +
        '            <div class="desc">' +
        '                <div class="ellipsis">조치원읍 남리 358</div>' +
        '                <div class="jibun ellipsis">(우) 30035 (지번) 장안길 97-7</div>' +
        '                <div><a href="http://sejongchungang.or.kr/" target="_blank" class="link">홈페이지</a></div>' +
        '            </div>' +
        '        </div>' +
        '    </div>' +
        '</div>',
        latlng : new kakao.maps.LatLng(36.5963902176803, 127.301015424638)
    },
    {
        content : '<div class="wrap">' +
        '    <div class="info">' +
        '        <div class="title">' +
        '            세종 YWCA' +
        '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
        '        </div>' +
        '        <div class="body">' +
        '            <div class="img">' +
        '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
        '           </div>' +
        '            <div class="desc">' +
        '                <div class="ellipsis">조치원읍 교리 22-6</div>' +
        '                <div class="jibun ellipsis">(우) 30024 (지번) 새내12길 35</div>' +
        '                <div><a href="http://www.iywca.com/" target="_blank" class="link">홈페이지</a></div>' +
        '            </div>' +
        '        </div>' +
        '    </div>' +
        '</div>',
        latlng : new kakao.maps.LatLng(36.6027956854572, 127.299876549653)
    },
    {
       content : '<div class="wrap">' +
        '    <div class="info">' +
        '        <div class="title">' +
        '            세종특별자치시 사회복지협의회' +
        '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
        '        </div>' +
        '        <div class="body">' +
        '            <div class="img">' +
        '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
        '           </div>' +
        '            <div class="desc">' +
        '                <div class="ellipsis">조치원읍 신안리 35-20</div>' +
        '                <div class="jibun ellipsis">(우) 30016 (지번) 세종로 2567</div>' +
        '                <div><a href="http://m.sjcsw.or.kr/" target="_blank" class="link">홈페이지</a></div>' +
        '            </div>' +
        '        </div>' +
        '    </div>' +
        '</div>',
        latlng : new kakao.maps.LatLng(36.6154437181143, 127.292399665348)
    },
    {
        content : '<div class="wrap">' +
        '    <div class="info">' +
        '        <div class="title">' +
        '            세종특별자치시 자원봉사 센터' +
        '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
        '        </div>' +
        '        <div class="body">' +
        '            <div class="img">' +
        '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
        '           </div>' +
        '            <div class="desc">' +
        '                <div class="ellipsis">종촌동 674</div>' +
        '                <div class="jibun ellipsis">(우) 30064 (지번) 도움1로 116</div>' +
        '                <div><a href="http://www.sjvc1365.or.kr/" target="_blank" class="link">홈페이지</a></div>' +
        '            </div>' +
        '        </div>' +
        '    </div>' +
        '</div>',
        latlng : new kakao.maps.LatLng(36.5952730081064, 127.301825498491)
    }
];

for (var i=0; i<positions.length; i++){
    var marker = new kakao.maps.Marker({
        map: map,
        position: positions[i].latlng
    });

    var overlay = new kakao.maps.CustomOverlay({
        content: positions[i].content,
        map: map,
        position: marker.getPosition()
    });

    kakao.maps.event.addListener(marker, 'click', function () {
        overlay.setMap(map);
    });
    function closeOverlay(){
        overlay.setMap(null);
    }
}


//var marker1 = new kakao.maps.Marker({
//    map: map,
//    position: positions[0].latlng
//});
//
//var overlay1 = new kakao.maps.CustomOverlay({
//    content: positions[0].content,
//    map: map,
//    position: marker.getPosition()
//});
//
// kakao.maps.event.addListener(marker, 'click', function() {
//        overlay1.setMap(map);
// });
//
// function closeOverlay(){
//    overlay1.setMap(null);
// }
//



//var marker2 = new kakao.maps.Marker({
//    map: map,
//    position: positions[1].latlng
//});
//
//var overlay2 = new kakao.maps.CustomOverlay({
//    content: positions[1].content,
//    map: map,
//    position: marker.getPosition()
//});
//
// kakao.maps.event.addListener(marker, 'click', function() {
//        overlay2.setMap(map);
// });
//
// function closeOverlay(){
//    overlay2.setMap(null);
// }

