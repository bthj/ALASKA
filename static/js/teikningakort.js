var map;
var infoWindow;
var lurkur = {
	url: staticUrlPrefix+"images/lurkur_lodrettur_x80.png",
	size: new google.maps.Size(20.0, 80.0), 
	origin: new google.maps.Point(0, 0),
	anchor: new google.maps.Point(10.0, 80.0)
};
var lurkurHalffullur = {
	url: staticUrlPrefix+"images/lurkur_lodrettur_halffullur_x80.png",
	size: new google.maps.Size(20.0, 80.0), 
	origin: new google.maps.Point(0, 0),
	anchor: new google.maps.Point(10.0, 80.0)
};
var shadow = {
	url: staticUrlPrefix+"images/shadow-lurkur_lodrettur_x80.png",
	size: new google.maps.Size(61.0, 80.0), 
	origin: new google.maps.Point(0, 0),
	anchor: new google.maps.Point(10.0, 80.0)
};

function openInfoWindow( marker ) {
	if( infoWindow ) {
		infoWindow.close();
	}
	infoWindow = new google.maps.InfoWindow({
        content: marker.infoWindowContent,
        pixelOffset: new google.maps.Size(0, 80)
    });
	infoWindow.open(map, marker);
}
function addLurkMarker(placemark) {
	if( placemark.styleUrl == '#withoutScansIcon' ) {
		var icon = lurkurHalffullur;
	} else {
		var icon = lurkur;
	}
	var marker = new google.maps.Marker({
		position: placemark.latlng,
		map: map,
        icon: icon,
        shadow: shadow
	});
	var nameContent = '<div style="font-weight: bold; font-size: medium; margin-bottom: 0.5em">'+placemark.name+'</div>';
	marker.infoWindowContent = nameContent + placemark.description;
    google.maps.event.addListener(marker, 'click', function () {
    	openInfoWindow( this );
    });
}
function mapsInitialize() {

	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	
	var kmlParser = new geoXML3.parser({
		map: map, 
		createMarker: addLurkMarker, 
		zoom: geoXML3ZoomToFit
	});
    kmlParser.parse('/teikningar/kml/');
    
    google.maps.event.addListener(map, 'click', function () {
		if( infoWindow ) {
			infoWindow.close();
		}
    });
  
	$("#map-canvas").on("click", "a", function(event){
		$(this).attr('target','_self');
	});
}