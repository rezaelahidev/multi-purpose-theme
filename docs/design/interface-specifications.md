# UX Interface Specifications — E-commerce and Blog / Magazine

- Status: Draft — requires human UX approval
- Version: 0.1.0
- Date: 2026-11-05
- Priority: E-commerce (primary), Blog / Magazine (second)
- Audiences: International and Iranian users are first-class audiences
- Scope: UX/interface behavior only; no theme implementation authorized

## 1. Shared foundations

All interface families must work in English/LTR, Persian (fa-IR)/RTL, mixed Persian-Latin content, and narrow/medium/wide viewports. Persian support includes natural localized microcopy, correct glyph shaping, ZWNJ/half-space, Persian punctuation, suitable font fallbacks and line-height, direction-aware layout, locale-aware date/number/currency presentation, and realistic Iranian content examples. It is not merely translation.

Use logical layout properties; do not hard-code left/right assumptions. Preserve semantic and keyboard order across direction changes. Test Latin URLs, email, SKU, model names, phone numbers, codes, numerals and punctuation embedded in RTL text. Do not silently transform identifiers or user input. Calendar, numeral and currency formats are configurable, not assumed. Persian fonts must have appropriate licensing, glyph coverage, fallbacks and performance characteristics.

Shared shell: optional announcement, brand/header, primary and utility navigation, main landmark, contextual content, footer, and plugin-owned notices. Menus must be keyboard-operable, have visible focus/current states, and never rely on hover alone. All layouts require semantic headings/landmarks, meaningful accessible names, contrast checks, reduced-motion support, responsive reflow, and explicit empty/loading/error/success states.

## 2. E-commerce — primary archetype

### Audiences and tasks

**Store owner:** establish storefront identity/navigation; present categories and products; compose editorial storefront sections; maintain Persian/English content; ensure plugin-provided product/cart/checkout/account views are coherent.

**Shopper:** discover products; evaluate suitability, price, availability, options and delivery information; add the intended item; complete the actual commerce-plugin purchase flow; understand notices and next steps.

### Information architecture

Candidate destinations: Shop/فروشگاه, Categories/دسته‌بندی‌ها, optional Offers/پیشنهادها, Guides/راهنماها, About/درباره ما, Contact/تماس با ما, Account/حساب کاربری and Cart/سبد خرید where supported. Labels/order/visibility are configurable. B2B may add quote/bulk-buying/business-account routes only when supported by integrations.

### Page contexts and hierarchy

| Context | Required hierarchy and behavior |
|---|---|
| Store home | Intro/offer, category discovery, featured products, trust/editorial sections; clear paths to products |
| Shop/archive | Archive title, optional intro, result count, plugin-owned sorting/filtering, product grid, pagination and empty state |
| Category | Category title/description, optional media, product results and clear category context |
| Product detail | Title, media, price, availability, options, summary, purchase action, details, reviews/related products |
| Search | Query context, result count, products and useful no-results recovery |
| Cart | Cart contents/totals, plugin-owned controls and empty-cart state |
| Checkout | Customer details, delivery/payment sections, order review, accessible validation and actual provider errors |
| Account | Plugin/WordPress-owned authentication and account views, styled only where supported |

Final template inventory depends on the approved WordPress/WooCommerce versions and extension points.

### Product-card anatomy

Optional/configurable: image with meaningful alt text, title with safe multi-line wrapping, plugin-supplied price/sale price, rating, badge, short metadata, availability, and a purchase action only if it performs a real supported action. Avoid nested interactive controls.

Iran-market content must tolerate configurable تومان/ریال display, Persian or Latin digits, Persian titles with Latin brand/model/SKU, units, Iranian and international phone/address formats. The theme must not convert currency, calculate exchange rates, invent delivery/warranty/authenticity claims, or hard-code one payment provider.

### Product interaction states

| State | Presentation | Owner |
|---|---|---|
| Available / unavailable | Clear availability and real action or unavailable state | Commerce plugin |
| Variable product incomplete | Explain missing option and retain context | Commerce plugin |
| Add-to-cart success/failure | Accessible notice and next step | Commerce plugin |
| Sale / price variation | Unambiguous current price and context | Commerce plugin |
| Reviews empty/loading/error | Distinct states | Commerce plugin |
| Product not found | Recovery to shop/search/category | WordPress/plugin + theme |

The theme may style supported WooCommerce blocks/templates. It must not implement cart calculations, inventory, taxes, shipping calculations, payment gateway UI/processing, order persistence or account logic. Iranian payment gateways, shipping, installment and SMS services are optional plugin integrations; named provider/version compatibility must be researched and tested before being claimed. Provider outages must never be rendered as fake success. Phone/address validation belongs to the form/plugin/provider.

### E-commerce localization fixtures

Test content such as:
- «گوشی Samsung Galaxy S25 Ultra»
- «شناسه محصول: AB-120/XL»
- «۲۵,۰۰۰,۰۰۰ تومان» plus English/LTR equivalent
- Persian description containing Latin SKU, phone, URL and brand.
- Long Persian category/title and mixed Persian-English product attributes.

These are layout fixtures, not prescribed prices or currency rules.

## 3. Blog / Magazine — second priority

### Audiences and tasks

**Publisher/editor:** organize topics/categories/tags/authors; publish featured and regular stories; maintain article readability; expose newsletter/subscription only when a real integration exists.

**Reader:** discover stories from home/archive/author/search/external link; understand title/author/date; read comfortably; continue to related content or subscribe.

### Information architecture

Candidate destinations: Home/خانه, Topics/موضوعات, Categories/دسته‌بندی‌ها, optional Latest/تازه‌ها, Authors/نویسندگان, About/درباره نشریه, Search/جستجو and optional Subscribe/عضویت در خبرنامه (requires integration). Do not force English editorial taxonomy onto Persian publications.

### Page contexts

| Context | Required hierarchy and behavior |
|---|---|
| Editorial home | Featured story, latest stories, selected topics and optional modules; avoid competing highlights |
| Blog index | Page title, post list/grid, excerpts and pagination |
| Category/tag archive | Taxonomy title/description, post results and empty state |
| Single article | Title, dek/excerpt, author/date, featured media, article body and related content |
| Author archive | Author identity/bio and authored posts; omit missing optional fields cleanly |
| Search | Query, results and no-results recovery |
| 404 | Localized explanation and routes to home/search/topics |

### Editorial card anatomy

Optional featured image with consistent crop and alt guidance, category label, clear title, optional excerpt, author/date, and reading-time only if calculated by a reliable source. Card links must be semantically unambiguous and must not nest interactive controls.

Persian editorial requirements: correct ZWNJ and punctuation; natural title wrapping/line-height; configurable Persian-calendar date presentation; support Persian/Latin author and publication names; mixed script must not break reading order.

### Article reading experience

Maintain comfortable reading measure. Distinguish title, summary, metadata, body, captions, quotes and related content semantically. Media, galleries, embeds and tables must reflow. Headings remain semantic and sequential. Latin phrases, code, URLs and numbers inside Persian paragraphs must remain legible and correctly ordered. Wide tables/code may use intentional, keyboard-accessible horizontal scrolling. Sticky reading/share controls are optional and must not obscure content or focus. Newsletter, comments, paywall and social-sharing behavior belong to plugins/services.

### Editorial states

Specify no posts, no search results, missing author bio/image, very long title, missing featured image, RTL article with Latin URL/code, pagination boundary, and unavailable related content. Omit empty modules rather than showing empty headings.

### Blog localization fixtures

Test Persian headlines with Latin brand names; technical English terms and code in Persian body copy; correct half-space; configurable Persian/Gregorian dates; Persian numerals with Latin identifiers; long RTL title/author/category; English articles on Persian sites and Persian articles on multilingual sites.

## 4. Shared editor experience

Prefer native WordPress core blocks and patterns. Patterns must state intent and required/optional content. Never create fake product, checkout, newsletter, course or membership behavior. Site owners must replace sample content without breaking semantic hierarchy. Validate editor and front-end separately for LTR/RTL. Include genuine Persian and English examples in priority patterns. Starter-site import remains out of scope until approved.

## 5. B2B overlay

Optional patterns may present bulk/business purchasing, quote requests, product specifications, downloadable documents, industry editorial content and case studies. Quote workflows, restricted catalogs, business account permissions, document access and CRM handoff are plugin/service responsibilities. Do not imply functionality without an integration.

## 6. Validation and release gates

| Dimension | E-commerce | Blog / Magazine |
|---|---|---|
| English/LTR | Required | Required |
| Persian/RTL | Required | Required |
| Mixed-script content | Required | Required |
| Mobile/tablet/desktop | Required | Required |
| Keyboard/screen-reader | Required | Required |
| Empty/error/unavailable states | Required | Required |
| Editor/front-end parity | Required | Required |
| Plugin compatibility | WooCommerce and named supported versions | Only named editorial integrations in scope |
| Performance | Product media, fonts, grids, plugin output | Article media, fonts, embeds, archive density |
| Iranian-market realism | Configurable currency/phone/address and verified plugin presentation | Persian editorial conventions, dates and typography |

English/LTR screenshots alone are not sufficient evidence for a Persian/RTL release.

## 7. Open decisions

1. Minimum WordPress version and theme.json schema target.
2. WooCommerce versions and WooCommerce Blocks compatibility target.
3. Exact Iranian payment/shipping/SMS plugins to support, if any.
4. Multilingual plugin compatibility (e.g. WPML/Polylang) versus WordPress locale switching only.
5. Whether Persian calendar presentation is theme-owned or site/plugin-configured.
6. Newsletter/comments/reviews/quote-request scope and owning integrations.
7. Primary site-creator persona and customization philosophy.
8. Accessibility target and supported browser/device matrix.

## 8. Handoff and implementation boundary

After owner review, UX/UI Architect resolves approved decisions; Design System Agent derives semantic typography, spacing, color and direction-aware layout proposals; Theme Architect validates template/plugin constraints; QA Agent creates bilingual RTL/LTR fixtures and acceptance tests.

No theme.json, template, pattern, custom block, checkout implementation or plugin integration is authorized by this draft.
