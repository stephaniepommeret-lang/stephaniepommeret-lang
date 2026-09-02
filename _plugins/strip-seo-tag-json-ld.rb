# frozen_string_literal: true
#
# jekyll-seo-tag génère un bloc JSON-LD qui décrit chaque page de collection
# comme un « BlogPosting », avec une date déduite du système de fichiers.
# Ce n'est ni une date de création d'œuvre ni une date d'exposition : c'est
# faux, et les moteurs comme les LLM le lisent.
#
# Ce hook retire uniquement ce bloc JSON-LD. Tout le reste de jekyll-seo-tag
# (title, description, canonical, Open Graph, Twitter Cards) est conservé.
# Les données structurées correctes sont produites par _includes/structured-data.html.

Jekyll::Hooks.register %i[pages documents], :post_render do |doc|
  next unless doc.output_ext == ".html"
  next unless doc.output.is_a?(String)
  next unless doc.output.include?("<!-- Begin Jekyll SEO tag")

  doc.output = doc.output.sub(
    %r{
      (<!--\ Begin\ Jekyll\ SEO\ tag.*?)
      (\s*<script\ type="application/ld\+json">.*?</script>)
      (.*?<!--\ End\ Jekyll\ SEO\ tag)
    }mx,
    '\1\3'
  )
end
