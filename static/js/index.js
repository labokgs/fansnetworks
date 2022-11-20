// Initialize and add the map

function initMap() {
    // The location of Tokyo tower
    const tokyo_tower = { lat: 35.658584, lng: 139.7454316 };
    // The map, centered at Tokyo tower
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: tokyo_tower,
    });
    // The marker, positioned at Tokyo tower
    const marker = new google.maps.Marker({
      position: tokyo_tower,
      map: map,
    });
  }
  
  window.initMap = initMap;