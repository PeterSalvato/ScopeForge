Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# SEO & Semantics Rules

This document defines all metadata, schema, and semantic-packing rules required for the Savepoint publishing system. These rules must be enforced structurally before deployment.

---

## 1. Meta & OpenGraph Tags

Every page’s `<head>` must include:

```html
<title>[Page Title] | Peter Salvato</title>
<meta name="description" content="[155-char summary]">

<meta property="og:title"         content="[Page Title] | Peter Salvato">
<meta property="og:description"   content="[155-char summary]">
<meta property="og:url"           content="https://petersalvato.com/[path]/">
<meta property="og:image"         content="https://petersalvato.com/assets/og/[image].jpg">
<meta property="og:type"          content="website|article|software">
<meta name="twitter:card"         content="summary_large_image">

✅ All tags must be present
❌ No tag may be missing or empty
2. JSON-LD Blocks

Before </head>, every page must include a valid JSON-LD <script> block matching its type:

    Home → @type: WebSite

    Journal → @type: Article

    System → @type: SoftwareApplication

Blocks must be:

    Structurally valid JSON

    Fully filled out

    Located in <head>, not <body>

3. ARIA & Data Attributes

Key structural elements must be semantically annotated:

<body data-entity="PageType">
  <nav role="navigation" aria-label="Main"></nav>
  <main role="main">
    <section data-entity="System">…</section>
    <article data-entity="JournalEntry">…</article>
  </main>
  <footer role="contentinfo"></footer>
</body>

4. Microformats2

Journal entries must include:

<article class="h-entry">
  <time class="dt-published" datetime="YYYY-MM-DD">…</time>
  <a class="p-author h-card" href="/about/">Peter Salvato</a>
</article>

5. Site Search Schema

All pages with @type: WebSite must include:

"potentialAction":{
  "@type":"SearchAction",
  "target":"https://petersalvato.com/?s={search_term_string}",
  "query-input":"required name=search_term_string"
}

6. Sitemap

The site must expose:

<link rel="sitemap" href="/sitemap.html">

OR a public page at /sitemap.html.
7. Pagination

If a page is part of a paginated sequence, it must include:

<link rel="prev" href="[previous-page-url]">
<link rel="next" href="[next-page-url]">

8. FAQ / HowTo Schema

Tutorials or FAQs must include:

<div itemscope itemtype="https://schema.org/FAQPage">

OR use HowTo schema.
9. RDFa Concept Types

Semantic pages may include:

<section typeof="skos:Concept" resource="#Savepoint">

This is optional, but if used, must be valid RDFa.
10. JSON-LD Dataset

A page at /data.jsonld must contain a valid schema @type: Dataset listing all pages.
11. Microformats2 Index Markup

Index pages must mark content items as:

<article class="h-entry">…</article>

12. hreflang Support

If translations exist, include:

<link rel="alternate" hreflang="fr" href="https://petersalvato.com/fr/">

13. oEmbed Declaration

Embeddable pages must include:

<link rel="alternate" type="application/json+oembed" href="/oembed?url=[page]">

14. WebMention / Pingback

If enabled, pages must include:

<link rel="pingback" href="https://petersalvato.com/webmention">

🔎 Fixture Reference

See:

    fixtures/meta-opengraph/

    fixtures/jsonld-home/

    fixtures/data-attributes/

    Additional folders for each rule above