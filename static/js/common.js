/**
 * Created by vampire on 13.11.14.
 */
$(function(){
    $(".gallery").owlCarousel({
        items:1,
        loop: true,
        dots: true
    });

    $(".text-body").mCustomScrollbar({
        setHeight: 200,
        scrollInertia: 0
    });

    $(".contact-form-wrapper").click(function(){
        $("#thx-msg").fancybox('open');
        return false;
    });
});