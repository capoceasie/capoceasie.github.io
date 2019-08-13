$(document).ready(function() {
  var $gallery = $("#image-gallery").lightGallery({
    thumbnail: false,
    selector: '.image'
  });
  // init isotope
	var $grid = $('#image-gallery').isotope({
	  percentPosition: true,
	  columnWidth: '#gallery-sizer',
	  itemSelector: '.image-wrapper',
	  layoutMode: "masonry"
	});

	// layout Isotope after each image loads
	$grid.imagesLoaded().progress( function() {
	  $grid.masonry();
	});
});