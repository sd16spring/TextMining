// 160x600 Flashtalking HTML5 Animation
function init() {

	var line_1_1			= document.getElementById(	"line_1_1"				);
	var line_1_2			= document.getElementById(	"line_1_2"				);
	var line_1_3			= document.getElementById(	"line_1_3"				);
	var line_1_4			= document.getElementById(	"line_1_4"				);

	var line_2_1			= document.getElementById(	"line_2_1"				);
	var line_2_2			= document.getElementById(	"line_2_2"				);
	var line_2_3			= document.getElementById(	"line_2_3"				);
	var line_2_4			= document.getElementById(	"line_2_4"				);
	var line_2_5			= document.getElementById(	"line_2_5"				);

	var line_3_1			= document.getElementById(	"line_3_1"				);
	var line_3_2			= document.getElementById(	"line_3_2"				);
	var line_3_3			= document.getElementById(	"line_3_3"				);
	var line_3_4			= document.getElementById(	"line_3_4"				);

	//

	var loading				= document.getElementById(	"loading"				);
	var cta					= document.getElementById(	"cta"					);
	var cta_default			= document.getElementById(	"cta_default"			);
	var cta_default_shell	= document.getElementById(	"cta_default_shell"		);
	var cta_hover			= document.getElementById(	"cta_over"				);
	var logo				= document.getElementById(	"logo"					);

	//var iOS_image			= document.getElementById(	"iOS_image"				);
	var video_div			= document.getElementById(	"video"					);
	//var _video				= document.getElementById(	"mainVideo"				);
	var _canvas				= document.getElementById(	"canvas"				);

	var ad = document.getElementById("ad");

	_desktop();
	//_testIOS();
	//_iOS();

	function _startAnimation() {

		tl = new TimelineLite();
		var _initDelay 	= 0.5;
		var _pause 		= 1.25;
		var _enter 		= 1;
		var _exit 		= 0.5;

		//var _enterEase 	= Elastic.easeOut.config(0.75,0.5);
		var _enterEase 	= Elastic.easeOut.config(0.8,0.8);
		//var _exitEase 	= Back.easeIn.config(2);
		var _exitEase 	= Back.easeIn.config(1);
		var _bgEase		= Back.easeIn.config(2);

		var _ctaEase 	= Elastic. easeOut.config( 0.75, 0.75);

		var xHide = document.getElementById("loading").offsetWidth;
		var yHide = document.getElementById("loading").offsetHeight;

		tl

		.to( loading		, 	0.5,		{	opacity:0, delay:0.25	}) // fade out loader

		//.call(contCanvas)
		//.call(pauseGSAP)

		.from(	line_1_1 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_1"				)
		.from(	line_1_2 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_1+=.125"		)
		.from(	line_1_3 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_1+=.250"		)
		.from(	line_1_4 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_1+=.375"		)
		.to(	line_1_4 	,	_pause,		{})
		.to(	line_1_1 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_1_out"			)
		.to(	line_1_2 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_1_out+=.125"	)
		.to(	line_1_3 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_1_out+=.250"	)
		.to(	line_1_4	,	_exit,		{	x:xHide, ease:_exitEase		},"line_1_out+=.375"	)

		//.call(contCanvas)
		//.call(pauseGSAP)

		.from(	line_2_1 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_2"				)
		.from(	line_2_2 	,	_enter,		{	x:xHide, ease:_enterEase	},"line_2+=.125"		)
		.from(	line_2_3 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_2+=.250"		)
		.from(	line_2_4 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_2+=.375"		)
		.from(	line_2_5	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_2+=.500"		)
		.to(	line_2_5	,	_pause,		{})
		.to(	line_2_1 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_2_out"			)
		.to(	line_2_2 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_2_out+=.125"	)
		.to(	line_2_3 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_2_out+=.250"	)
		.to(	line_2_4 	,	_exit,		{	x:xHide, ease:_exitEase		},"line_2_out+=.375"	)
		.to(	line_2_5	,	_exit,		{	x:xHide, ease:_exitEase		},"line_2_out+=.500"	)

		//.call(contCanvas)
		//.call(pauseGSAP)

		.from(	line_3_1 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_3"				)
		.from(	line_3_2 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_3+=.125"		)
		.from(	line_3_3 	,	_enter,		{	x:xHide, ease:_enterEase 	},"line_3+=.250"		)
		.from(	line_3_4 	,	_enter,		{	autoAlpha:0, scale:0, ease:_enterEase	 	},"line_3+=1.000"		)

		;

	}

	function _addListeners() {
		loading.addEventListener("mouseover",	_over);
		loading.addEventListener("mouseout",	_out);
		loading.style.cursor="pointer";
	}

	function _over() {
		TweenLite.to(cta_default_shell,		0.3,		{	y:document.getElementById("cta_default_shell").offsetHeight, ease:Power3.easeOut	});
		TweenLite.to(cta_default,			0.3,		{	y:-1*document.getElementById("cta_default_shell").offsetHeight, ease:Power3.easeOut	});
	}

	function _out() {
		TweenLite.to(cta_default_shell,		0.3,	{	y:0, ease:Power3.easeOut	});
		TweenLite.to(cta_default,			0.3,	{	y:0, ease:Power3.easeOut	});
	}

	function _desktop() {
		_addListeners();
		initCanvas();
		_startAnimation();
	}

}

var tl;

function contCanvas() {
	exportRoot.play();
}

function contGSAP() {
	tl.resume();
}

function pauseGSAP() {
	tl.pause();
}
