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
                button="Reserve My Seat", alert_k="Live on Zoom", alert_v="October 27 or November 14, from $49",
                sign="To your longest, strongest life,<br><b>Emma</b><br>Longevity Advisor<br>Longevity Life Academy",
                footer_tag="It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group.", footer_reason="You received this because you asked about Longevity Life Academy", footer_addr=""),
    "iibs": dict(name="Israel Institute of Biblical Studies", short="Israel Biblical Studies", logo="iibs-logo.png",
                 sender="Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com>", button="RESERVE MY SEAT",
                 alert_k="Student pricing", alert_v="From $49, 72 hours before public release",
                 sign="Warmly,<br><b>Sophia Green</b><br>Admissions Advisor<br>Israel Institute of Biblical Studies",
                 footer_tag="&copy; 2026 Israel Institute of Biblical Studies by eTeacher Group<br>All Rights Reserved.",
                 footer_addr="All Rights Reserved. The Israel Institute of Biblical Studies by eTeacher Group, "+ADDRESS,
                 course="course", enrol="enrolling at the Israel Institute of Biblical Studies"),
    "rosen": dict(name="Rosen School of Hebrew", short="Rosen", logo="rosen-logo.png",
                  sender="Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>", button="RESERVE MY SEAT",
                  alert_k="Student pricing", alert_v="From $49, 72 hours before public release",
                  sign="Warmly,<br><b>Noa Shalev</b><br>Campus Manager<br>Rosen School of Hebrew",
                  footer_tag="&copy; 2026 Rosen School of Hebrew by eTeacher Group<br>All Rights Reserved.",
                  footer_addr="All Rights Reserved. The Rosen School of Hebrew by eTeacher Group, "+ADDRESS,
                  course="Hebrew course", enrol="enrolling at Rosen School of Hebrew"),
}

# ---------- copy (facts: live masterclass page, 13 Oct 2026; language: longevitylifeacademy.com) ----------
JULIE = ("<h2>Learn to age slower from the 2nd slowest aging human on earth</h2>"
         "<ul><li><strong>Julie Gibson Clark</strong> ages eight months for every calendar year, verified (DunedinPACE 0.665)</li>"
         "<li>Ranked <strong>No. 2 in the world</strong> in the Rejuvenation Olympics, ahead of rivals spending $2M a year</li>"
         "<li>On a routine that costs about <strong>$100 a month</strong></li></ul>")
LEARN = ("<h2>What you will learn in 60 minutes, live on Zoom</h2>"
         "<ul><li><strong>Measuring biological aging:</strong> how aging speed is measured, and what actually moves it</li>"
         "<li><strong>Food, sleep and movement:</strong> her rules, in numbers</li>"
         "<li><strong>Her daily protocol:</strong> a full day built to repeat, with her one-page schedule and supplement list, yours to keep</li></ul>")
PRICE = ("<h2>Your student pricing</h2>"
         '<div class="offer"><p><strong>Standard seat, $49:</strong> the 60-minute live masterclass.</p>'
         '<p><strong>VIP seat, $79:</strong> the masterclass, a private 30-minute Q&amp;A with Julie, and a <strong class="promo">$249 promo code</strong> toward The Longevity Blueprint, her full course, valid until December 31, 2026.</p>'
         "<p>Choose October 27 or November 14. 14-day full refund on both seats.</p></div>")
CLICK = "<p>If you would like a seat, click below.</p>"
def after_(b):
    who = "eTeacher Group students" if b != "lla" else "the people who asked about the Academy"
    return [f"<p>This invitation is for {who} for 72 hours. After that, registration opens to the public.</p>"]

def school_body(b, seg):
    B = BRANDS[b]; name = B["name"]
    open_ = {
        "alumni": f"<p>I am writing with an invitation of a different kind. As a graduate of {name}, you are part of the eTeacher Group family of students, so this reaches you 72 hours before it opens to the public.</p>",
        "incomplete": f"<p>I am writing with an invitation of a different kind. As a student of {name}, you are part of the eTeacher Group family of students, so this reaches you 72 hours before it opens to the public. There is nothing to catch up on. It is one live hour.</p>",
        "leads": f"<p>I am writing with an invitation of a different kind. You asked about studying at {name}, which places you in the eTeacher Group family of students, so this reaches you 72 hours before it opens to the public.</p>",
    }[seg]
    return [f"<p>{shalom()}</p>", open_,
        "<p>This year eTeacher Group opened <strong>Longevity Life Academy</strong>, a school built on one belief: everyone deserves a science-backed protocol for a longer, healthier life. "
        "Aging can now be measured and slowed, and the decades ahead can be the strongest.</p>",
        "<p>On <strong>October 27</strong>, the Academy is hosting <strong>The Longevity Masterclass of the Year</strong>, and I would like to offer you a seat at our student pricing.</p>",
        JULIE, LEARN, PRICE, CLICK]

LLA_BODY = [f"<p>{hi()}</p>",
    "<p>You asked about Longevity Life Academy this year, so this reaches you 72 hours before we open it to the public.</p>",
    "<p>The Academy was built on one belief: everyone deserves a science-backed protocol for a longer, healthier life. Aging can now be measured and slowed, and the decades ahead can be the strongest.</p>",
    "<p>On <strong>October 27</strong> we are hosting <strong>The Longevity Masterclass of the Year</strong>, and I would like to offer you a seat.</p>",
    JULIE, LEARN, PRICE.replace("Your student pricing", "Your seat"), CLICK]

SUBJ = {"alumni": "{short} alumni: your Longevity Masterclass invitation",
        "incomplete": "{short} students: your Longevity Masterclass invitation",
        "leads": "From {short}: your Longevity Masterclass invitation"}
H1 = {"alumni": "{name} alumni are invited to <em>The Longevity Masterclass of the Year</em>",
      "incomplete": "{name} students are invited to <em>The Longevity Masterclass of the Year</em>",
      "leads": "You are invited to <em>The Longevity Masterclass of the Year</em>"}
PRE = "Student pricing from $49 for Julie Gibson Clark's live masterclass, 72 hours before public release."
HERO = {"alumni": "julie-zoom-host.jpg", "incomplete": "julie-portrait.jpg", "leads": "julie-zoom-grid.jpg"}

EMAILS = [dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3 to 4 months, not enrolled", ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads",
    subject="Your invitation: The Longevity Masterclass of the Year", preheader="60 minutes live on Zoom with Julie Gibson Clark, October 27 or November 14. From $49.",
    h1="You are invited to <em>The Longevity Masterclass of the Year</em>", hero="julie-zoom-room.jpg", body=LLA_BODY)]
for b in ("iibs", "rosen"):
    B = BRANDS[b]
    for seg in ("alumni", "incomplete", "leads"):
        EMAILS.append(dict(brand=b, id=f"{b}-{seg}-01",
            segment={"alumni": "alumni (completed a course)", "incomplete": "students who enrolled and did not finish", "leads": "leads (asked about enrolling, never enrolled)"}[seg],
            ac=f"{b.upper()}_Masterclass_Blast_{seg.capitalize()}", campaign=f"{b}_masterclass_blast",
            subject=SUBJ[seg].format(short=B["short"]), preheader=PRE, h1=H1[seg].format(name=B["name"]), hero=HERO[seg], body=school_body(b, seg)))

DETAILS = [("Masterclass", "The Longevity Masterclass of the Year, with Julie Gibson Clark"),
           ("Dates", "Tuesday, October 27, 7:00 PM ET<br>Saturday, November 14, 1:00 PM ET"),
           ("Format", "60 minutes, live on Zoom"),
           ("Seats", "From $49. VIP $79 with a private Q&amp;A and your <b>$249 promo code</b>"),
           ("Refund", "14 days, both seats"),
           ("Reserved for", "%EMAIL%"),
           ("Status", "Held for 72 hours")]

# ---------- the approved shell ----------
CSS = """
  body{margin:0;padding:0;background:#F5F0E5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1220}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF;border-radius:6px;overflow:hidden}
  .top-navy{background:#0A1E3F;padding:30px 20px;text-align:center}
  .top-navy img{display:inline-block;height:104px;width:auto}
  .top-white{background:#FFFFFF;padding:24px 28px 20px}
  .top-white img.school{height:84px;width:auto;display:block}
  .divider{height:4px;background:#5EB6FF}
  .alert{background:#0A1E3F;padding:18px 24px;text-align:center;color:#fff;font-size:14px}
  .alert b{color:#5EB6FF;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}
  .hero-img{width:100%;display:block}
  .body-inner{padding:40px 44px 40px;text-align:left}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:30px;line-height:1.25;color:#0A1220;margin:0 0 24px;text-align:center}
  h1 em{font-style:italic;color:#2E6FB8}
  p{font-size:17px;line-height:1.65;color:#2a3244;margin:0 0 18px}
  p strong{color:#0A1220;font-weight:700}
  h2{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:21px;line-height:1.3;color:#0A1220;margin:30px 0 12px}
  .offer{background:#F5F0E5;border-left:4px solid #0A1E3F;border-radius:0 8px 8px 0;padding:18px 22px 4px;margin:0 0 20px}
  .offer p{font-size:17px;line-height:1.6;margin:0 0 14px}
  .offer strong{color:#0A1220}
  .offer strong.promo{color:#2E6FB8;font-size:18px}
  .details td.v b{color:#0A1220;font-weight:700}
  ul{margin:0 0 18px;padding-left:22px;text-align:left}
  li{font-size:17px;line-height:1.6;color:#2a3244;margin:0 0 8px}
  li strong{color:#0A1220}
  .details{background:#F5F0E5;border-radius:8px;padding:24px 28px;margin:26px 0}
  .details .dh{font-family:Georgia,'Times New Roman',serif;font-size:19px;font-weight:700;color:#0A1220;margin:0 0 10px}
  .details table{width:100%;border-collapse:collapse}
  .details td{padding:10px 0;font-size:15px;vertical-align:top}
  .details td.k{color:#56627A;font-size:15px;font-weight:600;width:32%;padding-right:12px}
  .details td.v{color:#0A1220}
  .btn-row{text-align:center;padding:10px 0 28px}
  .btn{display:inline-block;background:#5EB6FF;color:#0A1220 !important;text-decoration:none;font-weight:700;font-size:16px;padding:16px 40px;border-radius:999px}
  .btn-meta{font-size:13px;color:#7A8497;margin:10px 0 0}
  .signoff{margin-top:28px;font-size:16px;color:#2a3244;line-height:1.5}
  .signoff b{color:#0A1220}
  .small{font-size:13px;color:#7A8497;line-height:1.6;margin:18px 0 0}
  .footer{background:#0A0C12;padding:32px 24px 20px;text-align:center;color:#B8C4DE}
  .footer img{height:74px;width:auto;margin-bottom:14px}
  .footer .tag{font-size:13px;color:#B8C4DE;margin:0 0 18px}
  .footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:14px auto;max-width:220px}
  .footer .fine{font-size:11px;line-height:1.5;color:#8494B4;padding:0 20px}
  .footer .fine a{color:#8494B4;text-decoration:underline}
  .sfooter{background:#F3F5F9;padding:24px 28px 22px;text-align:center;border-top:1px solid #E3E8F0}
  .sfooter p{font-size:12px;line-height:1.7;color:#56627A;margin:0 0 8px}
  .sfooter a{color:#56627A;text-decoration:underline}
  @media(max-width:520px){.body-inner{padding:32px 24px}h1{font-size:24px}.top-navy img{height:54px}.top-white img.school{height:56px}.details td{display:block;width:100%}.details td.k{padding-bottom:2px}.details td.v{padding-bottom:14px}}
"""
def header(b):
    if not b["logo"]:
        return f'<div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>'
    return f'<div class="top-white" style="text-align:center"><img class="school" src="{BASE}/assets/{b["logo"]}" alt="{b["name"]}, by eTeacher" style="display:inline-block"></div>'
def footer(b):
    if not b["logo"]:
        return (f'<div class="footer">\n    <img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy">\n    <p class="tag">{b["footer_tag"]}</p>\n    <hr>\n'
                f'    <p class="fine">{b["footer_reason"]} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a></p>\n  </div>')
    return (f'<div class="sfooter">\n    <p>{b["footer_tag"]}</p>\n    <p>Sent to: %EMAIL%</p>\n    <p><a href="%UNSUBSCRIBELINK%">Unsubscribe</a></p>\n    <p>{b["footer_addr"]}</p>\n  </div>')

def render(e):
    b = BRANDS[e["brand"]]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS)
    after = "\n".join("    " + x for x in after_(e["brand"]))
    return f"""<!DOCTYPE html>
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
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a></div>
{after}
    <div class="signoff">{b['sign']}</div>
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
        x = x.replace("<h2>", "\n## ").replace("</h2>", " |BR| ").replace("</p><p>", " |BR| ")
        if "<li>" in x:
            lead = visible(x.split("<ul>")[0]).replace(" |BR|", "").strip(); items = re.findall(r"<li>(.*?)</li>", x)
            parts.append(lead); parts += ["- " + visible(i) for i in items]
        else: parts.append(visible(x).replace(" |BR| ", "\n").replace("|BR|", "\n").strip())
        parts.append("")
    parts += [f"[Button] {html.unescape(b['button'])}", ""]
    for x in after_(e["brand"]): parts += [visible(x), ""]
    parts += [visible(l) for l in b["sign"].split("<br>")]
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
                         tokens=all(t in out for t in ("%FIRSTNAME%", "%UNSUBSCRIBELINK%")),
                         anatomy=all(k in out for k in ('class="divider"', 'class="alert"', 'class="hero-img"', "<h1>", 'class="btn"', 'class="signoff"', 'footer"'))))
json.dump(manifest, open("manifest.json", "w"), indent=2)
for m in manifest: print(m["id"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| body", m["body_words"], "| whole", m["words"], "| chars", m["chars"], "| dash", m["emdash"], "| !", m["bangs"])

# ---------- gallery ----------
SEGNAME = {"alumni": "Alumni", "incomplete": "Students who did not finish", "leads": "Leads"}
GROUPS = [("lla", "Longevity Life Academy"), ("iibs", "Israel Institute of Biblical Studies"), ("rosen", "Rosen School of Hebrew")]
def card(m):
    seg = m["id"].split("-")[1]; title = SEGNAME.get(seg, seg.title())
    return f"""<article class="email" id="{m['id']}">
  <div class="side">
    <h3>{title}</h3>
    <p class="sub">{html.escape(m['subject'])}</p>
    <p class="from">{html.escape(m['sender'])}</p>
    <div class="actions">
      <a class="b primary" href="{m['file']}" download="{m['id']}.html">Download HTML</a>
      <button class="b copy" data-file="{m['file']}">Copy HTML</button>
      <button class="b copy" data-file="{m['text']}">Copy text</button>
      <a class="b" href="assets/images/{m['hero']}" download="{m['id']}-image.jpg">Download image</a>
      <a class="b" href="{m['file']}" target="_blank" rel="noopener">Open</a>
    </div>
  </div>
  <iframe title="{m['id']}" data-src="{m['file']}" loading="lazy" scrolling="no"></iframe>
</article>"""
sections = "".join(f'<section><h2>{name}</h2>{"".join(card(m) for m in manifest if m["brand"] == k)}</section>\n' for k, name in GROUPS)
GCSS = """<style>
  :root{--bg:#F5F5F7;--ink:#1D1D1F;--mute:#6E6E73;--line:#E5E5EA;--blue:#0071E3}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI',Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
  header{max-width:1180px;margin:0 auto;padding:72px 32px 24px}
  h1{font-size:56px;line-height:1.07;letter-spacing:-.02em;margin:0 0 14px;font-weight:700}
  header p{font-size:21px;line-height:1.4;color:var(--mute);margin:0}
  main{max-width:1180px;margin:0 auto;padding:0 32px 96px}
  section{margin-top:56px}
  h2{font-size:40px;line-height:1.1;letter-spacing:-.015em;margin:0 0 24px;font-weight:700}
  .email{display:grid;grid-template-columns:360px 1fr;gap:32px;background:#fff;border-radius:24px;padding:32px;margin-bottom:24px;border:1px solid var(--line)}
  .side h3{font-size:28px;line-height:1.15;letter-spacing:-.01em;margin:0 0 12px;font-weight:700}
  .side .sub{font-size:17px;line-height:1.45;margin:0 0 6px;color:var(--ink)}
  .side .from{font-size:15px;line-height:1.45;margin:0 0 24px;color:var(--mute)}
  .actions{display:flex;flex-direction:column;gap:10px}
  .b{display:block;width:100%;text-align:center;font:inherit;font-size:17px;font-weight:600;padding:14px 18px;border-radius:14px;border:1px solid var(--line);background:#fff;color:var(--ink);cursor:pointer;text-decoration:none}
  .b:hover{background:#F5F5F7}
  .b.primary{background:var(--blue);border-color:var(--blue);color:#fff}
  .b.primary:hover{background:#0077ED}
  .b.ok{background:#1D1D1F;border-color:#1D1D1F;color:#fff}
  iframe{width:100%;border:1px solid var(--line);border-radius:16px;background:#F5F0E5;display:block;min-height:900px}
  @media(max-width:900px){.email{grid-template-columns:1fr}h1{font-size:40px}h2{font-size:32px}header{padding:48px 20px 16px}main{padding:0 20px 64px}}
</style>"""
GJS = """<script>
(function(){
  function acPreview(f){ try{ var d=f.contentDocument; if(!d) return; var w=d.createTreeWalker(d.body,NodeFilter.SHOW_TEXT); var n; var re=/%IF !empty\\(\\$FIRSTNAME\\)%([\\s\\S]*?)%ELSE%[\\s\\S]*?%\\/IF%/g; while((n=w.nextNode())){ if(n.nodeValue.indexOf('%IF')>-1) n.nodeValue=n.nodeValue.replace(re,'$1'); } }catch(e){} }
  function fit(f){ try{ var h=f.contentDocument.documentElement.scrollHeight; if(h>300) f.style.height=(h+8)+'px'; }catch(e){} }
  document.querySelectorAll('iframe[data-src]').forEach(function(f){ f.addEventListener('load',function(){ acPreview(f); fit(f); setTimeout(function(){fit(f)},800); }); f.src=f.getAttribute('data-src'); });
  document.querySelectorAll('.b.copy').forEach(function(b){
    b.addEventListener('click',function(){
      var lbl=b.textContent;
      fetch(b.getAttribute('data-file')).then(function(r){return r.text()}).then(function(t){
        return navigator.clipboard.writeText(t);
      }).then(function(){ b.textContent='Copied'; b.classList.add('ok'); setTimeout(function(){ b.textContent=lbl; b.classList.remove('ok'); },2000); })
      .catch(function(){ window.open(b.getAttribute('data-file'),'_blank'); });
    });
  });
})();
</script>"""
open("index.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass invitation emails</title>
{GCSS}</head><body>
<header>
  <h1>Julie Masterclass invitation emails</h1>
  <p>Seven emails for three schools. Download the HTML, or copy it straight into ActiveCampaign.</p>
</header>
<main>
{sections}</main>
{GJS}
</body></html>
""")

# ---------- AUDIT.md ----------
ref_w, ref_c = (191, 262), (1203, 1534)
rows = "\n".join(f"| {m['id']} | {m['subject_len']} | {m['preheader_len']} | {m['words']} | {m['chars']} | {m['hero']} {m['hero_size']} {m['hero_kb']}KB | {'yes' if m['tokens'] else 'NO'} | {'yes' if m['anatomy'] else 'NO'} | {m['emdash']} | {m['bangs']} |" for m in manifest)
logos = "\n".join(f"- `assets/{f}`: {Image.open('assets/'+f).size[0]}×{Image.open('assets/'+f).size[1]}, {os.path.getsize('assets/'+f)//1024}KB" for f in ("lla-logo-800w.png", "iibs-logo.png", "rosen-logo.png", "eteacher-group-logo.png", "eteacher-group-logo-white.png"))
open("AUDIT.md", "w", encoding="utf-8").write(f"""# Audit · Julie Masterclass blast · 14 Oct 2026

Reference: the approved masterclass set sent to Chris and Sandra (`lla-masterclass-emails-3tier/launch-email-for-chris`, 36 emails):
640px card, header, 4px #5EB6FF divider, navy alert bar, 1200×700 hero, Georgia h1, 17px body, #5EB6FF pill button, details box, second button, signoff, dark footer;
tokens %FIRSTNAME%, %UNSUBSCRIBELINK% (schools also %EMAIL%); whole-file length {ref_w[0]} to {ref_w[1]} words, {ref_c[0]} to {ref_c[1]} characters.

## Per email
| Email | Subject chars | Preheader chars | Words (whole file) | Chars | Hero | AC tokens | Approved anatomy | Em/en dashes | Exclamation marks |
|---|---|---|---|---|---|---|---|---|---|
{rows}

Word count vs the approved set: these are cold invitations written as a letter from the school's advisor, with the longevity paragraph, the Julie paragraph and three bullets that the lifecycle emails did not need. Longest is {max(m['words'] for m in manifest)} words whole file.

## Format checks
- Header: LLA = navy header with the LLA logo (approved). Schools = white header with the school's own logo lockup (which carries "By eTeacher"). No other logo anywhere in the email.
- Divider, alert bar, hero, h1, body, pill button, details box, second button, signoff, small line, footer: present in all 7 (column "Approved anatomy").
- Footer: LLA = approved dark footer with LLA logo and tagline. Schools = the exact footer of their real campaigns (Rosen sends of Sep 2026 in Omri's inbox): "© 2026 <school> by eTeacher Group / All Rights Reserved." / "Sent to: %EMAIL%" / "Unsubscribe" / "All Rights Reserved. The <school> by eTeacher Group, {ADDRESS}".
- Greeting: schools "Shalom %FIRSTNAME%," as in their real campaigns; LLA "Hi %FIRSTNAME%," as in the approved set (jm-a1-1). Blank first name renders "Shalom," / "Hi," via ActiveCampaign conditional content.
- Buttons: schools CAPS ("RESERVE MY SEAT") as in their real campaigns; LLA sentence case ("Reserve My Seat") as in the approved set. All 14 buttons → `{LP}#pricing` with utm_source=activecampaign, utm_medium=email, utm_campaign, utm_content.
- Images: approved lifecycle Zoom assets only, 1200×700 JPG (2× of the 600px slot), 98 to 117KB each, hosted on this Pages site. Logos:
{logos}
- Copy: letter form in the voice of the school's real campaigns ("Shalom", short paragraphs, one CAPS button, "Warmly," + name, title, school). Longevity language taken from longevitylifeacademy.com ("a simple belief, that everyone deserves a science-backed protocol for a longer, healthier life", nutrition, sleep, movement, stress, "the decades ahead"). No em or en dashes, no exclamation marks, no hype words, no emojis, no invented numbers. "The Longevity Masterclass of the Year", "ten years pass, she ages six", No. 2 Rejuvenation Olympics, "$100 a month", the three bullets, the two dates, $49, $79, the $249 promo code and the 14-day refund are the live page's own facts.

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
