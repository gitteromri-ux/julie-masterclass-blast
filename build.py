# -*- coding: utf-8 -*-
"""Julie Masterclass blast: 7 segments x 2 shells, one copy source.
Copy follows Omri's 13 Oct brief: exclusive benefit for eTeacher students, one line on the world of longevity,
invitation to The Longevity Masterclass of the Year by Longevity Life Academy with Julie Gibson Clark,
72-hour priority seating, exclusive VIP promo code ($249 Blueprint credit), live Q&A on VIP, seats from $49.
V1 = house format of each sender (LLA: approved lifecycle shell; IIBS/Rosen: the letter format their campaigns use,
with school logo + eTeacher Group logo). V2 = announcement design (school + eTeacher Group + LLA header, approved
Zoom hero, stat band, date and seat cards). Imagery: approved lifecycle Zoom assets only."""
import os, re, json, html

BASE = os.environ.get("BASE", "https://gitteromri-ux.github.io/julie-masterclass-blast")
LP = "https://www.longevitylifeacademy.com/julie-masterclass/"
ADDRESS = "8 Aholiav St, 5252261 Ramat Gan, Israel"

def cta(campaign, content):
    return (f"{LP}?utm_source=activecampaign&amp;utm_medium=email&amp;utm_campaign={campaign}"
            f"&amp;utm_content={content}#pricing")

def greet_shalom(): return "%IF !empty($FIRSTNAME)%Shalom %FIRSTNAME%,%ELSE%Shalom,%/IF%"
def you_lla(): return "%IF !empty($FIRSTNAME)%%FIRSTNAME%, you%ELSE%You%/IF%"

# ---------------- brands ----------------
BRANDS = {
    "lla": dict(name="Longevity Life Academy", logo=None,
                button="Reserve My Priority Seat", kicker="Priority seating &middot; Live on Zoom",
                sender="Emma | Longevity Advisor <advisor@longevitylifeacademy.com>",
                footer_reason="Sent because you asked about Longevity Life Academy"),
    "iibs": dict(name="Israel Institute of Biblical Studies", short="Israel Biblical Studies", logo="iibs-logo.png",
                 button="RESERVE MY PRIORITY SEAT", kicker="An eTeacher Group student benefit",
                 sender="Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com>",
                 sign="Warmly,<br><b>Sophia Green</b><br>Admissions Advisor<br>Israel Institute of Biblical Studies",
                 copyright="&copy; 2026 Israel Institute of Biblical Studies by eTeacher Group. All Rights Reserved.",
                 footer_reason="Sent to you as a student or contact of the Israel Institute of Biblical Studies",
                 course="course", asked="studying with us"),
    "rosen": dict(name="Rosen School of Hebrew", short="Rosen", logo="rosen-logo.png",
                  button="RESERVE MY PRIORITY SEAT", kicker="An eTeacher Group student benefit",
                  sender="Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>",
                  sign="Warmly,<br><b>Noa Shalev</b><br>Campus Manager<br>Rosen School of Hebrew",
                  copyright="&copy; 2026 Rosen School of Hebrew by eTeacher Group. All Rights Reserved.",
                  footer_reason="Sent to you as a student or contact of Rosen School of Hebrew",
                  course="Hebrew course", asked="learning Hebrew with us"),
}

# ---------------- shared copy (Omri's brief) ----------------
LONGEVITY = ("<p>Longevity has stopped being theory. People in their 50s, 60s and 70s are now measurably slowing how fast they age, "
             "with sleep, food and movement rather than money. Our sister school, <strong>Longevity Life Academy</strong>, teaches exactly that, "
             "live, with the same teacher-led method you know from us.</p>")
INVITE = ("<p>On <strong>October 27</strong> the Academy hosts <strong>The Longevity Masterclass of the Year</strong>: 60 minutes live on Zoom with "
          "<strong>Julie Gibson Clark</strong>, the <strong>2nd slowest-aging human on Earth</strong>. Her verified pace of aging is 0.665, about "
          "eight months a year, on a routine of about $100 a month. She reveals her complete protocol in her only two live sessions this year.</p>")
BENEFIT = ("<p>As an eTeacher student you receive <strong>priority seating for the next 72 hours</strong>, before seats open to the public. "
           "The <strong>VIP seat</strong> includes an exclusive promo code worth <strong>$249 toward the full Longevity Blueprint course</strong>, "
           "plus a private 30-minute Q&amp;A with Julie.</p>")
PRICE = "<p>Seats start at <strong>$49</strong>. Pick October 27 or November 14 at checkout.</p>"

def school_emails(b):
    B = BRANDS[b]; name = B["name"]; the = "the " if b == "iibs" else ""
    segs = [
        dict(seg="alumni", segment="alumni (completed a course)",
             subject=f"{B['short']} graduates: your exclusive longevity invitation",
             preheader="Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49.",
             h1="An exclusive invitation for our graduates",
             opening=f"<p>As a graduate of {the}{name}, you are part of eTeacher Group, a family of five online schools. "
                     f"Once in a while that comes with a benefit I want to pass on to you personally, and this is one.</p>"),
        dict(seg="incomplete", segment="students who enrolled and did not finish",
             subject=f"A student benefit from {B['short']}, with nothing to catch up on",
             preheader="Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49.",
             h1="A benefit for our students, with nothing to catch up on",
             opening=f"<p>You began a {B['course']} with us, and as a student of {the}{name} you are part of eTeacher Group, a family of five online schools. "
                     f"That comes with a benefit I want to pass on to you, and it asks for one hour, with nothing to keep up with afterwards.</p>"),
        dict(seg="leads", segment="leads (asked about a course, never enrolled)",
             subject=f"An exclusive invitation from {name}",
             preheader="Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49.",
             h1=f"An exclusive invitation from {name}",
             opening=f"<p>You asked about {B['asked']}, which places you with eTeacher Group, a family of five online schools. "
                     f"Once in a while that comes with a benefit I want to pass on to you, and this is one.</p>"),
    ]
    out = []
    for s in segs:
        out.append(dict(brand=b, id=f"{b}-{s['seg']}-01", segment=s["segment"],
                        ac=f"{b.upper()}_Masterclass_Blast_{s['seg'].capitalize()}", campaign=f"{b}_masterclass_blast",
                        sender=B["sender"], subject=s["subject"], preheader=s["preheader"], h1=s["h1"],
                        hero={"alumni": "julie-zoom-host.jpg", "incomplete": "julie-portrait.jpg", "leads": "julie-zoom-grid.jpg"}[s["seg"]],
                        body=[f"<p>{greet_shalom()}</p>", s["opening"], LONGEVITY, INVITE, BENEFIT, PRICE],
                        signoff=B["sign"]))
    return out

EMAILS = [dict(
    brand="lla", id="lla-leads-01", segment="LLA leads, last 3-4 months, not enrolled",
    ac="LGV_Masterclass_Blast_Leads", campaign="lgv_masterclass_blast_leads", sender=BRANDS["lla"]["sender"],
    subject="Your priority seat: Julie Gibson Clark, live on Zoom",
    preheader="The Longevity Masterclass of the Year. Priority seating for 72 hours. From $49.",
    h1="Priority seats: <em>The Longevity Masterclass of the Year</em>",
    hero="julie-zoom-room.jpg",
    body=[
        f"<p>{you_lla()} asked about Longevity Life Academy this year, so you hear this first, before the public.</p>",
        ("<p>On <strong>October 27</strong> we host <strong>The Longevity Masterclass of the Year</strong>: 60 minutes live on Zoom with "
         "<strong>Julie Gibson Clark</strong>, the <strong>2nd slowest-aging human on Earth</strong>. Her verified pace of aging is 0.665, about "
         "eight months a year, on about $100 a month. She reveals her complete protocol in her only two live sessions this year.</p>"),
        ("<p>You receive <strong>priority seating for the next 72 hours</strong>. The <strong>VIP seat</strong> includes an exclusive promo code worth "
         "<strong>$249 toward The Longevity Blueprint</strong>, plus a private 30-minute Q&amp;A with Julie.</p>"),
        PRICE,
    ],
    signoff="To your longest, strongest life,<br><b>The Longevity Life Academy team</b>",
)] + school_emails("iibs") + school_emails("rosen")

DETAILS_ROWS = [
    ("Dates", "Tue, Oct 27, 7:00 PM ET<br>Sat, Nov 14, 1:00 PM ET"),
    ("Seats", "From $49"),
    ("VIP seat", "$79: private Q&amp;A, $249 Blueprint promo code"),
    ("Refund", "14 days, both seats"),
]

# ---------------- V1 LLA: approved lifecycle shell ----------------
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
def details_block():
    rows = "\n".join(f'        <tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in DETAILS_ROWS)
    return f'    <div class="details">\n      <p class="dh">At a glance</p>\n      <table role="presentation">\n{rows}\n      </table>\n    </div>'

def head(e, css, title_brand):
    return (f"<!DOCTYPE html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
            f"<title>{e['subject']} &middot; {title_brand}</title>\n<style>{css}</style></head><body>\n<div class=\"preheader\">{e['preheader']}</div>\n")

def comment(e, v):
    return f"<!-- AC: {e['ac']} | one-time campaign | {v} | segment: {e['segment']} | sender: {e['sender']} | file {v}/{e['brand']}/{e['id']} -->\n"

def render_lla_v1(e):
    b = BRANDS["lla"]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    return comment(e, "v1") + head(e, CSS_LLA, b["name"]) + f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F0E5"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  <div class="top-navy"><img src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></div>
  <div class="divider"></div>
  <div class="alert"><b>Priority seating</b>&middot;&nbsp; The Longevity Masterclass of the Year, live on Zoom</div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="Julie Gibson Clark hosting the live masterclass on Zoom">
  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">14-day full refund, both seats.</p></div>
{details_block()}
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

# ---------------- V1 schools: the letter format IIBS / Rosen campaigns use ----------------
CSS_SCHOOL = """
  body{margin:0;padding:0;background:#EEF1F6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1428}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  .wrap{max-width:640px;margin:0 auto;background:#FFFFFF}
  .hdr{background:#FFFFFF;padding:22px 32px 18px;border-bottom:1px solid #E3E8F0}
  .hdr table{width:100%;border-collapse:collapse}
  .hdr td{vertical-align:middle}
  .hdr img.school{height:78px;width:auto;display:block}
  .hdr img.etg{height:30px;width:auto;display:block}
  .hdr .of{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#56627A;margin:0 0 6px;text-align:right}
  .hero-img{width:100%;display:block}
  .body-inner{padding:36px 40px 34px;text-align:left}
  h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:30px;line-height:1.25;color:#0A1428;margin:0 0 22px}
  p{font-size:17px;line-height:1.65;color:#2A3244;margin:0 0 18px}
  p strong{color:#0A1428;font-weight:700}
  .btn-row{text-align:center;padding:14px 0 10px}
  .btn{display:inline-block;background:#0A1E3F;color:#FFFFFF !important;text-decoration:none;font-weight:700;font-size:15px;letter-spacing:.06em;padding:17px 40px;border-radius:6px}
  .btn-meta{font-size:13px;color:#56627A;margin:12px 0 0;text-align:center}
  .signoff{margin-top:26px;font-size:17px;color:#2A3244;line-height:1.5}
  .signoff b{color:#0A1428}
  .small{font-size:13px;color:#7A8497;line-height:1.6;margin:18px 0 0}
  .footer{background:#F3F5F9;padding:26px 32px 24px;text-align:center;color:#56627A;border-top:1px solid #E3E8F0}
  .footer img{height:26px;width:auto;margin-bottom:12px}
  .footer p{font-size:12px;line-height:1.7;color:#56627A;margin:0}
  .footer a{color:#56627A;text-decoration:underline}
  @media(max-width:520px){.body-inner{padding:28px 22px}h1{font-size:24px}.hdr{padding:18px 20px 14px}.hdr img.school{height:54px}.hdr img.etg{height:22px}}
"""
def render_school_v1(e):
    b = BRANDS[e["brand"]]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"])
    return comment(e, "v1") + head(e, CSS_SCHOOL, b["name"]) + f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF1F6"><tr><td align="center" style="padding:24px 12px">
<div class="wrap">
  <div class="hdr"><table role="presentation"><tr>
    <td style="width:55%"><img class="school" src="{BASE}/assets/{b['logo']}" alt="{b['name']}"></td>
    <td style="width:45%;text-align:right"><p class="of">A school of</p><img class="etg" src="{BASE}/assets/eteacher-group-logo.png" alt="eTeacher Group" style="margin-left:auto"></td>
  </tr></table></div>
  <img class="hero-img" src="{BASE}/assets/images/{e['hero']}" alt="Julie Gibson Clark teaching live on Zoom, Longevity Life Academy">
  <div class="body-inner">
    <h1>{e['h1']}</h1>
{body}
    <div class="btn-row"><a class="btn" href="{href}">{b['button']}</a><p class="btn-meta">Priority seating for eTeacher students for 72 hours. 14-day full refund, both seats.</p></div>
    <div class="signoff">{e['signoff']}</div>
    <p class="small">Julie Gibson Clark&rsquo;s pace-of-aging result is verified through DunedinPACE testing. The masterclass is hosted by Longevity Life Academy, an eTeacher Group school.</p>
  </div>
  <div class="footer">
    <img src="{BASE}/assets/eteacher-group-logo.png" alt="eTeacher Group">
    <p>{b['copyright']}<br>{ADDRESS}</p>
    <p>{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a></p>
  </div>
</div>
</td></tr></table></body></html>
"""

# ---------------- V2: announcement design (all brands) ----------------
CSS_V2 = """
  body{margin:0;padding:0;background:#EEF3FA;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0A1428}
  .preheader{display:none;font-size:0;line-height:0;max-height:0;overflow:hidden;opacity:0;color:transparent}
  table{border-collapse:collapse}
  .wrap{width:640px;max-width:640px;margin:0 auto;background:#FFFFFF}
  .cb td{vertical-align:middle;text-align:center}
  .cb img.school{height:72px;width:auto;display:inline-block}
  .cb img.etg{height:26px;width:auto;display:inline-block}
  .cb img.lla{height:62px;width:auto;display:inline-block}
  .cb img.llawhite{height:110px;width:auto;display:inline-block}
  .cb td.rule{width:1px;border-left:1px solid #D7DEEA}
  .cb .of{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#56627A;margin:0 0 6px}
  .hero{display:block;width:100%;height:auto}
  .navy{background:#0A1E3F}
  .kicker{font-size:15px;line-height:1.4;letter-spacing:.14em;text-transform:uppercase;color:#5EB6FF;font-weight:700}
  .h1{font-family:Georgia,'Times New Roman',serif;font-weight:700;font-size:38px;line-height:1.14;color:#FFFFFF;margin:12px 0 0}
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
  .footer img{height:28px;width:auto;margin-bottom:14px}
  .footer .tag{font-size:14px;color:#B8C4DE;margin:0 0 18px}
  .footer hr{border:none;border-top:1px solid rgba(255,255,255,.12);margin:14px auto;max-width:220px}
  .footer .fine{font-size:12px;line-height:1.6;color:#8494B4;padding:0 20px}
  .footer .fine a{color:#8494B4;text-decoration:underline}
  @media(max-width:620px){
    .wrap{width:100% !important}
    .body{padding:28px 22px 8px !important}
    .h1{font-size:28px !important}
    .cb img.school{height:48px !important}.cb img.etg{height:18px !important}.cb img.lla{height:42px !important}.cb img.llawhite{height:64px !important}
    .cb .of{font-size:10px !important}
    .stat .n{font-size:30px !important}
    .stack td.col{display:block !important;width:100% !important;padding:0 0 14px 0 !important}
    .seat .price{font-size:38px !important}
    .press{letter-spacing:.08em !important;font-size:14px !important}
  }
"""
def header_v2(b):
    if not b["logo"]:
        return (f'<table role="presentation" width="100%" class="cb navy"><tr><td style="padding:28px 20px 24px">'
                f'<img class="llawhite" src="{BASE}/assets/lla-logo-800w.png" alt="Longevity Life Academy by eTeacher Group"></td></tr></table>')
    return (f'<table role="presentation" width="100%" class="cb" style="background:#FFFFFF"><tr>'
            f'<td style="width:36%;padding:20px 12px 16px"><img class="school" src="{BASE}/assets/{b["logo"]}" alt="{b["name"]}"></td>'
            f'<td class="rule"></td>'
            f'<td style="width:28%;padding:20px 12px 16px"><p class="of">A school of</p><img class="etg" src="{BASE}/assets/eteacher-group-logo.png" alt="eTeacher Group"></td>'
            f'<td class="rule"></td>'
            f'<td style="width:36%;padding:20px 12px 16px"><p class="of">Hosted by</p><img class="lla" src="{BASE}/assets/lla-logo-dark.png" alt="Longevity Life Academy"></td>'
            f'</tr></table>')

def render_v2(e):
    b = BRANDS[e["brand"]]; href = cta(e["campaign"], e["id"]); body = "\n".join("    " + x for x in e["body"][:-1])  # price line lives in the cards
    footer_tag = ("It&rsquo;s Your Life. Live It Well. Powered by eTeacher Group." if e["brand"] == "lla"
                  else f"{b['name']} and Longevity Life Academy are schools of eTeacher Group.")
    addr = "" if e["brand"] == "lla" else f"<br>{b['copyright']} {ADDRESS}"
    return comment(e, "v2") + head(e, CSS_V2, b["name"]) + f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF3FA"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" class="wrap" cellpadding="0" cellspacing="0" width="640" style="border-radius:8px;overflow:hidden">
  <tr><td>{header_v2(b)}</td></tr>
  <tr><td style="height:4px;background:#5EB6FF;font-size:0;line-height:0">&nbsp;</td></tr>
  <tr><td><img class="hero" src="{BASE}/assets/images/julie-zoom-hero.jpg" width="640" alt="Julie Gibson Clark hosting the live masterclass on Zoom"></td></tr>
  <tr><td class="navy" style="padding:30px 44px 6px;text-align:left">
    <div class="kicker">{b['kicker']}</div>
    <div class="h1">{e['h1']}</div>
  </td></tr>
  <tr><td class="navy" style="padding:18px 24px 26px">
    <table role="presentation" width="100%"><tr>
      <td class="stat" width="33%"><div class="n">0.665</div><div class="l">pace of aging,<br>DunedinPACE, verified</div></td>
      <td class="stat mid" width="34%"><div class="n">8 mo</div><div class="l">of aging<br>per calendar year</div></td>
      <td class="stat" width="33%"><div class="n">No. 2</div><div class="l">on Earth, Rejuvenation<br>Olympics</div></td>
    </tr></table>
  </td></tr>
  <tr><td class="body" style="text-align:left">
{body}
  </td></tr>
  <tr><td style="padding:16px 44px 0">
    <table role="presentation" width="100%" class="stack"><tr>
      <td class="col" width="50%" style="padding:0 8px 0 0"><div class="card"><div class="d">Date one</div><div class="t">Tue, Oct 27</div><div class="s">7:00 PM ET</div></div></td>
      <td class="col" width="50%" style="padding:0 0 0 8px"><div class="card"><div class="d">Date two</div><div class="t">Sat, Nov 14</div><div class="s">1:00 PM ET</div></div></td>
    </tr></table>
    <p class="cap">Same masterclass, two dates. Pick yours at checkout.</p>
  </td></tr>
  <tr><td style="padding:26px 44px 0">
    <table role="presentation" width="100%" class="stack"><tr>
      <td class="col" width="50%" style="padding:0 8px 0 0"><table role="presentation" width="100%"><tr><td class="seat std">
        <div class="name">Seats from</div><div class="price">$49</div>
        <div class="inc">60 minutes live with Julie. Her full protocol, her daily schedule and supplement list, yours to keep.</div>
      </td></tr></table></td>
      <td class="col" width="50%" style="padding:0 0 0 8px"><table role="presentation" width="100%"><tr><td class="seat vip">
        <div class="name">VIP seat</div><div class="price">$79</div>
        <div class="inc">Everything in the masterclass, plus a private 30-minute Q&amp;A with Julie and your <strong style="color:#FFFFFF">exclusive $249 promo code</strong> toward The Longevity Blueprint.</div>
      </td></tr></table></td>
    </tr></table>
  </td></tr>
  <tr><td style="padding:30px 44px 0;text-align:center">
    <a class="btn" href="{href}">{b['button']}</a>
    <p class="btn-meta">Priority seating for 72 hours. 14-day full refund, both seats.</p>
  </td></tr>
  <tr><td class="press">Covered by <b>Fortune</b> &middot; <b>Business Insider</b> &middot; <b>Daily Mail</b></td></tr>
  <tr><td style="padding:16px 44px 40px;text-align:left">
    <div class="signoff">{e['signoff']}</div>
    <p class="small">Julie Gibson Clark&rsquo;s pace-of-aging result is verified through DunedinPACE testing.</p>
  </td></tr>
  <tr><td class="footer">
    <img src="{BASE}/assets/eteacher-group-logo-white.png" alt="eTeacher Group">
    <p class="tag">{footer_tag}</p>
    <hr>
    <p class="fine">{b['footer_reason']} &nbsp;&middot;&nbsp; <a href="%UNSUBSCRIBELINK%">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="%UPDATELINK%">Update preferences</a> &nbsp;&middot;&nbsp; <a href="https://www.longevitylifeacademy.com/privacy.html">Privacy</a>{addr}</p>
  </td></tr>
</table>
</td></tr></table></body></html>
"""

# ---------------- write ----------------
def visible(out):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", out, flags=re.S)); t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", t)).strip()
def body_words(e): return len(visible(" ".join(e["body"]) + " " + e["h1"]).split())

manifest = []
for e in EMAILS:
    rec = dict(id=e["id"], brand=e["brand"], segment=e["segment"], ac=e["ac"], sender=e["sender"],
               subject=e["subject"], subject_len=len(e["subject"]), preheader=e["preheader"], preheader_len=len(e["preheader"]),
               button=html.unescape(BRANDS[e["brand"]]["button"]), cta=html.unescape(cta(e["campaign"], e["id"])), body_words=body_words(e))
    v1 = render_lla_v1(e) if e["brand"] == "lla" else render_school_v1(e)
    for v, out in (("v1", v1), ("v2", render_v2(e))):
        os.makedirs(os.path.join(v, e["brand"]), exist_ok=True)
        path = os.path.join(v, e["brand"], e["id"] + ".html"); open(path, "w", encoding="utf-8").write(out)
        rec[f"file_{v}"] = path; rec[f"words_{v}"] = len(visible(out).split()); rec[f"chars_{v}"] = len(visible(out))
    manifest.append(rec)
json.dump(manifest, open("manifest.json", "w"), indent=2)
for m in manifest:
    print(m["id"], "| subj", m["subject_len"], "| pre", m["preheader_len"], "| body words", m["body_words"], "| total v1", m["words_v1"], "| v2", m["words_v2"])

# ---------------- gallery ----------------
src = open('/home/user/workspace/gallery-src.html', encoding='utf-8').read()
css = src[src.index('<style>'):src.index('</style>')+8]
script = src[src.index('<script>'):src.index('</script>')+9]
script = script.replace("f.addEventListener('load',function(){ fit(f);", "f.addEventListener('load',function(){ acPreview(f); fit(f);")
script = script.replace("(function(){", "(function(){\n  function acPreview(f){ try{ var d=f.contentDocument; if(!d) return; var w=d.createTreeWalker(d.body,NodeFilter.SHOW_TEXT); var n; var re=/%IF !empty\\(\\$FIRSTNAME\\)%([\\s\\S]*?)%ELSE%[\\s\\S]*?%\\/IF%/g; while((n=w.nextNode())){ if(n.nodeValue.indexOf('%IF')>-1) n.nodeValue=n.nodeValue.replace(re,'$1'); } }catch(e){} }", 1)
assert 'acPreview(f); fit(f)' in script
COL = {"lla": "#5EB6FF", "iibs": "#F5C451", "rosen": "#A78BFA"}
GROUPS = [
  ("lla", "Longevity Life Academy", "LLA leads from the last 3 to 4 months who did not enrol. Sender: Emma | Longevity Advisor &lt;advisor@longevitylifeacademy.com&gt;. V1 = approved lifecycle shell.", "1 email"),
  ("iibs", "Israel Institute of Biblical Studies", "Alumni, enrolled-did-not-finish, leads. Sender: Sophia Green, Israel Biblical Studies &lt;SophiaG@israelbiblicalstudies.com&gt; (verified IIBS-domain sender). V1 = the letter format IIBS campaigns use, school logo + eTeacher Group logo.", "3 emails"),
  ("rosen", "Rosen School of Hebrew", "Alumni, enrolled-did-not-finish, leads. Sender: Noa Shalev, Campus Manager &lt;admissions@rosenhebrewschool.com&gt; (verified, 5 campaigns Sep 2026). V1 = the letter format Rosen campaigns use, school logo + eTeacher Group logo.", "3 emails"),
]
def card(m):
    fid = m["id"]; col = COL[m["brand"]]
    return f"""<article class="email" id="{fid}">
  <div class="meta">
    <div>
      <span class="tier" style="--c:{col}">{m['brand'].upper()}</span> <span class="msg">{fid.upper()}</span>
      <div class="subject">{m['ac']} | {m['segment']}</div>
      <div class="dest"><b>Subject</b> ({m['subject_len']}): {html.escape(m['subject'])}<br><b>Preheader</b> ({m['preheader_len']}): {html.escape(m['preheader'])}<br><b>Sender</b>: {html.escape(m['sender'])}<br><b>Button</b> “{m['button']}” → Julie page, pricing fold<br><code>{html.escape(m['cta'])}</code><br><b>Body words</b>: {m['body_words']} · whole file V1 {m['words_v1']} · V2 {m['words_v2']}</div>
    </div>
    <div class="actions">
      <div class="vswitch"><button class="vbtn on" data-v="v1">V1 · house format</button><button class="vbtn" data-v="v2">V2 · announcement design</button></div>
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
    sections += f'<section class="funnel"><h2>{name} <span class="count" style="background:{COL[key]}">{cnt}</span></h2><p class="fdesc">{desc}</p>{"".join(card(m) for m in manifest if m["brand"] == key)}</section>\n'
extra_css = """<style>.vswitch{display:flex;gap:6px;margin-bottom:8px}.vbtn{font:600 12px/1 inherit;padding:8px 10px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:transparent;color:#B8C4DE;cursor:pointer}.vbtn.on{background:#5EB6FF;color:#0A1428;border-color:#5EB6FF}.vbtn:hover{border-color:#5EB6FF}</style>"""
extra_js = """<script>
document.querySelectorAll('article.email').forEach(function(a){a.querySelectorAll('.vbtn').forEach(function(b){b.addEventListener('click',function(){var v=b.getAttribute('data-v');a.querySelectorAll('.vbtn').forEach(function(x){x.classList.toggle('on',x===b)});a.querySelectorAll('[data-v1]').forEach(function(el){var f=el.getAttribute('data-'+v);if(el.tagName==='IFRAME'){el.setAttribute('data-src',f);el.src=f;}else if(el.classList.contains('copy')){el.setAttribute('data-file',f);}else{el.href=f;if(el.hasAttribute('download'))el.setAttribute('download',a.id+'-'+v+'.html');}});});});});
</script>"""
index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Julie Masterclass blast · 7 segments · V1 house format + V2 announcement design · 13 Oct 2026</title>
{css}{extra_css}</head><body>
<header>
  <h1>Julie Masterclass blast for Chris &amp; Sandra <span class="count">7 segments · 2 designs</span></h1>
  <p>Install-ready HTML for ActiveCampaign one-time campaigns, 13 Oct 2026. Copy per Omri's brief: an exclusive benefit for eTeacher students, the invitation to The Longevity Masterclass of the Year by Longevity Life Academy with Julie Gibson Clark, 72-hour priority seating, the exclusive VIP promo code ($249 toward The Longevity Blueprint), seats from $49. <b>V1</b> is each sender's house format (LLA: approved lifecycle shell; IIBS and Rosen: the letter format their own campaigns use, school logo + eTeacher Group logo). <b>V2</b> is the announcement design. Imagery: approved lifecycle Zoom assets only. AC tokens: %FIRSTNAME% with ActiveCampaign's blank-name fallback (previews show the filled branch; the files keep the logic), %UNSUBSCRIBELINK%, %UPDATELINK%.</p>
  <p>Facts from the live Julie page on 13 Oct 2026: two dates (Tue 27 Oct 7:00 PM ET, Sat 14 Nov 1:00 PM ET), seats from $49, VIP $79 with private 30-min Q&amp;A and the $249 Blueprint promo code, 14-day full refund on both seats. Per email: switch <b>V1 / V2</b>, then <b>Copy HTML</b>, <b>Download .html</b> or <b>Open</b>. <a href="README.md">README</a>.</p>
</header>
<nav class="toc">{toc}</nav>
<main>
{sections}</main>
{script}
{extra_js}
</body></html>
"""
open("index.html", "w", encoding="utf-8").write(index)

rows = "\n".join(f"| `{m['id']}` | {m['brand'].upper()} | {m['segment']} | `{m['ac']}` | {m['sender']} | {m['subject']} ({m['subject_len']}) | {m['preheader']} ({m['preheader_len']}) | {m['body_words']} |" for m in manifest)
readme = f"""# Julie Masterclass blast · 7 segments · V1 house format + V2 announcement design

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time ActiveCampaign campaigns (not automations). Files: `v1/<brand>/<id>.html` and `v2/<brand>/<id>.html`, identical copy, two shells.

## Copy brief (Omri, 13 Oct 2026) and how each email follows it
1. Exclusive benefit you are entitled to as an eTeacher student (opening paragraph, per segment).
2. One short paragraph on the world of longevity and how people live better longer.
3. The invitation: The Longevity Masterclass of the Year by Longevity Life Academy, 60 minutes live on Zoom with Julie Gibson Clark, the 2nd slowest-aging human on Earth, her only two live sessions this year.
4. The benefit: priority seating for 72 hours before public release; the VIP seat includes the exclusive promo code worth $249 toward The Longevity Blueprint plus the private 30-minute Q&A.
5. Seats start at $49. Date picked at checkout. No sentence states or implies a $79 floor.

## Senders (verified in Omri's inbox, Aug to Oct 2026)
- IIBS: Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com>, the only IIBS-domain campaign sender received. Signature title: Admissions Advisor.
- Rosen: Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com>, five campaigns Sep 2026. Greeting "Shalom %FIRSTNAME%," and "Warmly, Noa Shalev" match her real campaigns.
- LLA: Emma | Longevity Advisor <advisor@longevitylifeacademy.com>, sender of the live masterclass automations.
- School footer: "© 2026 <school> by eTeacher Group. All Rights Reserved. {ADDRESS}", as printed in the real IIBS and Rosen campaign footers. eTeacher Group logo from eteachergroup.com.

## Files
| Id | Brand | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Body words |
|---|---|---|---|---|---|---|---|
{rows}

All buttons go to `{LP}#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.

## Offer facts (live page, 13 Oct 2026)
- Two dates: Tue 27 Oct 2026 7:00 PM ET, Sat 14 Nov 2026 1:00 PM ET. Seats from $49; VIP $79 with private 30-minute Q&A and the $249 Blueprint promo code (code MASTERCLASS-VIP, revealed after VIP payment, valid to 31 Dec 2026). 14-day full refund on both seats.
- The page's own title is "The Longevity Masterclass of the Year"; "only two live sessions this year" matches the page's "Two live dates this year".
- The checkout promo field accepts no masterclass discount code ("Not valid for this package"), so the only code promised is the VIP's $249 Blueprint code, which is real. The 72-hour priority window is Omri's offer to students; it is a message, not a checkout rule.

## Segments
1. Alumni (completed a course) · 2. Enrolled, did not finish · 3. Leads (asked, never enrolled) · 4. Fourth segment: to be named by Omri; add as `*-<segment>-01` with the same shells.
Exclude from every school send: contacts already registered for the masterclass (LGV buyer tags) and anyone in the LLA leads list.

## Audit
- All 14 files rendered in Chromium at 720px and 390px; mail-client framed mockups in `mockups/`.
- All asset URLs on the Pages host return HTTP 200; every CTA resolves to the live Julie page pricing fold.
- Ban greps: zero em dashes, zero exclamation marks in copy, zero hype words.
- Not tested: Gmail, Apple Mail, Outlook rendering. Tables plus one media query, same risk profile as the approved set.

## Rollback
Repo is standalone; nothing in production changed.
"""
open("README.md", "w", encoding="utf-8").write(readme)
print("gallery + readme written")
