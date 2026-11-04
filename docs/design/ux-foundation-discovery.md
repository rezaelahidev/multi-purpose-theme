# UX Foundation & Design System Discovery

- Status: Discovery proposal — not approved for implementation
- Version: 0.1.0
- Date: 2026-11-05
- Scope: WordPress Multi-Purpose Block Theme
- Owners: UX/UI Architect (journeys and interaction), Design System Agent (tokens and theme.json mapping), Theme Architect (platform and compatibility review)
- Approval gate: Human Design System baseline approval

## 1. Executive summary

The project should be designed as a configurable Block Theme platform, not as a collection of unrelated demo websites. Its multi-purpose capability should come from a deliberate combination of:

1. A small, stable foundation of semantic design tokens and global styles.
2. WordPress style variations for alternative visual identities (skins).
3. Block patterns for reusable page sections and composition.
4. Templates and template parts for structural page layouts and shared regions.
5. Native core blocks first; custom blocks only where an approved requirement cannot be met adequately with core blocks, patterns, block styles, or variations.

This separation keeps visual identity, page composition, and document structure independently configurable. It also avoids using style variations as a substitute for templates or using custom blocks to solve problems that WordPress already supports.

This is a research proposal. The repository currently has no approved product brief, target audience definition, prioritized site archetypes, or recorded minimum WordPress version. Therefore, no final visual direction, exact token values, style-variation count, or template catalogue is selected here.

## 2. Current repository baseline and constraints

The repository is an architecture scaffold; the theme implementation has not started. The current project state records Product Scope and Architecture approvals as pending. The requirements directory contains only its README, not an approved product brief.

The UX/UI Architect contract requires approved product requirements and architecture. The Design System Agent contract requires approved product requirements, UX specifications, and theme architecture. Consequently:

- This discovery can define platform capabilities, design-system structure, options, and unresolved decisions.
- It must not invent user research, target personas, or product requirements.
- It must not create or modify `theme.json`, templates, parts, patterns, or custom blocks.
- The human owner must approve the product scope and architecture inputs before the design baseline becomes canonical.

## 3. Native WordPress capability map

| Design concern | Preferred native mechanism | Intended responsibility |
|---|---|---|
| Global design settings and editor controls | `theme.json` settings | Expose curated color, typography, spacing, layout, border, shadow, and other supported controls |
| Global visual defaults | `theme.json` styles | Define root, element, and core-block styles |
| Alternative visual identities | `styles/*.json` style variations | Offer named visual skins while retaining the same structural system |
| Reusable page sections | `patterns/*.php` | Compose hero, feature, testimonial, CTA, FAQ, pricing, and other sections from blocks |
| Site-wide reusable regions | `parts/*.html` | Header, footer, and other template parts |
| Page and archive structures | `templates/*.html` | Define index, singular, page, archive, search, 404, and approved custom layouts |
| Block-specific appearance options | Core block style variations / registered block styles | Offer limited visual treatments without creating a new block |
| Genuinely new editing capability | Custom block | Only when native blocks and composition mechanisms cannot satisfy a validated requirement |

WordPress documents `theme.json` as the central configuration for settings and styles, and supports root, element, and block styling. The standard Block Theme structure separates templates, template parts, patterns, and style variations into dedicated locations.

### Important distinction: style variation versus layout

A style variation is an alternative `theme.json` configuration (a visual skin), not a complete website demo or a different information architecture. Selecting one stores its data as user customization in the database. This has an update implication: later theme updates do not automatically overwrite a user's saved variation values. Variation governance and upgrade behavior must therefore be tested and documented.

### Version compatibility

The current official living reference describes `theme.json` version 3 as supported by WordPress 6.6 or later. Version 3 should be the preferred design-system format only if the project explicitly sets its minimum WordPress version to 6.6 or newer. If broader compatibility is required, the exact version-specific schema and supported properties must be evaluated before committing to tokens or settings.

Do not use Gutenberg-plugin-only or trunk-schema features in the baseline unless the project explicitly chooses and tests that dependency.

## 4. Proposed design-system architecture

The following layers are proposed. Exact values and visual styling remain undecided.

### 4.1 Semantic token groups

- **Color:** canvas, surface, elevated surface, primary text, secondary text, muted text, border, accent, primary action, success, warning, danger, focus indicator.
- **Typography:** font families, body size, heading scale, line heights, weights, letter spacing, text measure.
- **Spacing:** a consistent scale for inline, stack, section, and page-level spacing.
- **Layout:** content width, wide width, full-width behavior, readable text width, responsive gutters.
- **Shape:** border widths, radius scale, outline treatment.
- **Elevation:** a restrained shadow scale, if required by the approved visual direction.
- **Motion:** duration and easing principles for transitions; respect reduced-motion preferences.
- **Interaction:** focus-visible, hover, active, disabled, and selected states.

Prefer semantic tokens over raw palette names in component and pattern guidance. Palette primitives may exist underneath, but patterns should consume semantic roles.

### 4.2 Token-to-WordPress mapping

- Use `settings.color`, `settings.typography`, `settings.spacing`, `settings.layout`, `settings.border`, and `settings.shadow` where supported by the chosen WordPress schema.
- Use `styles` for root, elements, and supported core blocks.
- Use `settings.custom` only for genuinely theme-specific values that cannot be represented by standard presets.
- Keep the editor's exposed controls intentional. Enabling every possible customization control would make the editor harder to use and could undermine visual consistency.
- Keep custom CSS small and evidence-based; document each case where native `theme.json` is insufficient.

### 4.3 Variation strategy

Start with one default visual system and a small, deliberately differentiated set of candidate variations after product archetypes and visual direction are approved.

A variation should change visual identity (for example palette, typography, border and surface treatment), not redefine the site's content model or page structure. Each variation needs:
- A distinct purpose and target context.
- Preview/reference screens.
- Contrast and focus-state checks.
- Editor/front-end parity checks.
- A migration/update policy acknowledging that selected variation data is stored as user customization.

Do not create one variation per page template or one variation per minor color change.

### 4.4 Pattern and template strategy

Patterns should be organized by reusable content purpose rather than by arbitrary visual names. Candidate pattern families include:
- Hero and page introduction.
- Feature and benefit presentation.
- Social proof and testimonials.
- Services or product highlights.
- Pricing and comparison.
- FAQ and support.
- Lead capture and calls to action.
- Editorial content and related content.

These are candidate families only. The final catalogue depends on approved site archetypes and user journeys.

Templates should represent actual WordPress content contexts and template hierarchy needs. Template parts should represent reusable global regions. Avoid encoding a full page's structure inside a single monolithic pattern.

## 5. UX foundation principles

1. **Editor-first clarity:** controls should be understandable to a site owner who is not a developer.
2. **Progressive flexibility:** provide sensible defaults first; expose advanced controls only where they solve a real use case.
3. **Composition over duplication:** assemble pages from native blocks and patterns before creating custom blocks.
4. **Consistent semantics:** colors, typography, spacing, and interaction states must have documented meaning.
5. **Responsive by design:** define behavior at narrow, medium, and wide viewport ranges; do not treat mobile as a scaled desktop.
6. **Accessibility by default:** semantic structure, keyboard operation, visible focus, adequate contrast, reduced-motion support, and meaningful link/button behavior.
7. **Editor/front-end parity:** validate that the experience in the Site Editor is consistent with the rendered site.
8. **Safe customization:** document which choices users can make freely and which combinations are intentionally constrained.
9. **Performance-aware design:** avoid unnecessary assets, font weights, effects, and custom JavaScript.
10. **Internationalization-ready:** do not hard-code left-to-right assumptions; verify long labels, translated content, and RTL layout behavior.

## 6. UX and design-system deliverables

The following deliverables are recommended for this phase:

| Artifact | Owner | Required content |
|---|---|---|
| `docs/design/ux-architecture.md` | UX/UI Architect | Information architecture, user roles once approved, editor and visitor journeys |
| `docs/design/user-journeys.md` | UX/UI Architect | Core site-owner and visitor journeys, states, exceptions, success criteria |
| `docs/design/interface-specifications.md` | UX/UI Architect | Navigation, responsive behavior, interaction states, accessibility requirements |
| `docs/design/design-system.md` | Design System Agent | Principles, token architecture, usage rules, variation governance |
| `docs/design/design-tokens.md` | Design System Agent | Semantic token names, values, mapping, rationale, and change policy |
| `theme.json` | Design System Agent + Theme Architect | Only after scope, architecture, and Design System approval |

## 7. Validation plan before approval

- Validate the selected `theme.json` against the schema for the declared minimum WordPress version.
- Confirm all selected settings appear and behave as expected in the Site Editor.
- Compare editor and front-end rendering for representative core blocks and patterns.
- Test each candidate style variation on the same representative content.
- Test variation switching and update behavior with saved user customizations.
- Check responsive layouts at narrow, medium, and wide viewport widths.
- Check keyboard navigation, visible focus, color contrast, reduced motion, and semantic heading order.
- Test RTL and translated/long content before finalizing layout and typography decisions.
- Run WordPress theme validation and automated accessibility/performance checks once implementation exists.

## 8. Decisions still required from the project owner

These decisions materially affect UX, information architecture, and the design-system baseline:

1. **Primary site archetypes:** which types of websites must the first release serve? Examples: business/corporate, agency/portfolio, blog/editorial, SaaS/product landing, ecommerce storefront, education, or community.
2. **Priority:** which one or two archetypes are the primary launch targets, and which are secondary?
3. **Audience:** is the primary site owner a beginner, a designer/agency, or a developer?
4. **Customization philosophy:** should the theme provide a curated set of polished options, or expose extensive controls to advanced users?
5. **Minimum WordPress version:** may the theme require WordPress 6.6+ and use `theme.json` v3, or is older-version compatibility required?
6. **Language direction:** is RTL/Persian a first-class launch requirement alongside LTR, or a later compatibility milestone?

No token values, demo catalogue, visual identity, or custom-block requirements should be finalized until these answers and the upstream approval gates are recorded.

## 9. Recommendation

Proceed in this order:

1. Approve product scope and minimum platform compatibility.
2. Select launch archetypes and the primary site-owner persona.
3. Produce UX architecture and user journeys for those archetypes.
4. Define semantic token taxonomy and candidate style directions.
5. Map the approved tokens to the selected `theme.json` schema.
6. Build a representative design-system preview using native blocks and patterns in a disposable validation fixture, not the production theme.
7. Complete accessibility, responsive, editor/front-end, and variation-switching reviews.
8. Request human Design System baseline approval.
9. Only then begin theme implementation tasks.

## 10. Official references

- WordPress Theme Handbook: https://developer.wordpress.org/themes/
- Block Theme structure: https://developer.wordpress.org/themes/core-concepts/theme-structure/
- Global Settings and Styles: https://developer.wordpress.org/themes/global-settings-and-styles/
- `theme.json` Version 3 living reference: https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/theme-json-living/
- Applying styles: https://developer.wordpress.org/themes/global-settings-and-styles/styles/applying-styles/
- Style variations: https://developer.wordpress.org/themes/global-settings-and-styles/style-variations/
