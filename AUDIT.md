# Audit · Julie Masterclass blast · 14 Oct 2026

Reference: the approved masterclass set sent to Chris and Sandra (`lla-masterclass-emails-3tier/launch-email-for-chris`, 36 emails):
640px card, header, 4px #5EB6FF divider, navy alert bar, 1200×700 hero, Georgia h1, 17px body, #5EB6FF pill button, details box, second button, signoff, dark footer;
tokens %FIRSTNAME%, %UNSUBSCRIBELINK% (schools also %EMAIL%); whole-file length 191 to 262 words, 1203 to 1534 characters.

## Per email
| Email | Subject chars | Preheader chars | Words (whole file) | Chars | Hero | AC tokens | Approved anatomy | Em/en dashes | Exclamation marks |
|---|---|---|---|---|---|---|---|---|---|
| lla-leads-01 | 54 | 85 | 346 | 2045 | julie-zoom-room.jpg 1200x700 117KB | yes | yes | 0 | 0 |
| iibs-alumni-01 | 69 | 99 | 388 | 2390 | julie-zoom-host.jpg 1200x700 109KB | yes | yes | 0 | 0 |
| iibs-incomplete-01 | 71 | 99 | 400 | 2447 | julie-portrait.jpg 1200x700 98KB | yes | yes | 0 | 0 |
| iibs-leads-01 | 67 | 99 | 384 | 2363 | julie-zoom-grid.jpg 1200x700 104KB | yes | yes | 0 | 0 |
| rosen-alumni-01 | 51 | 99 | 380 | 2282 | julie-zoom-host.jpg 1200x700 109KB | yes | yes | 0 | 0 |
| rosen-incomplete-01 | 53 | 99 | 392 | 2339 | julie-portrait.jpg 1200x700 98KB | yes | yes | 0 | 0 |
| rosen-leads-01 | 49 | 99 | 377 | 2269 | julie-zoom-grid.jpg 1200x700 104KB | yes | yes | 0 | 0 |

Word count vs the approved set: these are cold invitations written as a letter from the school's advisor, with the longevity paragraph, the Julie paragraph and three bullets that the lifecycle emails did not need. Longest is 400 words whole file.

## Format checks
- Header: LLA = navy header with the LLA logo (approved). Schools = white header with the school's own logo lockup (which carries "By eTeacher"). No other logo anywhere in the email.
- Divider, alert bar, hero, h1, body, pill button, details box, second button, signoff, small line, footer: present in all 7 (column "Approved anatomy").
- Footer: LLA = approved dark footer with LLA logo and tagline. Schools = the exact footer of their real campaigns (Rosen sends of Sep 2026 in Omri's inbox): "© 2026 <school> by eTeacher Group / All Rights Reserved." / "Sent to: %EMAIL%" / "Unsubscribe" / "All Rights Reserved. The <school> by eTeacher Group, 8 Aholiav St, 5252261 Ramat Gan, Israel".
- Greeting: schools "Shalom %FIRSTNAME%," as in their real campaigns; LLA "Hi %FIRSTNAME%," as in the approved set (jm-a1-1). Blank first name renders "Shalom," / "Hi," via ActiveCampaign conditional content.
- Buttons: schools CAPS ("RESERVE MY SEAT") as in their real campaigns; LLA sentence case ("Reserve My Seat") as in the approved set. All 14 buttons → `https://www.longevitylifeacademy.com/julie-masterclass/#pricing` with utm_source=activecampaign, utm_medium=email, utm_campaign, utm_content.
- Images: approved lifecycle Zoom assets only, 1200×700 JPG (2× of the 600px slot), 98 to 117KB each, hosted on this Pages site. Logos:
- `assets/lla-logo-800w.png`: 800×362, 185KB
- `assets/iibs-logo.png`: 630×297, 28KB
- `assets/rosen-logo.png`: 630×296, 28KB
- `assets/eteacher-group-logo.png`: 228×44, 6KB
- `assets/eteacher-group-logo-white.png`: 228×44, 5KB
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
