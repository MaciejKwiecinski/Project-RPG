$(document).ready(function () {
    var menuVisible = $('.menu-visible');
    var menuHidden = $('.menu-hidden');

    menuVisible.mouseenter(function () {
        menuVisible.css('display', 'none');
        //menuHidden.css('display', 'block');
        menuHidden.fadeIn('slow');
    });

    menuHidden.mouseleave(function () {
        menuHidden.fadeOut('slow');
        menuVisible.fadeIn('slow')
        //menuHidden.css('display', 'none');
        menuVisible.css('display', 'block');
    });

    var menuVisible1 = $('.menu-visible1');
    var menuHidden1 = $('.menu-hidden1');

    menuVisible1.mouseenter(function () {
        menuVisible1.css('display', 'none');
        //menuHidden.css('display', 'block');
        menuHidden1.fadeIn('slow');
    });

    menuHidden1.mouseleave(function () {
        menuHidden1.fadeOut('slow');
        menuVisible1.fadeOut('slow');
        //menuHidden.css('display', 'none');
        menuVisible1.css('display', 'block');
    });
    var timeout = setTimeout(function () {
    $('#theme').css('display','none')
}, 3000);
});
