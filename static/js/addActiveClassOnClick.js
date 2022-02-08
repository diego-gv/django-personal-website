// not working

$("#home-nav-item").click(function () {
    $('#projects-nav-item').removeClass('active')
    $('#blog-nav-item').removeClass('active')
    $(this).addClass('active');
});

$("#projects-nav-item").click(function () {
    $('#home-nav-item').removeClass('active')
    $('#blog-nav-item').removeClass('active')
    $(this).addClass('active');
});

$("#blog-nav-item").click(function () {
    $('#projects-nav-item').removeClass('active')
    $('#home-nav-item').removeClass('active')
    $(this).addClass('active');
});