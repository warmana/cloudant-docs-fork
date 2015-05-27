<script type="text/javascript">
  $(document).ready(function() {
    var outputField = $("#output-marker").next();
    var httpRequestField = $("#request-http-marker").next();
    var curlRequestField = $("#request-curl-marker").next();
    var highlight = function(elem) {
      elem.each(function(i, block) {
        hljs.highlightBlock(block);
      });
    };
    var requestTypes = {
      analyzers: {
        queries: {
          'email-address': {query: '{"analyzer": "email", "text":"Jane\'s email address is jane.smith@example.com."}'},
          'english': {query: '{"analyzer": "english", "text":"Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers. Where’s the peck of pickled peppers Peter Piper picked?"}'},
          'german': {query: '{"analyzer": "german", "text":"Fischers Fritz fischt frische Fische, frische Fische fischt Fischers Fritz."}'},
          'default': {query: '{"analyzer": "email", "text":"Jane`s email address is jane.smith@example.com."}'},
        },
        form: $('form.analyzers'),
        queryInput: $('form.analyzers .query'),
        renderHttpRequest: function() {
          return 'POST /_search_analyze HTTP/1.1\nHost: examples.cloudant.com\nContent-Type: application/json\n\n' + this.queryInput.val();
        },
        renderCurlRequest: function() {
          return "curl 'https://examples.cloudant.com/_search_analyze' -H 'Content-Type: application/json' -X POST -d '" + this.queryInput.val() + "'";
        },
        submitForm: function(event) {
          var query = this.queryInput.val();
          jQuery.ajax({
            url: 'https://examples.cloudant.com/_search_analyze',
            type: 'POST',
            data: query,
            beforeSend: function(xhr) {
              xhr.setRequestHeader("Content-Type", "application/json");
              xhr.setRequestHeader("Authorization", "Basic " + btoa('thereencespedgetytolisir:c1IimpBSAC3b3A66N8LHKwKF'));
            },
            error: function(one, two) {},
            complete: displayResult
          });
          event.preventDefault();
        }
      },
      search: {
        queryInput: $('form.search #test-search-query'),
        countsInput: $('form.search #search-counts'),
        drilldownInput: $('form.search #search-drilldown'),
        groupFieldInput: $('form.search #search-group-field'),
        groupLimitInput: $('form.search #search-group-limit'),
        groupSortInput: $('form.search #search-group-sort'),
        includeDocsInput: $('form.search #search-include-docs'),
        limitInput: $('form.search #search-limit'),
        rangesInput: $('form.search #search-ranges'),
        sortInput: $('form.search #search-sort'),
        form: $('form.search'),
        queries: {
          'author-is-john': { query: 'author:John' },
          'sorting': { query: 'author:J*', sort: '"-year"' },
          'default': { query: 'author:John' },
          'drilldown': { query: 'year:[2000 TO 2010]', drilldown: '["author","J. K. Rowling"]' },
          'counts': { query: 'year:[2000 TO 2010]', counts: '["author"]', limit: 0 },
          'ranges': { query: 'author:J*', ranges: '{"year":{"21st century":"[2000 TO 2099]","20th century":"[1900 TO 1999]"}}', limit: 0 },
          
          
          
      /*     <option selected="selected" value="author-is-john">Books written by John</option>
      <option value="sorting">Sorting by year</option>
      <option value="ranges">Year ranges</option>
      <option value="counts">Count authors</option>
      <option value="drilldown">Drilldown</option>    */  
          
          
        },
        buildUrl: function() {
          var url = '/docs-examples/_design/ddoc/_search/books?q=' + this.queryInput.val();
          var counts = this.countsInput.val();
          if (counts != '') {
            url += '&counts=' + encodeURIComponent(counts);
          }
          var drilldown = this.drilldownInput.val();
          if (drilldown != '') {
            url += '&drilldown=' + encodeURIComponent(drilldown);
          }
          var groupField = this.groupFieldInput.val();
          if (groupField != '') {
            url += '&group_field=' + encodeURIComponent(groupField);
          }
          var groupLimit = this.groupLimitInput.val();
          if (groupLimit != '') {
            url += '&group_limit=' + encodeURIComponent(groupLimit);
          }
          var groupSort = this.groupSortInput.val();
          if (groupSort != '') {
            url += '&group_sort=' + encodeURIComponent(groupSort);
          }
          var limit = this.limitInput.val();
          if (limit != '') {
            url += '&limit=' + encodeURIComponent(limit);
          }
          var ranges = this.rangesInput.val();
          if (ranges != '') {
            url += '&ranges=' + encodeURIComponent(ranges);
          }
          var sort = this.sortInput.val();
          if (sort != '') {
            url += '&sort=' + encodeURIComponent(sort);
          }
          var includeDocs = this.includeDocsInput.is(':checked');
          if (includeDocs) {
            url += '&include_docs=' + encodeURIComponent(includeDocs);
          }
          return url;
        },
        renderHttpRequest: function() {
          return 'GET ' + this.buildUrl() + ' HTTP/1.1';
        },
        renderCurlRequest: function() {
          return 'curl "https://examples.cloudant.com' + this.buildUrl() + '"';
        },
        doAjaxRequest: function() {
        
        },
        submitForm: function(event) {
          var query = this.queryInput.val();
          var url = 'https://examples.cloudant.com' + this.buildUrl();
          jQuery.ajax({
            url: url,
            type: 'GET',
            beforeSend: function(xhr) {
              xhr.setRequestHeader("Authorization", "Basic " + btoa('thereencespedgetytolisir:c1IimpBSAC3b3A66N8LHKwKF'));
            },
            error: function(one, two) {},
            complete: displayResult
          });
          event.preventDefault();
        }
      },
      cq: {
        queryInput: $('form.cq .query'),
        form: $('form.cq'),
        queries: {
          'actor-is-zoe-saldana': {query: '{ "selector": { "Person_name": "Zoe Saldana" } }'},
          'sorting': {query: '{ "selector": { "Movie_year": {"$gte": 2000, "$lte": 2001}}, "sort": ["Movie_year"]}'},
          'pg2010': {query: '{ "selector": { "Movie_year": 2010, "Movie_rating": {"$in": ["PG", "PG-13"]} } }'},
          'default': {query: '{ "selector": { "Person_name": "Zoe Saldana" } }'}
        },
        renderHttpRequest: function() {
          return 'POST /movies-demo-with-indexes/_find HTTP/1.1\nHost: examples.cloudant.com\n\n' + this.queryInput.val();
        },
        renderCurlRequest: function() {
          return "curl 'https://examples.cloudant.com/movies-demo-with-indexes/_find' -X POST -d '" + this.queryInput.val() + "'";
        },
        submitForm: function(event){
          var query = this.queryInput.val();
          jQuery.ajax({
            url: 'https://examples.cloudant.com/movies-demo-with-indexes/_find',
            type: 'POST',
            data: query,
            beforeSend: function(xhr) {
              xhr.setRequestHeader("Authorization", "Basic " + btoa('thereencespedgetytolisir:c1IimpBSAC3b3A66N8LHKwKF'));
            },
            error: function(one, two) {},
            complete: displayResult
          });
          event.preventDefault();
        }
    
      }
    };
    
    var displayResult = function(jqXHR, textStatus) {
      var result = JSON.stringify(jQuery.parseJSON(jqXHR.responseText), null, '    ');
      outputField.show();
      outputField.text(result);
      highlight(outputField);
    }
    
    for (var rt in requestTypes) {
      requestTypes[rt].form.submit(requestTypes[rt].submitForm);
    }
    
    var requestChanged = function(formName) {
      httpRequestField.text(requestTypes[formName].renderHttpRequest());
      highlight(httpRequestField);
      curlRequestField.text(requestTypes[formName].renderCurlRequest());
      highlight(curlRequestField);
      requestTypes[formName].submitForm({preventDefault:function(){}});
    }
    
    var requestTypeSelect = $('div.test-form-container select.request-type');
    var showSelectedType = function() {
      for (var requestType in requestTypes) {
        requestTypes[requestType].form.hide();
      }
      var type = requestTypeSelect.val();
      requestTypes[type].form.show();
      requestChanged(type);
    };
    requestTypeSelect.on("change", showSelectedType);
    
    var initForm = function(formName, request) {
      console.log(formName);
      console.log(request);
      $('form.' + formName + ' input[type=text]').val('');
      for (var field in request) {
        $('form.' + formName + ' .' + field).val(request[field]);
      }
    };
    var initPredefinedSelect = function(formName) {
      var predefinedSelect = $('form.' + formName + ' select.predefined');
      predefinedSelect.on('change', function() {
        var request = predefinedSelect.val();
        initForm(formName, requestTypes[formName].queries[request]);
        requestChanged(formName);
      });
    };
    for (var rt in requestTypes) {
      initPredefinedSelect(rt);
      initForm(rt, requestTypes[rt].queries['default']);
    }
    requestTypes.search.includeDocsInput.on('change', function() {requestChanged('search');});
    for (var rt in requestTypes) {
      var createFunc = function(rtp) { return function(){requestChanged(rtp)}}
      requestTypes[rt].form.on('keyup', createFunc(rt));
    }
    //init form from query param values
    function getParameterByName(name) {
      name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
      var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"), results = regex.exec(location.search);
      return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var requestType = getParameterByName('requestType');
    if (!requestType) { requestType = 'search'; }
    var predefinedQuery = getParameterByName('predefinedQuery');
    if (!predefinedQuery) { predefinedQuery = 'default'; }
    requestTypeSelect.val(requestType);
    $('form.' + requestType + ' .predefined').val(predefinedQuery);
    console.log(requestType);
    showSelectedType();
    console.log(requestType);
    initForm(requestType, requestTypes[requestType].queries[predefinedQuery]);
    requestChanged(requestType);
  });
  
</script>

## Try it!

> Request

<p id="request-http-marker"></p>

```http
GET /examples/_design/ddoc/_search/books?q=author:John HTTP/1.1
```

<p id="request-curl-marker"></p>

```shell
curl https://$USERNAME:$PASSWORD@$USERNAME.cloudant.com/examples/_design/ddoc/_search/books?q=author:John
```

> Response

<p id="output-marker"></p>

```json
{
  "total_rows": 1,
  "bookmark": "g2wAAAABaANkACFkYmNvcmVAZGIxMS5tZXJpdGFnZS5jbG91ZGFudC5uZXRsAAAAAm4EAAAAAIBuBAD___-_amgCRkACik3gAAAAYRtq",
  "rows": [
    {
      "id": "book91",
      "order": [
        2.3175313472747803,
        27
      ],
      "fields": {
        "author": "John Steinbeck",
        "title_English": "The Grapes of Wrath"
      }
    }
  ]
}
```

You can try out requests and output will be shown in the code column to the right. We have put together some sample data so that you can play with Cloudant straight away.

<div class="test-form-container">

  <label for="request-type">Type of request</label>
  <select name="request-type" class="request-type">
    <option selected="selected" value="search">Search</option>
    <option value="analyzers">Search analyzers</option>
    <option value="cq">Cloudant Query</option>
  </select>
  <br>
  <form action="#" class="search">
    <label for="predefined">Predefined queries</label>
    <select name="predefined" class="predefined">
      <option selected="selected" value="author-is-john">Books written by John</option>
      <option value="sorting">Sorting by year</option>
      <option value="ranges">Year ranges</option>
      <option value="counts">Count authors</option>
      <option value="drilldown">Drilldown</option>      
    </select>
    <label for="query">Search query (q)</label>
    <input size="100" type="text" name="query" class="query" id="test-search-query">
    <label for="counts">Counts</label>
    <input size="100" type="text" name="counts" class="counts" id="search-counts">
    <label for="drilldown">Drilldown</label>
    <input size="100" type="text" name="drilldown" class="drilldown" id="search-drilldown">
    <label for="groupfield">Group field</label>
    <input size="100" type="text" name="groupfield" class="groupField" id="search-group-field">
    <label for="group-limit">Group limit</label>
    <input size="100" type="text" name="group-limit" class="groupLimit" id="search-group-limit">
    <label for="group-sort">Group sort</label>
    <input size="100" type="text" name="group-sort" class="groupSort" id="search-group-sort">
    <label for="limit">Limit</label>
    <input size="100" type="text" name="limit" class="limit" id="search-limit">
    <label for="ranges">Ranges</label>
    <input size="100" type="text" name="ranges" class="ranges" id="search-ranges">
    <label for="sort">Sort</label>
    <input size="100" type="text" name="sort" class="sort" id="search-sort">
    
    <input type="checkbox" name="include-docs" class="includeDocs" id="search-include-docs">
    <label style="margin-left: 0px;display: inline" for="include-docs">Include docs</label>
  </form>
  
  <form action="#" class="cq">
    <label for="predefined">Predefined queries</label>
    <select name="predefined" class="predefined">
      <option selected="selected" value="actor-is-zoe-saldana">Movies with Zoe Saldana</option>
      <option value="sorting">Query with sorting</option>
      <option value="pg2010">2010 Movies rated PG or PG-13</option>
    </select>
    <textarea rows="10" class="query" cols="80" id="requestBody"></textarea><br /><br />
  </form>
  
  <form action="#" class="analyzers">
    <label for="predefined">Predefined queries</label>
    <select name="predefined" class="predefined">
      <option selected="selected" value="email-address">Email address analyzer</option>
      <option value="english">English analyzer</option>
      <option value="german">German analyzer</option>
    </select>
    <textarea rows="10" class="query" cols="80" id="analyzersRequestBody"></textarea><br /><br />
  </form>
    
</div>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<style type="text/css">
  .test-form-container textarea {
  
  }
  div.test-form-container {
    clear:none;
  }
  div.test-form-container * {
    margin: 0;
    padding: 0;
  }
  .test-form-container textarea, div.test-form-container input[type=text], div.test-form-container select, div.test-form-container label {
    margin-left: 40px;
    display: block;
  }
  .test-form-container textarea, div.test-form-container input[type=text], div.test-form-container select {
    margin-bottom: 12px;
    width: 40%;
    height: 24px;
  }
  .test-form-container textarea {
    height: 300px;
  }
  .test-form-container form {
    display: none;
  }
  .test-form-container form.search {
    display: block;
  }
  
  .test-form-container input[type=text] {
    padding-left: 5px;
  }
  
  .test-form-container input[type=checkbox] {
    display: inline;
    margin-left: 40px;
    width: 20px;
  }
    
</style>
