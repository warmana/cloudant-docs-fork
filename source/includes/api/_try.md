<script type="text/javascript">
  $(document).ready(function() {
    var searchForm = $('form.search');
    var cqForm = $('form.cq');
    var outputField = $("#output-marker").next();
    var httpRequestField = $("#request-http-marker").next();
    var curlRequestField = $("#request-curl-marker").next();
    var highlight = function(elem) {
      elem.each(function(i, block) {
        hljs.highlightBlock(block);
      });
    };
    var requestTypes = {
      search: {
        queryInput: $('form.search #test-search-query'),
        countsInput: $('form.search #search-counts'),
        form: searchForm,
        queries: {
          'author-is-john': {query: 'author:John'},
          'sorting': {query: ''},
          default: {query: 'author:John'}
        },
        buildUrl: function() {
          var url = '/docs-examples/_design/ddoc/_search/books?q=' + this.queryInput.val();
          var counts = requestTypes.search.countsInput.val();
          if (counts != '') {
            url += '&counts=' + counts;
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
          var query = requestTypes.search.queryInput.val();
          var url = '//examples.cloudant.com' + requestTypes.search.buildUrl();
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
        form: cqForm,
        queries: {
          'actor-is-zoe-saldana': {query: '{ "selector": { "Person_name": "Zoe Saldana" } }'},
          'sorting': {query: '{ "selector": { "Movie_year": {"$gte": 2000, "$lte": 2001}}, "sort": ["Movie_year"]}'},
          'pg2010': {query: '{ "selector": { "Movie_year": 2010, "Movie_rating": {"$in": ["PG", "PG-13"]} } }'},
          default: {query: '{ "selector": { "Person_name": "Zoe Saldana" } }'}
        },
        renderHttpRequest: function() {
          return 'POST /movies-demo-with-indexes/_find HTTP/1.1\nHost: examples.cloudant.com\n\n' + this.queryInput.val();
        },
        renderCurlRequest: function() {
          return "curl 'https://examples.cloudant.com/movies-demo-with-indexes/_find' -X POST -d '" + this.queryInput.val() + "'";
        },
        submitForm: function(event){
          var query = requestTypes.cq.queryInput.val();
          jQuery.ajax({
            url: '//examples.cloudant.com/movies-demo-with-indexes/_find',
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
    
    requestTypes.search.form.submit(requestTypes.search.submitForm);
    requestTypes.cq.form.submit(requestTypes.cq.submitForm);
    
    var requestChanged = function(formName) {
      httpRequestField.text(requestTypes[formName].renderHttpRequest());
      highlight(httpRequestField);
      curlRequestField.text(requestTypes[formName].renderCurlRequest());
      highlight(curlRequestField);
      requestTypes[formName].submitForm({preventDefault:function(){}});
    }
    
    var requestTypeSelect = $('div.test-form-container select.request-type');
    var showSelectedType = function() {
      for (requestType in requestTypes) {
        requestTypes[requestType].form.hide();
      }
      var type = requestTypeSelect.val();
      requestTypes[type].form.show();
      requestChanged(type);
    };
    requestTypeSelect.on("change", showSelectedType);
    
    var initForm = function(formName, request) {
      for (field in request) {
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
    for (requestType in requestTypes) {
      initPredefinedSelect(requestType);
    }
    for (rt in requestTypes) {
      initForm(rt, requestTypes[rt].queries.default);
    }
    requestTypes.search.form.on('keyup keypress', function() {requestChanged('search');});
    requestTypes.cq.queryInput.on('keyup keypress', function() {requestChanged('cq');});
    //init form from query param values
    function getParameterByName(name) {
      name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
      var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"), results = regex.exec(location.search);
      return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var requestType = getParameterByName('requestType');
    var predefinedQuery = getParameterByName('predefinedQuery');
    if (requestType) {
      if (predefinedQuery) {
        $('form.' + requestType + ' .predefined').val(predefinedQuery);
      }
      requestTypeSelect.val(requestType);
      showSelectedType(requestType);
      requestChanged(requestType);
    } else {
      showSelectedType();
      highlight(outputField);
      highlight(httpRequestField);
      highlight(curlRequestField);
    
    }
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
    <option value="cq">Cloudant Query</option>
  </select>
  <br>
  <form action="#" class="search">
    <label for="predefined">Predefined queries</label>
    <select name="predefined" class="predefined">
      <option selected="selected" value="author-is-john">Books written by John</option>
      <option value="sorting">Search with sorting</option>
    </select>
    <label for="query">Search query (q)</label>
    <input size="100" type="text" name="query" class="query" id="test-search-query">
    <label for="counts">Counts</label>
    <input size="100" type="text" name="counts" id="search-counts">
    <input type="submit" value="search" class="submit-button"></input>
  </form>
  
  <form action="#" class="cq">
    <label for="predefined">Predefined queries</label>
    <select name="predefined" class="predefined">
      <option selected="selected" value="actor-is-zoe-saldana">Movies with Zoe Saldana</option>
      <option value="sorting">Query with sorting</option>
      <option value="pg2010">2010 Movies rated PG or PG-13</option>
    </select>
    <textarea rows="10" class="query" cols="80" id="requestBody"></textarea><br /><br />
    <input class="submit-button" type="submit" value="query"></input>
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
  .test-form-container textarea, div.test-form-container input, div.test-form-container select, div.test-form-container label {
    margin-left: 40px;
    display: block;
  }
  .test-form-container textarea, div.test-form-container input, div.test-form-container select {
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
  
  .test-form-container input {
    padding-left: 5px;
  }
  
  .test-form-container .submit-button {
    width: 100px;
    padding: 0;
  }
  
</style>
