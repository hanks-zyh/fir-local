function showQrcode(qrindex, qrpath) {
    $('#qr' + qrindex).popover({
        html: true,
        content: function () {
            return "<img src=\"" + qrpath + "\" width=\"250px\" height=\"250px\"/>";
        }
    });
}