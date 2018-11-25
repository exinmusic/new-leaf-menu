var ntracker = [];
(function(){
	$.getJSON( '/json_menu/', function(obj) {
		if (obj.ncount != ntracker) {
			$("#nopheno").empty();
			$.each(obj.nopheno, function(key, value) {
				$("#nopheno").append('<tr><td>'+value[0]+'</td></tr>');
			});
			ntracker.push(obj.sativas);
		}
	});
	setTimeout(arguments.callee, 10000);
})();