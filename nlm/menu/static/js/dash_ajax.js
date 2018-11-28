(function(){
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