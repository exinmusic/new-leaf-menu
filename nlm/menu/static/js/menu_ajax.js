var stracker = [];
var htracker = [];
var itracker = [];
(function(){
	$.getJSON( '/json_menu/', function(obj) {
		if (obj.scount != stracker) {
			$("#sativas").empty();
			$.each(obj.sativas, function(key, value) {
				if (value[3] & value[4]) {
					$("#sativas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span> <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else if (value[3]) {
					$("#sativas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span></small>');
				}
				else if (value[4]) {
					$("#sativas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'  <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else {
					$("#sativas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'</small>');	
				}
			});
			stracker.push(obj.sativas);
		}
		if (obj.hcount != htracker) {
			$("#hybrids").empty();
			$.each(obj.hybrids, function(key, value) {
				if (value[3] & value[4]) {
					$("#hybrids").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span> <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else if (value[3]) {
					$("#hybrids").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span></small>');
				}
				else if (value[4]) {
					$("#hybrids").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'  <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else {
					$("#hybrids").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'</small>');	
				}		
			});
			htracker.push(obj.hybrids);
		}
		if (obj.icount != itracker) {
			$("#indicas").empty();
			$.each(obj.indicas, function(key, value) {
				if (value[3] & value[4]) {
					$("#indicas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span> <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else if (value[3]) {
					$("#indicas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | <span class="text-white">CBD: '+value[2]+'</span>  <span class="badge badge-pill badge-info">CBD</span></small>');
				}
				else if (value[4]) {
					$("#indicas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'  <span class="badge badge-pill badge-danger">staff pick</span></small>');
				}
				else {
					$("#indicas").append('<p class="mb-0 text-white lh-100">'+value[0]+'</p><small class="mb-0 text-white-50 lh-100">THC: '+value[1]+' | CBD: '+value[2]+'</small>');	
				}		
			});
			itracker.push(obj.indicas);
		}
	});
	setTimeout(arguments.callee, 10000);
})();