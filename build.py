# -*- coding: utf-8 -*-
"""Builds the 7 masterclass blast emails. Shell = approved LLA lifecycle email anatomy
(lla-masterclass-emails-3tier / launch-email-for-chris), school header swapped per brand."""
import os, re, json, html

BASE = "https://gitteromri-ux.github.io/julie-masterclass-blast"
LP = "https://www.longevitylifeacademy.com/julie-masterclass/"

def cta(campaign, content):
    return (f"{LP}?utm_source=activecampaign&amp;utm_medium=email&amp;utm_campaign={campaign}"
            f"&amp;utm_content={content}#pricing")

CSS = """
  body{margin:0;padding:0;background:#F5F0E5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1220}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF;border-radius:6px;overflow:hidden}
  .top-navy{background:#0A1E3F;padding:30px 20px;text-align:center}
  .top-navy img{display:inline-block;height:104px;width:auto}
  .top-white{background:#FFFFFF;padding:26px 20px 22px;text-align:center}
  .top-white img{display:inline-block;height:96px;width:auto}
  .divider{height:4px;background:#5EB6FF}
  .alert{background:#0A1E3F;padding:18px 24px;text-align:center;color:#fff;font-size:14px}
  .alert b{color:#5EB6FF;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}
  .hero-img{width:100%;display:block}
  .body-inner{padding:44px 40px 40px}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:34px;line-height:1.25;color:#0A1220;margin:0 0 26px}
  h1 em{font-style:italic;color:#2E6FB8}
  p{font-size:17px;line-height:1.65;color:#2a3244;margin:0 0 18px}
  p b, p strong{color:#0A1220;font-weight:700}
  ul{margin:0 0 20px;padding-left:22px}
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
  @media(max-width:520px){.body-inner{padding:32px 24px}h1{font-size:24px}.top-navy img{height:54px}.top-white img{height:78px}.details td{display:block;width:100%}.details td.k{padding-bottom:2px}.details td.v{padding-bottom:14px}}
"""

DETAILS_ROWS = [
    ("Instructor", "Julie Gibson Clark, Longevity Life Academy"),
    ("Format", "Live on Zoom, 60 minutes"),
    ("Dates", "Tue, October 27, 7:00 PM ET<br>Sat, November 14, 1:00 PM ET"),
    ("Standard seat", "$49"),
    ("VIP seat", "$79, with a private 30-minute Q&amp;A and a $249 Blueprint credit (valid to Dec 31, 2026)"),
    ("Refund", "14 days, both seats"),
]

def details_block(title="The masterclass at a glance"):
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS_ROWS)
    return f"""    <div class="details">
      <p class="dh">{title}</p>
      <table role="presentation">
{rows}
      </table>
    </div>"""

BRANDS = {
    "lla": dict(
        header=f'<div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>',
        divider="#5EB6FF",
        alert='<b>Live on Zoom</b>&middot;&nbsp; Julie Gibson Clark, ranked No. 2 in the Rejuvenation Olympics',
        footer_tag="It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group.",
        footer_reason="You received this because you asked about Longevity Life Academy at longevitylifeacademy.com",
        button="Reserve My Seat &middot; From $49",
    ),
    "iibs": dict(
        header=f'<div class="top-white"><img src="{BASE}/assets/iibs-logo.png" alt="Israel Institute of Biblical Studies, by eTeacher"></div>',
        divider="#0A1E3F",
        alert='<b>From the eTeacher family</b>&middot;&nbsp; A live masterclass hosted by Longevity Life Academy',
        footer_tag="Israel Institute of Biblical Studies and Longevity Life Academy are schools of eTeacher Group.",
        footer_reason="You received this as a student or contact of the Israel Institute of Biblical Studies",
        button="RESERVE MY SEAT &middot; FROM $49",
    ),
    "rosen": dict(
        header=f'<div class="top-white"><img src="{BASE}/assets/rosen-logo.png" alt="Rosen School of Hebrew, by eTeacher"></div>',
        divider="#1C3657",
        alert='<b>From the eTeacher family</b>&middot;&nbsp; A live masterclass hosted by Longevity Life Academy',
        footer_tag="Rosen School of Hebrew and Longevity Life Academy are schools of eTeacher Group.",
        footer_reason="You received this as a student or contact of Rosen School of Hebrew",
        button="RESERVE MY SEAT &middot; FROM $49",
    ),
}

def render(e):
    b = BRANDS[e["brand"]]
    href = cta(e["campaign"], e["id"])
    body = "\n".join(e["body"])
    btn_meta = e.get("btn_meta", "Pick your date at checkout. Both seats fully refundable within 14 days.")
    return f"""<!-- AC: {e['ac']} | one-time campaign | segment: {e['segment']} | sender: {e['sender']} | file {e['brand']}/{e['id']} -->
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e['subject_plain']} &middot; {e['title_brand']}</title>
<style>{CSS.replace('.divider{height:4px;background:#5EB6FF}', '.divider{height:4px;background:' + b['divider'] + '}')}</style></head><body>
<div class="preheader">{e['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F0E5"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  {b['header']}
  <div class="divider"></div>
  <div class="alert">{b['alert']}</div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="{e['hero_alt']}">

  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">{btn_meta}</p></div>
{details_block()}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a></div>
    <div class="signoff">{e['signoff']}</div>
    <p class="small">{e['small']}</p>
  </div>

  <div class="footer">
    <img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy">
    <p class="tag">{b['footer_tag']}</p>
    <hr>
    <p class="fine">{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a></p>
  </div>
</div>
</td></tr></table></body></html>
"""

# ---------- shared copy blocks ----------
JULIE_INTRO = ("      <p>Julie is 56, a single mother and a recruiter from Phoenix. Her verified pace of aging is <strong>0.665</strong> on the DunedinPACE test, "
               "about <strong>eight months of biological aging per calendar year</strong>. That places her <strong>No. 2 in the Rejuvenation Olympics</strong>, "
               "ahead of Bryan Johnson and his two-million-dollar-a-year program. Her routine costs about <strong>$100 a month</strong>. "
               "Fortune, Business Insider and the Daily Mail have all covered her.</p>")

WHAT_SHE_COVERS = ("      <p>In the hour: how aging is measured, what she eats and when, lights out at 9:00 pm and up at 5:00 am, "
                   "her three-two-one training week, the four-item supplement stack, and the one change to make on Monday.</p>")

DATES_PARA = ("      <p>Two live dates this year: <strong>Tuesday, October 27 at 7:00 PM ET</strong> or <strong>Saturday, November 14 at 1:00 PM ET</strong>. "
              "Seats start at <strong>$49</strong>. The <strong>VIP seat ($79)</strong> adds a <strong>private 30-minute Q&amp;A with Julie</strong> and a "
              "<strong>$249 credit toward The Longevity Blueprint</strong>, her full 18-lesson course.</p>")

VIP_PARA = ""

def school_para(school, short, sister):
    return (f"      <p>{school} is one of eTeacher Group&rsquo;s five online schools, alongside {sister} and, since last year, "
            f"<strong>Longevity Life Academy</strong>. On <strong>October 27</strong> the Academy is hosting a live masterclass on Zoom with "
            f"<strong>Julie Gibson Clark</strong>, and I wanted our own students to hear about it first.</p>")

IIBS = ("The Israel Institute of Biblical Studies", "IIBS", "Rosen School of Hebrew")
ROSEN = ("Rosen School of Hebrew", "Rosen", "the Israel Institute of Biblical Studies")

EMAILS = []

# ---------- 1. LLA leads ----------
EMAILS.append(dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3-4 months, not enrolled",
    ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads",
    sender="Longevity Life Academy (existing LLA sender)", title_brand="Longevity Life Academy",
    subject_plain="Julie is teaching her full protocol live. Two dates only",
    preheader="October 27 or November 14, live on Zoom. Sixty minutes, her exact numbers, seats from $49.",
    hero="julie-zoom-room.jpg", hero_alt="Julie Gibson Clark hosting the live masterclass room on Zoom",
    h1="Sixty live minutes with the woman who ages <em>eight months a year</em>",
    body=[
        "    <p>%FIRSTNAME%, you looked at Longevity Life Academy earlier this year, so you are hearing this from us directly, not through an ad.</p>",
        "      <p><strong>Julie Gibson Clark</strong>, our founding faculty member, is teaching her complete protocol <strong>live on Zoom</strong>. Sixty minutes, her exact numbers, not a recording.</p>",
        JULIE_INTRO,
        WHAT_SHE_COVERS,
        DATES_PARA,
    ],
    signoff="To your longest, strongest life,<br><b>The Longevity Life Academy team</b>",
    small="Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing. Longevity Life Academy is a school of eTeacher Group.",
))

# ---------- IIBS ----------
def iibs_common(segment_id, segment, subject, preheader, hero, h1, opening):
    return dict(
        brand="iibs", id=segment_id, segment=segment,
        ac=f"IIBS_Masterclass_Blast_{segment_id.split('-')[1].capitalize()}", campaign="iibs_masterclass_blast",
        sender="Esther David, Israel Biblical Studies <Estherd@israelbiblicalstudies.com>",
        title_brand="Israel Institute of Biblical Studies",
        subject_plain=subject, preheader=preheader, hero=hero,
        hero_alt="Julie Gibson Clark teaching live on Zoom, Longevity Life Academy",
        h1=h1,
        body=["    <p>Shalom %FIRSTNAME%,</p>"] + opening + [
            school_para(*IIBS),
            JULIE_INTRO, WHAT_SHE_COVERS, DATES_PARA,
        ],
        signoff="Warmly,<br><b>Esther David</b><br>Israel Institute of Biblical Studies, by eTeacher",
        small="Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing. The Israel Institute of Biblical Studies and Longevity Life Academy are both schools of eTeacher Group.",
    )

EMAILS.append(iibs_common(
    "iibs-alumni-01", "IIBS alumni (completed a course)",
    "An invitation for our graduates, from the eTeacher family",
    "The 2nd slowest-aging woman on Earth teaches her protocol live on Zoom. Seats from $49.",
    "julie-zoom-host.jpg",
    "A different kind of class, from the <em>same family</em> of schools",
    ["      <p>You completed a course with us, which makes you part of a larger family than you may realize.</p>"],
))
EMAILS.append(iibs_common(
    "iibs-incomplete-01", "IIBS students who enrolled and did not finish",
    "A 60-minute class, with nothing to catch up on",
    "One live hour on Zoom with the 2nd slowest-aging woman on Earth. Nothing to keep up with. From $49.",
    "julie-portrait.jpg",
    "One hour, live, and <em>nothing to catch up on</em>",
    ["      <p>You began a course with us and life, as it does, got in the way. I am not writing about that. This asks for one hour, with nothing to keep up with afterwards.</p>"],
))
EMAILS.append(iibs_common(
    "iibs-leads-01", "IIBS leads (asked about a course, never enrolled)",
    "She ages eight months a year. Live on Zoom, from $49",
    "A live hour with the 2nd slowest-aging woman on Earth, hosted by our sister school. Two dates.",
    "julie-zoom-grid.jpg",
    "Sixty live minutes with the woman who ages <em>eight months a year</em>",
    ["      <p>You asked about studying with us, and we have kept in touch since. Today I am writing from a different corner of the same family.</p>"],
))

# ---------- Rosen ----------
def rosen_common(segment_id, segment, subject, preheader, hero, h1, opening):
    return dict(
        brand="rosen", id=segment_id, segment=segment,
        ac=f"ROSEN_Masterclass_Blast_{segment_id.split('-')[1].capitalize()}", campaign="rosen_masterclass_blast",
        sender="Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>",
        title_brand="Rosen School of Hebrew",
        subject_plain=subject, preheader=preheader, hero=hero,
        hero_alt="Julie Gibson Clark teaching live on Zoom, Longevity Life Academy",
        h1=h1,
        body=["    <p>Shalom %FIRSTNAME%,</p>"] + opening + [
            school_para(*ROSEN),
            JULIE_INTRO, WHAT_SHE_COVERS, DATES_PARA,
        ],
        signoff="Warmly,<br><b>Noa Shalev</b><br>Campus Manager, Rosen School of Hebrew, by eTeacher",
        small="Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing. Rosen School of Hebrew and Longevity Life Academy are both schools of eTeacher Group.",
    )

EMAILS.append(rosen_common(
    "rosen-alumni-01", "Rosen alumni (completed a course)",
    "An invitation for our graduates, from the eTeacher family",
    "The 2nd slowest-aging woman on Earth teaches her protocol live on Zoom. Seats from $49.",
    "julie-zoom-host.jpg",
    "A different kind of class, from the <em>same family</em> of schools",
    ["      <p>You completed a Hebrew course with us, which makes you part of a larger family than you may realize.</p>"],
))
EMAILS.append(rosen_common(
    "rosen-incomplete-01", "Rosen students who enrolled and did not finish",
    "A 60-minute class, with nothing to catch up on",
    "One live hour on Zoom with the 2nd slowest-aging woman on Earth. Nothing to keep up with. From $49.",
    "julie-portrait.jpg",
    "One hour, live, and <em>nothing to catch up on</em>",
    ["      <p>You began a Hebrew course with us and life, as it does, got in the way. I am not writing about that. This asks for one hour, with nothing to keep up with afterwards.</p>"],
))
EMAILS.append(rosen_common(
    "rosen-leads-01", "Rosen leads (asked about a course, never enrolled)",
    "She ages eight months a year. Live on Zoom, from $49",
    "A live hour with the 2nd slowest-aging woman on Earth, hosted by our sister school. Two dates.",
    "julie-zoom-grid.jpg",
    "Sixty live minutes with the woman who ages <em>eight months a year</em>",
    ["      <p>You asked about learning Hebrew with us, and we have kept in touch since. Today I am writing from a different corner of the same family.</p>"],
))

# ---------- write ----------
manifest = []
for e in EMAILS:
    out = render(e)
    path = os.path.join(e["brand"], e["id"] + ".html")
    open(path, "w", encoding="utf-8").write(out)
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S))
    words = len(html.unescape(re.sub(r"\s+", " ", text)).split())
    manifest.append(dict(file=path, brand=e["brand"], segment=e["segment"], ac=e["ac"], sender=e["sender"],
                         subject=e["subject_plain"], subject_len=len(e["subject_plain"]),
                         preheader=e["preheader"], preheader_len=len(e["preheader"]),
                         hero=e["hero"], button=html.unescape(BRANDS[e["brand"]]["button"]),
                         cta=html.unescape(cta(e["campaign"], e["id"])), words=words))
json.dump(manifest, open("manifest.json", "w"), indent=2)
for m in manifest:
    print(m["file"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| words", m["words"])

# ---------- gallery + README ----------
GROUPS = [
  ("lla", "Longevity Life Academy", "#5EB6FF", "LLA leads from the last 3–4 months who did not enrol. Sender: the existing LLA ActiveCampaign sender.", "1 email"),
  ("iibs", "Israel Institute of Biblical Studies", "#F5C451", "Three segments, one email each. Sender: Esther David, Israel Biblical Studies &lt;Estherd@israelbiblicalstudies.com&gt;. Greeting “Shalom %FIRSTNAME%,” as in current IIBS campaigns.", "3 emails"),
  ("rosen", "Rosen School of Hebrew", "#A78BFA", "Three segments, one email each. Sender: Noa Shalev, Campus Manager, Rosen School of Hebrew &lt;admissions@rosenhebrewschool.com&gt;. Greeting “Shalom %FIRSTNAME%,” as in current Rosen campaigns.", "3 emails"),
]
def card(m):
    fid = m["file"].replace("/", "-").replace(".html", "")
    col = {"lla":"#5EB6FF","iibs":"#F5C451","rosen":"#A78BFA"}[m["brand"]]
    return f"""<article class="email" id="{fid}">
  <div class="meta">
    <div>
      <span class="tier" style="--c:{col}">{m['brand'].upper()}</span> <span class="msg">{m['file'].split('/')[1].replace('.html','').upper()}</span>
      <div class="subject">{m['ac']} | {m['segment']}</div>
      <div class="dest"><b>Subject</b> ({m['subject_len']}): {html.escape(m['subject'])}<br><b>Preheader</b> ({m['preheader_len']}): {html.escape(m['preheader'])}<br><b>Sender</b>: {html.escape(m['sender'])}<br><b>Button</b> “{m['button']}” → Julie page, pricing fold<br><code>{html.escape(m['cta'])}</code></div>
    </div>
    <div class="actions">
      <button class="btn copy" data-file="{m['file']}">Copy HTML</button>
      <a class="btn dl" href="{m['file']}" download="{fid}.html">Download .html</a>
      <a class="btn raw" href="{m['file']}" target="_blank" rel="noopener">Open</a>
    </div>
  </div>
  <iframe title="{fid}" data-src="{m['file']}" loading="lazy" scrolling="no"></iframe>
</article>"""

src = open('/tmp/lla-masterclass-emails-3tier/launch-email-for-chris/index.html', encoding='utf-8').read()
css = src[src.index('<style>'):src.index('</style>')+8]
script = src[src.index('<script>'):src.index('</script>')+9]
toc = "".join(f'<a href="#{m["file"].replace("/","-").replace(".html","")}">{m["file"].split("/")[1].replace(".html","").upper()} <small>{m["brand"].upper()}</small></a>' for m in manifest)
sections = ""
for key, name, col, desc, cnt in GROUPS:
    cards = "".join(card(m) for m in manifest if m["brand"] == key)
    sections += f'<section class="funnel"><h2>{name} <span class="count" style="background:{col}">{cnt}</span></h2><p class="fdesc">{desc}</p>{cards}</section>\n'
index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass blast · 7 install-ready emails · 13 Oct 2026</title>
{css}</head><body>
<header>
  <h1>Julie Masterclass blast for Chris &amp; Sandra <span class="count">7 emails</span></h1>
  <p>Install-ready HTML for ActiveCampaign, 13 Oct 2026. Same 640px shell, CSS, details box, pill button, footer and AC tokens (%FIRSTNAME%, %UNSUBSCRIBELINK%, %UPDATELINK%) as the approved masterclass set. Header swaps to the official IIBS / Rosen “By eTeacher” logo for the school sends. All facts from the live Julie page on 13 Oct 2026: two dates (Tue 27 Oct 7:00 PM ET, Sat 14 Nov 1:00 PM ET), Standard $49, VIP $79 with private 30-min Q&amp;A and $249 Blueprint credit valid to 31 Dec 2026, 14-day full refund on both seats.</p>
  <p>Per email: <b>Copy HTML</b> puts the full production HTML on your clipboard · <b>Download .html</b> saves the file · <b>Open</b> shows the raw file. Also: <a href="README.md">README with segments, senders, subjects, UTM and audit</a>.</p>
</header>
<nav class="toc">{toc}</nav>
<main>
{sections}</main>
{script}
</body></html>
"""
open("index.html", "w", encoding="utf-8").write(index)

rows = "\n".join(f"| `{m['file']}` | {m['brand'].upper()} | {m['segment']} | `{m['ac']}` | {m['sender']} | {m['subject']} ({m['subject_len']}) | {m['preheader']} ({m['preheader_len']}) | `{m['hero']}` |" for m in manifest)
readme = f"""# Julie Masterclass blast · 7 install-ready ActiveCampaign emails

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time campaigns (not automations). Same shell as the approved masterclass lifecycle set
(`lla-masterclass-emails-3tier/launch-email-for-chris`): 640px card, Georgia h1 with blue italic,
17px body, details box, `#5EB6FF` pill button, dark footer with LLA logo, AC tokens `%FIRSTNAME%`,
`%UNSUBSCRIBELINK%`, `%UPDATELINK%`. School sends swap the header to the official
“By eTeacher” logo of the school so the recipient recognises the sender brand; the eTeacher link to
Longevity Life Academy is stated in the first body paragraph of every school email.

## Files

| File | Brand | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Hero |
|---|---|---|---|---|---|---|---|
{rows}

All seven buttons go to `https://www.longevitylifeacademy.com/julie-masterclass/#pricing` with
`utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<file id>`.
Julie-page tracking (pixel + CAPI) only fires on `www.longevitylifeacademy.com/julie-masterclass/`, so do not point these at any other host.
If Anant needs CRM attribution (`cid` / `adGroupID`) for the IIBS and Rosen sends, a CRM campaign ID must be issued first; the UTM set above is complete for GA4 and ActiveCampaign reporting.

## Offer facts used (live page, 13 Oct 2026)

- Instructor: Julie Gibson Clark, 56, Phoenix. DunedinPACE 0.665 (about eight months of biological aging per calendar year). No. 2 on the Rejuvenation Olympics leaderboard, ahead of Bryan Johnson. Routine about $100/month. Press: Fortune, Business Insider, Daily Mail.
- Format: live on Zoom, 60 minutes. Two dates: Tuesday 27 Oct 2026, 7:00 PM ET; Saturday 14 Nov 2026, 1:00 PM ET. Date chosen at checkout.
- Standard seat $49. VIP seat $79: private 30-minute Q&A with Julie after the hour, $249 credit toward The Longevity Blueprint (18 lessons) valid until 31 Dec 2026, four VIP follow-up emails.
- 14-day full refund on both seats (live page footer and checkout policy text).
- Pricing language: “Seats start at $49.” The $249 Blueprint credit is described only as part of the VIP seat; no sentence states or implies a floor of $79.

## Senders (from the user's own inbox, Sep–Oct 2026 campaigns)

- IIBS campaigns arrive from named advisors or “Admissions Office - Israel Biblical Studies <admissions@israelbiblicalstudies.com>”. Chosen here: **Esther David, Israel Biblical Studies <Estherd@israelbiblicalstudies.com>** (sender of the Sep 2026 grant and nurture emails). Greeting “Shalom %FIRSTNAME%,”.
- Rosen campaigns arrive from “Ayala Golan, Rosen Hebrew School” (drips) and **“Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>”** (campaigns). Chosen here: Noa Shalev. Greeting “Shalom %FIRSTNAME%,”.
- LLA: the existing Longevity Life Academy sender already in use for the masterclass automations.
Swap the signature block if Chris prefers a different name; nothing else in the email depends on it.

## Segments (per school, pull from ActiveCampaign / CRM)

1. **Alumni**: completed at least one course. File `*-alumni-01`.
2. **Enrolled, did not finish**: paid, course not completed. File `*-incomplete-01`. Tone written so it does not read as a win-back.
3. **Leads**: asked about a course, never enrolled. File `*-leads-01`.
4. Fourth segment: to be named by Omri; add as `*-<segment>-01` with the same shell.

Exclude from every school send: contacts already registered for the masterclass (LGV buyer tags) and anyone in the LLA leads list, so no contact receives two versions on the same day.

## Audit (done before push)

- Every file rendered at 720px and in a 390px frame; no clipped text, no overflow, logos legible, details box stacks on mobile.
- Word count (whole file incl. footer and details box): 397–458, versus 222–258 for the approved lifecycle emails; the extra ~150 words are the eTeacher link and the Julie introduction that cold segments need.
- Subjects 46–57 chars; preheaders 87–99 chars (approved set: 64–92).
- Images: four approved 1200×700 heroes from the lifecycle set (`julie-zoom-room`, `julie-zoom-host`, `julie-zoom-grid`, `julie-portrait`), LLA logo 800w, official IIBS and Rosen SVG logos rendered to PNG at 630px.
- No claim appears that is not on the live Julie page: no “only time this year”, no seat-count or “reserved block” claim, no “sold out” language.

## Rollback

Repo is standalone; nothing in production changed. Delete the repo or the Pages site to remove the review gallery.
"""
open("README.md", "w", encoding="utf-8").write(readme)
print("gallery + readme written")
