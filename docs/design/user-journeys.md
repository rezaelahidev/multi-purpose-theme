# User Journeys — Multi-Purpose Block Theme

- Status: Draft proposal — priority archetypes selected; implementation not approved
- Version: 0.1.0
- Date: 2026-11-05
- Owner: UX/UI Architect
- Scope: First-release archetypes selected by the product owner
- Approval gate: Human review after Product Scope and Architecture inputs are recorded

## 1. Purpose

This document maps the main site-owner and visitor journeys implied by the selected first-release website archetypes:

- Business / Corporate
- Agency / Portfolio
- Blog / Magazine
- SaaS / Product Landing
- E-commerce
- Education / LMS
- Community / Membership
- B2B as a cross-cutting context

**Owner-selected priority:** E-commerce is the primary launch archetype; Blog / Magazine is the second priority. The other selected archetypes remain in the first-release scope, and B2B remains cross-cutting.

These journeys are hypotheses for product and UX review, not findings from user research. They describe how a site owner may compose and maintain a site using native WordPress capabilities, and how a visitor may complete the site's primary task.

## 2. Shared site-owner journey

### J-OWNER-01 — Create and customize a site

**Actor:** Site owner / administrator  
**Goal:** Establish a coherent site without needing to understand theme internals.

| Step | User action | Expected system response | Failure / edge case |
|---|---|---|---|
| 1 | Installs and activates the theme | Site renders a usable baseline and exposes supported editor controls | Existing theme customizations or plugin styles may affect appearance |
| 2 | Opens Appearance / Editor | Site Editor presents templates, template parts, styles and navigation in native WordPress terms | User may not know where global versus local changes belong |
| 3 | Chooses a site archetype starting direction | User can identify recommended page structures/pattern families for the intended site | Archetype is guidance, not a locked mode; user can combine patterns |
| 4 | Selects a visual style variation | Global visual identity changes without changing content structure | Saved variation customization may persist in database |
| 5 | Sets brand identity and global styles | Logo, colors and typography can be adjusted through documented controls | Missing logo, unsupported font, low contrast |
| 6 | Creates essential pages and composes sections | Native blocks and patterns support page composition | Pattern content may not fit long or translated copy |
| 7 | Configures header, navigation and footer | Global regions are consistent across templates | Long menu labels, nested menu complexity, RTL direction |
| 8 | Connects optional plugin functionality | Plugin provides its own commerce, LMS, membership, forms or community behavior | Plugin absent, incompatible, disabled, or styles conflict |
| 9 | Previews key pages and viewport sizes | Editor and front-end remain visually consistent | Responsive overflow, missing content, focus/contrast issues |
| 10 | Publishes and maintains the site | Site owner can edit content and global design without rebuilding layouts | Theme update or variation switch affects saved customization |

**Success criteria**
- User can identify where to change global styles versus page-specific content.
- Core site pages can be composed without custom code for common cases.
- The same style identity applies consistently across templates.
- Visitor-critical journeys work at mobile and desktop widths.
- No plugin-dependent functionality is represented as working when the plugin is absent.

## 3. Shared visitor journey

### J-VISITOR-01 — Discover, evaluate, and act

**Actor:** Site visitor / prospect / customer  
**Goal:** Find relevant information and complete the site's primary action.

1. Arrive through direct URL, search, referral, or campaign link.
2. Understand the site's purpose and current page context.
3. Navigate to the relevant service, product, article, course, or community information.
4. Evaluate details, proof, pricing/terms, and trust signals where relevant.
5. Take the primary action (contact, subscribe, purchase, enroll, join, or participate).
6. Receive clear confirmation or next-step guidance from the owning WordPress/plugin functionality.

**Cross-cutting expectations:** readable hierarchy, clear navigation, accessible controls, responsive layouts, clear CTA labels, no misleading dead-end buttons, and useful empty/error states.

## 4. Archetype journeys

### J-BUSINESS-01 — Evaluate a business and request contact

**Primary visitor:** Prospective customer or business stakeholder  
**Goal:** Understand the organization and initiate a qualified conversation.

1. Land on homepage or a service/industry page.
2. Understand what the company offers and whom it serves.
3. Review services/solutions, differentiators, industries and delivery approach.
4. Inspect case studies, testimonials, metrics or credentials.
5. Find relevant contact route and provide inquiry details.
6. Receive confirmation and clear expectation for follow-up.

**Theme presentation needs**
- Business-oriented hero and page-introduction patterns.
- Service/solution cards and structured detail sections.
- Case-study/testimonial/metrics patterns.
- Contact/CTA presentation and readable footer contact details.

**Success signals:** visitor reaches a relevant service page and can find a contact path without relying on decorative elements or hidden interactions.

### J-AGENCY-01 — Evaluate creative work and submit a project inquiry

**Primary visitor:** Prospective client  
**Goal:** Assess the agency's capabilities and start a project conversation.

1. Arrive at agency homepage or a relevant discipline page.
2. Scan selected work and understand the agency's positioning.
3. Open a project/case-study detail.
4. Review scope, role, process, outcomes and visual evidence.
5. Review services/team/about information as needed.
6. Submit a project inquiry or brief.

**Theme presentation needs**
- Portfolio/project listing and detail composition.
- Image/media-focused layouts with accessible text alternatives.
- Service, process, team and testimonial patterns.
- Clear inquiry CTA and contact path.

**Success signals:** visitor can understand the agency's role and evidence of capability before submitting an inquiry. Media-heavy presentation must not compromise performance or accessibility.

### J-BLOG-01 — Discover and consume editorial content

**Primary visitor:** Reader / subscriber  
**Goal:** Find useful content and continue reading.

1. Arrive at homepage, category/archive, search result or article.
2. Identify topic, title, author and publication context.
3. Open an article and read a comfortable content layout.
4. Navigate to related articles, category or author content.
5. Optionally subscribe or follow the publication.

**Theme presentation needs**
- Blog index, archive, search, single-post and author contexts.
- Readable content width, typography, metadata and media handling.
- Related-content and newsletter CTA patterns where in scope.
- Clear pagination/navigation and semantic article structure.

**Success signals:** readers can locate, read and continue to relevant content; long-form readability and heading hierarchy remain strong across viewports.

### J-SAAS-01 — Understand a product and start a trial or request a demo

**Primary visitor:** Evaluator / decision-maker  
**Goal:** Determine product fit and take a conversion action.

1. Land on product homepage or use-case landing page.
2. Understand product value and target user.
3. Explore features, use cases, integrations and workflow.
4. Review pricing, proof, FAQs, security/trust information where applicable.
5. Choose self-serve signup/trial or sales-led demo/contact path.
6. Continue through the product's own signup or lead-capture system.

**Theme presentation needs**
- Product hero, feature/benefit, workflow, integration and proof patterns.
- Pricing/comparison presentation.
- FAQ and CTA patterns.
- B2B overlays for enterprise use cases, security, procurement and sales contact.

**Success signals:** visitor understands value, target fit and next step; primary and secondary conversion actions are distinguishable.

### J-ECOM-01 — Discover a product and complete a purchase

**Primary visitor:** Shopper  
**Goal:** Find a suitable product and complete checkout.

1. Arrive at shop, category, search or product page.
2. Browse/filter/sort products using the commerce plugin's capabilities.
3. Open product detail and review media, description, price, attributes and availability.
4. Add product to cart and review cart contents.
5. Continue to plugin-owned checkout and payment.
6. Receive order confirmation and next-step information.

**Theme presentation needs**
- Shop/category/product presentation compatible with the selected commerce plugin.
- Cart, checkout and account styling only to the extent supported and tested.
- Clear product information hierarchy, notices, validation and empty states.
- Responsive product media and accessible purchase controls.

**Boundary:** The theme does not own inventory, tax, shipping, cart calculations, checkout validation, payment, order processing or customer account logic. These belong to WooCommerce or the selected commerce system.

**Success signals:** product information is understandable and plugin-owned purchase steps remain usable and visually coherent on supported devices.

### J-EDU-01 — Evaluate a course and begin learning

**Primary visitor:** Prospective learner  
**Goal:** Understand a course and enroll or access learning.

1. Arrive at education homepage, program listing or course detail.
2. Review learning outcomes, audience, prerequisites, curriculum, instructor and format.
3. Review price/access conditions where relevant.
4. Enroll or sign in through the LMS/plugin flow.
5. Access course/lesson content and understand progress/navigation.

**Theme presentation needs**
- Program/course discovery and course detail presentation.
- Instructor, curriculum and learning-outcome patterns.
- LMS-owned lesson/course/account contexts styled only after compatibility review.
- Clear distinction between public marketing pages and authenticated learning UI.

**Boundary:** Enrollment, access control, lesson progression, assessment, certificates, student records and learning progress are LMS responsibilities, not theme logic.

**Success signals:** prospective learners can assess fit before enrollment; enrolled learners can navigate plugin-provided learning screens without visual or responsive regressions.

### J-COMM-01 — Understand membership and join or participate

**Primary visitor:** Prospective or existing member  
**Goal:** Understand community value and join or participate.

1. Arrive at community homepage or membership-benefits page.
2. Understand purpose, audience, benefits and participation expectations.
3. Compare membership options or access levels where relevant.
4. Join/sign in through the membership/community plugin.
5. Access permitted resources, events, profiles or discussions.
6. Find help, account or renewal information.

**Theme presentation needs**
- Community introduction and membership-benefit patterns.
- Tier/plan comparison presentation if required.
- Event/resource/member-content presentation where plugin supports it.
- Consistent account/navigation presentation for plugin-owned screens.

**Boundary:** Authentication, authorization, subscriptions, renewals, member directories, discussions, notifications and access rules are plugin responsibilities.

**Success signals:** visitors understand what membership offers and how to join; members can locate the next relevant participation action.

## 5. B2B cross-cutting journey

### J-B2B-01 — Build confidence and request a sales conversation

**Primary visitor:** B2B evaluator, buyer or decision-maker  
**Goal:** Reduce organizational purchase risk and initiate a qualified sales conversation.

1. Arrive through an industry/use-case page, product page, referral or campaign.
2. Identify the business problem and relevant solution.
3. Review capability details, deployment/integration context and implementation approach.
4. Inspect case studies, measurable outcomes, testimonials or customer evidence.
5. Review security, privacy, compliance and support information when supplied by the business.
6. Request a demo, consultation, quote or sales contact.
7. Receive confirmation and a clear next step.

**Theme presentation needs**
- Industry/use-case landing sections.
- Integration and capability grids.
- Case-study and outcome patterns.
- Trust/security content layouts that display only owner-provided claims.
- Sales CTA and lead-capture presentation.

**Success signals:** a decision-maker can locate relevant evidence and a clear contact route. The theme must never fabricate security, compliance, customer or performance claims.

## 6. Journey state and exception inventory

Across archetypes, the interface should account for:

- Empty state: no products, articles, courses, projects, events or related content.
- Missing optional content: no logo, image, testimonial, author bio, price, or CTA configured.
- Long content: lengthy titles, translated navigation labels, long descriptions, unusually large media.
- Search: no results, many results, query retained, accessible result count where available.
- Form: required field, invalid input, submission pending, success, failure; actual form behavior is plugin/service-owned.
- Commerce: unavailable product, out-of-stock state, validation/notice, empty cart, checkout error; commerce plugin-owned.
- LMS: course unavailable, access denied, lesson not found, not enrolled; LMS-owned.
- Membership/community: logged-out, insufficient permissions, expired membership, empty feed; plugin-owned.
- Navigation: menu unavailable, deeply nested menu, keyboard-only interaction, narrow viewport.
- Theme variation: variation changed, user customization persisted, contrast regression detected.
- RTL/localization: direction changes, mixed-direction text, translated strings overflow, numerals and punctuation.

## 7. Accessibility and responsive acceptance criteria

Every journey must satisfy these baseline checks before release:

- Primary navigation, menus, links, buttons and interactive plugin controls are keyboard operable.
- Focus is visible and not obscured by sticky elements or overlays.
- Heading levels reflect content hierarchy; visual styling does not replace semantic structure.
- Images with meaningful content have appropriate alternative text; decorative images are not announced redundantly.
- Text and interactive elements meet the agreed contrast target.
- Content reflows without horizontal page scrolling at supported narrow viewport widths, except for genuinely two-dimensional content.
- Touch targets and spacing support touch interaction.
- Motion respects reduced-motion preferences.
- Forms and validation messages are associated with their controls and understandable to assistive technology.
- RTL and long translated content are tested, not inferred from LTR screenshots.
- Plugin-owned journeys are included in compatibility tests for every declared supported plugin/version.


## 8. Dual-market journeys: international and Iranian users

All journeys above must work for both general/international users and Iranian users. Persian/RTL is a first-class localization path, not a separate archetype or optional polish task. The same journey must be validated in English/LTR, Persian/RTL and mixed-direction content.

### J-LOCALE-01 — Iranian site owner launches a Persian-first or bilingual site

1. Installs and activates the theme in a WordPress environment that may have Persian as its site language.
2. Selects an archetype starting point without being forced into an Iran-only design.
3. Applies a visual variation and configures Persian typography, logo and brand colors.
4. Builds RTL navigation and page layouts; mixed Latin product names, URLs, email addresses and codes remain readable.
5. Creates Persian content with correct Persian character forms, ZWNJ, natural line breaks and localized CTA copy.
6. Configures local services through compatible plugins where required (payment, shipping, SMS, forms, LMS or membership).
7. Previews Persian RTL, English LTR and mixed-content states on mobile and desktop.
8. Publishes with clear fallbacks when a local or international external service is unavailable.

**Success criteria:** the owner can create a production-usable Persian/RTL site without custom CSS workarounds for ordinary layouts, while retaining the option to serve international visitors.

### J-LOCALE-02 — Iranian shopper completes an e-commerce journey

1. Discovers a shop, category or product page in Persian or English.
2. Understands product title, attributes, availability, price and any shipping/return information.
3. Sees an unambiguous currency label and configured toman/rial presentation; no currency conversion is inferred by the theme.
4. Uses product options and purchase controls in an RTL-safe layout with readable mixed Latin model numbers/SKUs.
5. Proceeds through the configured WooCommerce checkout and payment extension.
6. Receives plugin-owned order/payment feedback and can find support/contact information.

**Theme responsibility:** product/shop presentation, RTL-safe layout, readable localized price labels and notices.  
**Plugin responsibility:** currency storage/conversion, gateway, shipping calculations, tax, inventory, checkout validation and order processing.

### J-LOCALE-03 — Iranian reader consumes a Blog / Magazine

1. Arrives at a Persian editorial homepage, archive, search result or article.
2. Scans Persian titles, summaries, author/date metadata and category labels with correct RTL typography.
3. Reads long-form content with appropriate line length, line-height, punctuation, image captions and embedded Latin terms.
4. Navigates to related articles, categories, authors or search without directionality regressions.
5. Optionally subscribes or contacts the publisher using a configured service.

**Theme responsibility:** editorial hierarchy, RTL typography, archive/article templates and accessible navigation.  
**Integration responsibility:** newsletter delivery, SMS, analytics or other external services.

### J-LOCALE-04 — Iranian learner/member/customer uses other archetypes

For Business/Corporate, Agency/Portfolio, SaaS, Education/LMS and Community/Membership, apply the same localized journey rules: natural Persian copy and CTAs; RTL-safe forms, navigation, pricing and account presentation; locally relevant contact/service options where configured; and plugin-owned access/payment behavior. International LTR use must remain fully supported.

### Localized edge cases to test

- Persian/Arabic character variants, ZWNJ and mixed-script shaping.
- Long Persian menu labels and headings; no clipping or forced truncation of meaningful text.
- Persian, Arabic and Latin numerals; date/calendar presentation; timezone display.
- Toman/rial labels and digit grouping without theme-side currency conversion.
- Mixed-direction product names, SKUs, phone numbers, URLs, email addresses and coupon codes.
- Local gateway/shipping/SMS/form plugin absent, disabled, incompatible or unreachable.
- External fonts/CDNs/services unavailable; local fallback remains usable.
- Language switch preserves the equivalent page context when a translation exists.
- RTL keyboard navigation, focus order, icons, chevrons, carousels and responsive menu behavior.

## 9. Prioritization proposal

All seven archetypes remain in the first-release target set. The product owner selected E-commerce as the primary launch archetype and Blog / Magazine as the second priority. Prioritize shared foundations first, then validate these two journeys in depth before extending the same system to the remaining archetypes.

**Foundation (shared across all archetypes)**
- Global navigation/header/footer behavior.
- Page, post, archive, search and 404 contexts.
- Semantic typography, color, spacing and layout rules.
- Responsive and accessible patterns.
- Editor/front-end parity.
- Style variation switching and persistence behavior.

**Archetype composition — priority order**
1. **E-commerce (primary):** shop/catalog discovery, category and product presentation, cart/checkout visual compatibility, product states, account surfaces, responsive and accessible purchase journey. Commerce operations remain plugin-owned.
2. **Blog / Magazine (second):** editorial home/index, archive/category, single article, author, search, related content, reading experience, and subscription CTA presentation.
3. **Business / Agency / SaaS / B2B:** hero, value proposition, proof, services/features, CTA, contact/demo.
4. **Education / LMS and Community / Membership:** course discovery and membership/community presentation, subject to selected plugin compatibility.
- Education/LMS: course discovery and LMS presentation compatibility.
- Community/Membership: benefits, membership information and plugin presentation compatibility.

This ordering is a planning recommendation, not a final MVP commitment. The owner must select the primary launch archetype(s) before effort estimates and implementation sequencing are approved.

## 10. Open decisions

1. **Resolved:** E-commerce is the primary launch archetype; Blog / Magazine is second. The remaining archetypes stay in first-release scope.
2. Who is the primary site creator: beginner site owner, designer/agency, or developer?
3. Is customization philosophy curated, balanced, or highly advanced?
4. What is the minimum supported WordPress version?
5. Is Persian/RTL a first-release requirement?
6. Which commerce, LMS and membership/community plugins are explicitly supported?
7. Does the first release include starter-site/demo import, or only patterns/templates/style variations?
8. Which conversion mechanisms (forms, newsletter, booking, lead capture) are expected to be provided by third-party plugins?

## 11. Handoff

After owner review and upstream approvals, the UX/UI Architect should produce interface specifications for the selected priority journeys and hand approved UX constraints to the Design System Agent. The Design System Agent should translate these into semantic token and variation proposals. The Theme Architect must validate WordPress-version and plugin-compatibility assumptions.

No theme implementation is authorized by this draft.
