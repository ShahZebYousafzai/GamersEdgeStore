(function ($) {
	
	"use strict";

	// Page loading animation
	$(window).on('load', function() {

        $('#js-preloader').addClass('loaded');

    });


	$(window).scroll(function() {
	  var scroll = $(window).scrollTop();
	  var box = $('.header-text').height();
	  var header = $('header').height();

	  if (scroll >= box - header) {
	    $("header").addClass("background-header");
	  } else {
	    $("header").removeClass("background-header");
	  }
	})

	var width = $(window).width();
		$(window).resize(function() {
		if (width > 767 && $(window).width() < 767) {
			location.reload();
		}
		else if (width < 767 && $(window).width() > 767) {
			location.reload();
		}
	})

	// init Isotope
	var $grid = $('.trending-box').isotope({
		itemSelector: '.trending-items'
	});
	// filter functions
	var filterFns = {
		// show if number is greater than 50
		categoryType: function() {
		var category = $(this).find('.category').text();
		return category;
		}
	};

	// bind filter button click
	$('.trending-filter').on( 'click', 'a', function() {
		var filterValue = $( this ).attr('data-filter');
		// use filterFn if matches value
		filterValue = filterFns[ filterValue ] || filterValue;
		$grid.isotope({ filter: filterValue });
	});

	// change is-checked class on buttons
	$('.trending-filter').each( function( i, trendingFilter ) {
		var $trendingFilter = $( trendingFilter );
		$trendingFilter.on( 'click', 'a', function() {
		$trendingFilter.find('.is-checked').removeClass('is-checked');
		$( this ).addClass('is-checked');
		});
	});

	$('.trending-filter').each( function( i, trendingFilter ) {
		var $trendingFilter = $( trendingFilter );
		$trendingFilter.on( 'click', 'a', function() {
		  $trendingFilter.find('.is_active').removeClass('is_active');
		  $( this ).addClass('is_active');
		});
	  });
  


	// Menu Dropdown Toggle
	if($('.menu-trigger').length){
		$(".menu-trigger").on('click', function() {	
			$(this).toggleClass('active');
			$('.header-area .nav').slideToggle(200);
		});
	}


	// Menu elevator animation
	$('.scroll-to-section a[href*=\\#]:not([href=\\#])').on('click', function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			if (target.length) {
				var width = $(window).width();
				if(width < 991) {
					$('.menu-trigger').removeClass('active');
					$('.header-area .nav').slideUp(200);	
				}				
				$('html,body').animate({
					scrollTop: (target.offset().top) - 80
				}, 700);
				return false;
			}
		}
	});


	// Page loading animation
	$(window).on('load', function() {
		if($('.cover').length){
			$('.cover').parallax({
				imageSrc: $('.cover').data('image'),
				zIndex: '1'
			});
		}

		$("#preloader").animate({
			'opacity': '0'
		}, 600, function(){
			setTimeout(function(){
				$("#preloader").css("visibility", "hidden").fadeOut();
			}, 300);
		});
	});
    


})(window.jQuery);