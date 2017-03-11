/**
 * Created by fshaw on 06/03/2017.
 */
$(document).ready(function () {
    $('.active').removeClass('active')
    $('#batch_link').addClass('active')
    var batch_id = $('#batch_id').val()
    var table_data_url = "/snps/get_samples_in_batch_data/" + batch_id
    var table = $('#example').DataTable({
        "ajax": table_data_url,
        "columns": [
            {
                "className": 'text-center details-control',
                "orderable": false,
                "data": null,
                "defaultContent": '<span class="glyphicon glyphicon-plus"></span>'
            },
            {"data": "name"}

        ],
        "order": [[1, 'asc']]
    });

    // Add event listener for opening and closing details
    $('#example tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
            var td = $(tr).children()[0]
            console.log(td)
            $(td).html("<span class='glyphicon glyphicon-plus'></span>")

        }
        else {
            // Open this row
            expand_row(row)
            tr.addClass('shown');
            var td = $(tr).children()[0]
            console.log(td)
            $(td).html("<span class='glyphicon glyphicon-minus'></span>")

        }
    });
})


function expand_row(d) {
    var img_url = $('#preload_img_url').val()
    var sample_name = d.data().name
    $('#last_sample_clicked').val(sample_name)
    var batch_id = $('#batch_id').val()
    var url = '/snps/get_snps_in_sample/' + batch_id + '/' + sample_name + '/'
    $.ajax({
        "url": url,
        "type": "GET",
        "dataType": 'json'
    }).done(function (data) {
        var table = $('<table class="snps_table"></table>')
        var thead = $('<thead>').append($('<tr>').append($('<th>').html('gene')).append($('<th>').html('rs')).append($('<th>').html('snp')).append($('<th>').html('chromosome')).append($('<th>').html('position')).append($('<th>').html('trait')))
        var tbody = $('<tbody>')
        $(data.snps[0].snps[0].characteristics).each(function (index, element) {
            var line = '<tr class="snp_row"><td class="genename">' + '&nbsp&nbsp' + element.gene + '<img src=' + img_url + '>' + '</td><td class="rs">' + element.rs + '</td><td class="variant">' + element.snp + '</td><td class="chromosome cell_pending">pending...</td><td class="position cell_pending">pending...</td><td class="trait cell_pending">pending...</td></tr>'
            $(tbody).append(line)
        })
        table.append(thead)
        table.append(tbody)
        d.child(table).show()
        lookup_row(table)
    })
}

function lookup_snp(e) {
    var t
    if ('currentTarget' in e) {
        t = $(e.target)
    }
    else{
        t = $(e)
    }
    console.log(this)
    $(t.find('img', this)).css('visibility', 'visible')
    var row = $($(t).closest('tr')[0])

    var snp = $(row).find('.rs').html()
    var variant = $(row).find('.variant').html()
    var sample = $('#last_sample_clicked').val()
    var batch_id = $('#batch_id').val()
    $.ajax({
        url: '/snps/get_snp_data/',
        data: {"snp": snp, "variant": variant, "sample": sample, "batch_id": batch_id},
        dataType: "json",
        type: 'GET'
    }).done(function (d) {
        if('error' in d){
            row.find('.chromosome').attr('colspan', 3).addClass('text-center').html(d.error)
            row.find('.position').remove()
            row.find('.trait').remove()
        }
        // update row info
        row.find('.chromosome').removeClass('cell_pending').html(d.chromosome)
        row.find('.position').removeClass('cell_pending').html(d.position)
        row.find('.trait').removeClass('cell_pending').html(d.trait)
        row.find('img').hide()
        row.addClass('lookup_complete')
    })
}


function lookup_row(table){
    // table is the table just created in the clicked expanded row
    // get the rows which now need to be lookup up in snpedia
    var rows = $(table).find('.snp_row')
    $(rows).each(function(idx, row) {
        lookup_snp(row)
    })
}