  $(document).ready(function () {
        // execute
        (function () {
          // map options
          var options = {
            zoom: 5,
            center: new google.maps.LatLng(39.909736, -98.522109), // centered US
            mapTypeId: google.maps.MapTypeId.TERRAIN,
            mapTypeControl: false,
          };

          // init map
          var map = new google.maps.Map(
            document.getElementById('map_canvas'),
            options
          );

          // NY and CA sample Lat / Lng
          var southWest = new google.maps.LatLng(40.744656, -74.005966);
          var northEast = new google.maps.LatLng(34.052234, -118.243685);
          var lngSpan = northEast.lng() - southWest.lng();
          var latSpan = northEast.lat() - southWest.lat();

          // set multiple marker
          for (var i = 0; i < 250; i++) {
            // init markers
            var marker = new google.maps.Marker({
              position: new google.maps.LatLng(
                southWest.lat() + latSpan * Math.random(),
                southWest.lng() + lngSpan * Math.random()
              ),
              map: map,
              title: 'Click Me ' + i,
            });

            // process multiple info windows
            (function (marker, i) {
              // add click event
              google.maps.event.addListener(marker, 'click', function () {
                infowindow = new google.maps.InfoWindow({
                  content: 'Hello, World!!',
                });
                infowindow.open(map, marker);
              });
            })(marker, i);
          }
        })();
      });