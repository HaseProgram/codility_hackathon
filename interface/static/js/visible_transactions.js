 $(document).ready(function() {

    $('.set-visible').click(function() {
        var tid = $(this).data('transactionid');
        console.log(tid);
    console.log('1');
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        var checked =$(this).prop("checked");
        if (csrftoken == null)
            csrftoken = Cookies.get('csrftoken'); // read from input csrftoken
        $.ajax({
            type: 'POST',
            url: '/publictransaction/',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken},
            data: JSON.stringify({tid: tid, checked: checked}),
        }).done(function(resp) 
        {
            if (resp.visible) 
            {
                $('#visible'+resp.tid).html("Public");
            } 
            else 
            {
                $('#visible'+resp.tid).html("Private");
            }
        }).fail(function(err) {
            console.log(err);
        });
    });
});
