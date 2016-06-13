/**
 * controller.js
 * 2016-05-01 K.OHWADA @ FabLab Kannai
 */

var SLIDE_MIN = -100;
var SLIDE_MAX = 100;
var SLIDE_STEP = 1;
var SLIDE_ZERO = 0;

var TIME_INTERVAL = 100;  // 0.1 sec
var timer_id;

$(function() {
    // button
    updateButton();
    timer_id = setInterval("updateButton()", TIME_INTERVAL);
    // servo
    var sliderHandler0 = function(e, ui){
        var val = ui.value;
        $( "#servo_value" ).html( val );
        postServo( val );
    };
    $( "#servo_silder" ).slider({
        orientation: "horizontal",
        min: SLIDE_MIN,
        max: SLIDE_MAX,
        step: SLIDE_STEP,
        value: SLIDE_ZERO,
        change: sliderHandler0,
        slide: sliderHandler0
    });
    $( "#servo_value" ).html( SLIDE_ZERO );
});

function updateButton(){
    $.ajax({
        url: '/status',
        type: 'GET',
        cache : false
    })
    .done(function(data) {
        var obj = JSON.parse(data);
        var ele = $( "#button_status" );
        if ( obj != null ) {
            if ( obj.status == 1 ) {
                ele.html( "On" );
            } else {
                ele.html( "Off" );
           }
        }
    }); 
}

function stopServo(){
    $( "#servo_silder" ).slider({  value: SLIDE_ZERO });
    $( "#servo_value" ).html( SLIDE_ZERO );
    postServo( SLIDE_ZERO );
}

function postServo(val){
    post("servo", val);
}

function postLed(val){
    post("led", val);
}

function post(type, value){
	var data = {
	    	"type": type,
		"value": value
	};
	$.post("/action", data);
}

function applyCustomCss(custom_css){
    var head = document.getElementsByTagName('head')[0];
    var style = document.createElement('link');
    style.rel = "stylesheet";
    style.type = 'text/css';
    style.href = custom_css;
    head.appendChild(style);
}

