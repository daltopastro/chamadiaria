"""Gera as paginas publicas da Chama Diaria a partir da politica que esta no app.

Fonte da politica: lib/pages/privacy_page.dart (_pt, _en, _es). Assim a pagina
publicada e o texto dentro do app nunca divergem.
"""
import html, pathlib, re

PROJETO = pathlib.Path('/home/claude/dev/chama_diaria')
SAIDA = pathlib.Path(__file__).resolve().parent
def _constante(nome):
    """Le uma constante de lib/config/links.dart, para a pagina publicada e o
    texto dentro do app nunca divergirem."""
    fonte = (PROJETO / 'lib/config/links.dart').read_text()
    m = re.search(r"const String %s =\s*'([^']*)'" % nome, fonte)
    assert m, 'constante %s nao encontrada em links.dart' % nome
    return m.group(1)

NOME = _constante('kNomeDoResponsavel')
EMAIL = _constante('kEmailDeContato')
# Credito de autoria nas telas: o nome pelo qual ele e conhecido, nao o legal.
PASTORAL = 'Pr. Dalto Pastro'
MARCADORES = {'[NOME COMPLETO]': NOME, '[FULL NAME]': NOME, '[NOMBRE COMPLETO]': NOME,
              '[E-MAIL DO APP]': EMAIL, '[APP E-MAIL]': EMAIL, '[CORREO DE LA APP]': EMAIL}

def texto_da_politica(idioma):
    fonte = (PROJETO / 'lib/pages/privacy_page.dart').read_text()
    m = re.search(r"const String _%s = '''(.*?)''';" % idioma, fonte, re.S)
    assert m, 'politica %s nao encontrada' % idioma
    t = m.group(1)
    for k, v in MARCADORES.items():
        t = t.replace(k, v)
    resto = re.findall(r'\[[^\]]+\]', t)
    assert not resto, 'sobrou marcador em %s: %s' % (idioma, resto)
    return t

def em_html(idioma):
    partes = [p.strip() for p in texto_da_politica(idioma).split('\n\n') if p.strip()]
    cabeca = partes[0].split('\n')
    titulo, data = cabeca[0], (cabeca[1] if len(cabeca) > 1 else '')
    blocos = []
    for p in partes[1:]:
        m = re.match(r'^(\d+)\.\s+([^.]+)\.\s*(.*)$', p, re.S)
        if m:
            blocos.append('<h2><span>%s</span>%s</h2>\n<p>%s</p>'
                          % (m.group(1), html.escape(m.group(2)), html.escape(m.group(3))))
        else:
            blocos.append('<p>%s</p>' % html.escape(p))
    return html.escape(titulo), html.escape(data), '\n'.join(blocos)

SIMBOLO = ('<svg class="marca" viewBox="0 0 100 100" aria-hidden="true">'
  '<g transform="translate(10 15.2) scale(0.8)">'
  '<clipPath id="cc"><rect x="0" y="-100" width="100" height="300"/></clipPath>'
  '<g clip-path="url(#cc)"><path class="chama" transform="translate(0 -22) translate(50 50) scale(0.95) translate(-50 -50)" '
  'd="M 48.5 88.4 C 64 88.4 74 79 69 64 C 66 55.5 57.5 47.5 55 35 C 53.5 27 54.5 18.5 56.5 9 '
  'C 42 21 31 38 31 58 C 31 76 37 88.4 48.5 88.4 Z"/></g>'
  '<path class="folha" d="M 48.3 69 Q 27.17 57.12 8.5 62 L 8.5 77 Q 27.17 75 48.3 90 Z"/>'
  '<path class="folha" d="M 51.7 69 Q 72.82 61.4 91.5 62 L 91.5 77 Q 72.82 75 51.7 90 Z"/></g></svg>')

ESTILO = '''
:root{--papel:#F7F0E4;--marfim:#FFF9F0;--tinta:#302820;--marrom:#69584A;--ambar:#C98B32;--borda:rgba(48,40,32,.16)}
@media (prefers-color-scheme:dark){:root{--papel:#171310;--marfim:#1E1915;--tinta:#FFF9F0;--marrom:#C9BBAA;--ambar:#E0AA55;--borda:rgba(255,249,240,.16)}}
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);font:16px/1.65 "DM Sans",system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-text-size-adjust:100%}
.env{max-width:680px;margin:0 auto;padding:0 20px 72px}
header{text-align:center;padding:56px 0 10px}
.marca{width:64px;height:64px;display:block;margin:0 auto 18px}
.marca .chama{fill:var(--ambar)}.marca .folha{fill:var(--tinta)}
h1{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:clamp(34px,7vw,46px);line-height:1.12;margin:0 0 6px}
.sub{color:var(--marrom);margin:0;font-size:15px}
.regua{width:64px;height:2px;background:var(--ambar);border:0;margin:30px auto}
h2{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:23px;line-height:1.25;margin:32px 0 8px;display:flex;gap:11px;align-items:baseline}
h2 span{font-family:"DM Sans",sans-serif;font-size:12px;font-weight:500;letter-spacing:.12em;color:var(--ambar);min-width:1.4em}
h2.simples{display:block}
h3{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:27px;margin:0 0 4px;text-align:center;line-height:1.2}
p{margin:0 0 14px}
a{color:var(--tinta);text-decoration-color:var(--ambar);text-underline-offset:3px}
nav{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:26px 0 0}
nav a{display:inline-block;padding:8px 16px;border:1px solid var(--borda);border-radius:999px;font-size:13.5px;text-decoration:none;color:var(--marrom)}
nav a:hover{border-color:var(--ambar);color:var(--tinta)}
.cartao{background:var(--marfim);border:1px solid var(--borda);border-radius:18px;padding:22px 24px;margin:28px 0}
.rodape{margin-top:54px;padding-top:22px;border-top:1px solid var(--borda);color:var(--marrom);font-size:13.5px;text-align:center}
section{scroll-margin-top:16px}
.data{text-align:center;color:var(--marrom);font-size:13.5px;margin:0 0 20px}
'''
FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">')

def pagina(titulo, corpo, descricao):
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{titulo}</title>\n<meta name="description" content="{descricao}">\n'
            '<link rel="icon" href="icone.svg" type="image/svg+xml">\n'
            f'{FONTES}\n<style>{ESTILO}</style>\n</head>\n<body>\n<div class="env">\n{corpo}\n'
            f'<p class="rodape">Chama Diária · {NOME} · Cascavel, Paraná, Brasil<br>'
            f'<a href="mailto:{EMAIL}">{EMAIL}</a></p>\n</div>\n</body>\n</html>\n')

secoes, abas = [], []
for cod, rotulo in (('pt', 'Português'), ('en', 'English'), ('es', 'Español')):
    titulo, data, corpo = em_html(cod)
    abas.append('<a href="#%s">%s</a>' % (cod, rotulo))
    secoes.append('<section id="%s"><hr class="regua"><h3>%s</h3><p class="data">%s</p>%s</section>'
                  % (cod, titulo, data, corpo))

(SAIDA / 'privacidade.html').write_text(pagina(
    'Política de privacidade · Chama Diária',
    '<header>%s<h1>Política de privacidade</h1><p class="sub">Chama Diária · devocional diário</p>'
    '<nav>%s</nav></header>%s' % (SIMBOLO, ''.join(abas), '\n'.join(secoes)),
    'Como o aplicativo Chama Diária trata as suas informações. Português, inglês e espanhol.'))

inicio = f'''<header>{SIMBOLO}<h1>Chama Diária</h1>
<p class="sub">Um devocional para cada dia</p></header>
<hr class="regua">
<p>A Chama Diária oferece um devocional para cada dia do ano. Em poucos minutos você lê o versículo do dia, uma explicação clara, uma aplicação prática para a vida e uma oração para fechar o momento com Deus. A Bíblia completa fica no aparelho e funciona sem internet.</p>
<p>O app está em português, inglês e espanhol, cada idioma com a sua tradução bíblica.</p>
<div class="cartao">
<h2 class="simples" style="margin-top:0">Suporte</h2>
<p>Dúvidas, problemas ou pedidos sobre os seus dados: escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p style="margin:0"><a href="privacidade.html">Leia a política de privacidade</a></p>
</div>
<p style="color:var(--marrom);font-size:14px">Idealização e revisão pastoral: {PASTORAL}. A Chama Diária é um projeto pessoal e não é uma publicação oficial de nenhuma igreja ou denominação.</p>
'''
(SAIDA / 'index.html').write_text(pagina('Chama Diária · Devocional diário', inicio,
    'Chama Diária: um devocional para cada dia do ano, com versículo, explicação, aplicação e oração, e a Bíblia completa.'))
# O icone ja esta na pasta do site; so e regravado se a fonte existir.
_fonte_icone = pathlib.Path('/home/claude/dev/logo_limpo/icone_chama_diaria.svg')
if _fonte_icone.is_file():
    (SAIDA / 'icone.svg').write_text(_fonte_icone.read_text())
print('paginas geradas em', SAIDA)
