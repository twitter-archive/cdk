/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*
  
If there's a span.slidetheme in an h2 then add the .slidetheme to the
enclosing section

*/

(function($, deck, undefined) {
    var $d = $(document);
    $d.bind('deck.init', function() {
        $("h2 span").each(function(){
            var cls = $(this).attr('class');
            $(this).parents("section").addClass(cls);
        });
        // copy alt to title for all img tags
        $("img").each(function(){
            var $this = $(this);
            $this.attr('title', $this.attr('alt'));
        });
        // any img-slide need to have first img scaled to window
        $("section.image-slide").each(function(){
            var $img = $(this).find('img:first');
            $(this).css('background-image', 'url("' + $img.prop('src') + '")');
            $img.hide();
        });

    })
})(jQuery, 'deck');
