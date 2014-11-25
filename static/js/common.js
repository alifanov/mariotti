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

//    $(".contact-form-wrapper button").click(function(){
//        $.fancybox("#thx-msg", {
//            padding: 0,
//            closeBtn: false
//        });
//        return false;
//    });

    $(".contact-form-wrapper form").submit(function(){
        $(".error-alert").hide();
        $(this).find('input[name="email"]').removeClass('error');
        if($(this).find('input[name="name"]').val() == ''){
            $(this).find('input[name="name"]').addClass('error');
            $(".error-alert").show();
            return false;
        }
        if($(this).find('input[name="email"]').val() == ''){
            $(this).find('input[name="email"]').addClass('error');
            $(".error-alert").show();
            return false;
        }
        $.ajax({
            'type': 'POST',
            'url': '/contact/apply/',
            data: $(this).serializeArray(),
            success: function(){
                $.fancybox("#thx-msg", {
                    padding: 0,
                    closeBtn: false
                });
                setTimeout(function(){
                    $.fancybox.hide();
                }, 3000);
            }
        });
        return false;
    });
});