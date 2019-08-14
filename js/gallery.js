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
	
	//init lightgallery for click on image behaviour to zoom
	$('.main-lightgallery').lightGallery({
		thumbnail:true
	}); 
	
	//init lightslider for diaporama img layout
	$(".light-slider").lightSlider({
		gallery:true,
		item: 1,
		enableDrag: false,
		onSliderLoad: function(el) {
            el.lightGallery({
                selector: '.light-slider .lslide'
            });
        }
	});
});