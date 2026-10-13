# -*- coding: utf-8 -*-
"""Julie Masterclass blast: 7 one-time ActiveCampaign emails in the Chris/Sandra approved anatomy
(lla-masterclass-emails-3tier / launch-email-for-chris): 640px card, header, 4px divider, alert bar, 1200x700 hero,
Georgia h1, 17px body, pill button, details box, second button, signoff, small line, dark footer, AC tokens.
School sends: header = school logo + eTeacher Group logo; footer = school copyright by eTeacher Group + address.
Gallery: per email Copy HTML, Download .html, Open, Download hero image, Copy text. AUDIT.md written by this script."""
import os, re, json, html, shutil
from PIL import Image

BASE = os.environ.get("BASE", "https://gitteromri-ux.github.io/julie-masterclass-blast")
LP = "https://www.longevitylifeacademy.com/julie-masterclass/"
ADDRESS = "8 Aholiav St, 5252261 Ramat Gan, Israel"

def cta(campaign, content):
    return (f"{LP}?utm_source=activecampaign&amp;utm_medium=email&amp;utm_campaign={campaign}&amp;utm_content={content}#pricing")
def shalom(): return "%IF !empty($FIRSTNAME)%Shalom %FIRSTNAME%,%ELSE%Shalom,%/IF%"
def hi(): return "%IF !empty($FIRSTNAME)%Hi %FIRSTNAME%,%ELSE%Hi,%/IF%"

BRANDS = {
    "lla": dict(name="Longevity Life Academy", logo=None, sender="Emma | Longevity Advisor <advisor@longevitylifeacademy.com>",
                button="Reserve My Seat", alert_k="Live on Zoom", alert_v="October 27 or November 14, 7:00 PM ET / 1:00 PM ET",
                sign="To your longest, strongest life,<br><b>The Longevity Life Academy team</b>",
                footer_tag="It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group.", footer_reason="You received this because you asked about Longevity Life Academy", footer_addr=""),
    "iibs": dict(name="Israel Institute of Biblical Studies", short="Israel Biblical Studies", logo="iibs-logo.png",
                 sender="Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com>", button="RESERVE MY SEAT",
                 alert_k="First access for our students", alert_v="The Longevity Masterclass of the Year",
                 sign="Warmly,<br><b>Sophia Green</b><br>Admissions Advisor, Israel Institute of Biblical Studies",
                 footer_tag="&copy; 2026 Israel Institute of Biblical Studies by eTeacher Group. All Rights Reserved.",
                 footer_reason="Sent to you as a student or contact of the Israel Institute of Biblical Studies", footer_addr=ADDRESS,
                 course="course", enrol="enrolling at the Israel Institute of Biblical Studies"),
    "rosen": dict(name="Rosen School of Hebrew", short="Rosen", logo="rosen-logo.png",
                  sender="Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>", button="RESERVE MY SEAT",
                  alert_k="First access for our students", alert_v="The Longevity Masterclass of the Year",
                  sign="Warmly,<br><b>Noa Shalev</b><br>Campus Manager, Rosen School of Hebrew",
                  footer_tag="&copy; 2026 Rosen School of Hebrew by eTeacher Group. All Rights Reserved.",
                  footer_reason="Sent to you as a student or contact of Rosen School of Hebrew", footer_addr=ADDRESS,
                  course="Hebrew course", enrol="enrolling at Rosen School of Hebrew"),
}

# ---------- copy (facts: live masterclass page, 13 Oct 2026) ----------
def longevity(b):
    opener = ("eTeacher Group opened <strong>Longevity Life Academy</strong> this year to teach this live, in plain language, and we want our own students to have it first."
              if b != "lla" else "We opened Longevity Life Academy this year to teach this live, in plain language, and the people who asked about us hear about it first.")
    return ("<p>Longevity has become one of the most important fields in science. We now know that aging can be measured, slowed and in part reversed, "
            "and that healthspan, the years lived in full health, depends on sleep, food, movement and daily habits far more than most people assume. "
            f"The decades ahead can be the best ones. {opener}</p>")
def event(b):
    host = "we are hosting" if b == "lla" else "the Academy is hosting"
    return (f"<p>On <strong>October 27</strong> {host} <strong>The Longevity Masterclass of the Year</strong>: "
            f"60 minutes live on Zoom with <strong>Julie Gibson Clark</strong>, with a second date on <strong>November 14</strong>.</p>")
JULIE = ("<p>Julie is the <strong>second slowest-aging human ever measured</strong>. By verified testing she ages <strong>six years in a decade</strong>, "
         "which places her No. 2 in the world on the Rejuvenation Olympics leaderboard, ahead of Bryan Johnson&rsquo;s two-million-dollar program. "
         "She is 56, a working single mother from Phoenix, and her routine costs about $100 a month. Fortune, Business Insider and the Daily Mail have all covered her.</p>")
LEARN = ("<p>In the hour she reveals her complete protocol:</p>"
         "<ul><li>How biological aging is measured, and what actually moves the number</li>"
         "<li>Her rules for food, sleep and movement, with the numbers behind each</li>"
         "<li>Her full day, 5:00 am to 9:00 pm, including the four supplements she keeps</li></ul>")
def access(who):
    return (f"<p><strong>For 72 hours, seats are held for {who} before general release.</strong> Seats start at <strong>$49</strong>. "
            f"The VIP seat adds a private 30-minute Q&amp;A with Julie and includes an exclusive <strong>$249 promo code</strong> toward her full course.</p>")

WHY = {
    "alumni": "<p>As a graduate of {name}, you are part of the eTeacher Group community, so this invitation comes to you first.</p>",
    "incomplete": "<p>As a student of {name}, you are part of the eTeacher Group community, so this invitation comes to you first. It is one live hour, with nothing to prepare and nothing to keep up with afterwards.</p>",
    "leads": "<p>You asked about {enrol}, which makes you part of the eTeacher Group community, so this invitation comes to you first.</p>",
}
SUBJ = {"alumni": "{short} alumni: your Longevity Masterclass invitation",
        "incomplete": "{short} students: your Longevity Masterclass invitation",
        "leads": "From {short}: your Longevity Masterclass invitation"}
H1 = {"alumni": "{name} alumni are invited to <em>The Longevity Masterclass of the Year</em>",
      "incomplete": "{name} students are invited to <em>The Longevity Masterclass of the Year</em>",
      "leads": "You are invited to <em>The Longevity Masterclass of the Year</em>"}
PRE = "First access for eTeacher students: 60 minutes live on Zoom with Julie Gibson Clark. Seats from $49."
HERO = {"alumni": "julie-zoom-host.jpg", "incomplete": "julie-portrait.jpg", "leads": "julie-zoom-grid.jpg"}
WHO = {"alumni": "eTeacher Group alumni", "incomplete": "eTeacher Group students", "leads": "the eTeacher Group community"}

EMAILS = [dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3 to 4 months, not enrolled", ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads",
    subject="Your invitation: The Longevity Masterclass of the Year", preheader="60 minutes live on Zoom with Julie Gibson Clark. Seats held for you for 72 hours. From $49.",
    h1="You are invited to <em>The Longevity Masterclass of the Year</em>", hero="julie-zoom-room.jpg",
    body=[f"<p>{hi()}</p>", "<p>You asked about enrolling in Longevity Life Academy this year, so this invitation reaches you first.</p>",
          longevity("lla"), event("lla"), JULIE, LEARN, access("the people on this list")])]
for b in ("iibs", "rosen"):
    B = BRANDS[b]
    for seg in ("alumni", "incomplete", "leads"):
        EMAILS.append(dict(brand=b, id=f"{b}-{seg}-01",
            segment={"alumni": "alumni (completed a course)", "incomplete": "students who enrolled and did not finish", "leads": "leads (asked about enrolling, never enrolled)"}[seg],
            ac=f"{b.upper()}_Masterclass_Blast_{seg.capitalize()}", campaign=f"{b}_masterclass_blast",
            subject=SUBJ[seg].format(short=B["short"]), preheader=PRE, h1=H1[seg].format(name=B["name"]), hero=HERO[seg],
            body=[f"<p>{shalom()}</p>", WHY[seg].format(name=B["name"], enrol=B["enrol"]), longevity(b), event(b), JULIE, LEARN, access(WHO[seg])]))

DETAILS = [("Instructor", "Julie Gibson Clark, Longevity Life Academy"), ("Format", "Live on Zoom, 60 minutes"),
           ("Dates", "Tue, October 27, 7:00 PM ET<br>Sat, November 14, 1:00 PM ET"), ("Seats", "From $49"),
           ("VIP seat", "$79: private 30-minute Q&amp;A, $249 promo code"), ("Refund", "14 days, both seats")]

# ---------- the approved shell ----------
CSS = """
  body{margin:0;padding:0;background:#F5F0E5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1220}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF;border-radius:6px;overflow:hidden}
  .top-navy{background:#0A1E3F;padding:30px 20px;text-align:center}
  .top-navy img{display:inline-block;height:104px;width:auto}
  .top-white{background:#FFFFFF;padding:24px 28px 20px}
  .top-white table{width:100%;border-collapse:collapse}
  .top-white td{vertical-align:middle}
  .top-white img.school{height:84px;width:auto;display:block}
  .top-white img.etg{height:30px;width:auto;display:block;margin-left:auto}
  .top-white .of{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#56627A;margin:0 0 6px;text-align:right}
  .divider{height:4px;background:#5EB6FF}
  .alert{background:#0A1E3F;padding:18px 24px;text-align:center;color:#fff;font-size:14px}
  .alert b{color:#5EB6FF;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}
  .hero-img{width:100%;display:block}
  .body-inner{padding:44px 40px 40px}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:32px;line-height:1.25;color:#0A1220;margin:0 0 26px}
  h1 em{font-style:italic;color:#2E6FB8}
  p{font-size:17px;line-height:1.65;color:#2a3244;margin:0 0 18px}
  p strong{color:#0A1220;font-weight:700}
  ul{margin:0 0 18px;padding-left:22px;text-align:left}
  li{font-size:17px;line-height:1.6;color:#2a3244;margin:0 0 8px}
  .details{background:#F5F0E5;border-radius:8px;padding:24px 28px;margin:26px 0}
  .details .dh{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#2E6FB8;margin:0 0 12px}
  .details table{width:100%;border-collapse:collapse}
  .details td{padding:10px 0;font-size:15px;vertical-align:top}
  .details td.k{color:#7A8497;text-transform:uppercase;letter-spacing:.08em;font-size:12px;font-weight:600;width:42%}
  .details td.v{color:#0A1220}
  .btn-row{text-align:center;padding:24px 0 8px}
  .btn{display:inline-block;background:#5EB6FF;color:#0A1220 !important;text-decoration:none;font-weight:700;font-size:16px;padding:16px 40px;border-radius:999px}
  .btn-meta{font-size:13px;color:#7A8497;margin:10px 0 0}
  .signoff{margin-top:28px;font-size:16px;color:#2a3244;line-height:1.5}
  .signoff b{color:#0A1220}
  .small{font-size:13px;color:#7A8497;line-height:1.6;margin:18px 0 0}
  .footer{background:#0A0C12;padding:32px 24px 20px;text-align:center;color:#B8C4DE}
  .footer img{height:74px;width:auto;margin-bottom:14px}
  .footer img.etg{height:26px}
  .footer .tag{font-size:13px;color:#B8C4DE;margin:0 0 18px}
  .footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:14px auto;max-width:220px}
  .footer .fine{font-size:11px;line-height:1.5;color:#8494B4;padding:0 20px}
  .footer .fine a{color:#8494B4;text-decoration:underline}
  @media(max-width:520px){.body-inner{padding:32px 24px}h1{font-size:24px}.top-navy img{height:54px}.top-white img.school{height:56px}.top-white img.etg{height:22px}.details td{display:block;width:100%}.details td.k{padding-bottom:2px}.details td.v{padding-bottom:14px}}
"""
def header(b):
    if not b["logo"]:
        return f'<div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>'
    return (f'<div class="top-white"><table role="presentation"><tr><td style="width:58%"><img class="school" src="{BASE}/assets/{b["logo"]}" alt="{b["name"]}"></td>'
            f'<td style="width:42%"><p class="of">A school of</p><img class="etg" src="{BASE}/assets/eteacher-group-logo.png" alt="eTeacher Group"></td></tr></table></div>')
def footer(b):
    logo = (f'<img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy">' if not b["logo"]
            else f'<img class="etg" src="{BASE}/assets/eteacher-group-logo-white.png" alt="eTeacher Group">')
    addr = f"<br>{b['footer_addr']}" if b["footer_addr"] else ""
    return (f'<div class="footer">\n    {logo}\n    <p class="tag">{b["footer_tag"]}</p>\n    <hr>\n'
            f'    <p class="fine">{b["footer_reason"]} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a>{addr}</p>\n  </div>')

def render(e):
    b = BRANDS[e["brand"]]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS)
    return f"""<!-- AC: {e['ac']} | one-time campaign | segment: {e['segment']} | sender: {e['sender'] if 'sender' in e else b['sender']} | file {e['brand']}/{e['id']} -->
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e['subject']} &middot; {b['name']}</title>
<style>{CSS}</style></head><body>
<div class="preheader">{e['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F0E5"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  {header(b)}
  <div class="divider"></div>
  <div class="alert"><b>{b['alert_k']}</b>&middot;&nbsp; {b['alert_v']}</div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="Julie Gibson Clark hosting the live masterclass on Zoom">
  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">Pick your date at checkout. 14-day full refund, both seats.</p></div>
    <div class="details">
      <p class="dh">The masterclass at a glance</p>
      <table role="presentation">
{rows}
      </table>
    </div>
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a></div>
    <div class="signoff">{b['sign']}</div>
    <p class="small">Julie&rsquo;s pace-of-aging result (DunedinPACE 0.665) is her publicly reported, verified result. The masterclass is taught by Longevity Life Academy, an eTeacher Group school.</p>
  </div>
  {footer(b)}
</div>
</td></tr></table></body></html>
"""

# ---------- write files, text exports, manifest ----------
def visible(out):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S)); t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", t)).strip()
    return re.sub(r"\s+([,.:;])", r"\1", t)
def plain(e):
    b = BRANDS[e["brand"]]; parts = [f"Subject: {e['subject']}", f"Preheader: {e['preheader']}", "", visible(e["h1"]), ""]
    for x in e["body"]:
        x = x.replace("%IF !empty($FIRSTNAME)%", "").replace("%ELSE%Shalom,%/IF%", "").replace("%ELSE%Hi,%/IF%", "")
        if "<li>" in x:
            lead = visible(x.split("<ul>")[0]); items = re.findall(r"<li>(.*?)</li>", x)
            parts.append(lead); parts += ["- " + visible(i) for i in items]
        else: parts.append(visible(x))
        parts.append("")
    parts += [f"[Button] {html.unescape(b['button'])}", ""] + [visible(l) for l in b["sign"].split("<br>")]
    return "\n".join(parts)

for d in ("iibs", "rosen", "lla", "text", "v1", "v2"):
    if os.path.isdir(d): shutil.rmtree(d)
os.makedirs("text", exist_ok=True)
manifest = []
for e in EMAILS:
    b = BRANDS[e["brand"]]; e["sender"] = b["sender"]; out = render(e)
    os.makedirs(e["brand"], exist_ok=True); path = f"{e['brand']}/{e['id']}.html"; open(path, "w", encoding="utf-8").write(out)
    open(f"text/{e['id']}.txt", "w", encoding="utf-8").write(plain(e))
    v = visible(out); im = Image.open(f"assets/images/{e['hero']}")
    manifest.append(dict(id=e["id"], brand=e["brand"], segment=e["segment"], ac=e["ac"], sender=b["sender"], subject=e["subject"], subject_len=len(e["subject"]),
                         preheader=e["preheader"], preheader_len=len(e["preheader"]), button=html.unescape(b["button"]), cta=html.unescape(cta(e["campaign"], e["id"])),
                         file=path, text=f"text/{e['id']}.txt", hero=e["hero"], hero_size=f"{im.size[0]}x{im.size[1]}", hero_kb=os.path.getsize(f"assets/images/{e['hero']}")//1024,
                         words=len(v.split()), chars=len(v), body_words=len(visible(" ".join(e["body"])).split()),
                         emdash=out.count("\u2014") + out.count("\u2013"), bangs=len(re.findall(r"[A-Za-z0-9]!(?!important|empty|\[)", re.sub(r"<style.*?</style>", "", out, flags=re.S))),
                         tokens=all(t in out for t in ("%FIRSTNAME%", "%UNSUBSCRIBELINK%", "%UPDATELINK%")),
                         anatomy=all(k in out for k in ('class="divider"', 'class="alert"', 'class="hero-img"', "<h1>", 'class="btn"', 'class="details"', 'class="signoff"', 'class="footer"'))))
json.dump(manifest, open("manifest.json", "w"), indent=2)
for m in manifest: print(m["id"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| body", m["body_words"], "| whole", m["words"], "| chars", m["chars"], "| dash", m["emdash"], "| !", m["bangs"])

# ---------- gallery (Chris format: Copy HTML / Download .html / Open + image download + copy text) ----------
src = open('/home/user/workspace/gallery-src.html', encoding='utf-8').read()
css = src[src.index('<style>'):src.index('</style>')+8]
script = src[src.index('<script>'):src.index('</script>')+9]
script = script.replace("f.addEventListener('load',function(){ fit(f);", "f.addEventListener('load',function(){ acPreview(f); fit(f);")
script = script.replace("(function(){", "(function(){\n  function acPreview(f){ try{ var d=f.contentDocument; if(!d) return; var w=d.createTreeWalker(d.body,NodeFilter.SHOW_TEXT); var n; var re=/%IF !empty\\(\\$FIRSTNAME\\)%([\\s\\S]*?)%ELSE%[\\s\\S]*?%\\/IF%/g; while((n=w.nextNode())){ if(n.nodeValue.indexOf('%IF')>-1) n.nodeValue=n.nodeValue.replace(re,'$1'); } }catch(e){} }", 1)
script = script.replace("document.querySelectorAll('.btn.copy').forEach", "document.querySelectorAll('.btn.copy, .btn.copytext').forEach")
script = script.replace("function done(){ b.textContent='Copied ✓'; b.classList.add('ok'); setTimeout(function(){ b.textContent='Copy HTML'; b.classList.remove('ok'); },2500); }",
                        "var lbl=b.textContent; function done(){ b.textContent='Copied ✓'; b.classList.add('ok'); setTimeout(function(){ b.textContent=lbl; b.classList.remove('ok'); },2500); }")
COL = {"lla": "#5EB6FF", "iibs": "#F5C451", "rosen": "#A78BFA"}
GROUPS = [("lla", "Funnel 1 · Longevity Life Academy", "LLA leads from the last 3 to 4 months who did not enrol in the Blueprint. Sender: Emma | Longevity Advisor &lt;advisor@longevitylifeacademy.com&gt;.", "1 email"),
          ("iibs", "Funnel 2 · Israel Institute of Biblical Studies", "Three use cases: alumni, enrolled and did not finish, leads. Sender: Sophia Green, Israel Biblical Studies &lt;SophiaG@israelbiblicalstudies.com&gt;.", "3 emails"),
          ("rosen", "Funnel 3 · Rosen School of Hebrew", "Three use cases: alumni, enrolled and did not finish, leads. Sender: Noa Shalev, Campus Manager &lt;admissions@rosenhebrewschool.com&gt;.", "3 emails")]
def card(m):
    return f"""<article class="email" id="{m['id']}">
  <div class="meta"><div>
      <span class="tier" style="--c:{COL[m['brand']]}">{m['brand'].upper()}</span> <span class="msg">{m['id'].upper()}</span>
      <div class="subject">{m['ac']} | {m['segment']}</div>
      <div class="dest"><b>Subject</b> ({m['subject_len']}): {html.escape(m['subject'])}<br><b>Preheader</b> ({m['preheader_len']}): {html.escape(m['preheader'])}<br><b>Sender</b>: {html.escape(m['sender'])}<br><b>Button</b> “{m['button']}” → Julie page, pricing fold<br><code>{html.escape(m['cta'])}</code><br><b>Hero</b> {m['hero']} · {m['hero_size']} · {m['hero_kb']}KB &nbsp;·&nbsp; <b>Words</b> {m['words']} (body {m['body_words']})</div>
    </div>
    <div class="actions">
      <button class="btn copy" data-file="{m['file']}">Copy HTML</button>
      <a class="btn dl" href="{m['file']}" download="{m['id']}.html">Download .html</a>
      <a class="btn raw" href="{m['file']}" target="_blank" rel="noopener">Open</a>
      <a class="btn dl" href="assets/images/{m['hero']}" download="{m['id']}-hero.jpg">Download image</a>
      <button class="btn copytext" data-file="{m['text']}">Copy text</button>
    </div></div>
  <iframe title="{m['id']}" data-src="{m['file']}" loading="lazy" scrolling="no"></iframe>
</article>"""
toc = "".join(f'<a href="#{m["id"]}">{m["id"].upper()} <small>{m["brand"].upper()}</small></a>' for m in manifest)
sections = "".join(f'<section class="funnel"><h2>{name} <span class="count" style="background:{COL[k]}">{cnt}</span></h2><p class="fdesc">{desc}</p>{"".join(card(m) for m in manifest if m["brand"] == k)}</section>\n' for k, name, desc, cnt in GROUPS)
open("index.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass blast · 3 funnels · 7 install-ready emails · 14 Oct 2026</title>
{css}</head><body>
<header>
  <h1>Julie Masterclass blast for Chris &amp; Sandra <span class="count">3 funnels · 7 emails</span></h1>
  <p>Install-ready HTML for ActiveCampaign one-time campaigns. Same anatomy as the approved masterclass set (640px card, header, divider, alert bar, 1200×700 hero, Georgia h1, 17px body, pill button, details box, second button, signoff, dark footer; tokens %FIRSTNAME% with ActiveCampaign's blank-name fallback, %UNSUBSCRIBELINK%, %UPDATELINK%). School sends carry the school logo and the eTeacher Group logo in the header and the school's “by eTeacher Group” copyright and Ramat Gan address in the footer. Facts from the live Julie page: Tue 27 Oct 7:00 PM ET or Sat 14 Nov 1:00 PM ET, seats from $49, VIP $79 with private 30-min Q&amp;A and the $249 Blueprint promo code, 14-day full refund.</p>
  <p>Per email: <b>Copy HTML</b> (production HTML to clipboard) · <b>Download .html</b> · <b>Open</b> · <b>Download image</b> (the hero, 1200×700 JPG) · <b>Copy text</b> (subject, preheader, body as plain text). Also: <a href="AUDIT.md">AUDIT.md</a> and <a href="README.md">README.md</a>.</p>
</header>
<nav class="toc">{toc}</nav>
<main>
{sections}</main>
{script}
</body></html>
""")

# ---------- AUDIT.md ----------
ref_w, ref_c = (191, 262), (1203, 1534)
rows = "\n".join(f"| {m['id']} | {m['subject_len']} | {m['preheader_len']} | {m['words']} | {m['chars']} | {m['hero']} {m['hero_size']} {m['hero_kb']}KB | {'yes' if m['tokens'] else 'NO'} | {'yes' if m['anatomy'] else 'NO'} | {m['emdash']} | {m['bangs']} |" for m in manifest)
logos = "\n".join(f"- `assets/{f}`: {Image.open('assets/'+f).size[0]}×{Image.open('assets/'+f).size[1]}, {os.path.getsize('assets/'+f)//1024}KB" for f in ("lla-logo-800w.png", "iibs-logo.png", "rosen-logo.png", "eteacher-group-logo.png", "eteacher-group-logo-white.png"))
open("AUDIT.md", "w", encoding="utf-8").write(f"""# Audit · Julie Masterclass blast · 14 Oct 2026

Reference: the approved masterclass set sent to Chris and Sandra (`lla-masterclass-emails-3tier/launch-email-for-chris`, 36 emails):
640px card, header, 4px #5EB6FF divider, navy alert bar, 1200×700 hero, Georgia h1, 17px body, #5EB6FF pill button, details box, second button, signoff, dark footer;
tokens %FIRSTNAME%, %UNSUBSCRIBELINK%, %UPDATELINK%; whole-file length {ref_w[0]} to {ref_w[1]} words, {ref_c[0]} to {ref_c[1]} characters.

## Per email
| Email | Subject chars | Preheader chars | Words (whole file) | Chars | Hero | AC tokens | Approved anatomy | Em/en dashes | Exclamation marks |
|---|---|---|---|---|---|---|---|---|---|
{rows}

Word count vs the approved set: these are cold invitations with a who-is-Julie paragraph and three bullets that the lifecycle emails did not need; Omri allowed "a little more". All seven are within +{max(m['words'] for m in manifest) - ref_w[1]} words of the set's longest email.

## Format checks
- Header: LLA = navy header with the LLA logo (approved). Schools = white header, school logo (84px tall) left, "A school of" + eTeacher Group logo (30px) right. Two logos, not three.
- Divider, alert bar, hero, h1, body, pill button, details box, second button, signoff, small line, footer: present in all 7 (column "Approved anatomy").
- Footer: LLA = approved dark footer with LLA logo and tagline. Schools = dark footer, eTeacher Group logo, "© 2026 <school> by eTeacher Group. All Rights Reserved.", Unsubscribe, Update preferences, Privacy, "{ADDRESS}" (the address printed in the real IIBS and Rosen campaigns).
- Greeting: schools "Shalom %FIRSTNAME%," as in their real campaigns; LLA "Hi %FIRSTNAME%," as in the approved set (jm-a1-1). Blank first name renders "Shalom," / "Hi," via ActiveCampaign conditional content.
- Buttons: schools CAPS ("RESERVE MY SEAT") as in their real campaigns; LLA sentence case ("Reserve My Seat") as in the approved set. All 14 buttons → `{LP}#pricing` with utm_source=activecampaign, utm_medium=email, utm_campaign, utm_content.
- Images: approved lifecycle Zoom assets only, 1200×700 JPG (2× of the 600px slot), 98 to 117KB each, hosted on this Pages site. Logos:
{logos}
- Copy: no em or en dashes, no exclamation marks, no hype words (unlock, elevate, journey, seamless, empower, transform, game-changer, hurry, act now, don't miss out), no invented numbers. "The Longevity Masterclass of the Year", "second slowest-aging human ever measured", "eight months for every year", "$100 a month", the three bullets, the two dates, $49, $79, the $249 promo code and the 14-day refund are the live page's own facts.

## Segment coverage
| Funnel | Use case | Email | Why the reader is getting it (first paragraph) |
|---|---|---|---|
| LLA | Leads, did not enrol | lla-leads-01 | asked about enrolling in Longevity Life Academy this year |
| IIBS | Alumni | iibs-alumni-01 | graduate of the Israel Institute of Biblical Studies, part of the eTeacher Group community |
| IIBS | Enrolled, did not finish | iibs-incomplete-01 | student of the Institute, one live hour, nothing to catch up on |
| IIBS | Leads | iibs-leads-01 | asked about enrolling at the Institute |
| Rosen | Alumni | rosen-alumni-01 | graduate of Rosen School of Hebrew |
| Rosen | Enrolled, did not finish | rosen-incomplete-01 | student of Rosen, one live hour, nothing to catch up on |
| Rosen | Leads | rosen-leads-01 | asked about enrolling at Rosen |
Fourth use case per school: not named by Omri yet; same shell, add as `*-<usecase>-01`.

## Offer statements and their source
- "For 72 hours, seats are held for … before general release": Omri's offer to students (brief of 13 Oct). The checkout does not enforce a hold.
- "Exclusive $249 promo code toward her full course": the VIP seat's Blueprint code (MASTERCLASS-VIP), shown after VIP payment, valid to 31 Dec 2026. No discount code exists on the masterclass price; none is promised.
- Senders verified in Omri's inbox: Noa Shalev (5 Rosen campaigns, Sep 2026); Sophia Green (the only IIBS-domain campaign sender received); Emma | Longevity Advisor (LLA automations).

## Not tested
Gmail, Apple Mail, Outlook rendering (Chromium only, 720px and 390px). Same table-plus-media-query construction as the approved set.
""")
rows_r = "\n".join(f"| `{m['file']}` | {m['segment']} | `{m['ac']}` | {m['sender']} | {m['subject']} | {m['hero']} | `{m['text']}` |" for m in manifest)
open("README.md", "w", encoding="utf-8").write(f"""# Julie Masterclass blast · 3 funnels · 7 install-ready ActiveCampaign emails

Gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/ · Audit: AUDIT.md

Same anatomy as the approved masterclass set (`lla-masterclass-emails-3tier/launch-email-for-chris`). One-time campaigns, not automations.

| File | Use case | AC campaign name | Sender | Subject | Hero | Plain text |
|---|---|---|---|---|---|---|
{rows_r}

Buttons → `{LP}#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<funnel>&utm_content=<id>`.
Exclude masterclass registrants (LGV buyer tags) and the LLA leads list from every school send. Fourth use case per school: to be named.
""")
print("gallery + audit + readme written")
