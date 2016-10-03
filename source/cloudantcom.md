---
title: Cloudant Documentation - cloudant.com

language_tabs:
  - http
  - shell: curl
#  - javascript: node.js
#  - python

toc_footers:
  - <a href="https://cloudant.com/">Cloudant</a>
  - <a href="https://cloudant.com/sign-up/">Sign up</a> / <a href="https://cloudant.com/sign-in/">Sign in</a>
  - <a href="http://stackoverflow.com/questions/tagged/cloudant">Cloudant on StackOverflow</a>
  - <a href='http://github.com/tripit/slate'>Documentation Powered by Slate</a>
  - <a href="https://github.com/cloudant-labs/slate">Documentation Source</a>

includes:
  - cloudantcom/index

---

<script>
fragments = {
  '#cloudantcompliance': 'cloudantcompliance.html',
  '#dbaassecurity': 'dbaassecurity.html'
}
fragment = window.location.hash;
dest = fragments[fragment];
if (dest) {
  window.location = dest;
}
</script>
