---
layout: page
title: Posts
---

{% for post in site.posts %} 
### [ {{ post.title }} ]({{ post.url }})
  
 {{ post.date | date_to_string }}
 
 {{ post.excerpt | remove: '<p>' | remove: '</p>' }}
    {% for categories in post.categories %}
        {{ categories.category }}
    {% endfor %}
{% endfor %}