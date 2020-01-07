---
title: AWS
author: linuxtm
layout: page
slug: aws
tags:
  - comenzi aws
  - tutoriale aws
  - aws tips
  - aws cloud tutorial
  - tutoriale cloud aws
  - aws tutoriale cli
  - tutoriale cloud
  - comenzi aws
  - tutoriale linux
---
<div class="home">
  <h1 class="page-heading">Posts</h1>
  <ul class="post-list">
    {% for post in site.categories.AWS %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>
</div>
