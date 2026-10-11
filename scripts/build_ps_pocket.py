#!/usr/bin/env python3
"""Build the P’s Pocket static pages; Python 3 standard library only.

Run from any directory. The generated HTML is committed alongside its source,
so GitHub Pages requires no custom workflow or runtime build step.
"""
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'ps-pocket'
DATA = json.loads((SITE / 'content.json').read_text(encoding='utf-8'))
LOCALES = DATA['locales']
BASE = DATA['base_url'].rstrip('/')
EMAIL = DATA['support_email']
REFERENCES = {
    'apple': 'https://www.apple.com/legal/privacy/en-ww/',
    'microsoft': 'https://www.microsoft.com/privacy/privacystatement',
    'github': 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement',
}


def path(locale, page):
    suffix = '' if page == 'home' else f'{page}.html'
    return f'/ps-pocket/{locale}/{suffix}'


def inline(text, content):
    """Only allow known link markers; all author text is escaped as plain text."""
    def link(match):
        key = match.group(1)
        if key == 'email':
            return f'<a href="mailto:{escape(EMAIL, quote=True)}">{escape(EMAIL)}</a>'
        return f'<a href="{REFERENCES[key]}" rel="noreferrer">{escape(content["privacy"]["references"][key])}</a>'
    return re.sub(r'\[(email|apple|microsoft|github)\]', link, escape(text))


def paragraphs(items, content):
    return '\n'.join(f'<p>{inline(item, content)}</p>' for item in items)


def cards(items):
    return '\n'.join(f'<article class="feature"><h3>{escape(title)}</h3><p>{escape(text)}</p></article>' for title, text in items)


def promo_device(image, tone, alt='', inverted=False, eager=False):
    svg = (SITE / 'assets/promo/shell.svg').read_text()
    svg = svg.replace('<svg ', '<svg class="promo-shell" aria-hidden="true" ')
    png = (SITE / 'assets/promo' / image).read_bytes()
    width, height = int.from_bytes(png[16:20], 'big'), int.from_bytes(png[20:24], 'big')
    loading = 'eager' if eager else 'lazy'
    priority = ' fetchpriority="high"' if eager else ''
    turned = ' device-inverted' if inverted else ''
    return f'<div class="promo-device {tone}{turned}">{svg}<img class="promo-screen" src="/ps-pocket/assets/promo/{image}" width="{width}" height="{height}" alt="{escape(alt, quote=True)}" loading="{loading}" decoding="async"{priority}></div>'


def line_title(lines):
    return ''.join(f'<span>{escape(line)}</span>' for line in lines)


def home(locale, c):
    h, v = c['home'], c['home']['presentation']
    multi = ''.join(promo_device(f'iphone-multi-screen-{i}.png', tone) for i, tone in enumerate(['shell-peach', 'shell-blue', 'shell-lilac', 'shell-rose'], 1))
    facing = promo_device('iphone-face-screen-top.png', 'shell-rose', inverted=True) + promo_device('iphone-face-screen-bottom.png', 'shell-blue')
    facts = ''.join(f'<li>{escape(text)}</li>' for text in v['facts'])
    steps = ''.join(f'<li><span>{i:02}</span>{escape(text)}</li>' for i, text in enumerate(v['steps'], 1))
    turn_arc = '<svg class="turn-arc" viewBox="0 0 180 200" aria-hidden="true"><path d="M152 14C15-2 0 85 76 108s68 72-31 69" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 9"/><path d="m67 159-24 18 22 11" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'''<section class="home-hero" aria-labelledby="page-title">
  <div class="hero-copy"><p class="eyebrow">P’s Pocket</p><h1 id="page-title" class="hero-title">{line_title(v['headline'])}</h1><p class="lead">{escape(h['lead'])}</p><div class="actions"><a class="button primary" href="{path(locale, 'support')}">{escape(h['primary'])}<span aria-hidden="true">↗</span></a><a class="button secondary" href="{path(locale, 'privacy')}">{escape(h['secondary'])}</a></div></div>
  <figure class="hero-visual"><div class="hero-stage">{promo_device('iphone-multi-screen-1.png', 'shell-rose hero-device-secondary')}{promo_device('iphone-screen.png', 'shell-honey hero-device-main', h['screen_alt'], eager=True)}</div><figcaption>{escape(h['screen_caption'])}</figcaption></figure>
</section>
<ul class="home-facts" aria-label="P’s Pocket">{facts}</ul>
<section class="product-scene multi-section" aria-labelledby="multi-title"><div class="scene-inner"><div class="multi-scene product-art" aria-hidden="true">{multi}</div><div class="scene-copy"><p class="eyebrow">{escape(v['multi_kicker'])}</p><h2 id="multi-title">{line_title(v['multi_title'])}</h2><p>{escape(v['multi_text'])}</p></div></div></section>
<section class="product-scene face-section" aria-labelledby="face-title"><div class="scene-inner"><div class="scene-copy"><p class="eyebrow">{escape(v['face_kicker'])}</p><h2 id="face-title">{line_title(v['face_title'])}</h2><p>{escape(v['face_text'])}</p></div><div class="facing-scene product-art" aria-hidden="true">{facing}<span class="facing-angle">180°</span>{turn_arc}</div></div></section>
<section class="product-scene lcd-section" aria-labelledby="lcd-title"><div class="scene-inner"><div class="lcd-art"><img src="/ps-pocket/assets/promo/iphone-pixel-detail.png" width="270" height="270" loading="lazy" decoding="async" alt="{escape(v['lcd_alt'], quote=True)}"></div><div class="scene-copy"><p class="eyebrow">{escape(v['lcd_kicker'])}</p><h2 id="lcd-title">{line_title(v['lcd_title'])}</h2><p>{escape(v['lcd_text'])}</p></div></div></section>
<section class="getting-started" aria-labelledby="intro-title"><div class="tutorial-intro"><img class="tutorial-mascot" src="/ps-pocket/assets/promo/assistant-wave.png" width="64" height="64" alt="" loading="lazy"><div><h2 id="intro-title">{escape(h['intro_title'])}</h2><p>{escape(h['intro'])}</p><a class="text-link" href="{path(locale, 'support')}#tutorial">{escape(v['help_link'])}<span aria-hidden="true"> →</span></a></div></div><ol class="start-steps">{steps}</ol></section>
<section class="records-section" aria-labelledby="records-title"><p class="eyebrow">{escape(v['records_kicker'])}</p><h2 id="records-title">{escape(h['features'][2][0])}</h2><p>{escape(h['features'][2][1])}</p></section>
<aside class="firmware-footnote"><h2>{escape(h['note_title'])}</h2><p>{escape(h['note'])}</p></aside>'''


def support(locale, c):
    s = c['support']
    mailto = f'mailto:{EMAIL}?subject={quote(c["ui"]["support_subject"])}'
    faq = '\n'.join(f'''<details id="{anchor}" class="faq"><summary>{escape(question)}<span class="toggle" aria-hidden="true"></span></summary><div class="answer">{paragraphs(answer, c)}</div></details>''' for anchor, question, answer in s['faq'])
    return f'''<header class="page-heading"><p class="eyebrow">P’s Pocket</p><h1 id="page-title">{escape(s['title'])}</h1><p class="lead">{escape(s['lead'])}</p></header>
<section class="contact-card" aria-labelledby="contact-title"><div><h2 id="contact-title">{escape(s['contact_title'])}</h2><p>{escape(s['contact_text'])}</p><a class="email-address" href="mailto:{EMAIL}">{EMAIL}</a></div><a class="button primary" href="{escape(mailto, quote=True)}">{escape(c['ui']['email'])}<span aria-hidden="true">↗</span></a></section>
<section class="faq-section" aria-labelledby="faq-title"><h2 id="faq-title">{escape(s['faq_title'])}</h2>{faq}</section>
<aside class="note"><h2>{escape(s['privacy_title'])}</h2><p>{escape(s['privacy_text'])}</p><a class="text-link" href="{path(locale, 'privacy')}">{escape(c['nav']['privacy'])}<span aria-hidden="true"> →</span></a></aside>'''


def privacy(locale, c):
    p = c['privacy']
    toc = '\n'.join(f'<li><a href="#{anchor}">{escape(title)}</a></li>' for anchor, title, _ in p['sections'])
    body = '\n'.join(f'''<section id="{anchor}" class="policy-section" aria-labelledby="{anchor}-title"><p class="section-number" aria-hidden="true">{number:02}</p><h2 id="{anchor}-title">{escape(title)}</h2>{paragraphs(text, c)}</section>''' for number, (anchor, title, text) in enumerate(p['sections'], 1))
    return f'''<header class="page-heading"><p class="eyebrow">P’s Pocket</p><h1 id="page-title">{escape(p['title'])}</h1><p class="lead">{escape(p['lead'])}</p><p class="updated">{escape(c['ui']['updated'])} <time datetime="{DATA['updated']}">{DATA['updated']}</time></p></header>
<div class="policy-layout"><aside class="toc"><nav class="toc-desktop" aria-label="{escape(c['ui']['contents'], quote=True)}"><h2>{escape(c['ui']['contents'])}</h2><ol>{toc}</ol></nav><details class="toc-mobile"><summary>{escape(c['ui']['contents'])}<span class="toggle" aria-hidden="true"></span></summary><nav aria-label="{escape(c['ui']['contents'], quote=True)}"><ol>{toc}</ol></nav></details></aside><article class="policy-body" aria-label="{escape(p['title'], quote=True)}">{body}</article></div>'''


def current(value, active):
    return f' aria-current="{value}"' if active else ''


def render(locale, page, automatic=False):
    c = LOCALES[locale]
    title = c['nav']['home'] if page == 'home' else c[page]['title']
    description = c[page]['lead']
    canonical = BASE + path(locale, page)
    nav = ''.join(f'<a href="{path(locale, item)}"{current("page", item == page)}>{escape(label)}</a>' for item, label in c['nav'].items())
    language_links = ''.join(f'<a lang="{key}" hreflang="{key}" href="{path(key, page)}"{current("true", key == locale)}>{escape(LOCALES[key]["label"])}</a>' for key in LOCALES)
    alternates = '\n'.join(f'  <link rel="alternate" hreflang="{key}" href="{BASE + path(key, page)}">' for key in LOCALES)
    aliases = '' if page == 'home' else page + '.html'
    main = {'home': home, 'support': support, 'privacy': privacy}[page](locale, c)
    return f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <meta name="referrer" content="no-referrer">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; img-src 'self'; script-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
  <title>{escape(title)} · P’s Pocket</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:title" content="{escape(title, quote=True)} · P’s Pocket">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/ps-pocket/assets/app-icon.png">
  <link rel="canonical" href="{canonical}">
{alternates}
  <link rel="alternate" hreflang="x-default" href="{BASE}/ps-pocket/{aliases}">
  <link rel="icon" href="/ps-pocket/assets/app-icon.png" type="image/png">
  <link rel="stylesheet" href="/ps-pocket/assets/site.css">
  <script src="/ps-pocket/assets/language.js" data-auto-language="{str(automatic).lower()}"></script>
</head>
<body class="page-{page}">
<a class="skip-link" href="#main">{escape(c['ui']['skip'])}</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="{path(locale, 'home')}" aria-label="{escape(c['ui']['back'], quote=True)}"><img src="/ps-pocket/assets/app-icon.png" width="40" height="40" alt=""><span>P’s Pocket</span></a><nav class="main-nav" aria-label="{escape(c['ui']['navigation'], quote=True)}">{nav}</nav></div></header>
<div class="language-bar"><nav aria-label="{escape(c['ui']['languages'], quote=True)}">{language_links}</nav></div>
<main id="main" class="container" tabindex="-1">
{main}
</main>
<footer class="site-footer"><div><span>{escape(c['ui']['footer'])}</span><a href="mailto:{EMAIL}">{EMAIL}</a></div><nav aria-label="{escape(c['ui']['navigation'], quote=True)}"><a href="{path(locale, 'support')}">{escape(c['nav']['support'])}</a><a href="{path(locale, 'privacy')}">{escape(c['nav']['privacy'])}</a><a href="/">Meets Link ↗</a></nav><p class="footer-name-note">{escape(c["ui"]["name_origin"])}</p></footer>
</body>
</html>
'''


for locale in LOCALES:
    folder = SITE / locale
    folder.mkdir(parents=True, exist_ok=True)
    for page in ['home', 'support', 'privacy']:
        name = 'index.html' if page == 'home' else page + '.html'
        (folder / name).write_text(render(locale, page), encoding='utf-8')
# Shared entry pages choose a browser language; complete English HTML remains the no-script fallback.
for page in ['home', 'support', 'privacy']:
    name = 'index.html' if page == 'home' else page + '.html'
    (SITE / name).write_text(render('en-US', page, automatic=True), encoding='utf-8')

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for locale in LOCALES:
    for page in ['home', 'support', 'privacy']:
        sitemap.append(f'  <url><loc>{escape(BASE + path(locale, page))}</loc><lastmod>{DATA["updated"]}</lastmod></url>')
sitemap.append('</urlset>')
(SITE / 'sitemap.xml').write_text('\n'.join(sitemap) + '\n', encoding='utf-8')
print(f'Built {len(LOCALES) * 3 + 3} HTML pages, plus sitemap.')
