function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

function showLoading() {
    $('#loadingModal').modal({ backdrop: 'static', keyboard: false });
}

function hideLoading() {
    $('#loadingModal').modal('hide');
}


function ajaxDeteleObject(url, data) {
    $saved_id = data.pk;
    $.ajax(url, {
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        type: 'POST',
        data: data,
        dataType: 'json',
        success: function (data) {
            if (data.err) {
                toastr.error(data.text);
            } else {
                toastr.success(data.text);

                $dt = $('#data_table').DataTable();
                $dt.row('#' + $saved_id).remove().draw(false);
                $('#confirm-delete').modal('hide');
            }

        },
        error: function (jqXhr, textStatus, errorMessage) {
            toastr.error(errorMessage);
        }
    });

};
