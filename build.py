# -*- coding: utf-8 -*-
"""Builds the Julie Masterclass blast: 7 segments x 2 shells.
V1 = approved LLA lifecycle email anatomy (lla-masterclass-emails-3tier / launch-email-for-chris),
     school sends get a co-branded header (school logo + LLA logo).
V2 = announcement design: co-branded header, Julie hero + stat band, date cards, seat cards, press line.
Both shells share ONE corrected copy source (this file). Facts: live Julie page, 13 Oct 2026."""
import os, re, json, html

BASE = os.environ.get("BASE", "https://gitteromri-ux.github.io/julie-masterclass-blast")
LP = "https://www.longevitylifeacademy.com/julie-masterclass/"

def cta(campaign, content):
    return (f"{LP}?utm_source=activecampaign&amp;utm_medium=email&amp;utm_campaign={campaign}"
            f"&amp;utm_content={content}#pricing")

# ActiveCampaign conditional content (custom-HTML syntax AC inserts itself): survives a blank first name.
def greet_shalom():
    return "%IF !empty($FIRSTNAME)%Shalom %FIRSTNAME%,%ELSE%Shalom,%/IF%"
def you_lla():
    return "%IF !empty($FIRSTNAME)%%FIRSTNAME%, you%ELSE%You%/IF%"

ADDRESS = "eTeacher Group, 8 Aholiav St, 5252261 Ramat Gan, Israel"

# ---------------- shared, corrected copy ----------------
JULIE_INTRO = ("<p>Julie is 56. Her verified pace of aging is <strong>0.665</strong> on the DunedinPACE test, "
               "about <strong>eight months a year</strong>: the <strong>2nd slowest-aging human on Earth</strong>, ahead of Bryan Johnson. "
               "Her routine costs about <strong>$100 a month</strong>. In sixty live minutes she shows the whole protocol: food, sleep, training, supplements.</p>")

WHAT_SHE_COVERS = ("<p>In the hour: how aging is measured, what she eats and when, lights out at 9:00 pm, up at 5:00 am, "
                   "her training week (three strength, two zone-2, one sprint), her four supplements, and the one change to make on Monday.</p>")

DATES_PARA = ("<p>Seats start at <strong>$49</strong>. Pick <strong>October 27</strong> or <strong>November 14</strong> at checkout.</p>")

def school_para(school, sister):
    return (f"<p>{school} and <strong>Longevity Life Academy</strong> are eTeacher Group schools. On <strong>October 27</strong> the Academy "
            f"hosts a live Zoom masterclass with <strong>Julie Gibson Clark</strong>, and I wanted you to hear it from me.</p>")

IIBS = ("Israel Institute of Biblical Studies", "Rosen School of Hebrew")
ROSEN = ("Rosen School of Hebrew", "the Israel Institute of Biblical Studies")

DETAILS_ROWS = [
    ("Dates", "Tue, Oct 27, 7:00 PM ET<br>Sat, Nov 14, 1:00 PM ET"),
    ("Standard seat", "$49"),
    ("VIP seat", "$79: 30-minute private Q&amp;A, $249 Blueprint credit"),
    ("Refund", "14 days, both seats"),
]

BRANDS = {
    "lla": dict(
        name="Longevity Life Academy", short="LLA",
        logo=None, button="Reserve My Seat &middot; From $49",
        alert_k="Live on Zoom", alert_v="The 2nd slowest-aging human on Earth",
        footer_tag="It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group.",
        footer_reason="Sent because you asked about Longevity Life Academy",
        footer_addr="Longevity Life Academy, an eTeacher Group company",
    ),
    "iibs": dict(
        name="Israel Institute of Biblical Studies", short="IIBS",
        logo="iibs-logo.png", button="RESERVE MY SEAT &middot; FROM $49",
        alert_k="From the eTeacher family", alert_v="Live on Zoom with Longevity Life Academy",
        footer_tag="By eTeacher Group.",
        footer_reason="Sent to you as an IIBS student or contact",
        footer_addr=ADDRESS,
    ),
    "rosen": dict(
        name="Rosen School of Hebrew", short="ROSEN",
        logo="rosen-logo.png", button="RESERVE MY SEAT &middot; FROM $49",
        alert_k="From the eTeacher family", alert_v="Live on Zoom with Longevity Life Academy",
        footer_tag="By eTeacher Group.",
        footer_reason="Sent to you as a Rosen student or contact",
        footer_addr=ADDRESS,
    ),
}

# ---------------- emails ----------------
EMAILS = []
EMAILS.append(dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3-4 months, not enrolled",
    ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads",
    sender="Emma | Longevity Advisor <advisor@longevitylifeacademy.com> (existing LLA sender)",
    subject="Julie is teaching her full protocol live. Two dates only",
    preheader="October 27 or November 14, live on Zoom. From $49.",
    hero="julie-zoom-room.jpg", hero_alt="Julie Gibson Clark hosting the live masterclass room on Zoom",
    h1="Sixty live minutes with the woman who ages <em>eight months a year</em>",
    h1_v2="Sixty live minutes with the woman who ages <em>eight months a year</em>",
    body=[
        f"<p>{you_lla()} looked at Longevity Life Academy this year, so you hear this from us directly, not through an ad.</p>",
        "<p><strong>Julie Gibson Clark</strong>, our founding faculty member, is teaching her complete protocol <strong>live on Zoom</strong>, not a recording.</p>",
        JULIE_INTRO,
    ],
    signoff="To your longest, strongest life,<br><b>The Longevity Life Academy team</b>",
    small="Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing.",
))

def school(brand, seg, subject, preheader, hero, h1, opening, sender, signoff, names):
    school_name, sister = names
    return dict(
        brand=brand, id=f"{brand}-{seg}-01",
        segment={"alumni": "alumni (completed a course)", "incomplete": "students who enrolled and did not finish",
                 "leads": "leads (asked about a course, never enrolled)"}[seg],
        ac=f"{brand.upper()}_Masterclass_Blast_{seg.capitalize()}", campaign=f"{brand}_masterclass_blast",
        sender=sender, subject=subject, preheader=preheader, hero=hero,
        hero_alt="Julie Gibson Clark teaching live on Zoom, Longevity Life Academy",
        h1=h1, h1_v2=h1,
        body=[f"<p>{greet_shalom()}</p>", opening, school_para(school_name, sister), JULIE_INTRO],
        signoff=signoff,
        small="Julie&rsquo;s pace-of-aging result is verified through DunedinPACE testing.",
    )

IIBS_SENDER = "Sophia Green, Israel Institute of Biblical Studies <SophiaG@israelbiblicalstudies.com>"
IIBS_SIGN = "Warmly,<br><b>Sophia Green</b><br>Admissions Advisor, Israel Institute of Biblical Studies"
ROSEN_SENDER = "Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>"
ROSEN_SIGN = "Warmly,<br><b>Noa Shalev</b><br>Campus Manager, Rosen School of Hebrew"

SEGS = {
    "alumni": dict(
        subject="For our graduates: a live hour with Julie Gibson Clark",
        preheader="She teaches her protocol live on Zoom. From $49.",
        hero="julie-zoom-host.jpg",
        h1="A different kind of class, from the <em>same family</em> of schools",
        open_iibs="<p>You finished a course with us. That family is larger than you may realize.</p>",
        open_rosen="<p>You finished a Hebrew course with us. That family is larger than you may realize.</p>",
    ),
    "incomplete": dict(
        subject="A 60-minute class, with nothing to catch up on",
        preheader="One live hour on Zoom. From $49.",
        hero="julie-portrait.jpg",
        h1="One hour, live, and <em>nothing to catch up on</em>",
        open_iibs="<p>You began a course with us and life got in the way. This asks for one hour, nothing to keep up with afterwards.</p>",
        open_rosen="<p>You began a Hebrew course with us and life got in the way. This asks for one hour, nothing to keep up with afterwards.</p>",
    ),
    "leads": dict(
        subject="She ages eight months a year. Live on Zoom, from $49",
        preheader="Live on Zoom, October 27 or November 14. From $49.",
        hero="julie-zoom-grid.jpg",
        h1="Sixty live minutes with the woman who ages <em>eight months a year</em>",
        open_iibs="<p>You asked about studying with us. Today I write from another corner of it.</p>",
        open_rosen="<p>You asked about learning Hebrew with us. Today I write from another corner of it.</p>",
    ),
}
for seg, s in SEGS.items():
    EMAILS.append(school("iibs", seg, s["subject"], s["preheader"], s["hero"], s["h1"], s["open_iibs"], IIBS_SENDER, IIBS_SIGN, IIBS))
for seg, s in SEGS.items():
    EMAILS.append(school("rosen", seg, s["subject"], s["preheader"], s["hero"], s["h1"], s["open_rosen"], ROSEN_SENDER, ROSEN_SIGN, ROSEN))

# ---------------- V1 shell (approved anatomy) ----------------
CSS_V1 = """
  body{margin:0;padding:0;background:#F5F0E5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1220}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF;border-radius:6px;overflow:hidden}
  .top-navy{background:#0A1E3F;padding:30px 20px;text-align:center}
  .top-navy img{display:inline-block;height:104px;width:auto}
  .cobrand{background:#FFFFFF;padding:24px 20px 20px}
  .cobrand table{width:100%;border-collapse:collapse}
  .cobrand td{vertical-align:middle;text-align:center}
  .cobrand img.school{height:84px;width:auto;display:inline-block}
  .cobrand img.lla{height:70px;width:auto;display:inline-block}
  .cobrand td.rule{width:1px;border-left:1px solid #D7DEEA}
  .divider{height:4px;background:#5EB6FF}
  .alert{background:#0A1E3F;padding:18px 24px;text-align:center;color:#fff;font-size:14px}
  .alert b{color:#5EB6FF;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}
  .hero-img{width:100%;display:block}
  .body-inner{padding:44px 40px 40px}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:34px;line-height:1.25;color:#0A1220;margin:0 0 26px}
  h1 em{font-style:italic;color:#2E6FB8}
  p{font-size:17px;line-height:1.65;color:#2a3244;margin:0 0 18px}
  p b, p strong{color:#0A1220;font-weight:700}
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
  @media(max-width:520px){.body-inner{padding:32px 24px}h1{font-size:24px}.top-navy img{height:54px}.cobrand img.school{height:56px}.cobrand img.lla{height:48px}.details td{display:block;width:100%}.details td.k{padding-bottom:2px}.details td.v{padding-bottom:14px}}
"""

def details_block(title="At a glance"):
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS_ROWS)
    return f"""    <div class="details">
      <p class="dh">{title}</p>
      <table role="presentation">
{rows}
      </table>
    </div>"""

def header_v1(b):
    if not b["logo"]:
        return f'<div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>'
    return (f'<div class="cobrand"><table role="presentation"><tr>'
            f'<td style="width:50%"><img class="school" src="{BASE}/assets/{b["logo"]}" alt="{b["name"]}, by eTeacher"></td>'
            f'<td class="rule"></td>'
            f'<td style="width:50%"><img class="lla" src="{BASE}/assets/lla-logo-dark.png" alt="Longevity Life Academy by eTeacher Group"></td>'
            f'</tr></table></div>')

def comment(e, v):
    return f"<!-- AC: {e['ac']} | one-time campaign | {v} | segment: {e['segment']} | sender: {e['sender']} | file {v}/{e['brand']}/{e['id']} -->"

def render_v1(e):
    b = BRANDS[e["brand"]]
    href = cta(e["campaign"], e["id"])
    body = "\n".join("    " + x for x in e["body"] + [DATES_PARA])
    return f"""{comment(e, 'v1')}
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e['subject']} &middot; {b['name']}</title>
<style>{CSS_V1}</style></head><body>
<div class="preheader">{e['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F0E5"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  {header_v1(b)}
  <div class="divider"></div>
  <div class="alert"><b>{b['alert_k']}</b>&middot;&nbsp; {b['alert_v']}</div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="{e['hero_alt']}">

  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">14-day full refund, both seats.</p></div>
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

# ---------------- V2 shell (announcement design) ----------------
CSS_V2 = """
  body{margin:0;padding:0;background:#EEF3FA;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1428}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  table{border-collapse:collapse}
  .wrap{width:640px;max-width:640px;margin:0 auto;background:#FFFFFF}
  .cb td{vertical-align:middle;text-align:center}
  .cb img.school{height:88px;width:auto;display:inline-block}
  .cb img.lla{height:74px;width:auto;display:inline-block}
  .cb img.llawhite{height:110px;width:auto;display:inline-block}
  .cb td.rule{width:1px;border-left:1px solid #D7DEEA}
  .hero{display:block;width:100%;height:auto}
  .navy{background:#0A1E3F}
  .kicker{font-size:15px;line-height:1.4;letter-spacing:.14em;text-transform:uppercase;color:#5EB6FF;font-weight:700}
  .h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:40px;line-height:1.12;color:#FFFFFF;margin:12px 0 0}
  .h1 em{font-style:italic;color:#5EB6FF}
  .stat{text-align:center;padding:22px 8px 24px}
  .stat .n{font-family:Georgia,'Times New Roman',serif;font-size:40px;line-height:1;color:#FFFFFF}
  .stat .l{font-size:15px;line-height:1.35;color:#B8C4DE;margin-top:8px}
  .stat.mid{border-left:1px solid rgba(255,255,255,.14);border-right:1px solid rgba(255,255,255,.14)}
  .body{padding:40px 44px 8px}
  p{font-size:18px;line-height:1.6;color:#2A3244;margin:0 0 18px}
  p strong{color:#0A1428}
  .cap{font-size:15px;line-height:1.4;color:#56627A;margin:10px 0 0;text-align:center}
  .card{background:#F2F7FF;border-radius:12px;padding:22px 20px;text-align:center}
  .card .d{font-size:15px;letter-spacing:.12em;text-transform:uppercase;color:#2E6FB8;font-weight:700}
  .card .t{font-family:Georgia,'Times New Roman',serif;font-size:30px;line-height:1.1;color:#0A1428;margin-top:8px}
  .card .s{font-size:17px;color:#2A3244;margin-top:6px}
  .seat{border-radius:12px;padding:24px 22px;vertical-align:top}
  .seat.std{background:#FFFFFF;border:1px solid #D7DEEA}
  .seat.vip{background:#0A1E3F}
  .seat .name{font-size:15px;letter-spacing:.12em;text-transform:uppercase;font-weight:700}
  .seat .price{font-family:Georgia,'Times New Roman',serif;font-size:44px;line-height:1;margin:10px 0 6px}
  .seat .inc{font-size:16px;line-height:1.55}
  .seat.std .name{color:#2E6FB8}.seat.std .price{color:#0A1428}.seat.std .inc{color:#2A3244}
  .seat.vip .name{color:#5EB6FF}.seat.vip .price{color:#FFFFFF}.seat.vip .inc{color:#DCE6F6}
  .btn{display:inline-block;background:#5EB6FF;color:#0A1428 !important;text-decoration:none;font-weight:700;font-size:18px;padding:19px 46px;border-radius:999px}
  .btn-meta{font-size:15px;color:#56627A;margin:12px 0 0;text-align:center}
  .press{text-align:center;padding:26px 24px 10px;font-family:Georgia,'Times New Roman',serif;font-size:16px;letter-spacing:.16em;text-transform:uppercase;color:#56627A}
  .press b{color:#0A1428;font-weight:700}
  .signoff{font-size:17px;line-height:1.55;color:#2A3244;margin-top:10px}
  .signoff b{color:#0A1428}
  .small{font-size:13px;color:#7A8497;line-height:1.6;margin:18px 0 0}
  .footer{background:#070A12;padding:34px 24px 22px;text-align:center;color:#B8C4DE}
  .footer img{height:74px;width:auto;margin-bottom:14px}
  .footer .tag{font-size:14px;color:#B8C4DE;margin:0 0 18px}
  .footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:14px auto;max-width:220px}
  .footer .fine{font-size:12px;line-height:1.6;color:#8494B4;padding:0 20px}
  .footer .fine a{color:#8494B4;text-decoration:underline}
  @media(max-width:620px){
    .wrap{width:100% !important}
    .body{padding:28px 22px 8px !important}
    .h1{font-size:30px !important}
    .cb img.school{height:58px !important}.cb img.lla{height:48px !important}.cb img.llawhite{height:64px !important}
    .stat .n{font-size:30px !important}
    .stack td.col{display:block !important;width:100% !important;padding:0 0 14px 0 !important}
    .seat .price{font-size:38px !important}
  }
"""

def header_v2(b):
    if not b["logo"]:
        return (f'<table role="presentation" width="100%" class="cb navy"><tr><td style="padding:28px 20px 24px">'
                f'<img class="llawhite" src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></td></tr></table>')
    return (f'<table role="presentation" width="100%" class="cb" style="background:#FFFFFF"><tr>'
            f'<td style="width:50%;padding:22px 16px 18px"><img class="school" src="{BASE}/assets/{b["logo"]}" alt="{b["name"]}, by eTeacher"></td>'
            f'<td class="rule"></td>'
            f'<td style="width:50%;padding:22px 16px 18px"><img class="lla" src="{BASE}/assets/lla-logo-dark.png" alt="Longevity Life Academy by eTeacher Group"></td>'
            f'</tr></table>')

def render_v2(e):
    b = BRANDS[e["brand"]]
    href = cta(e["campaign"], e["id"])
    body = "\n".join("    " + x for x in e["body"])
    kicker = "Live on Zoom &middot; October 27 or November 14" if e["brand"] == "lla" else "From the eTeacher family &middot; Live on Zoom"
    return f"""{comment(e, 'v2')}
<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e['subject']} &middot; {b['name']}</title>
<style>{CSS_V2}</style></head><body>
<div class="preheader">{e['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF3FA"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" class="wrap" cellpadding="0" cellspacing="0" width="640" style="border-radius:8px;overflow:hidden">
  <tr><td>{header_v2(b)}</td></tr>
  <tr><td style="height:4px;background:#5EB6FF;font-size:0;line-height:0">&nbsp;</td></tr>
  <tr><td><img class="hero" src="{BASE}/assets/images/julie-golden-hero.jpg" width="640" alt="Julie Gibson Clark"></td></tr>
  <tr><td class="navy" style="padding:30px 44px 6px;text-align:left">
    <div class="kicker">{kicker}</div>
    <div class="h1">{e['h1_v2']}</div>
  </td></tr>
  <tr><td class="navy" style="padding:18px 24px 26px">
    <table role="presentation" width="100%"><tr>
      <td class="stat" width="33%"><div class="n">0.665</div><div class="l">verified pace of aging<br>(DunedinPACE)</div></td>
      <td class="stat mid" width="34%"><div class="n">8 mo</div><div class="l">of biological aging<br>per calendar year</div></td>
      <td class="stat" width="33%"><div class="n">No. 2</div><div class="l">on Earth, Rejuvenation<br>Olympics leaderboard</div></td>
    </tr></table>
  </td></tr>
  <tr><td class="body" style="text-align:left">
{body}
  </td></tr>
  <tr><td style="padding:6px 0 0"><img class="hero" src="{BASE}/assets/images/julie-zoom-band.jpg" width="640" alt="Julie Gibson Clark hosting the live Zoom room"></td></tr>
  <tr><td style="padding:0 44px"><p class="cap">Live on Zoom. Julie hosting, one room, not a recording.</p></td></tr>
  <tr><td style="padding:26px 44px 0">
    <table role="presentation" width="100%" class="stack"><tr>
      <td class="col" width="50%" style="padding:0 8px 0 0"><div class="card"><div class="d">Date one</div><div class="t">Tue, Oct 27</div><div class="s">7:00 PM ET</div></div></td>
      <td class="col" width="50%" style="padding:0 0 0 8px"><div class="card"><div class="d">Date two</div><div class="t">Sat, Nov 14</div><div class="s">1:00 PM ET</div></div></td>
    </tr></table>
    <p class="cap">Same masterclass, two dates. Pick yours at checkout.</p>
  </td></tr>
  <tr><td style="padding:26px 44px 0">
    <table role="presentation" width="100%" class="stack"><tr>
      <td class="col" width="50%" style="padding:0 8px 0 0"><table role="presentation" width="100%"><tr><td class="seat std">
        <div class="name">Standard seat</div><div class="price">$49</div>
        <div class="inc">60 minutes live with Julie. Her full protocol, her daily schedule and supplement list, yours to keep.</div>
      </td></tr></table></td>
      <td class="col" width="50%" style="padding:0 0 0 8px"><table role="presentation" width="100%"><tr><td class="seat vip">
        <div class="name">VIP seat</div><div class="price">$79</div>
        <div class="inc">Everything in Standard, plus a private 30-minute Q&amp;A with Julie and a <strong style="color:#FFFFFF">$249 credit</strong> toward The Longevity Blueprint, valid to Dec 31, 2026.</div>
      </td></tr></table></td>
    </tr></table>
  </td></tr>
  <tr><td style="padding:30px 44px 0;text-align:center">
    <a class="btn" href="{href}">{b['button']}</a>
    <p class="btn-meta">Seats start at $49. 14-day full refund, both seats.</p>
  </td></tr>
  <tr><td class="press">Covered by <b>Fortune</b> &middot; <b>Business Insider</b> &middot; <b>Daily Mail</b></td></tr>
  <tr><td style="padding:16px 44px 40px;text-align:left">
    <div class="signoff">{e['signoff']}</div>
    <p class="small">{e['small']}</p>
  </td></tr>
  <tr><td class="footer">
    <img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy">
    <p class="tag">{b['footer_tag']}</p>
    <hr>
    <p class="fine">{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a><br>{b['footer_addr']}</p>
  </td></tr>
</table>
</td></tr></table></body></html>
"""

# ---------------- write ----------------
def visible(out):
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S))
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()
def chars(out): return len(visible(out))
def words(out):
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S))
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return len(html.unescape(re.sub(r"\s+", " ", text)).split())

manifest = []
for e in EMAILS:
    rec = dict(id=e["id"], brand=e["brand"], segment=e["segment"], ac=e["ac"], sender=e["sender"],
               subject=e["subject"], subject_len=len(e["subject"]), preheader=e["preheader"], preheader_len=len(e["preheader"]),
               button=html.unescape(BRANDS[e["brand"]]["button"]), cta=html.unescape(cta(e["campaign"], e["id"])), hero_v1=e["hero"])
    for v, fn in (("v1", render_v1), ("v2", render_v2)):
        out = fn(e)
        os.makedirs(os.path.join(v, e["brand"]), exist_ok=True)
        path = os.path.join(v, e["brand"], e["id"] + ".html")
        open(path, "w", encoding="utf-8").write(out)
        rec[f"file_{v}"] = path; rec[f"words_{v}"] = words(out); rec[f"chars_{v}"] = chars(out)
    manifest.append(rec)
json.dump(manifest, open("manifest.json", "w"), indent=2)
CEIL_W, CEIL_C = 262, 1534
bad=[m["id"] for m in manifest if m["words_v1"]>CEIL_W or m["chars_v1"]>CEIL_C]
print("V1 ceiling check (<=262 words, <=1534 chars):", "PASS" if not bad else "FAIL "+str(bad))
for m in manifest:
    print(m["id"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| words v1", m["words_v1"], "| v2", m["words_v2"], "| chars v1", m["chars_v1"], "| v2", m["chars_v2"])

# ---------------- gallery ----------------
src = open('/home/user/workspace/gallery-src.html', encoding='utf-8').read()
css = src[src.index('<style>'):src.index('</style>')+8]
script = src[src.index('<script>'):src.index('</script>')+9]
script = script.replace("f.addEventListener('load',function(){ fit(f);", "f.addEventListener('load',function(){ acPreview(f); fit(f);")
script = script.replace("(function(){", "(function(){\n  function acPreview(f){ try{ var d=f.contentDocument; if(!d) return; var w=d.createTreeWalker(d.body,NodeFilter.SHOW_TEXT); var n; var re=/%IF !empty\\(\\$FIRSTNAME\\)%([\\s\\S]*?)%ELSE%[\\s\\S]*?%\\/IF%/g; while((n=w.nextNode())){ if(n.nodeValue.indexOf('%IF')>-1) n.nodeValue=n.nodeValue.replace(re,'$1'); } }catch(e){} }", 1)
assert 'acPreview(f); fit(f)' in script
COL = {"lla": "#5EB6FF", "iibs": "#F5C451", "rosen": "#A78BFA"}
GROUPS = [
  ("lla", "Longevity Life Academy", "LLA leads from the last 3 to 4 months who did not enrol. Sender: Emma | Longevity Advisor &lt;advisor@longevitylifeacademy.com&gt;, the existing LLA sender.", "1 email"),
  ("iibs", "Israel Institute of Biblical Studies", "Three segments, one email each. Sender: Sophia Green, Israel Institute of Biblical Studies &lt;SophiaG@israelbiblicalstudies.com&gt; (verified IIBS-domain sender in Omri's inbox). Greeting “Shalom %FIRSTNAME%,” with a blank-name fallback.", "3 emails"),
  ("rosen", "Rosen School of Hebrew", "Three segments, one email each. Sender: Noa Shalev, Campus Manager, Rosen School of Hebrew &lt;admissions@rosenhebrewschool.com&gt; (verified, 5 campaigns Sep 2026). Greeting “Shalom %FIRSTNAME%,” with a blank-name fallback.", "3 emails"),
]
def card(m):
    fid = m["id"]; col = COL[m["brand"]]
    return f"""<article class="email" id="{fid}">
  <div class="meta">
    <div>
      <span class="tier" style="--c:{col}">{m['brand'].upper()}</span> <span class="msg">{fid.upper()}</span>
      <div class="subject">{m['ac']} | {m['segment']}</div>
      <div class="dest"><b>Subject</b> ({m['subject_len']}): {html.escape(m['subject'])}<br><b>Preheader</b> ({m['preheader_len']}): {html.escape(m['preheader'])}<br><b>Sender</b>: {html.escape(m['sender'])}<br><b>Button</b> “{m['button']}” → Julie page, pricing fold<br><code>{html.escape(m['cta'])}</code><br><b>Words</b>: V1 {m['words_v1']} · V2 {m['words_v2']} (whole file incl. footer)</div>
    </div>
    <div class="actions">
      <div class="vswitch"><button class="vbtn on" data-v="v1">V1 · approved shell</button><button class="vbtn" data-v="v2">V2 · announcement design</button></div>
      <button class="btn copy" data-file="{m['file_v1']}" data-v1="{m['file_v1']}" data-v2="{m['file_v2']}">Copy HTML</button>
      <a class="btn dl" href="{m['file_v1']}" download="{fid}-v1.html" data-v1="{m['file_v1']}" data-v2="{m['file_v2']}">Download .html</a>
      <a class="btn raw" href="{m['file_v1']}" target="_blank" rel="noopener" data-v1="{m['file_v1']}" data-v2="{m['file_v2']}">Open</a>
    </div>
  </div>
  <iframe title="{fid}" data-src="{m['file_v1']}" data-v1="{m['file_v1']}" data-v2="{m['file_v2']}" loading="lazy" scrolling="no"></iframe>
</article>"""
toc = "".join(f'<a href="#{m["id"]}">{m["id"].upper()} <small>{m["brand"].upper()}</small></a>' for m in manifest)
sections = ""
for key, name, desc, cnt in GROUPS:
    cards = "".join(card(m) for m in manifest if m["brand"] == key)
    sections += f'<section class="funnel"><h2>{name} <span class="count" style="background:{COL[key]}">{cnt}</span></h2><p class="fdesc">{desc}</p>{cards}</section>\n'
extra_css = """<style>
.vswitch{display:flex;gap:6px;margin-bottom:8px}
.vbtn{font:600 12px/1 inherit;padding:8px 10px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:transparent;color:#B8C4DE;cursor:pointer}
.vbtn.on{background:#5EB6FF;color:#0A1428;border-color:#5EB6FF}
.vbtn:hover{border-color:#5EB6FF}
</style>"""
extra_js = """<script>
document.querySelectorAll('article.email').forEach(function(a){
  a.querySelectorAll('.vbtn').forEach(function(b){
    b.addEventListener('click',function(){
      var v=b.getAttribute('data-v');
      a.querySelectorAll('.vbtn').forEach(function(x){x.classList.toggle('on',x===b)});
      a.querySelectorAll('[data-v1]').forEach(function(el){
        var f=el.getAttribute('data-'+v);
        if(el.tagName==='IFRAME'){ el.src=f; el.setAttribute('data-src',f); }
        else if(el.classList.contains('copy')){ el.setAttribute('data-file',f); }
        else { el.href=f; if(el.hasAttribute('download')) el.setAttribute('download', a.id+'-'+v+'.html'); }
      });
    });
  });
});
</script>"""
index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass blast · 7 segments · V1 approved shell + V2 announcement design · 13 Oct 2026</title>
{css}{extra_css}</head><body>
<header>
  <h1>Julie Masterclass blast for Chris &amp; Sandra <span class="count">7 segments · 2 designs</span></h1>
  <p>Install-ready HTML for ActiveCampaign one-time campaigns, 13 Oct 2026. Every email exists in two shells with identical copy: <b>V1</b> is the approved masterclass lifecycle anatomy (640px, Georgia h1, details box, pill button, dark footer) with a co-branded school + LLA header on the school sends; <b>V2</b> is the announcement design (co-branded header, Julie hero and stat band, two date cards, Standard and VIP seat cards, press line). AC tokens: %FIRSTNAME% with a blank-name fallback (%IF !empty($FIRSTNAME)%), %UNSUBSCRIBELINK%, %UPDATELINK%.</p>
  <p>Facts from the live Julie page on 13 Oct 2026: two dates (Tue 27 Oct 7:00 PM ET, Sat 14 Nov 1:00 PM ET), Standard $49, VIP $79 with private 30-min Q&amp;A and $249 Blueprint credit valid to 31 Dec 2026, 14-day full refund on both seats. Per email: switch <b>V1 / V2</b>, then <b>Copy HTML</b>, <b>Download .html</b> or <b>Open</b>. <a href="README.md">README: segments, senders, subjects, UTMs, audit</a>.</p>
</header>
<nav class="toc">{toc}</nav>
<main>
{sections}</main>
{script}
{extra_js}
</body></html>
"""
open("index.html", "w", encoding="utf-8").write(index)

rows = "\n".join(f"| `{m['id']}` | {m['brand'].upper()} | {m['segment']} | `{m['ac']}` | {m['sender']} | {m['subject']} ({m['subject_len']}) | {m['preheader']} ({m['preheader_len']}) | {m['words_v1']} / {m['words_v2']} ({m['chars_v1']}) |" for m in manifest)
readme = f"""# Julie Masterclass blast · 7 segments · V1 approved shell + V2 announcement design

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time ActiveCampaign campaigns (not automations). Files: `v1/<brand>/<id>.html` and `v2/<brand>/<id>.html`, identical copy, two shells.

- **V1** = approved masterclass lifecycle anatomy (`lla-masterclass-emails-3tier/launch-email-for-chris`): 640px card, Georgia h1 with blue italic, 17px body, details box, `#5EB6FF` pill button, dark footer. School sends carry a co-branded header: school logo, thin rule, LLA logo.
- **V2** = announcement design: co-branded header, Julie golden-hour hero, navy headline block, stat band (0.665 / 8 mo / No. 2), Zoom live-room band, two date cards, Standard $49 and VIP $79 seat cards, one pill button, press line (Fortune, Business Insider, Daily Mail), same footer. Table-based, inline-safe CSS with one mobile media query.
- AC tokens: `%FIRSTNAME%` wrapped in AC conditional content so a blank first name renders "Shalom," / "You looked at…" instead of "Shalom ,"; `%UNSUBSCRIBELINK%`, `%UPDATELINK%`.

## Files

| Id | Brand | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Words V1 / V2 (chars V1) |
|---|---|---|---|---|---|---|---|
{rows}

All buttons go to `{LP}#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.
Julie-page tracking (pixel + CAPI) only fires on `www.longevitylifeacademy.com/julie-masterclass/`, so do not point these at any other host.
If Anant needs CRM attribution (`cid` / `adGroupID`) for the IIBS and Rosen sends, a CRM campaign ID must be issued first.

## Offer facts used (live page, 13 Oct 2026)

- Instructor: Julie Gibson Clark, 56, Phoenix. DunedinPACE 0.665 (about eight months of biological aging per calendar year). "2nd slowest-aging human on Earth", No. 2 on the Rejuvenation Olympics leaderboard, ahead of Bryan Johnson. Routine about $100/month. Press: Fortune, Business Insider, Daily Mail.
- Format: live on Zoom, 60 minutes. Two dates: Tuesday 27 Oct 2026, 7:00 PM ET; Saturday 14 Nov 2026, 1:00 PM ET. Date chosen at checkout.
- Standard seat $49. VIP seat $79: private 30-minute Q&A with Julie after the hour, $249 credit toward The Longevity Blueprint (18 lessons) valid until 31 Dec 2026.
- 14-day full refund on both seats (live page and checkout policy text).
- Pricing language: "Seats start at $49." The $249 Blueprint credit is described only as part of the VIP seat; no sentence states or implies a floor of $79.
- No masterclass discount code exists: the live checkout's promo field returns "Not valid for this package" for any code, so none is promised in any email.

## Senders (verified in Omri's inbox, Aug to Oct 2026)

- **IIBS**: Sophia Green, Israel Institute of Biblical Studies <SophiaG@israelbiblicalstudies.com>, the only IIBS-domain campaign sender received (3 Aug 2026). Title in her signature: Admissions Advisor. (Esther David, used in the first draft, is a Rosen School of Hebrew admissions sender, not IIBS; corrected.)
- **Rosen**: Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>, five campaigns 7 to 11 Sep 2026. Greeting "Shalom Omri," and sign-off "Warmly, Noa Shalev / Campus Manager" match her real campaigns.
- **LLA**: Emma | Longevity Advisor <advisor@longevitylifeacademy.com>, the sender of the live masterclass automations.
- Footer address on school sends: "{ADDRESS}", as printed in the real IIBS and Rosen campaign footers.

## Segments (per school, pull from ActiveCampaign / CRM)

1. **Alumni**: completed at least one course. `*-alumni-01`.
2. **Enrolled, did not finish**: paid, course not completed. `*-incomplete-01`. Written so it does not read as a win-back.
3. **Leads**: asked about a course, never enrolled. `*-leads-01`.
4. Fourth segment: to be named by Omri; add as `*-<segment>-01` with the same shells.

Exclude from every school send: contacts already registered for the masterclass (LGV buyer tags) and anyone in the LLA leads list, so nobody receives two versions on the same day.

## Corrections made on 13 Oct 2026 (second pass)

1. One phrasing for Julie's rank everywhere: "2nd slowest-aging human on Earth" (the live page's words), with "No. 2 on the Rejuvenation Olympics leaderboard" as the source.
2. Removed the unverified "since last year" about Longevity Life Academy.
3. Alumni subject no longer leans on the eTeacher name: "For our graduates: a live hour with Julie Gibson Clark".
4. "three-two-one training week" spelled out: three strength sessions, two zone-2 sessions, one sprint session.
5. Co-branded header (school logo + LLA logo) on every school email, both shells.
6. Length: V1 is at or under the approved lifecycle set's ceiling on every email (approved set: 191 to 262 words, 1,203 to 1,534 visible characters; the build fails otherwise). V2 carries the stat band and the date and seat cards, so it runs about 320 to 330 words; see the table.
7. Blank first name: AC conditional content fallback on every greeting.
8. IIBS sender corrected to a verified IIBS-domain sender (Sophia Green).
9. Footer carries the real eTeacher Group postal address on school sends.

## Audit (done before push)

- All 14 files rendered in Chromium at 720px and 390px; no clipped text, no overflow, cards stack on mobile.
- All asset URLs on the Pages host return HTTP 200; every CTA resolves to the live Julie page pricing fold.
- Ban greps: zero em dashes, zero exclamation marks in copy, zero hype words (unlock, elevate, journey, seamless, empower, transform, game-changer, hurry, act now, don't miss out).
- Not tested: Gmail, Apple Mail, Outlook rendering. Both shells use tables plus one media query, the same risk profile as the approved set. A Gmail test send to Omri is available on request.

## Rollback

Repo is standalone; nothing in production changed. Delete the repo or the Pages site to remove the review gallery.
"""
open("README.md", "w", encoding="utf-8").write(readme)
print("gallery + readme written")
