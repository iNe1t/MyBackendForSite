var clicks = 0;

$("#button").click(function(){
    clicks = clicks + 1;
    if (clicks === 1) {
        $("#menu").css("visibility", "visible"),
        $("#menu1").css("visibility", "visible")
        $("body").css("overflow-y", "hidden")
    } else if (clicks ===2) {
        $("#menu").css("visibility", "hidden"),
        $("#menu1").css("visibility", "hidden")
        $("body").css("overflow-y", "visible")
        clicks = 0; 
    }
});
