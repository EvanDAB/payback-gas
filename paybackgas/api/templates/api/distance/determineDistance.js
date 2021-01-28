function determineDistance(orig, dest) {
    var apiKey = 'AIzaSyCNyQlXhkdhJQ4iczZl79qrzPf8EJXhzL8';
    var endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json';
    console.log(typeof orig, ' ', orig);
    console.log(typeof dest, ' ', dest);
    $.ajax({
        crossDomain: true,
        dataType: 'jsonp',
        url: `${endpoint}?origins=${orig}&destinations=${dest}&key=${apiKey}&units=imperial`,
        success: function(response) {
            console.log(response);
        }  
    })
    
}