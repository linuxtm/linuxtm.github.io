---
title: Tutoriale
author: linuxtm
layout: page
slug: tutoriale
tags:
  - tutoriale linux
  - tutoriale administrare linux
  - tutoriale ubuntu
  - comenzi linux
---
<div class="home">

  <h1 class="page-heading">Posts</h1>

  <ul class="post-list">
    {% for post in site.categories.Tutoriale %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
	 <p class="post-excerpt">{{ post.excerpt }}</p>
      </li>
    {% endfor %}
  </ul>

</div>
