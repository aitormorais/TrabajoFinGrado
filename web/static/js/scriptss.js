$(function(){
     var locations = [
      ['Bondi Beach', -33.890542, 151.274856, 4],
      ['Coogee Beach', -33.923036, 151.259052, 5],
      ['Cronulla Beach', -34.028249, 151.157507, 3],
      ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
      ['Maroubra Beach', -33.950198, 151.259302, 1]
    ];
    
    
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(getCoords,getError);
    }
    else{
        initialize(13.30272,-87.194107);

    }
    function getCoords(position){
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        initialize(lat,lng);
    }
    function getError(err){
        initialize(13.30272,-87.194107);
    }
    function initialize(lat,lng){
        var latlng = new google.maps.LatLng(lat,lng);
        var mapSettings = {
            center: latlng,
            zoom:15,
            mapTypeId : 'roadmap'
        }
        map = new google.maps.Map($('#mapa').get(0),mapSettings);
        var marker = new google.maps.Marker({
            position: latlng,
            map:map,
            draggable:false,
            title:'Arrastra'

        });
        console.log("ssss");
        google.maps.event.addListener(marker,'position_changed',function(){
            console.log("cambia");
            getMarkerCoords(marker);
        });

    }
    function getMarkerCoords(marker){
        var markerCoords = marker.getPosition();
        console.log("hola");
        $('#id_Lat').val(markerCoords.lat());
        $('#id_Lng').val(markerCoords.lng());
    }
});