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
			    if (!('error' in response)) {
			        $('.map').attr('id', 'map');
                    initMap(response['latlng'], response['address']);
                    $list.append('<li class="itemForm" id="grandpy"> Bien sûr mon trésor, voici l\'adresse de ' + response['place'] + " : " + response['address'] + '</li>');
                    $list.append('<li class="itemForm" id="grandpy"> Savais-tu que : '+ response['history'] + '</li>');
			    } else if (response['error'] == "no history"){
			        $('.map').attr('id', 'map');
                    initMap(response['latlng'], response['address']);
                    $list.append('<li class="itemForm" id="grandpy"> Bien sûr mon trésor, voici l\'adresse de ' + response['place'] + " : " + response['address'] + '</li>');
			        $list.append('<li class="itemForm" id="grandpy"> Désolé mon poussin, impossible de trouver un historique de ce lieu.</li>');
			    } else if (response['error'] == "no pageid"){
			        $('.map').attr('id', 'map');
                    initMap(response['latlng'], response['address']);
                    $list.append('<li class="itemForm" id="grandpy"> Bien sûr mon trésor, voici l\'adresse de ' + response['place'] + " : " + response['address'] + '</li>');
			        $list.append('<li class="itemForm" id="grandpy"> Désolé mon poussin, impossible de trouver une page Wikipedia de ce lieu.</li>');
			    } else if (response['error'] == "no lat-lng"){
			        $list.append('<li class="itemForm" id="grandpy"> Désolé mon poussin, impossible de trouver ce lieu sur la carte.</li>');
			    } else if (response['error'] == "no place"){
			        $list.append('<li class="itemForm" id="grandpy"> Désolé mon poussin, je ne comprends pas ta question.</li>');
			    } else {
			        $list.append('<li class="itemForm" id="grandpy"> Désolé mon poussin mais peux-tu parler français?</li>');
			    };

			},
			error: function(error){
				$('.alert').attr('id', 'error');
			}
		});
        $list.append('<li class="itemForm" id="me">'+ text + '</li>');
        $('input:text').val('');
    });
});

let map;
function initMap(myLatLng, address) {
    if (myLatLng === undefined) {
        return;
    };
    map = new google.maps.Map(document.getElementById("map"), {
        center: myLatLng,
        zoom: 15,
    });
    const contentString = address

    const infowindow = new google.maps.InfoWindow({
    content: contentString,
    });
    const marker = new google.maps.Marker({
    position: myLatLng,
    map,
    });
    marker.addListener("click", () => {
    infowindow.open(map, marker);
    });
};
