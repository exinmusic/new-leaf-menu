(function() {
	$.getJSON( '/json_menu/', function(obj) {
		$("#nopheno").empty();
		$.each(obj.nopheno, function(key, value) {
			$("#nopheno").append('<tr><td>'+value[0]+'</td></tr>');
		});
		$("#sativas").empty();
		$.each(obj.sativas, function(key, value) {
			$("#sativas").append('<tr><td>'+value[0]+'</td></tr>');
		});
		$("#hybrids").empty();
		$.each(obj.hybrids, function(key, value) {
			$("#hybrids").append('<tr><td>'+value[0]+'</td></tr>');
		});
		$("#indicas").empty();
		$.each(obj.indicas, function(key, value) {
			$("#indicas").append('<tr><td>'+value[0]+'</td></tr>');
		});
	});
	setTimeout(arguments.callee, 15000);
})();

// Submit post on submit
$('#updateStrain').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// csrf token 
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/dash/", // the endpoint
        type : "POST", // http method
        data : { strain_name : $('#strain-name').val(), strain_pheno : $('#updateStrain input[name=strain-pheno]:checked').val() }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            $('#strain-name').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};