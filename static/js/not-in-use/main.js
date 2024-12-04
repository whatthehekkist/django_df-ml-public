$(document).ready(function () {
  $("navbar navbar-nav ul li").on("click", function () {
    $("li").removeClass("active");
    $(this).addClass("active");
  });

});