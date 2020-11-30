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
