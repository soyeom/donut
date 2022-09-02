/* 인기 게시글 롤링 */
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
        $banner.animate({left: - $bannerWidth + "px"}, 2000, function() {
            $(this).append("<li>" + $(this).find("li:first").html() + "</li>");
            $(this).find("li:first").remove();
            $(this).css("left", 0);
        });
    }
});

let state = "{{ state }}";

/* 움직이는 진행바 js*/
if (state == "a")
{
    $(function () {
        $(".progress-bar2").css({
            "width": "25%"
        });
        let animation = document.styleSheets[0].cssRules[0];
        animation.appendRule('100% {width: 25%; background-color: #ef476f;}');
    });
}
else if (state == "b")
{
    $(function () {
        $(".progress-bar2").css({
            "width": "50%"
        });
        let animation = document.styleSheets[0].cssRules[0];
        animation.appendRule('100% {width: 50%; background-color: #ef476f;}');
    });
}
else if (state == "c")
{
    $(function () {
        $(".progress-bar2").css({
            "width": "75%"
        });
        let animation = document.styleSheets[0].cssRules[0];
        animation.appendRule('100% {width: 75%; background-color: #ef476f;}');
    });
}
else
{
    $(function () {
        $(".progress-bar2").css({
            "width": "0%"
        });
        let animation = document.styleSheets[0].cssRules[0];
        animation.appendRule('100% {width: 0%; background-color: #ef476f;}');
    });
}

/* 진행 상황 스크롤 따라 움직이기 */
$(document).ready(function () {
    var currentPosition = parseInt($(".pro_container").css("top"));
    $(window).scroll(function () {
        var position = $(window).scrollTop();
        $(".pro_container").stop().animate({"top":position+currentPosition+"px"});
    });
});