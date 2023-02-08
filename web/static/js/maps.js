var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: new google.maps.LatLng(43.263002, -2.935004),
    mapTypeId: google.maps.MapTypeId.ROADMAP
});
function crearMapa(ubicaciones){
    var infowindow = new google.maps.InfoWindow();
    var marker, i;
    ubicaciones.forEach(generarMarkers);
}
function generarMarkers(mk){
    var lat = mk[1];
    var lng = mk[2];
    var contaminacion = mk[3];
    //colores
    var color;
    if (contaminacion < 11) {
        color = "green";
    } else if (contaminacion >= 11 && contaminacion < 25) {
        color = "yellow";
    }else if (contaminacion >= 26 && contaminacion < 50) {
        color = "orange";
    }
    else {
        color = "red";
    }
    // Crear el marcador
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat,lng),
        map: map,
        title: mk[0],
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10,
            fillColor: color,
            fillOpacity: 0.8,
            strokeColor: 'black',
            strokeWeight: 1
        }
      });
      (function(marker) {
        // Añadir evento de clic
        google.maps.event.addListener(marker, 'click', function() {
          infowindow = new google.maps.InfoWindow({
            content: 'Nombre:"'+mk[0]+'",Particulas:'+mk[3]
          });
          infowindow.open(map, marker);
        });
      })(marker);
}