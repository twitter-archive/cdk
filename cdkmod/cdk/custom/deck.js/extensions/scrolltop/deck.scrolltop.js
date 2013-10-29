/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*

  This module makes sure that switching to a new slide always scrolls
  to the top.

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
       $d.bind('deck.change', scrollup);
    })
})(jQuery, 'deck');