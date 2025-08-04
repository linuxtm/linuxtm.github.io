---
title: Scripturi
author: linuxtm
layout: page
slug: scripturi
tags:
  - scripturi linux
  - scripturi administrare linux
  - scripturi ubuntu
  - scripturi devops
  - comenzi linux
---
<div class="home">

  <h1 class="page-heading">Posts</h1>

  <ul class="post-list">
    {% for post in site.categories.Scripturi %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
	<p class="post-excerpt">{{ post.content | strip_html | truncate: 100 }}</p>
      </li>
    {% endfor %}
  </ul>

</div>
