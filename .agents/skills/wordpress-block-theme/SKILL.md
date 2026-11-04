---
name: wordpress-block-theme
description: Apply official WordPress block theme concepts and implementation practices when researching, designing, or building a block theme.
---

# WordPress Block Theme Skill

## Use this skill when
Working on block theme architecture, `theme.json`, templates, template parts,
patterns, global styles, editor/front-end parity, or block theme compatibility.

## Working method
1. Confirm the target WordPress version and relevant Gutenberg feature dependencies.
2. Prefer current official WordPress developer documentation and tested platform behavior.
3. Distinguish core WordPress features from plugin- or Gutenberg-plugin-only features.
4. Keep editor and front-end behavior consistent.
5. Use semantic, accessible markup and responsive design.
6. Avoid custom code when a stable native block theme capability satisfies the requirement.
7. Record compatibility assumptions and test them.
8. Treat Persian (fa-IR), RTL/LTR, mixed-direction content, and Iran-market usability as cross-cutting requirements for every archetype unless the product owner explicitly changes scope.
9. Validate Persian shaping, ZWNJ, typography, locale-aware dates/numbers, currency presentation, responsive navigation, and accessible focus behavior.
10. Keep local payment, shipping, SMS, LMS, membership, and other business logic in compatible plugins; document provider assumptions and graceful fallbacks.

## International and Iranian-market readiness

Every UX, design-system, implementation, and QA deliverable must account for both international/general users and Iranian users. Persian/RTL is a first-class locale, not a separate archetype. Support mixed Persian/Latin content and avoid hard-coded locale, currency, calendar, legal, or provider assumptions. Validate current Iran-specific provider and regulatory facts before making claims.

## Required references
- WordPress Theme Handbook: https://developer.wordpress.org/themes/
- Block themes: https://developer.wordpress.org/themes/features/block-themes/
- Theme JSON: https://developer.wordpress.org/themes/global-settings-and-styles/
- Block Editor Handbook: https://developer.wordpress.org/block-editor/

## Output expectations
When producing implementation guidance, include target versions, relevant file paths,
native-vs-custom rationale, compatibility notes, and validation steps.
