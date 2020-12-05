$(function() {
    var $list, $newItemForm;
    $list = $('#ulForm');
    $newItemForm = $('#newItemForm');

    $newItemForm.on('submit', function(e) {
        e.preventDefault();
        var text = $('input:text').val();
        var question = $('#itemField').val();
		$.ajax({
			url: '/Coord',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
        $list.append('<li class="itemForm">'+ text + '</li>');
        $('input:text').val('');
    });
});


let map;

function initMap() {
    var myLatLng = { lat: 48.8975156, lng: 2.3833993 };
    map = new google.maps.Map(document.getElementById("map"), {
        center: myLatLng,
        zoom: 15,
    });
    const contentString = "OpenClassrooms!"

    const infowindow = new google.maps.InfoWindow({
    content: contentString,
    });
    const marker = new google.maps.Marker({
    position: myLatLng,
    map,
    title: "hello world",
    });
    marker.addListener("click", () => {
    infowindow.open(map, marker);
    });
}
//
//$(function(){
//    var $newItemForm = $('#newItemForm');
//	$newItemForm.on('submit',function(){
//		var question = $('#itemField').val();
//		$.ajax({
//			url: '/Coord',
//			data: $('form').serialize(),
//			type: 'POST',
//			success: function(response){
//				console.log(response);
//			},
//			error: function(error){
//				console.log(error);
//			}
//		});
//	});
//});

