
function change_status (id, status){
    $.ajax({
        url: "/changestatus/",
        method: "POST",
        data: {id:id,status:status},
        success: function(response){
            var button = $('#current')
            if(response.booth==='Available'){
                button.removeClass('btn-success btn-warning btn-danger')
                button.addClass('btn-success')
                button.html(response.booth)
            }else if(response.booth==='Occupied'){
                button.removeClass('btn-success btn-warning btn-danger')
                button.addClass('btn-warning')
                button.html(response.booth)
            }else if(response.booth==='Closed'){
                button.removeClass('btn-success btn-warning btn-danger')
                button.addClass('btn-danger')
                button.html(response.booth)
            }
        },
        error: function(xhr, status, error){
        }
    });

}

$(document).ready(function(){
    var socket = new WebSocket('ws://localhost:8000/ws/test/' + $('#status-1').attr('data-href'))
    socket.onmessage = async function(event){
        // console.log(event);
        var data=JSON.parse(event.data);
        console.log(data);
    }
    $('#status-1').click(function(){
        var id = $(this).attr('data-href')
        var status = $(this).html()
        change_status(id, status)
    })
    $('#status-2').click(function(){
        var id = $(this).attr('data-href')
        var status = $(this).html()
        change_status(id, status)
    })
    $('#status-3').click(function(){
        var id = $(this).attr('data-href')
        var status = $(this).html()
        change_status(id, status)
    })
})
