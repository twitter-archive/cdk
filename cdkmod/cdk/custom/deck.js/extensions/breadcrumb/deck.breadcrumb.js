/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*
This module provides a breadcrumb menu listing the parent
slides. Requires extra classes put on slides (slide0), subslides
(slide1), subsubslides (slide2).

*/

(function($, deck, undefined) {
    var $d = $(document);
    $d.bind('deck.init', function() {
       var bread = $("<div id='breadcrumb'></div>");
       $("body").prepend(bread);
       var $bread = $("#breadcrumb");
       var opts = $[deck]('getOptions');
       var updateCurrent = function(evt, from, to){
           var $slide = $[deck]('getSlide', to);
           // only three levels supported
           if($slide.hasClass('slide2')){
               var $slide1 = $slide.prevAll('.slide1').eq(0);
               var $slide0 = $slide.prevAll('.slide0').eq(0);
               $bread.html("<h2><a href='#" + $slide0.attr('id') + "'>" + $.trim($slide0.find('h2:first').text()) +
                           "</a> &rsaquo;&rsaquo; <a href='#" + $slide1.attr('id') + " '>" +
                           $.trim($slide1.find('h2:first').text()) + "</a></h2>");

           }else if($slide.hasClass('slide1')){
               var $slide0 = $slide.prevAll('.slide0').eq(0);
               $bread.html("<h2><a href='#" + $slide0.attr('id') + "'>" +
                           $.trim($slide0.find('h2:first').text()) + "</a></h2>"); 
           }else{
               $bread.html("");
           }
       };
       $d.bind('deck.change', updateCurrent);
    })
})(jQuery, 'deck');