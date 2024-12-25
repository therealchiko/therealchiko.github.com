import os
import glob
import yaml
from pathlib import Path

def extract_tags_from_posts():
    tags = set()
    posts_path = '_posts'
    
    # Get all markdown files in _posts directory
    post_files = glob.glob(os.path.join(posts_path, '*.md'))
    post_files.extend(glob.glob(os.path.join(posts_path, '*.markdown')))
    
    for post_file in post_files:
        with open(post_file, 'r', encoding='utf-8') as f:
            # Read the YAML front matter
            content = f.read()
            if content.startswith('---'):
                _, front_matter, _ = content.split('---', 2)
                try:
                    post_data = yaml.safe_load(front_matter)
                    if 'tags' in post_data:
                        # Handle both string and list formats
                        post_tags = post_data['tags']
                        if isinstance(post_tags, str):
                            tags.add(post_tags)
                        else:
                            tags.update(post_tags)
                except yaml.YAMLError:
                    print(f"Error parsing YAML in {post_file}")
                    continue
    
    return sorted(tags)

def generate_tag_pages(tags):
    tag_template = """---
layout: tag
tag: {}
---"""
    
    # Create tag directory if it doesn't exist
    Path('tag').mkdir(exist_ok=True)
    
    # Generate a page for each tag
    for tag in tags:
        tag_dir = Path('tag') / tag.lower()
        tag_dir.mkdir(exist_ok=True)
        
        # Create index.html for the tag
        with open(tag_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(tag_template.format(tag))
        
        print(f"Generated page for tag: {tag}")

def main():
    print("Extracting tags from posts...")
    tags = extract_tags_from_posts()
    
    print(f"\nFound {len(tags)} tags:")
    print(", ".join(tags))
    
    print("\nGenerating tag pages...")
    generate_tag_pages(tags)
    
    print("\nTag pages generation complete!")

if __name__ == "__main__":
    main() 