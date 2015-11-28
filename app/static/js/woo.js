function showQrcode(loopindex,qrpath){
    $('#qr'+loopindex).popover({
        html : true,
        content : function(){
            return "<img src=\""+qrpath+"\" width=\"250px\" height=\"250px\"/>";
        }
    });
}
function hideQrcode(){
    $('#qr').popover('hide');
}