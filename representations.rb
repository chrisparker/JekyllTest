module Representations
  class RepresentationsGenerator < Jekyll::Generator
    safe true

    def generate(site)
      theta = site.data['theta']
      caboodle = theta[0]
	  
      dir = '.'
	  
	  caboodle.each do |name|
	    site.pages << Jekyll::PageWithoutAFile.new(site, site.source, dir, name).tap do |file|
	      file.content = '<p>abcdef ghji</p>'
          file.data.merge!(
            "layout"     => nil,
            "sitemap"    => false,
          )
          file.output
        end
      end
    end
  end
end