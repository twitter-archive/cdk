/*!

Copyright (c) 2012 Simeon Franklin
MIT license
*/

/*

This module provides quick-n-dirty quiz plugin. Requires use of class syntax in
asciidoc source so


[form]#marakana.com/form/#

[textarea]#This is the label for a textarea#
[text]#This is the label for a text input control#


transforms to an html form.
*/

(function($, deck, undefined) {
    var $d = $(document);
    $d.bind('deck.init', function() {
            var action = $("span.form").text();
            var $controls = $("span.textarea, span.text");
            $controls.filter(".text").each(function(){
                    $(this).replaceWith("<div class='form'><input type='text' name='" + $(this).text() + "' class='input'></div>");
                });
            $controls.filter(".textarea").each(function(){
                    $(this).replaceWith("<div class='form'><textarea name='" + $(this).text() + "' class='input' rows='20' cols='70'></textarea></div>");
                });

            $("div.form:last").append("<br><br><input type='button' class='btn' value='Submit Quiz' id='submitquiz'>");
            $('#submitquiz').click(function(){
                    var json = $(".input").serializeArray();
                    $(this).after("<form id='theform' method='POST' action='" + action +
                                  "' style='display:none;'><textarea name='json'>" + JSON.stringify(json) + "</textarea></form>");
                    $('#theform').submit();
                });
    })
})(jQuery, 'deck');