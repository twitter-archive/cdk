/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*
This module provides a popup menu listing the shortcut key.
*/

(function($, deck, undefined) {
    var $d = $(document);
    $.deck.defaults.keys.helpKeycode = 72; // 'h'
    $d.bind('deck.init', function() {
       var help_text = $("<div id='help-text' style='display:none;'><dl>" +
                     "<dt>&rarr; or space</dt><dd>Advance to the next slide</dd>" +
                     "<dt>t</dt><dd>Open Table of Contents</dd>" +
                     "<dt>g</dt><dd>Navigate to # slide.</dd>" +
                     "<dt>h</dt><dd>Show/Hide this help content</dd>" +                     
                     "<dt>m</dt><dd>Preview Slides</dd>" +
                     "<dt>s</dt><dd>Show/Hide sidebar</dd>" +                         
                     "</dl></div>");
       $("body").prepend(help_text);
       var $help_text = $("#help-text");
       $d.bind('keydown.help', function(event) {
          var opts = $['deck']('getOptions');
          if (event.which === opts.keys.helpKeycode) {
              $help_text.toggle();
          }
          else{
              $help_text.hide();
          }
       });
    });
})(jQuery, 'deck');