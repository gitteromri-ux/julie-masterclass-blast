# Julie Masterclass blast · 7 install-ready ActiveCampaign emails

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
| `lla/lla-leads-01.html` | LLA | LLA leads, last 3-4 months, not enrolled | `LGV_Masterclass_Blast_Leads` | Longevity Life Academy (existing LLA sender) | Julie is teaching her full protocol live. Two dates only (56) | October 27 or November 14, live on Zoom. Sixty minutes, her exact numbers, seats from $49. (90) | `julie-zoom-room.jpg` |
| `iibs/iibs-alumni-01.html` | IIBS | IIBS alumni (completed a course) | `IIBS_Masterclass_Blast_Alumni` | Esther David, Israel Biblical Studies <Estherd@israelbiblicalstudies.com> | An invitation for our graduates, from the eTeacher family (57) | The 2nd slowest-aging woman on Earth teaches her protocol live on Zoom. Seats from $49. (87) | `julie-zoom-host.jpg` |
| `iibs/iibs-incomplete-01.html` | IIBS | IIBS students who enrolled and did not finish | `IIBS_Masterclass_Blast_Incomplete` | Esther David, Israel Biblical Studies <Estherd@israelbiblicalstudies.com> | A 60-minute class, with nothing to catch up on (46) | One live hour on Zoom with the 2nd slowest-aging woman on Earth. Nothing to keep up with. From $49. (99) | `julie-portrait.jpg` |
| `iibs/iibs-leads-01.html` | IIBS | IIBS leads (asked about a course, never enrolled) | `IIBS_Masterclass_Blast_Leads` | Esther David, Israel Biblical Studies <Estherd@israelbiblicalstudies.com> | She ages eight months a year. Live on Zoom, from $49 (52) | A live hour with the 2nd slowest-aging woman on Earth, hosted by our sister school. Two dates. (94) | `julie-zoom-grid.jpg` |
| `rosen/rosen-alumni-01.html` | ROSEN | Rosen alumni (completed a course) | `ROSEN_Masterclass_Blast_Alumni` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | An invitation for our graduates, from the eTeacher family (57) | The 2nd slowest-aging woman on Earth teaches her protocol live on Zoom. Seats from $49. (87) | `julie-zoom-host.jpg` |
| `rosen/rosen-incomplete-01.html` | ROSEN | Rosen students who enrolled and did not finish | `ROSEN_Masterclass_Blast_Incomplete` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | A 60-minute class, with nothing to catch up on (46) | One live hour on Zoom with the 2nd slowest-aging woman on Earth. Nothing to keep up with. From $49. (99) | `julie-portrait.jpg` |
| `rosen/rosen-leads-01.html` | ROSEN | Rosen leads (asked about a course, never enrolled) | `ROSEN_Masterclass_Blast_Leads` | Noa Shalev, Campus Manager, Rosen School of Hebrew <admissions@rosenhebrewschool.com> | She ages eight months a year. Live on Zoom, from $49 (52) | A live hour with the 2nd slowest-aging woman on Earth, hosted by our sister school. Two dates. (94) | `julie-zoom-grid.jpg` |

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
