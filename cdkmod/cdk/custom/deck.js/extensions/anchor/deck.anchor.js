/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*

  Enables anchor targets to sections:

  <a href="#Some_Section">Some Section</a>

  

*/

(function($, deck, undefined) {
    var $d = $(document);
    $d.bind('deck.init', function() {
        var $links = $('a[href^="#"]').not('a[href^="#slide-"]').not('a[href="#title-slide"]');
        var $h2s = $("h2");
        $h2s.each(function(){
                $(this).attr('id', $.trim($(this).text()).replace(" ", "_"));
            });
        $links.click(function(e){
                var title = $(this).attr('href').replace(" ", "_");
                var page = $(title).parents('section').attr('id');
                $.deck('go', page);
                e.preventDefault();
            });
        });
})(jQuery, 'deck');