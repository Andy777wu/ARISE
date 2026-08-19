---
name: ARISE Asset Management
colors:
  surface: '#fcf8fb'
  surface-dim: '#dcd9dc'
  surface-bright: '#fcf8fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7ea'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#414755'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
  outline: '#727786'
  outline-variant: '#c1c6d7'
  surface-tint: '#0059c7'
  primary: '#0057c2'
  on-primary: '#ffffff'
  primary-container: '#006ef2'
  on-primary-container: '#fefcff'
  inverse-primary: '#afc6ff'
  secondary: '#5c5f60'
  on-secondary: '#ffffff'
  secondary-container: '#e1e3e4'
  on-secondary-container: '#626566'
  tertiary: '#9e3d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c64f00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#afc6ff'
  on-primary-fixed: '#001a43'
  on-primary-fixed-variant: '#004398'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb695'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#fcf8fb'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base-unit: 4px
  container-margin: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system for this home asset management application is rooted in a **Modern Corporate** aesthetic with a strong emphasis on clarity, precision, and tranquility. The target audience is homeowners and property managers who require a high-trust environment to manage significant financial and physical assets.

The UI evokes a "clean and refreshing" emotional response through expansive whitespace and a meticulous "High-Utility" layout. It avoids visual clutter, favoring functional elegance that makes complex data (inventories, valuations, and documents) feel manageable and secure.

## Colors
The palette is intentionally restrained to promote a professional and trustworthy atmosphere. 

- **Primary Blue (#1677FF):** Used for primary actions, active states, and critical navigational markers. It signifies reliability and technological competence.
- **Surface & Backgrounds:** The application relies on a pure White (#FFFFFF) base for primary content areas. Light Grey (#F5F6F7) is utilized for "container" backgrounds to create subtle structural separation between different modules without using heavy borders.
- **Neutral Tones:** Deep charcoal is used for text to ensure high legibility while remaining softer than pure black.

## Typography
This design system utilizes **Manrope** exclusively to maintain a modern, geometric, and highly readable interface across all platforms.

- **Headlines:** Use tighter letter-spacing and heavier weights to establish a clear information hierarchy.
- **Body Text:** Standardized on a 16px base for desktop and 14px for secondary information to ensure accessibility.
- **Labels:** Small caps with slight tracking are used for metadata, categories, and table headers to distinguish them from actionable content.

## Layout & Spacing
The design system employs a **Fluid Grid** model with fixed maximum widths for desktop to prevent line lengths from becoming unreadable.

- **Grid:** A 12-column grid for desktop, 8-column for tablet, and 4-column for mobile.
- **Margins:** 24px outer margins are consistent across all breakpoints to ground the interface.
- **Spacing Rhythm:** Based on a 4px baseline. Most components should use 16px (4 units) for internal padding to maintain a spacious, breathable feel.
- **Adaptation:** On mobile, complex side-by-side data tables reflow into vertical card stacks using the `stack-md` spacing token.

## Elevation & Depth
To maintain the "clean and refreshing" aesthetic, depth is achieved through **Tonal Layering** rather than heavy shadows.

- **Level 0 (Background):** #F5F6F7. Used for the application canvas.
- **Level 1 (Cards/Surface):** #FFFFFF with a 1px solid border (#E8E8E8). No shadow.
- **Level 2 (Interactive/Floating):** #FFFFFF with an ambient, extra-diffused shadow (0px 4px 20px rgba(0, 0, 0, 0.04)). Used for dropdowns and active modals.
- **Outlines:** Low-contrast ghost borders are preferred over drop shadows to define boundaries, keeping the UI light and architectural.

## Shapes
The shape language is defined by the **Rounded (12px)** standard for primary containers.

- **Cards & Modules:** Use `rounded-lg` (16px) for major asset containers to create a soft, modern silhouette.
- **Buttons & Inputs:** Use the base `rounded` (8px/0.5rem) to maintain a professional, slightly more structured appearance for functional elements.
- **Icons:** Should follow a 2px stroke weight with rounded terminals to match the typography.

## Components
- **Buttons:** Primary buttons use a solid Blue (#1677FF) fill with white text. Secondary buttons use a #F5F6F7 fill with primary blue text. No borders on buttons.
- **Asset Cards:** White background, 16px corner radius, 1px light grey border. Headers within cards should use `headline-md`.
- **Input Fields:** 8px corner radius, #F5F6F7 background, and a 1px border that turns Blue (#1677FF) on focus.
- **Chips/Status Tags:** High-radius (pill) shapes with low-saturation backgrounds (e.g., light green for 'Insured', light orange for 'Maintenance Due').
- **Lists:** Data-heavy lists should use thin #F5F6F7 dividers and `body-sm` for secondary metadata to maximize information density while remaining clear.
- **Progress Bars:** Use a 4px height with the primary blue for asset valuation or completion tracking, reinforcing the "Arise" upward-growth theme.