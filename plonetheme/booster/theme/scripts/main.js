(function () {

	'use strict';

	// iPad and iPod detection
	var isiPad = function(){
		return (navigator.platform.indexOf('iPad') !== -1);
	};

	var isiPhone = function(){
	    return (
			(navigator.platform.indexOf('iPhone') !== -1) ||
			(navigator.platform.indexOf('iPod') !== -1)
	    );
	};

	// Burger Menu
	var burgerMenu = function() {
		$('body').on('click', '.js-fh5co-nav-toggle', function(){
			if ( $('#fh5co-navbar').is(':visible') ) {
				$(this).removeClass('active');
			} else {
				$(this).addClass('active');
			}

		});
	};

	// Animate Feature
	var animateFeatureIcons = function() {
		if ( $('#fh5co-features').length > 0 ) {
			$('#fh5co-features .to-animate').each(function( k ) {

				var el = $(this);

				setTimeout ( function () {
					el.addClass('bounceIn animated');
				},  k * 200, 'easeInOutExpo' );

			});
		}
	};

	$(function(){

		burgerMenu();

	});

	// navbar menu

	$('.navbar li a').wrapInner('<span></span>');
	$('.navbar li a span').append('<span class="border"></span>');

	$('#portal-searchbox .LSBox').hover(function(){
	  $('.searchSection').toggleClass('show-searchSection');
	});

	$('.item.active').find(".to-animate").addClass('fadeInUp animated');
	$('#carousel-example-generic').on('slid.bs.carousel', function () {
		$('.item.active').find(".to-animate").addClass('fadeInUp animated');
	});
	$('#carousel-example-generic').on('slide.bs.carousel', function () {
		$('.item.active').find(".to-animate").removeClass('fadeInUp animated');
	});
	$( document ).ready(function() {
	  $('.fh5co-owl-text-wrap').find(".to-animate").addClass('fadeInUp animated');
	});


}());