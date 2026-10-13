# -*- coding: utf-8 -*-
"""Julie Masterclass blast: 7 one-time ActiveCampaign emails, one design each.
Schools (IIBS, Rosen): the letter format their own campaigns use (title, "Shalom %FIRSTNAME%,", short personal
paragraphs, one CAPS button, advisor signature, school footer "by eTeacher Group" with the Ramat Gan address).
LLA: the approved lifecycle shell. Imagery: approved lifecycle Zoom assets only, 1200px (2x of 600px slot), <=120KB.
Copy: a person writing to a student. One idea. An honest introduction to longevity, three plain bullets taken from
the masterclass page's three blocks, the student priority and the VIP promo stated once, seats from $49."""
import os, re, json, html

BASE = os.environ.get("BASE", "https://gitteromri-ux.github.io/julie-masterclass-blast")
LP = "https://www.longevitylifeacademy.com/julie-masterclass/"
ADDRESS = "8 Aholiav St, 5252261 Ramat Gan, Israel"

def cta(campaign, content):
    return (f"{LP}?utm_source=activecampaign&amp;utm_medium=email&amp;utm_campaign={campaign}"
            f"&amp;utm_content={content}#pricing")
def greet_shalom(): return "%IF !empty($FIRSTNAME)%Shalom %FIRSTNAME%,%ELSE%Shalom,%/IF%"
def you_lla(): return "%IF !empty($FIRSTNAME)%%FIRSTNAME%, you%ELSE%You%/IF%"

BRANDS = {
    "lla": dict(name="Longevity Life Academy", sender="Emma | Longevity Advisor <advisor@longevitylifeacademy.com>",
                button="Reserve My Seat", footer_reason="Sent because you asked about Longevity Life Academy"),
    "iibs": dict(name="Israel Institute of Biblical Studies", the="the ", logo="iibs-logo.png",
                 sender="Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com>",
                 sign="Warmly,<br><b>Sophia Green</b><br>Admissions Advisor<br>Israel Institute of Biblical Studies",
                 copyright="&copy; 2026 Israel Institute of Biblical Studies by eTeacher Group. All Rights Reserved.",
                 footer_reason="Sent to you as a student or contact of the Israel Institute of Biblical Studies",
                 button="RESERVE MY SEAT", course="course", asked="our courses", students="our students"),
    "rosen": dict(name="Rosen School of Hebrew", the="", logo="rosen-logo.png",
                  sender="Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>",
                  sign="Warmly,<br><b>Noa Shalev</b><br>Campus Manager<br>Rosen School of Hebrew",
                  copyright="&copy; 2026 Rosen School of Hebrew by eTeacher Group. All Rights Reserved.",
                  footer_reason="Sent to you as a student or contact of Rosen School of Hebrew",
                  button="RESERVE MY SEAT", course="Hebrew course", asked="learning Hebrew", students="our students"),
}

# ---------- shared paragraphs (facts: live masterclass page, 13 Oct 2026) ----------
def bridge(b):
    B = BRANDS[b]
    return (f"<p>{B['the'].capitalize()}{B['name']} is part of eTeacher Group, and this year the group opened a new school, "
            f"<strong>Longevity Life Academy</strong>. It teaches something most of us think about a little more each year: how to stay "
            f"sharp and well as the years add up. Not with clinics and millions, but with sleep, food and movement, measured.</p>")
JULIE = ("<p>Its founding teacher is <strong>Julie Gibson Clark</strong>. She is 56, a working single mother from Phoenix, and by verified "
         "testing she ages about <strong>eight months for every year</strong>, the second slowest-aging human ever measured. "
         "Her routine costs her about $100 a month.</p>")
HOUR = ("<p>On <strong>October 27</strong> she is teaching her protocol, live on Zoom, for 60 minutes. In the hour:</p>"
        "<ul><li>How biological aging is measured, and what actually moves the number</li>"
        "<li>Her rules for food, sleep and movement, with the numbers behind each</li>"
        "<li>Her full day, 5:00 am to 9:00 pm, including the four supplements she keeps</li></ul>")
def offer(b):
    who = {"alumni": "our graduates", "incomplete": "our students", "leads": "people who asked about us"}[b]
    return (f"<p>For the next <strong>72 hours</strong>, a block of seats is held for {who}. "
            f"Seats start at <strong>$49</strong>. The VIP seat adds a private 30-minute Q&amp;A with Julie and comes with a "
            f"<strong>$249 promo code</strong> toward her full course.</p>")
CLOSE = "<p>If it is not for you, ignore this and I will not write about it again. If it is, choose October 27 or November 14 below.</p>"

OPEN = {
    "alumni": "<p>You finished a {course} with us, so you know how we teach: live, in a small group, with a real teacher. This is about the same kind of hour, on a different subject, and I will explain how it reached you.</p>",
    "incomplete": "<p>You began a {course} with us, and I know life has its own schedule. This is not about that. It is one hour, live, with nothing to prepare and nothing to keep up with afterwards, and I thought of you when the seats were set aside.</p>",
    "leads": "<p>You asked us about {asked}, and we have stayed in touch since. This is not about Hebrew or the Bible, and I will explain how it reached you.</p>",
}
SUBJECT = {"alumni": "A seat I set aside for our graduates", "incomplete": "One hour, and nothing to catch up on", "leads": "Something I do not usually write to you about"}
TITLE = "Ten years pass. She ages six."   # the masterclass page's own line
PREHEADER = "Julie Gibson Clark, live on Zoom on October 27, and seats held for {school} students for 72 hours."

def school_emails(b):
    B = BRANDS[b]; out = []
    for seg in ["alumni", "incomplete", "leads"]:
        opening = OPEN[seg].format(course=B["course"], asked=B["asked"])
        if seg == "leads" and b == "rosen": opening = opening.replace("Hebrew or the Bible", "Hebrew")
        if seg == "leads" and b == "iibs": opening = opening.replace("Hebrew or the Bible", "the Bible or Hebrew")
        out.append(dict(brand=b, id=f"{b}-{seg}-01",
                        segment={"alumni": "alumni (completed a course)", "incomplete": "students who enrolled and did not finish", "leads": "leads (asked about a course, never enrolled)"}[seg],
                        ac=f"{b.upper()}_Masterclass_Blast_{seg.capitalize()}", campaign=f"{b}_masterclass_blast", sender=B["sender"],
                        subject=SUBJECT[seg], preheader=PREHEADER.format(school="Rosen" if b == "rosen" else "IIBS"),
                        h1=TITLE, hero="julie-zoom-host.jpg",
                        body=[f"<p>{greet_shalom()}</p>", opening, bridge(b), JULIE, HOUR, offer(seg), CLOSE], signoff=B["sign"]))
    return out

LLA = dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3-4 months, not enrolled",
    ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads", sender=BRANDS["lla"]["sender"],
    subject="Julie is teaching her protocol live. You hear it first", preheader="October 27 or November 14, live on Zoom. Seats held for you for 72 hours. From $49.",
    h1="Ten years pass. <em>She ages six.</em>", hero="julie-zoom-room.jpg",
    body=[
        f"<p>{you_lla()} asked about Longevity Life Academy this year, so you hear this before anyone else.</p>",
        ("<p><strong>Julie Gibson Clark</strong>, our founding teacher, is 56, a working single mother from Phoenix, and by verified testing she ages about "
         "<strong>eight months for every year</strong>, the second slowest-aging human ever measured. Her routine costs her about $100 a month.</p>"),
        HOUR,
        ("<p>For the next <strong>72 hours</strong>, a block of seats is held for the people on this list. Seats start at <strong>$49</strong>. "
         "The VIP seat adds a private 30-minute Q&amp;A with Julie and comes with a <strong>$249 promo code</strong> toward her full course.</p>"),
    ],
    signoff="To your longest, strongest life,<br><b>The Longevity Life Academy team</b>",
)
EMAILS = [LLA] + school_emails("iibs") + school_emails("rosen")

# ---------- shells ----------
CSS_SCHOOL = """
  body{margin:0;padding:0;background:#EEF1F6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1428}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:600px;margin:0 auto;background:#FFFFFF}
  .hdr{background:#FFFFFF;padding:22px 36px 16px;text-align:left}
  .hdr img{height:66px;width:auto;display:block}
  .hero-img{width:100%;display:block}
  .body-inner{padding:30px 36px 30px;text-align:left}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:28px;line-height:1.25;color:#0A1428;margin:0 0 20px}
  p{font-size:17px;line-height:1.6;color:#2A3244;margin:0 0 16px}
  p strong{color:#0A1428;font-weight:700}
  ul{margin:0 0 16px;padding-left:22px}
  li{font-size:17px;line-height:1.55;color:#2A3244;margin:0 0 8px}
  .btn-row{text-align:center;padding:10px 0 6px}
  .btn{display:inline-block;background:#0A1E3F;color:#FFFFFF !important;text-decoration:none;font-weight:700;font-size:15px;letter-spacing:.06em;padding:16px 38px;border-radius:6px}
  .signoff{margin-top:22px;font-size:17px;color:#2A3244;line-height:1.5}
  .signoff b{color:#0A1428}
  .small{font-size:12px;color:#7A8497;line-height:1.6;margin:18px 0 0}
  .footer{background:#F3F5F9;padding:22px 32px 22px;text-align:center;color:#56627A;border-top:1px solid #E3E8F0}
  .footer img{height:22px;width:auto;margin-bottom:10px}
  .footer p{font-size:12px;line-height:1.7;color:#56627A;margin:0}
  .footer a{color:#56627A;text-decoration:underline}
  @media(max-width:520px){.body-inner{padding:24px 20px}.hdr{padding:18px 20px 12px}.hdr img{height:50px}h1{font-size:24px}}
"""
CSS_LLA = """
  body{margin:0;padding:0;background:#F5F0E5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1220}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF;border-radius:6px;overflow:hidden}
  .top-navy{background:#0A1E3F;padding:30px 20px;text-align:center}
  .top-navy img{display:inline-block;height:104px;width:auto}
  .divider{height:4px;background:#5EB6FF}
  .alert{background:#0A1E3F;padding:18px 24px;text-align:center;color:#fff;font-size:14px}
  .alert b{color:#5EB6FF;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}
  .hero-img{width:100%;display:block}
  .body-inner{padding:44px 40px 40px}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:34px;line-height:1.25;color:#0A1220;margin:0 0 26px}
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
  .footer .tag{font-size:13px;color:#B8C4DE;margin:0 0 18px}
  .footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:14px auto;max-width:220px}
  .footer .fine{font-size:11px;line-height:1.5;color:#8494B4;padding:0 20px}
  .footer .fine a{color:#8494B4;text-decoration:underline}
  @media(max-width:520px){.body-inner{padding:32px 24px}h1{font-size:24px}.top-navy img{height:54px}.details td{display:block;width:100%}.details td.k{padding-bottom:2px}.details td.v{padding-bottom:14px}}
"""
DETAILS_ROWS = [("Dates", "Tue, Oct 27, 7:00 PM ET<br>Sat, Nov 14, 1:00 PM ET"), ("Seats", "From $49"),
                ("VIP seat", "$79: private Q&amp;A, $249 promo code"), ("Refund", "14 days, both seats")]

def head(e, css, title_brand):
    return (f"<!DOCTYPE html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
            f"<title>{e['subject']} &middot; {title_brand}</title>\n<style>{css}</style></head><body>\n<div class=\"preheader\">{e['preheader']}</div>\n")
def comment(e):
    return f"<!-- AC: {e['ac']} | one-time campaign | segment: {e['segment']} | sender: {e['sender']} | file {e['brand']}/{e['id']} -->\n"

def render_school(e):
    b = BRANDS[e["brand"]]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    return comment(e) + head(e, CSS_SCHOOL, b["name"]) + f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF1F6"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  <div class="hdr"><img src="{BASE}/assets/{b['logo']}" alt="{b['name']}, by eTeacher"></div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" width="600" alt="Julie Gibson Clark hosting the live masterclass on Zoom">
  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a></div>
    <div class="signoff">{e['signoff']}</div>
    <p class="small">Julie Gibson Clark&rsquo;s pace of aging (DunedinPACE 0.665) is her publicly reported, verified result. The masterclass is taught by Longevity Life Academy, an eTeacher Group school. 14-day full refund on both seats.</p>
  </div>
  <div class="footer">
    <img src="{BASE}/assets/eteacher-group-logo.png" alt="eTeacher Group">
    <p>{b['copyright']}<br>{ADDRESS}</p>
    <p>{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a></p>
  </div>
</div>
</td></tr></table></body></html>
"""

def render_lla(e):
    b = BRANDS["lla"]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS_ROWS)
    return comment(e) + head(e, CSS_LLA, b["name"]) + f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F0E5"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  <div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>
  <div class="divider"></div>
  <div class="alert"><b>Live on Zoom</b>&middot;&nbsp; October 27 or November 14</div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="Julie Gibson Clark hosting the live masterclass on Zoom">
  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">Pick your date at checkout. 14-day full refund, both seats.</p></div>
    <div class="details">
      <p class="dh">At a glance</p>
      <table role="presentation">
{rows}
      </table>
    </div>
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a></div>
    <div class="signoff">{e['signoff']}</div>
    <p class="small">Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing.</p>
  </div>
  <div class="footer">
    <img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy">
    <p class="tag">It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group.</p>
    <hr>
    <p class="fine">{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a></p>
  </div>
</div>
</td></tr></table></body></html>
"""

# ---------- write ----------
def visible(out):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S)); t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", t)).strip()
manifest = []
import shutil
for d in ["v1", "v2", "iibs", "rosen", "lla"]:
    if os.path.isdir(d): shutil.rmtree(d)
for e in EMAILS:
    out = render_lla(e) if e["brand"] == "lla" else render_school(e)
    os.makedirs(e["brand"], exist_ok=True); path = os.path.join(e["brand"], e["id"] + ".html"); open(path, "w", encoding="utf-8").write(out)
    bw = len(visible(" ".join(e["body"])).split())
    manifest.append(dict(id=e["id"], brand=e["brand"], segment=e["segment"], ac=e["ac"], sender=e["sender"], subject=e["subject"], subject_len=len(e["subject"]),
                         preheader=e["preheader"], preheader_len=len(e["preheader"]), button=html.unescape(BRANDS[e["brand"]]["button"]),
                         cta=html.unescape(cta(e["campaign"], e["id"])), file=path, body_words=bw, words=len(visible(out).split()), chars=len(visible(out))))
json.dump(manifest, open("manifest.json", "w"), indent=2)
for m in manifest: print(m["id"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| body words", m["body_words"], "| whole file", m["words"])

# ---------- gallery ----------
src = open('/home/user/workspace/gallery-src.html', encoding='utf-8').read()
css = src[src.index('<style>'):src.index('</style>')+8]
script = src[src.index('<script>'):src.index('</script>')+9]
script = script.replace("f.addEventListener('load',function(){ fit(f);", "f.addEventListener('load',function(){ acPreview(f); fit(f);")
script = script.replace("(function(){", "(function(){\n  function acPreview(f){ try{ var d=f.contentDocument; if(!d) return; var w=d.createTreeWalker(d.body,NodeFilter.SHOW_TEXT); var n; var re=/%IF !empty\\(\\$FIRSTNAME\\)%([\\s\\S]*?)%ELSE%[\\s\\S]*?%\\/IF%/g; while((n=w.nextNode())){ if(n.nodeValue.indexOf('%IF')>-1) n.nodeValue=n.nodeValue.replace(re,'$1'); } }catch(e){} }", 1)
COL = {"lla": "#5EB6FF", "iibs": "#F5C451", "rosen": "#A78BFA"}
GROUPS = [("lla", "Longevity Life Academy", "LLA leads from the last 3 to 4 months who did not enrol. Sender: Emma | Longevity Advisor. Approved lifecycle shell.", "1 email"),
          ("iibs", "Israel Institute of Biblical Studies", "Alumni, enrolled-did-not-finish, leads. Sender: Sophia Green, Israel Biblical Studies &lt;SophiaG@israelbiblicalstudies.com&gt;. The letter format IIBS campaigns use.", "3 emails"),
          ("rosen", "Rosen School of Hebrew", "Alumni, enrolled-did-not-finish, leads. Sender: Noa Shalev, Campus Manager &lt;admissions@rosenhebrewschool.com&gt;. The letter format Rosen campaigns use.", "3 emails")]
def card(m):
    return f"""<article class="email" id="{m['id']}">
  <div class="meta"><div>
      <span class="tier" style="--c:{COL[m['brand']]}">{m['brand'].upper()}</span> <span class="msg">{m['id'].upper()}</span>
      <div class="subject">{m['ac']} | {m['segment']}</div>
      <div class="dest"><b>Subject</b> ({m['subject_len']}): {html.escape(m['subject'])}<br><b>Preheader</b> ({m['preheader_len']}): {html.escape(m['preheader'])}<br><b>Sender</b>: {html.escape(m['sender'])}<br><b>Button</b> “{m['button']}” → Julie page, pricing fold<br><code>{html.escape(m['cta'])}</code><br><b>Body words</b>: {m['body_words']}</div>
    </div>
    <div class="actions">
      <button class="btn copy" data-file="{m['file']}">Copy HTML</button>
      <a class="btn dl" href="{m['file']}" download="{m['id']}.html">Download .html</a>
      <a class="btn raw" href="{m['file']}" target="_blank" rel="noopener">Open</a>
    </div></div>
  <iframe title="{m['id']}" data-src="{m['file']}" loading="lazy" scrolling="no"></iframe>
</article>"""
toc = "".join(f'<a href="#{m["id"]}">{m["id"].upper()} <small>{m["brand"].upper()}</small></a>' for m in manifest)
sections = "".join(f'<section class="funnel"><h2>{name} <span class="count" style="background:{COL[k]}">{cnt}</span></h2><p class="fdesc">{desc}</p>{"".join(card(m) for m in manifest if m["brand"] == k)}</section>\n' for k, name, desc, cnt in GROUPS)
index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass blast · 7 install-ready emails · 13 Oct 2026</title>
{css}</head><body>
<header>
  <h1>Julie Masterclass blast for Chris &amp; Sandra <span class="count">7 emails</span></h1>
  <p>Install-ready HTML for ActiveCampaign one-time campaigns, 13 Oct 2026. IIBS and Rosen emails use the letter format their own campaigns use (school logo, title, “Shalom %FIRSTNAME%,”, short paragraphs, one button, advisor signature, “by eTeacher Group” footer with the Ramat Gan address). The LLA email uses the approved lifecycle shell. Images: approved lifecycle Zoom assets, 1200px for a 600px slot, 104 to 117KB. Tokens: %FIRSTNAME% with ActiveCampaign's blank-name fallback (previews show the filled branch; the files keep the logic), %UNSUBSCRIBELINK%, %UPDATELINK%.</p>
  <p>Facts from the live Julie page on 13 Oct 2026: Tue 27 Oct 7:00 PM ET or Sat 14 Nov 1:00 PM ET, seats from $49, VIP $79 with private 30-min Q&amp;A and the $249 Blueprint promo code, 14-day full refund on both seats. Per email: <b>Copy HTML</b>, <b>Download .html</b> or <b>Open</b>. <a href="README.md">README</a>.</p>
</header>
<nav class="toc">{toc}</nav>
<main>
{sections}</main>
{script}
</body></html>
"""
open("index.html", "w", encoding="utf-8").write(index)
rows = "\n".join(f"| `{m['file']}` | {m['segment']} | `{m['ac']}` | {m['sender']} | {m['subject']} ({m['subject_len']}) | {m['preheader']} ({m['preheader_len']}) | {m['body_words']} |" for m in manifest)
open("README.md", "w", encoding="utf-8").write(f"""# Julie Masterclass blast · 7 install-ready ActiveCampaign emails

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time campaigns (not automations). One design per email.
- **IIBS / Rosen**: the letter format their own campaigns use (verified against 41 campaign emails in Omri's inbox, Aug to Oct 2026): school logo on top, one image, title, “Shalom %FIRSTNAME%,”, short personal paragraphs, one CAPS button, advisor signature, footer “© 2026 <school> by eTeacher Group. All Rights Reserved. {ADDRESS}” with the eTeacher Group logo (eteachergroup.com).
- **LLA**: the approved lifecycle shell (`lla-masterclass-emails-3tier/launch-email-for-chris`).
- Copy: a person writing to a student. One idea. An introduction to longevity and why it matters to this reader, three bullets taken from the masterclass page's three blocks, the 72-hour student priority and the VIP $249 promo code stated once, seats from $49, and an explicit “if it is not for you, ignore this”.
- Images: approved lifecycle Zoom assets only. 1200px wide for a 600px slot (2x), JPG 104 to 117KB; logos PNG 28KB; eTeacher Group logo 6KB. Hosted on this Pages site.
- Tokens: `%FIRSTNAME%` inside ActiveCampaign's conditional block (`%IF !empty($FIRSTNAME)% … %ELSE% … %/IF%`) so a blank name renders “Shalom,”; `%UNSUBSCRIBELINK%`, `%UPDATELINK%`.

| File | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Body words |
|---|---|---|---|---|---|---|
{rows}

All buttons go to `{LP}#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.

## Offer facts (live page, 13 Oct 2026)
Two dates: Tue 27 Oct 7:00 PM ET, Sat 14 Nov 1:00 PM ET. Seats from $49. VIP $79: private 30-minute Q&A and the $249 Blueprint promo code (MASTERCLASS-VIP, shown after VIP payment, valid to 31 Dec 2026). 14-day full refund on both seats. “Ten years pass. She ages six.” and the three bullets are the page's own words. The checkout accepts no masterclass discount code, so none is promised. The 72-hour hold for students is Omri's offer; it is a message, not a checkout rule.

## Senders (verified in Omri's inbox)
IIBS: Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> (only IIBS-domain campaign sender received; signature title Admissions Advisor). Rosen: Noa Shalev, Campus Manager <admissions@rosenhebrewschool.com> (five campaigns, Sep 2026). LLA: Emma | Longevity Advisor <advisor@longevitylifeacademy.com>.

## Segments
Alumni · Enrolled, did not finish · Leads, per school; LLA leads. Fourth segment per school: to be named by Omri. Exclude masterclass registrants (LGV buyer tags) and the LLA leads list from every school send.

## Rollback
Repo is standalone; nothing in production changed.
""")
print("gallery + readme written")
