import os
import glob
import yaml
from pathlib import Path

def extract_taxonomies_from_posts():
    tags = set()
    categories = set()
    posts_path = '_posts'
    
    # Get all markdown files in _posts directory
    post_files = glob.glob(os.path.join(posts_path, '*.md'))
    post_files.extend(glob.glob(os.path.join(posts_path, '*.markdown')))
    
    for post_file in post_files:
        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                _, front_matter, _ = content.split('---', 2)
                try:
                    post_data = yaml.safe_load(front_matter)
                    # Handle tags
                    if 'tags' in post_data:
                        post_tags = post_data['tags']
                        if isinstance(post_tags, str):
                            tags.add(post_tags)
                        else:
                            tags.update(post_tags)
                    # Handle categories
                    if 'categories' in post_data:
                        post_cats = post_data['categories']
                        if isinstance(post_cats, str):
                            categories.add(post_cats)
                        else:
                            categories.update(post_cats)
                except yaml.YAMLError:
                    print(f"Error parsing YAML in {post_file}")
                    continue
    
    return sorted(tags), sorted(categories)

def generate_taxonomy_pages(items, type_name):
    template = """---
layout: {}
{}: {}
---"""
    
    # Create directory if it doesn't exist
    Path(type_name).mkdir(exist_ok=True)
    
    # Generate a page for each item
    for item in items:
        item_dir = Path(type_name) / item.lower()
        item_dir.mkdir(exist_ok=True)
        
        # Create index.html for the item
        with open(item_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(template.format(type_name, type_name.rstrip('s'), item))
        
        print(f"Generated page for {type_name.rstrip('s')}: {item}")

def main():
    print("Extracting tags and categories from posts...")
    tags, categories = extract_taxonomies_from_posts()
    
    print(f"\nFound {len(tags)} tags:")
    print(", ".join(tags))
    
    print(f"\nFound {len(categories)} categories:")
    print(", ".join(categories))
    
    print("\nGenerating tag pages...")
    generate_taxonomy_pages(tags, 'tag')
    
    print("\nGenerating category pages...")
    generate_taxonomy_pages(categories, 'category')
    
    print("\nAll pages generation complete!")

if __name__ == "__main__":
    main() 