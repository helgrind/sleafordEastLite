function add_row(data) {
    $('#inputs>table').append('<tr><td>'+data['sysname']+'</td><td>'+data['username']+'</td></tr>')
}

$(function() {
    const ws = new WebSocket('ws://127.0.0.1:8000/ws')
    ws.onopen = () => {}
    ws.onmessage = (message) => {
        _.each(JSON.parse(message.data), add_row)
    }
});