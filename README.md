# Julie Masterclass blast · 7 install-ready ActiveCampaign emails

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time campaigns (not automations). One design per email.
- **IIBS / Rosen**: the letter format their own campaigns use (verified against 41 campaign emails in Omri's inbox, Aug to Oct 2026): school logo on top, one image, title, “Shalom %FIRSTNAME%,”, short personal paragraphs, one CAPS button, advisor signature, footer “© 2026 <school> by eTeacher Group. All Rights Reserved. 8 Aholiav St, 5252261 Ramat Gan, Israel” with the eTeacher Group logo (eteachergroup.com).
- **LLA**: the approved lifecycle shell (`lla-masterclass-emails-3tier/launch-email-for-chris`).
- Copy: a person writing to a student. One idea. An introduction to longevity and why it matters to this reader, three bullets taken from the masterclass page's three blocks, the 72-hour student priority and the VIP $249 promo code stated once, seats from $49, and an explicit “if it is not for you, ignore this”.
- Images: approved lifecycle Zoom assets only. 1200px wide for a 600px slot (2x), JPG 104 to 117KB; logos PNG 28KB; eTeacher Group logo 6KB. Hosted on this Pages site.
- Tokens: `%FIRSTNAME%` inside ActiveCampaign's conditional block (`%IF !empty($FIRSTNAME)% … %ELSE% … %/IF%`) so a blank name renders “Shalom,”; `%UNSUBSCRIBELINK%`, `%UPDATELINK%`.

| File | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Body words |
|---|---|---|---|---|---|---|
| `lla/lla-leads-01.html` | LLA leads, last 3-4 months, not enrolled | `LGV_Masterclass_Blast_Leads` | Emma | Longevity Advisor <advisor@longevitylifeacademy.com> | Julie is teaching her protocol live. You hear it first (54) | October 27 or November 14, live on Zoom. Seats held for you for 72 hours. From $49. (83) | 157 |
| `iibs/iibs-alumni-01.html` | alumni (completed a course) | `IIBS_Masterclass_Blast_Alumni` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | A seat I set aside for our graduates (36) | Julie Gibson Clark, live on Zoom on October 27, and seats held for IIBS students for 72 hours. (94) | 269 |
| `iibs/iibs-incomplete-01.html` | students who enrolled and did not finish | `IIBS_Masterclass_Blast_Incomplete` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | One hour, and nothing to catch up on (36) | Julie Gibson Clark, live on Zoom on October 27, and seats held for IIBS students for 72 hours. (94) | 274 |
| `iibs/iibs-leads-01.html` | leads (asked about a course, never enrolled) | `IIBS_Masterclass_Blast_Leads` | Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> | Something I do not usually write to you about (45) | Julie Gibson Clark, live on Zoom on October 27, and seats held for IIBS students for 72 hours. (94) | 260 |
| `rosen/rosen-alumni-01.html` | alumni (completed a course) | `ROSEN_Masterclass_Blast_Alumni` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | A seat I set aside for our graduates (36) | Julie Gibson Clark, live on Zoom on October 27, and seats held for Rosen students for 72 hours. (95) | 268 |
| `rosen/rosen-incomplete-01.html` | students who enrolled and did not finish | `ROSEN_Masterclass_Blast_Incomplete` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | One hour, and nothing to catch up on (36) | Julie Gibson Clark, live on Zoom on October 27, and seats held for Rosen students for 72 hours. (95) | 273 |
| `rosen/rosen-leads-01.html` | leads (asked about a course, never enrolled) | `ROSEN_Masterclass_Blast_Leads` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | Something I do not usually write to you about (45) | Julie Gibson Clark, live on Zoom on October 27, and seats held for Rosen students for 72 hours. (95) | 255 |

All buttons go to `https://www.longevitylifeacademy.com/julie-masterclass/#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.

## Offer facts (live page, 13 Oct 2026)
Two dates: Tue 27 Oct 7:00 PM ET, Sat 14 Nov 1:00 PM ET. Seats from $49. VIP $79: private 30-minute Q&A and the $249 Blueprint promo code (MASTERCLASS-VIP, shown after VIP payment, valid to 31 Dec 2026). 14-day full refund on both seats. “Ten years pass. She ages six.” and the three bullets are the page's own words. The checkout accepts no masterclass discount code, so none is promised. The 72-hour hold for students is Omri's offer; it is a message, not a checkout rule.

## Senders (verified in Omri's inbox)
IIBS: Sophia Green, Israel Biblical Studies <SophiaG@israelbiblicalstudies.com> (only IIBS-domain campaign sender received; signature title Admissions Advisor). Rosen: Noa Shalev, Campus Manager <admissions@rosenhebrewschool.com> (five campaigns, Sep 2026). LLA: Emma | Longevity Advisor <advisor@longevitylifeacademy.com>.

## Segments
Alumni · Enrolled, did not finish · Leads, per school; LLA leads. Fourth segment per school: to be named by Omri. Exclude masterclass registrants (LGV buyer tags) and the LLA leads list from every school send.

## Rollback
Repo is standalone; nothing in production changed.
