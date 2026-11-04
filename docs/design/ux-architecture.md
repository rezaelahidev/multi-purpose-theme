# UX Architecture — Multi-Purpose Block Theme

- Status: Draft proposal — priority archetypes selected; implementation not approved
- Version: 0.1.0
- Date: 2026-11-05
- Product: WordPress Multi-Purpose Block Theme
- Owner: UX/UI Architect
- Reviewers: Product Architect, Theme Architect, Design System Agent, human product owner
- Depends on: approved product brief, product scope, architecture baseline, minimum WordPress version
- Approval gate: Human approval (Product Scope, Architecture, then Design System)

## 1. Purpose and scope

This document defines a proposed user-experience architecture for a single WordPress Block Theme intended to support these first-release website archetypes:

1. Business / Corporate
2. Agency / Portfolio
3. Blog / Magazine
4. SaaS / Product Landing
5. E-commerce
6. Education / LMS
7. Community / Membership

**B2B is an additional cross-cutting business context**, not an eighth visual archetype. B2B requirements may affect information architecture, conversion paths, content, trust signals, lead capture, catalog presentation, and account journeys across several archetypes.

The goal is not to ship seven unrelated themes or seven hard-coded demo sites. The proposed product is one coherent theme system with reusable structural templates, composable page patterns, a small number of visual style variations, and clear customization boundaries.

This is a UX proposal, not an approved product brief. It does not authorize theme implementation, plugin-specific integrations, or final visual/token decisions.

### First-release priority

The product owner selected **E-commerce** as the primary launch archetype and **Blog / Magazine** as the second priority. The other five archetypes remain in the first-release scope, and B2B remains a cross-cutting context. Prioritization determines design depth and validation sequence; it does not remove any selected archetype from scope.

## 2. Product experience model

The experience has two connected surfaces:

- **Site creation and management (admin/editor):** selecting a starting point, understanding the theme's structure, composing pages, applying visual styles, customizing global regions, and maintaining content.
- **Published website (visitor/customer/member):** discovering information, consuming content, evaluating an offer, taking a conversion action, purchasing, learning, or participating, depending on the site's enabled capabilities.

The Block Theme owns presentation and composition. WordPress core and compatible plugins own domain behavior where relevant. The theme must not recreate commerce, LMS, membership, authentication, payment, course progression, or community business logic.

### 2.1 Experience layers

| Layer | Responsibility | Primary WordPress mechanism |
|---|---|---|
| Global visual foundation | Design tokens, global defaults, editor controls | `theme.json` |
| Visual identity | Alternative palettes/type/surface treatments | Style variations |
| Site structure | Header, footer, page, post, archive, search and error contexts | Templates and template parts |
| Page composition | Reusable sections and content layouts | Block patterns |
| Content editing | Semantic content and page sections | Core blocks first |
| Domain functionality | Products, checkout, courses, memberships, forums, CRM, forms | WordPress core / compatible plugins |
| Exceptional capabilities | Validated gaps in core block composition | Custom blocks only after review |

### 2.2 Key architectural principle

Separate **visual identity**, **page composition**, **content structure**, and **domain functionality**. Do not use a style variation to represent a page layout, a pattern to replace a template hierarchy, or a theme to implement plugin business logic.

## 3. Provisional user roles

These are working roles inferred from the selected archetypes, not validated research personas. Confirm priority, permissions, and proficiency in the approved product brief.

| Role | Main goal | Typical tasks | UX implication |
|---|---|---|---|
| Site owner / administrator | Launch and maintain a professional site | Choose starting direction, set brand, manage pages and global regions | Guided defaults, clear recovery, low-risk controls |
| Designer / agency builder | Deliver differentiated sites efficiently | Compose patterns, tune global styles, reuse layouts across projects | Predictable tokens, composability, controlled flexibility |
| Content editor / publisher | Publish and maintain content | Create posts/pages, assign categories, add media, manage editorial layouts | Content-first editing, accessible patterns, readable previews |
| Store manager | Present products and support shopping journeys | Manage product content through commerce plugin, shape storefront pages | Compatibility with WooCommerce or selected commerce plugin; no duplicated commerce logic |
| Educator / course manager | Present learning offer and course content | Manage course pages and learning content through LMS plugin | Plugin-aware templates/patterns, clear distinction between marketing and learning UI |
| Community / membership manager | Explain membership and support participation | Present benefits, plans, member information and community entry points | Plugin-owned access and account behavior; theme-owned presentation |
| Visitor / prospect / customer | Find information and complete a task | Browse, evaluate, contact, purchase, enroll, read, or join | Clear hierarchy, trust, responsive and accessible interactions |
| B2B buyer / decision-maker | Evaluate organizational fit and reduce purchase risk | Compare capabilities, inspect proof, request consultation/quote, involve stakeholders | Detailed evidence, business outcomes, integration/security content, lead-oriented CTAs |

## 4. Information architecture

### 4.1 Shared site-level structure

The theme should support a common information architecture without forcing every site to expose every section:

- **Global navigation:** brand/home, primary navigation, optional utility navigation, primary CTA, responsive menu.
- **Main content:** page title/introduction, primary content, contextual sections, related content or next action.
- **Global footer:** secondary navigation, contact/legal links, social links where configured, optional newsletter or CTA.
- **System contexts:** search results, archives, single posts, pages, 404, and other WordPress template contexts as required by scope.
- **Plugin contexts:** product, cart, checkout, account, course, lesson, membership, and community screens only where supported by selected plugins and validated compatibility.

### 4.2 Archetype information architecture

| Archetype | Typical top-level destinations | Key content entities | Primary conversion / success action |
|---|---|---|---|
| Business / Corporate | Home, About, Services/Solutions, Industries, Case Studies, Resources, Contact | Services, industries, case studies, team, company information | Contact, request consultation, request quote |
| Agency / Portfolio | Home, Work/Projects, Services, About/Team, Insights, Contact | Projects, capabilities, disciplines, team, testimonials | Project inquiry / brief submission |
| Blog / Magazine | Home, Topics/Categories, Articles, Authors, About, Subscribe | Posts, categories, tags, authors, media | Read, subscribe, explore related content |
| SaaS / Product Landing | Product, Features, Use Cases, Pricing, Integrations, Resources, Docs, Contact | Product capabilities, plans, integrations, use cases, proof | Start trial, sign up, book demo, contact sales |
| E-commerce | Shop, Categories, Product, Search, Cart, Checkout, Account | Products, categories, attributes, reviews, orders | Add to cart, purchase |
| Education / LMS | Programs/Courses, Course detail, Instructor, Learning resources, About, Account | Courses, lessons, instructors, learning resources | Enroll / start learning |
| Community / Membership | Community, Benefits, Plans, Events/Resources, About, Account | Membership tiers, member content, events, profiles, discussions | Join, renew, participate |
| B2B overlay | Solutions by industry/use case, capabilities, integrations, security/trust, case studies, resources, contact sales | Organization use cases, proof, implementation information, commercial offer | Request demo, consultation, quote, or sales contact |

This is a reference model. Each site owner should be able to omit irrelevant destinations and rename labels without breaking semantic structure.

### 4.3 Navigation rules

- Keep primary navigation focused on the site's top tasks; move secondary/legal/resource links to utility navigation or footer.
- Do not assume all archetypes require the same number of menu items.
- Support nested navigation only when information hierarchy justifies it; avoid deep menus as a substitute for clear page structure.
- On narrow screens, expose an accessible menu control with keyboard operation, visible focus, and an understandable expanded/collapsed state.
- Preserve clear current-page and current-section indication.
- Do not make hover the only way to reveal navigation content.

## 5. Site-owner setup and customization architecture

Proposed onboarding sequence:

1. **Understand the starting point:** explain that the theme provides structure and presentation, while plugins may provide commerce, LMS, or membership functionality.
2. **Choose a site direction:** select one of the supported archetypes as a content/layout starting point, not a permanent lock-in.
3. **Choose a visual identity:** apply a style variation independently of the site structure.
4. **Establish brand basics:** configure logo/site identity, key brand colors and typography using approved global controls.
5. **Compose essential pages:** create or adapt pages using patterns and core blocks.
6. **Configure global regions:** adjust header, navigation, footer and responsive behavior.
7. **Connect required functionality:** install/configure compatible plugins separately where commerce, LMS, forms, membership, or community behavior is needed.
8. **Preview and validate:** review desktop/mobile, keyboard navigation, contrast, content overflow and key conversion paths.
9. **Publish and maintain:** provide a clear path back to Site Editor controls and documented customization guidance.

The theme should not silently install plugins, configure payment providers, create user accounts, or enable paid functionality. Any future setup wizard is a separate product-scope decision and must not be assumed.

## 6. Reusable pattern architecture

Organize patterns around content intent and reusable composition rather than archetype-specific one-off page designs.

Candidate pattern families:

- **Identity and introduction:** hero, page intro, announcement, breadcrumb/context.
- **Value proposition:** feature grid, benefits, process, differentiators, comparison.
- **Proof and trust:** testimonials, logos, case study, metrics, certifications.
- **Offer and conversion:** pricing, product highlight, service card, CTA, lead-capture presentation.
- **Editorial:** article list, featured story, author profile, related content, newsletter CTA.
- **Commerce presentation:** product/category introduction, product feature story, promotional banner; commerce operations remain plugin-owned.
- **Learning presentation:** course/program introduction, instructor profile, curriculum overview; learning operations remain LMS-owned.
- **Community presentation:** membership benefits, tier comparison, event/resource promotion; access and participation remain plugin-owned.
- **B2B:** industry/use-case landing section, integration grid, implementation steps, security/trust content, request-demo CTA.

A pattern must have a clear semantic purpose, required/optional content guidance, responsive behavior, accessibility notes, and a defined set of customization expectations.

## 7. Template and template-part architecture

Templates represent WordPress content contexts, not marketing archetypes. The initial candidate template inventory should be derived from the declared WordPress minimum version and required content contexts.

Candidate contexts to assess:

- Index / blog home
- Front page
- Page
- Single post
- Archive / category / tag / author / date as required
- Search results
- 404
- Plugin-provided contexts only after compatibility requirements are confirmed

Candidate template parts:

- Header variants only where materially different navigation structures are needed
- Footer
- Optional sidebar or other global region only if justified by content and accessibility requirements

Do not create one template per archetype by default. Prefer shared templates with patterns and content composition where the underlying WordPress context is the same. Add distinct templates only when structure, content context, or plugin integration materially differs.

## 8. Customization model

The recommended direction is **curated flexibility with extensibility**, pending owner approval:

- Strong defaults and a limited set of intentional style variations.
- Semantic global controls rather than unrestricted arbitrary styling.
- Patterns that can be detached and edited using native blocks.
- Clear distinction between global styles and local block overrides.
- No dependence on a large proprietary page-builder layer.
- Advanced users retain native WordPress block-editor capabilities.
- Theme-specific custom controls are introduced only when a validated usability gap exists.

This is a recommendation, not a finalized decision. The owner must explicitly choose the customization philosophy.


## 9. International and Iranian-market experience requirements

International usability and Iranian-market usability are equal product requirements. Iran is not a separate archetype or a reduced/local-only edition: every archetype, shared journey, pattern family and relevant admin/editor workflow must provide a usable experience for both general/international audiences and Iranian users.

### 9.1 Locale and language model

- Support Persian (fa-IR) as a first-class content and interface locale, alongside English (en) as the initial international reference locale; keep the architecture extensible to additional locales.
- Support RTL and LTR at the document, component, editor-preview and mixed-content levels. Direction must be semantic and context-aware, not implemented by globally reversing layouts.
- Use direction-aware CSS/logical properties and test mixed Persian/Latin text, URLs, email addresses, product codes, prices, numbers and punctuation.
- Persian typography must use a legally distributable, performant font stack with appropriate weights, line-height, numerals and fallback behavior. Do not assume a specific font until licensing and performance are checked.
- Handle Persian text shaping, ZWNJ, Arabic/Persian character variants, long labels and translated content without clipping or broken line wrapping.
- Provide locale-appropriate date, time, number, currency and calendar presentation. Calendar choice and conversion behavior must be explicit and configurable; do not silently transform stored data.
- Keep content translation separate from layout direction: Persian content may appear in an LTR site and vice versa.

### 9.2 Iran-specific operational and ecosystem fit

- Treat Iran-specific payment gateways, shipping providers, SMS services, local forms, analytics, maps, and commerce/LMS/community integrations as compatibility targets to evaluate, not functionality the theme itself owns.
- For E-commerce, support clear presentation of Iranian toman/rial pricing conventions, price labels, product availability, shipping/return information, checkout notices and trust information. Currency storage, conversion, tax, payment and order rules remain owned by WooCommerce and its configured extensions.
- Do not hard-code a currency, gateway, shipping provider, legal statement, trust badge or regulatory claim. These must be configurable and supplied by the site owner or a compatible plugin.
- For lead generation, membership and education, patterns must accommodate locally relevant contact methods and service providers (for example phone/SMS and locally used forms) without making them mandatory or excluding international alternatives.
- Do not assume that an international SaaS service, payment provider, font CDN, analytics platform or external asset host is reachable or usable from Iran. Avoid unnecessary external dependencies; document graceful fallbacks and allow self-hosted assets where licensing permits.
- Any claim about Iranian law, tax, privacy, consumer rights, payment availability or regulatory compliance requires current, authoritative validation. The theme must not present legal compliance as guaranteed.

### 9.3 Dual-market content and conversion

- Patterns must support both international and Iranian content density, terminology, trust signals, contact conventions and calls to action.
- Iranian-ready demo content must be written naturally in Persian, use realistic local examples and avoid merely machine-translated English placeholders.
- International demo content must remain natural in English; neither locale should be treated as a mirrored afterthought.
- Support configurable localized CTA labels and contact options. Do not embed Iran-only assumptions in shared templates or patterns.
- Where a site serves both markets, support language switching and preserve the user's current content context when a translation exists.

### 9.4 Validation matrix

Every archetype and shared component must be reviewed in at least these configurations:
1. English LTR / international content.
2. Persian RTL / Iran-oriented content.
3. Mixed Persian and Latin content, including prices, SKUs, URLs and contact details.
4. Narrow/mobile and wide/desktop viewports.
5. Missing optional local integration or unavailable external service.

The release checklist must cover typography, text shaping, direction, navigation, forms, prices, dates, numbers, media, plugin UI, accessibility, performance and fallback behavior in both locales.

## 10. Cross-cutting quality requirements

- Responsive behavior must be specified for narrow, medium and wide viewports.
- All interactive controls must be keyboard operable and have visible focus.
- Color contrast, heading hierarchy, link purpose and accessible names must be checked.
- Reduced-motion preferences must be respected.
- Layouts must tolerate long translated strings, variable content length, missing optional content and RTL direction.
- Editor and front-end presentation must remain consistent.
- Core Web Vitals/performance impact should be considered for fonts, images, effects and scripts.
- Plugin compatibility must be tested against named supported versions; compatibility must not be implied by visual placeholders.

## 11. Decisions and assumptions requiring owner review

| Decision | Current status | Impact |
|---|---|---|
| First-release archetypes | **Selected by owner:** all seven listed archetypes | Drives information architecture and journey coverage |
| B2B | **Selected by owner as cross-cutting requirement** | Adds trust, procurement, integration and lead-generation paths |
| Primary launch archetype(s) | **Selected:** E-commerce (primary), Blog / Magazine (second) | Determines depth and prioritization for MVP |
| Primary site-owner persona | Open | Determines onboarding complexity and editor guidance |
| Customization philosophy | Proposed curated flexibility; not approved | Determines exposed controls and variation strategy |
| Minimum WordPress version | Open | Determines `theme.json` schema and supported features |
| Persian/RTL and Iran-market readiness | **Required cross-cutting product requirement** | Must be validated across every archetype and user journey, alongside English/LTR |
| Commerce/LMS/community plugin targets | Open | Determines integration and compatibility test scope |
| Demo content / starter-site packaging | Open | Determines whether onboarding includes import/setup functionality |

## 12. Approval and handoff

This document can be reviewed as a UX architecture proposal, but it is not an approved implementation specification. Before the Design System Agent defines canonical token values or the theme implementation begins:

1. Product Scope and Architecture gates must be explicitly reviewed and recorded.
2. Target site-owner persona, customization philosophy, minimum WordPress version, and RTL/Persian launch requirement must be decided. Primary archetypes are selected: E-commerce first, Blog / Magazine second.
3. Commerce, LMS, and community plugin targets must be selected or explicitly deferred.
4. User journeys and interface specifications must be reviewed by the human owner.
5. The Design System Agent may then translate approved UX requirements into semantic tokens and `theme.json` mapping proposals.

No `theme.json`, template, template-part, pattern, style-variation or custom-block implementation is authorized by this draft.
