function resetErrors() {
    $("label").removeClass("error");
}

function showErrors(errorFields) {
    errorFields.forEach(function(item) {
        $(`#${item }-label`).addClass("error");
    });
}

function registerUser() {
    var user = {
        login: $("#login").val(),
        firstName: $("#firstName").val(),
        lastName: $("#lastName").val(),
        password: $("#password").val(),
        pesel: $("#pesel").val()
    };

    resetErrors();

    $.ajax({
        url: '/api/users/register',
        type: 'post',
        contentType: 'application/json',
        success: function (data) {
            console.log('data: ', data);

            $('#target').html("<p><b class='ok'>Dane zostały zapisane na serwerze :-)</b></p>");
        },
        error: function(error) {
            console.log("error: ", error.responseJSON);
            console.log('error: ', error.responseJSON.invalid_field_names.split(","));

            $('#target').html("<p><b class='error'>Formularz zawiera błędy!</b></p>");

            let errorFields = error.responseJSON.invalid_field_names.split(",");
            showErrors(errorFields)
        },
        data: JSON.stringify(user)
    });
}

$(document).ready(function() {

    $("#register-user").submit(function(e) {
        e.preventDefault();
        registerUser();
    });
});
