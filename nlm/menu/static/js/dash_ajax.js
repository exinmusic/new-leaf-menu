(function(){
	$.getJSON( '/json_menu/', function(obj) {
		$("#nopheno").empty();
		$.each(obj.nopheno, function(key, value) {
			$("#nopheno").append('<tr><td>'+value[0]+'</td></tr>');
		});
	});
	setTimeout(arguments.callee, 15000);
})();