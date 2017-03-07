/**
 * Created by fshaw on 18/02/2017.
 */

$(document).ready(function () {
    $(document).ready(function () {
        $('.active').removeClass('active')
        $('#index_link').addClass('active')
        table = $('#files_table').DataTable();
    })
    $('table button').on('click', handle_table_btn_press)
    $('.genename img').hide()
    $('table').on('click', lookup_snp)
}).ajaxSend(function (event, jqxhr, settings) {
    console.log('ajax send')
    console.log(event.target)
});

function handle_table_btn_press(e) {
    var el = e.currentTarget
    var method = $(el).data('target')
    if (method == '#view') {
        var data = get_batch_data($(el).data('batch_id'))
    }
    else if (method == '#delete') {
        //console.log('delete: ' + $(el).data('batch_id'))
    }
}

function get_batch_data(batch_id) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        "url": "/snps/get_batch_data",
        "data": {'batch_id': batch_id},
        "headers": {'X-CSRFToken': csrftoken},
        "type": "POST",
        "dataType": 'json'
    }).done(function (data) {
        table.clear().draw()
    })
}


