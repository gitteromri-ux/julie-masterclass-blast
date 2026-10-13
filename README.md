# Julie Masterclass blast · 7 segments · V1 approved shell + V2 announcement design

Built 13 Oct 2026 for Chris and Sandra. Review gallery: https://gitteromri-ux.github.io/julie-masterclass-blast/

One-time ActiveCampaign campaigns (not automations). Files: `v1/<brand>/<id>.html` and `v2/<brand>/<id>.html`, identical copy, two shells.

- **V1** = approved masterclass lifecycle anatomy (`lla-masterclass-emails-3tier/launch-email-for-chris`): 640px card, Georgia h1 with blue italic, 17px body, details box, `#5EB6FF` pill button, dark footer. School sends carry a co-branded header: school logo, thin rule, LLA logo.
- **V2** = announcement design: co-branded header, Julie golden-hour hero, navy headline block, stat band (0.665 / 8 mo / No. 2), Zoom live-room band, two date cards, Standard $49 and VIP $79 seat cards, one pill button, press line (Fortune, Business Insider, Daily Mail), same footer. Table-based, inline-safe CSS with one mobile media query.
- AC tokens: `%FIRSTNAME%` wrapped in AC conditional content so a blank first name renders "Shalom," / "You looked at…" instead of "Shalom ,"; `%UNSUBSCRIBELINK%`, `%UPDATELINK%`.

## Files

| Id | Brand | Segment | AC campaign name | Sender | Subject (chars) | Preheader (chars) | Words V1 / V2 |
|---|---|---|---|---|---|---|---|
| `lla-leads-01` | LLA | LLA leads, last 3-4 months, not enrolled | `LGV_Masterclass_Blast_Leads` | Emma | Longevity Advisor <advisor@longevitylifeacademy.com> (existing LLA sender) | Julie is teaching her full protocol live. Two dates only (56) | October 27 or November 14, live on Zoom. Sixty minutes, her exact numbers, seats from $49. (90) | 391 / 395 |
| `iibs-alumni-01` | IIBS | alumni (completed a course) | `IIBS_Masterclass_Blast_Alumni` | Sophia Green, Israel Institute of Biblical Studies <SophiaG@israelbiblicalstudies.com> | For our graduates: a live hour with Julie Gibson Clark (54) | The 2nd slowest-aging human on Earth teaches her protocol live on Zoom. Seats from $49. (87) | 430 / 433 |
| `iibs-incomplete-01` | IIBS | students who enrolled and did not finish | `IIBS_Masterclass_Blast_Incomplete` | Sophia Green, Israel Institute of Biblical Studies <SophiaG@israelbiblicalstudies.com> | A 60-minute class, with nothing to catch up on (46) | One live hour on Zoom with the 2nd slowest-aging human on Earth. Nothing to keep up with. From $49. (99) | 446 / 449 |
| `iibs-leads-01` | IIBS | leads (asked about a course, never enrolled) | `IIBS_Masterclass_Blast_Leads` | Sophia Green, Israel Institute of Biblical Studies <SophiaG@israelbiblicalstudies.com> | She ages eight months a year. Live on Zoom, from $49 (52) | A live hour with the 2nd slowest-aging human on Earth, hosted by our sister school. Two dates. (94) | 441 / 444 |
| `rosen-alumni-01` | ROSEN | alumni (completed a course) | `ROSEN_Masterclass_Blast_Alumni` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | For our graduates: a live hour with Julie Gibson Clark (54) | The 2nd slowest-aging human on Earth teaches her protocol live on Zoom. Seats from $49. (87) | 423 / 426 |
| `rosen-incomplete-01` | ROSEN | students who enrolled and did not finish | `ROSEN_Masterclass_Blast_Incomplete` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | A 60-minute class, with nothing to catch up on (46) | One live hour on Zoom with the 2nd slowest-aging human on Earth. Nothing to keep up with. From $49. (99) | 439 / 442 |
| `rosen-leads-01` | ROSEN | leads (asked about a course, never enrolled) | `ROSEN_Masterclass_Blast_Leads` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | She ages eight months a year. Live on Zoom, from $49 (52) | A live hour with the 2nd slowest-aging human on Earth, hosted by our sister school. Two dates. (94) | 434 / 437 |

All buttons go to `https://www.longevitylifeacademy.com/julie-masterclass/#pricing` with `utm_source=activecampaign&utm_medium=email&utm_campaign=<group>&utm_content=<id>`.
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
- Footer address on school sends: "eTeacher Group, 8 Aholiav St, 5252261 Ramat Gan, Israel", as printed in the real IIBS and Rosen campaign footers.

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
6. Length: the dates paragraph moved into the details box (V1) or the date and seat cards (V2); word counts above.
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
