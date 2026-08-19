---
name: ARISE Professional Management
colors:
  surface: '#fcf8fb'
  surface-dim: '#d8d9e5'
  surface-bright: '#faf9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#f0edef'
  surface-container-high: '#e6e7f3'
  surface-container-highest: '#e0e2ed'
  on-surface: '#181b23'
  on-surface-variant: '#414755'
  inverse-surface: '#2d3039'
  inverse-on-surface: '#eff0fc'
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
  on-secondary-fixed-variant: '#444748'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb695'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#faf9ff'
  on-background: '#181b23'
  surface-variant: '#e0e2ed'
  error-base: '#ba1a1a'
  status-online: '#52c41a'
  status-away: '#faad14'
  status-offline: '#bfbfbf'
  creator-badge-bg: '#e6f4ff'
  member-badge-bg: '#f5f5f5'
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
  badge-label:
    fontFamily: Manrope
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  gutter: 16px
  margin: 24px
  avatar-size-sm: 32px
  avatar-size-md: 48px
  avatar-size-lg: 64px
---

## Brand & Style
The design system emphasizes **Modern Corporate** sophistication, tailored for high-stakes asset and community management. The aesthetic is defined by high-utility layouts, expansive whitespace, and a "clean and refreshing" atmosphere that builds trust between homeowners, family members, and service providers.

The visual style is **Minimalist** with a focus on structural clarity. It avoids decorative elements in favor of functional elegance, using precise geometry and a systematic approach to information hierarchy. The emotional goal is to provide a sense of security, transparency, and effortless control over complex financial and social structures.

## Colors
The palette is rooted in a professional **Corporate Blue**, used strategically for primary actions and brand presence. 

- **Primary Blue (#1677ff):** The anchor of the system, representing reliability.
- **Surface Palette:** Utilizes cool-toned neutrals to create a layered hierarchy. Pure white is reserved for primary content surfaces (cards/inputs), while subtle greys define the application shell.
- **Community Status:** Specific semantic colors are introduced for presence indicators: Emerald for online, Amber for away, and Silver for offline.
- **Destructive Actions:** A high-visibility Red (#ba1a1a) is reserved exclusively for "Remove," "Exit," or "Delete" actions to signal risk.

## Typography
**Manrope** is the sole typeface, chosen for its geometric balance and contemporary feel. 

Headlines utilize bold weights and negative letter-spacing for a confident, architectural presence. Body text is optimized for legibility with generous line heights. For family management patterns, a specialized `badge-label` is used for "Creator" and "Member" roles, emphasizing structural hierarchy through weight and uppercase styling rather than size.

## Layout & Spacing
This design system utilizes a **Fluid Grid** with a 4px baseline rhythm.

- **Desktop:** 12-column grid with 16px gutters.
- **Mobile:** 4-column grid with 24px side margins.
- **Family Lists:** Member rows use `stack-md` (16px) vertical spacing. Avatars are strictly sized in increments of 16px (32/48/64) to maintain the geometric grid.
- **Grouping:** Related family members should be grouped in cards using `stack-lg` to separate different community units.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and crisp boundaries rather than expressive shadows.

- **Surface Tiering:** The background sits at the lowest level. Content cards use a pure white surface with a 1px `outline-variant` border.
- **Community Overlays:** Hover states on member rows utilize a subtle shift to `surface-container-low` to provide immediate feedback without lifting the element.
- **Modals:** Destructive confirmation dialogs use a Level 2 diffused shadow (4% opacity) to float above the interface, commanding focus during sensitive operations.

## Shapes
The shape language is **Rounded**, balancing approachability with professional structure.

- **Containers:** Assets and Family Cards use a 1rem (`rounded-lg`) corner radius.
- **Actionable Elements:** Buttons and Input fields use a 0.5rem radius.
- **Avatars:** Strictly circular (pill-shaped) to distinguish human entities from square-ish asset icons.
- **Status Indicators:** 25% of the avatar's size, positioned at the bottom-right with a 2px white "safety border" to ensure visibility against the avatar image.

## Components

### Avatars & Status
Avatars must be circular. The **Status Indicator** is a solid dot placed in the bottom-right quadrant. Use `status-online` for active users and `status-offline` for inactive members. In a family management context, the avatar may include a 2px border of the `primary_color` if that user is the current "active" profile.

### Role Badges
- **Creator Badge:** Light blue background (`creator-badge-bg`) with `primary_color` text. Bold, all-caps.
- **Member Badge:** Neutral grey background (`member-badge-bg`) with `on-surface-variant` text. 
Badges should have a 4px corner radius and be placed immediately following the user's name.

### Community Lists
Member rows should include: Avatar (left), Name and Role Badge (center), and a contextual Action Menu (right). Use `body-sm` for secondary info like "Joined 2 months ago."

### Destructive Action Patterns
When removing a member or exiting a family:
- **Trigger:** A secondary button with red text or a "trash" icon.
- **Confirmation:** A modal dialog using a "Destructive Primary" button (solid red background). 
- **Verbiage:** Use clear, consequence-oriented language (e.g., "Remove from Family?" instead of "Delete?").

### Input Fields
Standardized with a 0.5rem radius and `surface-container` background. On focus, the border transitions to the Corporate Blue. For family invites, use a "tag-style" input to manage multiple email addresses.