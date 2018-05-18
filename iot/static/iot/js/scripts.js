function refresh_climate() {
    console.log('refresh last climate data from DB!');
    $.ajax({
        url: '/bathroom/climate',
        success: function (data) {
            //console.log(data);
            $('#climate').html(data);
        }
    })
}

console.log('START scripts.js');


$(document).ready(function () {
    console.log('START refresh');
    refresh_climate();
    setInterval('refresh_climate()', 5000);
});