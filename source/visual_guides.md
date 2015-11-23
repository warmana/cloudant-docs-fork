---
title: Cloudant Documentation - Visual Guide

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
  - visual/index

---

<script>
fragments = {
  '#account': 'account.html'
  '#active_tasks': 'active_tasks.html'
  '#databases': 'databases.html'
  '#helpful_links': 'helpful_links.html'
  '#overview': 'overview.html'
  '#replication': 'replication.html'
  '#support': 'support.html'
  '#warehousing': 'warehousing.html'
}
fragment = window.location.hash;
dest = fragments[fragment];
if (dest) {
  window.location = dest;
}
</script>
