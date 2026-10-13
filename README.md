# Julie Masterclass blast · 7 segments · V1 house format + V2 announcement design

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
- School footer: "© 2026 <school> by eTeacher Group. All Rights Reserved. 8 Aholiav St, 5252261 Ramat Gan, Israel", as printed in the real IIBS and Rosen campaign footers. eTeacher Group logo from eteachergroup.com.

## Files
| Id | Brand | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Body words |
|---|---|---|---|---|---|---|---|
| `lla-leads-01` | LLA | LLA leads, last 3-4 months, not enrolled | `LGV_Masterclass_Blast_Leads` | Emma | Longevity Advisor <advisor@longevitylifeacademy.com> | Your priority seat: Julie Gibson Clark, live on Zoom (52) | The Longevity Masterclass of the Year. Priority seating for 72 hours. From $49. (79) | 130 |
| `iibs-alumni-01` | IIBS | alumni (completed a course) | `IIBS_Masterclass_Blast_Alumni` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | Israel Biblical Studies graduates: your exclusive longevity invitation (70) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 220 |
| `iibs-incomplete-01` | IIBS | students who enrolled and did not finish | `IIBS_Masterclass_Blast_Incomplete` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | A student benefit from Israel Biblical Studies, with nothing to catch up on (75) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 236 |
| `iibs-leads-01` | IIBS | leads (asked about a course, never enrolled) | `IIBS_Masterclass_Blast_Leads` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | An exclusive invitation from Israel Institute of Biblical Studies (65) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 218 |
| `rosen-alumni-01` | ROSEN | alumni (completed a course) | `ROSEN_Masterclass_Blast_Alumni` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | Rosen graduates: your exclusive longevity invitation (52) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 218 |
| `rosen-incomplete-01` | ROSEN | students who enrolled and did not finish | `ROSEN_Masterclass_Blast_Incomplete` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | A student benefit from Rosen, with nothing to catch up on (57) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 235 |
| `rosen-leads-01` | ROSEN | leads (asked about a course, never enrolled) | `ROSEN_Masterclass_Blast_Leads` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | An exclusive invitation from Rosen School of Hebrew (51) | Priority seats for eTeacher students at The Longevity Masterclass of the Year. From $49. (88) | 218 |

All buttons go to `https://www.longevitylifeacademy.com/julie-masterclass/#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.

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
