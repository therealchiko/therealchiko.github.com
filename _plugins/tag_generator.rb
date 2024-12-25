module Jekyll
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      tags = site.posts.docs.flat_map { |post| post.data['tags'] || [] }.uniq
      tags.each do |tag|
        site.pages << TagPage.new(site, site.source, tag)
      end
    end
  end

  class TagPage < Page
    def initialize(site, base, tag)
      @site = site
      @base = base
      @dir = File.join('tag', tag.downcase)
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag.html')
      self.data['layout'] = 'tag'
      self.data['tag'] = tag
      self.data['title'] = "Posts tagged with ##{tag}"
      self.data['pagination'] = {
        'enabled' => true,
        'tag' => tag,
        'per_page' => 9,
        'permalink' => '/page/:num/'
      }
    end
  end
end 