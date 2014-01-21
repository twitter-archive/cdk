/*

  This module makes sure that switching to a new slide always scrolls
  to the top.

  It also checks body/slide height - for tall slides set overflow to scroll,
  for short slides hide scrollbars

  Currently in deck.js presentations with long slides, switching from
  one slide scrolled down the page to the next slide doesn't change
  the position of the scroll bar.
  

*/

(function($, deck, undefined) {
    var $d = $(document);
    $d.bind('deck.init', function() {
       var scrollup = function(evt, from, to){
           $(document).scrollTop(0);
       };
       var $body = $('body');
       var $html = $('html');    
       var height_check = function(evt, from, to){
           if(to > 0){
               var slide = $('#slide-' + to);
           }else{
               var slide = $('#title-slide');
           }
           if(slide.height() > $body.height()){
               $html.css('overflow', 'scroll');
           }else{
               $html.css('overflow', 'hidden');
           }
       }
       $d.bind('deck.change', scrollup);
       $d.bind('deck.change', height_check); 
    })
})(jQuery, 'deck');
