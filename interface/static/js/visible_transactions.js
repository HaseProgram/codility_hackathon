 $(document).ready(function() {

    $('.visible').click(function() {
        console.log('1');
        var aid = $(this).data('aid');
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        if (csrftoken == null)
            csrftoken = Cookies.get('csrftoken'); // read from input csrftoken
        var checked =$(this).prop("checked");
        console.log(csrftoken);
        console.log(aid);
        $.ajax({
            type: 'POST',
            url: '/visible',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            data: JSON.stringify({aid: aid, checked: checked}),
        }).done(function(resp) 
        {
            if (resp.visible) 
            {
                $('#visible'+resp.aid).html("Public");
            } 
            else 
            {
                $('#visible'+resp.aid).html("Private");
            }
        }).fail(function(err) {
            console.log(err);
        });
    });
});
