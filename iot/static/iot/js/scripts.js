function refresh() {
    console.log('refresh last climate data from DB!');
    $.ajax({
        url: 'climate',
        success: function (data) {
            //console.log(data);
            $('#temp').html(data);
        }
    })
}

console.log('START scripts.js');




$(document).ready(function () {
    var button = $('#button');
    console.log(button);
    console.log('Hello!');
    refresh();
    button.on('click', function () {
        console.log('CLiCK!');
    });

    setInterval('refresh()', 50000);
});