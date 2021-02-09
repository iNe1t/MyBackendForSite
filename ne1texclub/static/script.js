var clicks = 0;

$("#button").click(function(){
    clicks = clicks + 1;
    if (clicks === 1) {
        $("#menu").css("visibility", "visible"),
        $("#menu1").css("visibility", "visible")
    } else if (clicks ===2) {
        $("#menu").css("visibility", "hidden"),
        $("#menu1").css("visibility", "hidden")
        clicks = 0; 
    }
});
