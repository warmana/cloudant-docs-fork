## Node.js

<pre class="thebe">
var Cloudant = require("cloudant");
var examples = Cloudant({account: 'examples'});
var animaldb = examples.db.use('animaldb');
var res = animaldb.get('zebra', function(err, data){console.log(data);});
</pre>

<script src="//storage.googleapis.com/kimstebel-public/thebe/static/main-built.js" type="text/javascript" charset="utf-8"></script><script>
$(function(){
  new Thebe({
    url: 'https://tmpnb.kimstebel.com:8000',
		selector: 'pre.thebe',
    tmpnb_mode: true,
    kernel_name: 'javascript',
		debug: true,
  	image_name: 'kimstebel/thebe-demo-notebook',
	  inject_css: true,
    load_mathjax: false
  });
});
</script>


