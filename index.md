---
author: linuxtm
layout: page
tags:
  - tutoriale linux
  - tutoriale administrare linux
  - tutoriale ubuntu
  - comenzi linux
---
<div class="home">
  <h1 class="page-heading">Posts</h1>
  <ul class="post-list">
   {% for post in site.posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
         <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
         </h2>
	 <p class="post-excerpt">{{ post.content | strip_html | truncatewords: 30 }}</p>
      </li>
   {% endfor %}
  </ul>
</div>
