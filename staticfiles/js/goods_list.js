
$(document).ready(function() {
    var $banner = $(".banner").find("ul");

    var $bannerWidth = $banner.children().outerWidth();
    var $bannerHeight = $banner.children().outerHeight();
    var $bannerLength = $banner.children().length;
    var rollingId;

    rollingId = setInterval(function() { rollingStart(); });

    function rollingStart() {
        $banner.css("width", $bannerWidth * $bannerLength + "px");
        $banner.css("height", $bannerHeight + "px");
        $banner.animate({left: - $bannerWidth + "px"}, 1500, function() {
            $(this).append("<li>" + $(this).find("li:first").html() + "</li>");
            $(this).find("li:first").remove();
            $(this).css("left", 1);
        });
    }
});


<!-- 팝업창 띄우기 js -->

window.onload = function () {
    function onClick() {
        document.querySelector('.modal_wrap').style.display = 'block';
        document.querySelector('.black_bg').style.display = 'block';
    }
    function offClick() {
        document.querySelector('.modal_wrap').style.display = 'none';
        document.querySelector('.black_bg').style.display = 'none';
    }
    document.getElementById('modal_btn').addEventListener('click', onClick);
    document.querySelector('.modal_close').addEventListener('click', offClick);
};

<!-- 맨 위로 이동 하는 버튼-->
$('#top').click(function () {
    $('html, body').animate({scrollTop:0}, 'slow');
});