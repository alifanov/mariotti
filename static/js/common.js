/**
 * Created by vampire on 13.11.14.
 */
$(function(){
    $(".gallery").owlCarousel({
        items:1,
        loop: false,
        dots: true
    });

    $(".text-body").mCustomScrollbar({
        setHeight: 200,
        scrollInertia: 0
    });

    $(".fancybox").fancybox();

    $(".contact-form-wrapper form").submit(function(){
        $(".error-alert").hide();
        $(this).find('input[name="name"]').removeClass('error');
        $(this).find('input[name="email"]').removeClass('error');
        if($(this).find('input[name="name"]').val() == ''){
            $(this).find('input[name="name"]').addClass('error');
            $(".error-alert").css('display', 'inline-block');
            return false;
        }
        if($(this).find('input[name="email"]').val() == ''){
            $(this).find('input[name="email"]').addClass('error');
            $(".error-alert").css('display', 'inline-block');
            return false;
        }
        $.ajax({
            'type': 'POST',
            'url': '/contacts/apply/',
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