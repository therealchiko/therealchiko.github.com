#!/bin/bash

# Create tag directory
mkdir -p tag

# Get list of tags from posts
tags=$(grep -h "tags:" _posts/*.md | sed 's/tags: \[\(.*\)\]/\1/' | tr ',' '\n' | sed 's/[][ ]//g' | sort -u)

# Generate a page for each tag
for tag in $tags
do
  tag_dir="tag/${tag}"
  mkdir -p $tag_dir
  
  # Create index.html for the tag
  cat > "${tag_dir}/index.html" << EOF
---
layout: tag
tag: ${tag}
---
EOF
done 