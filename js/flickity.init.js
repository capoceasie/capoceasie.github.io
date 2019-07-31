$(function(){
	var $carousel = $('.main-flick').flickity({
	  // options
	  //cellAlign: 'left',
	  //contain: true,
	  fullscreen: true,
	  wrapAround: true,
	  cellSelector: '.carousel-cell',
	  imagesLoaded: true,
	  percentPosition: false
	});
	var $caption = $('.caption-flick');
	// Flickity instance
	var flkty = $carousel.data('flickity');
	$carousel.on( 'select.flickity', function() {
	  // set image caption using img's alt
	  $caption.text( flkty.selectedElement.children[0].alt )
	});
})