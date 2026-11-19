"""Gera termos.html, a pagina publica de Termos de Uso da Chama Diaria.

O Google Play exige um link de termos de servico de quem se declara
comerciante. O desenho vem do proprio gerar_site.py (ESTILO, SIMBOLO,
FONTES), para as paginas do site nao divergirem entre si.
"""
import html, pathlib, re

AQUI = pathlib.Path(__file__).resolve().parent
EMAIL = 'achamadiaria@gmail.com'
DATA = {'pt': 'Atualizado em 18 de novembro de 2026',
        'en': 'Updated on November 18, 2026',
        'es': 'Actualizado el 18 de noviembre de 2026'}
TITULO = {'pt': 'Termos de Uso', 'en': 'Terms of Use', 'es': 'Términos de uso'}

def _do_gerador(nome):
    """Le a constante do gerar_site.py sem copia-la: uma fonte so para o desenho."""
    fonte = (AQUI / 'gerar_site.py').read_text()
    i = fonte.index('\n%s = ' % nome) + 1
    j = i + len('%s = ' % nome)
    if fonte[j:j + 3] == "'''":
        fim = fonte.index("'''", j + 3) + 3
    else:
        nivel, fim = 0, j
        for k in range(j, len(fonte)):
            if fonte[k] == '(':
                nivel += 1
            elif fonte[k] == ')':
                nivel -= 1
                if nivel == 0:
                    fim = k + 1
                    break
    return eval(fonte[j:fim])

ESTILO = _do_gerador('ESTILO')
SIMBOLO = _do_gerador('SIMBOLO')
FONTES = _do_gerador('FONTES')

TEXTOS = {}

TEXTOS['pt'] = '''1. Quem oferece o app. A Chama Diária é oferecida por Dalto Antonio Vigano Pastro, pessoa física, em Cascavel, Paraná, Brasil. Contato: ''' + EMAIL + '''.

2. O que é o app. A Chama Diária é um aplicativo devocional cristão, com um devocional para cada dia do ano, a Bíblia completa para leitura sem internet e recursos de leitura, favoritos, anotações e lembrete diário. O conteúdo é de natureza devocional e espiritual. Não é aconselhamento médico, psicológico, jurídico ou financeiro, não substitui o acompanhamento de um profissional nem a orientação pastoral presencial.

3. Quem pode usar. O app é livre para todas as idades e não exige cadastro, login ou dados pessoais para funcionar.

4. O que é gratuito e o que é da assinatura. A trilha de boas-vindas, com sete devocionais, e a Bíblia completa estão disponíveis sem pagamento. A assinatura Chama Diária Premium dá acesso ao calendário completo de devocionais do ano e aos temas visuais.

5. Assinatura, cobrança e renovação. As assinaturas são vendidas e cobradas pela loja do seu aparelho, App Store ou Google Play, e não diretamente por mim. Elas se renovam automaticamente ao fim de cada período, pelo preço vigente, até que você cancele. O cancelamento é feito nos ajustes da sua conta na própria loja: ele impede as próximas renovações e, em regra, mantém o acesso até o fim do período já pago, ressalvadas as hipóteses de reembolso, revogação ou outras situações previstas pela legislação aplicável e pelas regras da loja. Eventuais alterações de preço seguem os procedimentos de comunicação e consentimento exigidos pela loja e pela legislação aplicável.

6. Direito de arrependimento e reembolso. Consumidores no Brasil têm, nas contratações feitas fora do estabelecimento comercial, inclusive por meios digitais, o direito de arrependimento previsto no artigo 49 da Lei nº 8.078/1990, o Código de Defesa do Consumidor, que pode ser exercido no prazo de sete dias contados da contratação. Pedidos de cancelamento e de reembolso podem ser encaminhados pelos canais da App Store ou do Google Play, conforme a loja usada, e você também pode escrever para o contato indicado no item 15 para receber orientação sobre os canais disponíveis, sem prejuízo dos seus direitos legais. Para consumidores de outros países valem os direitos de arrependimento, cancelamento e reembolso previstos na legislação obrigatória do seu país, inclusive quando forem mais favoráveis do que o descrito aqui. No Espaço Econômico Europeu e no Reino Unido, a legislação de contratos à distância prevê, em regra, prazo de quatorze dias.

7. Textos bíblicos. O app usa traduções licenciadas de terceiros, creditadas na tela Sobre com a obra, o titular e a licença: em português, a Biblica® Open Nova Bíblia Viva, sob CC BY-SA 4.0; em espanhol, a Biblica® Open Nueva Biblia Viva, sob CC BY-SA 4.0; em inglês, a World English Bible, em domínio público. Os direitos sobre cada tradução e as suas condições de utilização são regidos pela respectiva licença ou situação de domínio público.

8. Devocionais, nome e símbolo. Os textos devocionais, o nome Chama Diária, o símbolo e o desenho do aplicativo são de minha autoria. As imagens de versículo geradas pelo próprio aplicativo podem ser compartilhadas, respeitadas as condições das licenças dos textos bíblicos utilizados. A reprodução ou redistribuição dos textos devocionais fora das funcionalidades de compartilhamento oferecidas pelo aplicativo depende de autorização por escrito, ressalvados os usos permitidos por lei.

9. Uso do app. Você se compromete a não burlar indevidamente os mecanismos de assinatura, não extrair conteúdo em massa em violação aos direitos aplicáveis e não utilizar o aplicativo para fins ilegais, ressalvados os usos permitidos por lei.

10. Disponibilidade e mudanças. A Chama Diária busca oferecer acesso estável aos seus conteúdos e funcionalidades, mas podem ocorrer interrupções temporárias por manutenção, atualização, falha técnica ou circunstância externa. Recursos podem mudar ou ser descontinuados. Se um recurso pago for descontinuado, isso será comunicado antes.

11. Responsabilidade. Os conteúdos devocionais têm finalidade religiosa, educativa e de reflexão pessoal, e não constituem aconselhamento médico, psicológico, jurídico ou financeiro individualizado. Você é responsável pelas decisões pessoais tomadas a partir da leitura e da sua interpretação dos conteúdos, sem prejuízo da responsabilidade legal do fornecedor por defeitos na prestação do serviço ou por informação inadequada. Nenhuma disposição destes termos exclui ou limita responsabilidades que não possam ser legalmente afastadas, incluindo os direitos e as garantias assegurados ao consumidor pela legislação aplicável.

12. Privacidade. O app funciona sem cadastro e guarda os seus dados no próprio aparelho. Os detalhes estão na política de privacidade, publicada neste mesmo site.

13. Mudanças nestes termos. Se estes termos mudarem, a nova versão será publicada nesta mesma página, com a data atualizada.

14. Legislação aplicável e solução de conflitos. Estes termos são interpretados conforme a legislação brasileira, sem prejuízo das normas obrigatórias de proteção ao consumidor aplicáveis no país da sua residência habitual. Eventuais controvérsias podem ser resolvidas pelos meios administrativos, extrajudiciais ou judiciais disponíveis, respeitados os direitos do consumidor e as regras de competência aplicáveis. Nenhuma disposição destes termos limita o seu direito de recorrer às autoridades ou aos órgãos jurisdicionais competentes.

15. Contato. Dúvidas sobre estes termos: ''' + EMAIL + '''.'''

TEXTOS['en'] = '''1. Who offers the app. Chama Diária is offered by Dalto Antonio Vigano Pastro, an individual, in Cascavel, Paraná, Brazil. Contact: ''' + EMAIL + '''.

2. What the app is. Chama Diária is a Christian devotional app with one devotional for every day of the year, the full Bible for offline reading, and reading, favorites, notes and daily reminder features. The content is devotional and spiritual in nature. It is not medical, psychological, legal or financial advice, and it does not replace professional care or in-person pastoral guidance.

3. Who may use it. The app is suitable for all ages and requires no account, login or personal data to work.

4. Free content and subscription content. The welcome track, with seven devotionals, and the full Bible are available at no cost. The Chama Diária Premium subscription unlocks the complete devotional calendar for the year and the visual themes.

5. Subscription, billing and renewal. Subscriptions are sold and charged by your device store, App Store or Google Play, not directly by me. They renew automatically at the end of each period, at the current price, until you cancel. Cancellation is done in your account settings in the store itself: it prevents future renewals and generally preserves access until the end of the paid period, except in cases of refunds, revocations or other circumstances governed by applicable law and store policies. Price changes follow the notice and consent procedures required by the store and by applicable law.

6. Right of withdrawal and refunds. For consumers in Brazil, contracts entered into away from business premises, including by digital means, carry the right of withdrawal under article 49 of Law 8.078/1990, the Brazilian Consumer Protection Code, exercisable within seven days of the purchase. Cancellation and refund requests may be submitted through the App Store or Google Play channels, depending on the store used, and you may also contact the address in item 15 for guidance on the available channels, without prejudice to your legal rights. Consumers in other countries keep the withdrawal, cancellation and refund rights granted by the mandatory law of their country, including where those are more favourable than what is described here. In the European Economic Area and the United Kingdom, distance selling law generally provides a fourteen-day period.

7. Bible texts. The app uses licensed third-party translations, credited on the About screen with the work, the rights holder and the licence: in Portuguese, Biblica® Open Nova Bíblia Viva, under CC BY-SA 4.0; in Spanish, Biblica® Open Nueva Biblia Viva, under CC BY-SA 4.0; in English, the World English Bible, in the public domain. Rights and permitted uses for each translation are governed by its respective licence or public-domain status.

8. Devotionals, name and symbol. The devotional texts, the name Chama Diária, the symbol and the app design are mine. Verse images generated by the app may be shared, subject to the licence terms of the Bible texts used. Reproduction or redistribution of the devotional texts outside the sharing features offered by the app requires written permission, except where permitted by law.

9. Using the app. You agree not to unlawfully circumvent subscription controls, not to extract content in bulk in violation of applicable rights and not to use the app for unlawful purposes, without restricting uses permitted by law.

10. Availability and changes. Chama Diária aims to offer stable access to its content and features, but temporary interruptions may occur due to maintenance, updates, technical failures or external circumstances. Features may change or be discontinued. If a paid feature is discontinued, it will be announced in advance.

11. Liability. The devotional content serves a religious, educational and personal reflection purpose, and does not constitute individualised medical, psychological, legal or financial advice. You are responsible for personal decisions taken from reading and interpreting the content, without prejudice to the provider's legal liability for defects in the service or for inadequate information. Nothing in these terms excludes or limits liability that cannot lawfully be excluded, including the rights and guarantees granted to consumers by applicable law.

12. Privacy. The app works without an account and keeps your data on your own device. The details are in the privacy policy, published on this same site.

13. Changes to these terms. If these terms change, the new version will be published on this same page, with an updated date.

14. Governing law and dispute resolution. These terms are interpreted under Brazilian law, without prejudice to the mandatory consumer protection rules of the country where you habitually reside. Disputes may be resolved through the administrative, out-of-court or judicial means available, respecting consumer rights and the applicable rules of jurisdiction. Nothing in these terms limits your right to turn to the competent authorities or courts.

15. Contact. Questions about these terms: ''' + EMAIL + '''.'''

TEXTOS['es'] = '''1. Quién ofrece la app. Chama Diária es ofrecida por Dalto Antonio Vigano Pastro, persona física, en Cascavel, Paraná, Brasil. Contacto: ''' + EMAIL + '''.

2. Qué es la app. Chama Diária es una aplicación devocional cristiana, con un devocional para cada día del año, la Biblia completa para leer sin conexión y funciones de lectura, favoritos, notas y recordatorio diario. El contenido es de naturaleza devocional y espiritual. No es asesoramiento médico, psicológico, jurídico ni financiero, y no sustituye el acompañamiento de un profesional ni la orientación pastoral presencial.

3. Quién puede usarla. La app es apta para todas las edades y no exige registro, inicio de sesión ni datos personales para funcionar.

4. Qué es gratuito y qué es de la suscripción. La ruta de bienvenida, con siete devocionales, y la Biblia completa están disponibles sin pago. La suscripción Chama Diária Premium da acceso al calendario completo de devocionales del año y a los temas visuales.

5. Suscripción, cobro y renovación. Las suscripciones las vende y cobra la tienda de su dispositivo, App Store o Google Play, y no yo directamente. Se renuevan automáticamente al final de cada período, al precio vigente, hasta que usted cancele. La cancelación se hace en los ajustes de su cuenta en la propia tienda: impide futuras renovaciones y, por regla general, mantiene el acceso hasta el final del período pagado, salvo en casos de reembolso, revocación u otras circunstancias previstas por la legislación aplicable y las normas de la tienda. Los cambios de precio siguen los procedimientos de notificación y consentimiento exigidos por la tienda y la legislación aplicable.

6. Derecho de desistimiento y reembolso. Para los consumidores en Brasil, a las contrataciones hechas fuera del establecimiento comercial, incluso por medios digitales, se aplica el derecho de desistimiento del artículo 49 de la Ley 8.078/1990, el Código de Defensa del Consumidor, que puede ejercerse en el plazo de siete días contados desde la contratación. Las solicitudes de cancelación y de reembolso pueden presentarse por los canales de la App Store o de Google Play, según la tienda utilizada, y usted también puede escribir al contacto indicado en el punto 15 para recibir orientación sobre los canales disponibles, sin perjuicio de sus derechos legales. Para los consumidores de otros países rigen los derechos de desistimiento, cancelación y reembolso previstos en la legislación obligatoria de su país, incluso cuando sean más favorables que lo descrito aquí. En el Espacio Económico Europeo y en el Reino Unido, la legislación de contratos a distancia prevé, por regla general, un plazo de catorce días.

7. Textos bíblicos. La app usa traducciones licenciadas de terceros, acreditadas en la pantalla Acerca de con la obra, el titular y la licencia: en portugués, la Biblica® Open Nova Bíblia Viva, bajo CC BY-SA 4.0; en español, la Biblica® Open Nueva Biblia Viva, bajo CC BY-SA 4.0; en inglés, la World English Bible, en dominio público. Los derechos y usos permitidos de cada traducción se rigen por su respectiva licencia o condición de dominio público.

8. Devocionales, nombre y símbolo. Los textos devocionales, el nombre Chama Diária, el símbolo y el diseño de la aplicación son de mi autoría. Las imágenes de versículo generadas por la propia aplicación pueden compartirse respetando las condiciones de las licencias de los textos bíblicos utilizados. La reproducción o redistribución de los textos devocionales fuera de las funciones de compartir de la aplicación requiere autorización por escrito, salvo los usos permitidos por la ley.

9. Uso de la app. Usted se compromete a no eludir ilícitamente los mecanismos de suscripción, no extraer contenido de forma masiva en violación de los derechos aplicables y no utilizar la aplicación para fines ilegales, sin restringir los usos permitidos por la ley.

10. Disponibilidad y cambios. Chama Diária busca ofrecer acceso estable a sus contenidos y funciones, pero pueden producirse interrupciones temporales por mantenimiento, actualización, fallo técnico o circunstancia externa. Las funciones pueden cambiar o descontinuarse. Si se descontinúa una función de pago, se comunicará con antelación.

11. Responsabilidad. Los contenidos devocionales tienen finalidad religiosa, educativa y de reflexión personal, y no constituyen asesoramiento médico, psicológico, jurídico ni financiero individualizado. Usted es responsable de las decisiones personales tomadas a partir de la lectura y de su interpretación de los contenidos, sin perjuicio de la responsabilidad legal del proveedor por defectos en la prestación del servicio o por información inadecuada. Ninguna disposición de estos términos excluye ni limita responsabilidades que no puedan excluirse legalmente, incluidos los derechos y las garantías reconocidos al consumidor por la legislación aplicable.

12. Privacidad. La app funciona sin registro y guarda sus datos en el propio dispositivo. Los detalles están en la política de privacidad, publicada en este mismo sitio.

13. Cambios en estos términos. Si estos términos cambian, la nueva versión se publicará en esta misma página, con la fecha actualizada.

14. Legislación aplicable y solución de conflictos. Estos términos se interpretan conforme a la legislación brasileña, sin perjuicio de las normas obligatorias de protección al consumidor aplicables en el país de su residencia habitual. Las eventuales controversias pueden resolverse por los medios administrativos, extrajudiciales o judiciales disponibles, respetados los derechos del consumidor y las reglas de competencia aplicables. Ninguna disposición de estos términos limita su derecho a acudir a las autoridades o a los órganos jurisdiccionales competentes.

15. Contacto. Dudas sobre estos términos: ''' + EMAIL + '''.'''

def em_html(idioma):
    blocos = []
    for p in [p.strip() for p in TEXTOS[idioma].split('\n\n') if p.strip()]:
        m = re.match(r'^(\d+)\.\s+([^.]+)\.\s*(.*)$', p, re.S)
        if m:
            blocos.append('<h2><span>%s</span>%s</h2>\n<p>%s</p>'
                          % (m.group(1), html.escape(m.group(2)), html.escape(m.group(3))))
        else:
            blocos.append('<p>%s</p>' % html.escape(p))
    return '\n'.join(blocos)

def pagina(titulo, corpo, descricao):
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{titulo}</title>\n<meta name="description" content="{descricao}">\n'
            '<link rel="icon" href="icone.svg" type="image/svg+xml">\n'
            f'{FONTES}\n<style>{ESTILO}</style>\n</head>\n<body>\n<div class="env">\n{corpo}\n'
            f'<p class="rodape">Chama Diária · Cascavel, Paraná, Brasil<br>'
            f'<a href="mailto:{EMAIL}">{EMAIL}</a></p>\n</div>\n</body>\n</html>\n')

abas, secoes = [], []
for cod, rotulo in (('pt', 'Português'), ('en', 'English'), ('es', 'Español')):
    abas.append('<a href="#%s">%s</a>' % (cod, rotulo))
    secoes.append('<section id="%s"><hr class="regua"><h3>%s</h3><p class="data">%s</p>%s</section>'
                  % (cod, html.escape(TITULO[cod]), html.escape(DATA[cod]), em_html(cod)))

(AQUI / 'termos.html').write_text(pagina(
    'Termos de Uso · Chama Diária',
    '<header>%s<h1>Termos de Uso</h1><p class="sub">Chama Diária · devocional diário</p>'
    '<nav>%s</nav></header>%s' % (SIMBOLO, ''.join(abas), '\n'.join(secoes)),
    'Termos de uso do aplicativo Chama Diária. Português, inglês e espanhol.'))
print('termos.html gerado em', AQUI)
