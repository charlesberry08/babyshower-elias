#!/usr/bin/env python3
"""Incrusta los assets en la plantilla y genera babyshower-elias.html."""
import base64, os, sys
here = os.path.dirname(os.path.abspath(__file__))
def data_uri(name, mime):
    p = os.path.join(here, name)
    if not os.path.exists(p):
        return ""
    with open(p, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))
SITIO = "https://charlesberry08.github.io/babyshower-elias/"
OG = "".join([
    '<link rel="canonical" href="%s">\n' % SITIO,
    '<meta property="og:type" content="website">\n',
    '<meta property="og:site_name" content="Baby shower de Elías">\n',
    '<meta property="og:title" content="Baby shower de Elías">\n',
    '<meta property="og:description" content="Invitación al baby shower de Elías">\n',
    '<meta property="og:url" content="%s">\n' % SITIO,
    '<meta property="og:image" content="%sog.jpg">\n' % SITIO,
    '<meta property="og:image:secure_url" content="%sog.jpg">\n' % SITIO,
    '<meta property="og:image:type" content="image/jpeg">\n',
    '<meta property="og:image:width" content="1200">\n',
    '<meta property="og:image:height" content="630">\n',
    '<meta property="og:image:alt" content="Dragón bebé volando junto al nombre Elías">\n',
    '<meta property="og:locale" content="es_MX">\n',
    '<meta name="twitter:card" content="summary_large_image">\n',
    '<meta name="twitter:title" content="Baby shower de Elías">\n',
    '<meta name="twitter:description" content="Invitación al baby shower de Elías">\n',
    '<meta name="twitter:image" content="%sog.jpg">\n' % SITIO,
    '<meta name="theme-color" content="#f7f3ea">\n',
])
html = open(os.path.join(here, "web.template.html"), encoding="utf-8").read()
reemplazos = {
    "__VOLANDO__": data_uri("dragon-volando.webp", "image/webp"),
    "__PEEK__":    data_uri("dragon-volando.webp", "image/webp"),
    "__VERDE__":   data_uri("dragon-verde.webp", "image/webp"),
    "__AZUL__":    data_uri("dragon-azul.webp", "image/webp"),
    "__NUBE__":    data_uri("dragon-nube.webp", "image/webp"),
    "__AUDIO__":   data_uri("lullaby.mp3", "audio/mpeg"),
}
for k, v in reemplazos.items():
    html = html.replace(k, v)
out = os.path.join(here, "babyshower-elias.html")
open(out, "w", encoding="utf-8").write(html)
# Versión completa para GitHub Pages (el artefacto de Claude agrega su propio esqueleto)
pagina = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
          '<style>html{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
          + OG
          + html.replace("</style>\n\n<div class=\"intro\"", "</style>\n</head>\n<body>\n<div class=\"intro\"", 1)
          + "\n</body>\n</html>\n")
open(os.path.join(here, "index.html"), "w", encoding="utf-8").write(pagina)
print("ok", out, round(len(html.encode("utf-8")) / 1024), "KB", "| audio:", "sí" if reemplazos["__AUDIO__"] else "no (falta lullaby.mp3)")
