/**
 * Created by Tom on 2015/12/28.
 */
/* sequence-loader.js */
(function (doc) {
  function onReady(fn) {
    if (doc.addEventListener) {
      doc.addEventListener('DOMContentLoaded', fn);
    } else {
      doc.attachEvent('onreadystatechange', function() {
        if (doc.readyState === 'interactive')
          fn();
      });
    }
  }

  onReady(function(){convertUML('uml-sequence-diagram', Diagram, {theme: 'simple'});});
})(document)