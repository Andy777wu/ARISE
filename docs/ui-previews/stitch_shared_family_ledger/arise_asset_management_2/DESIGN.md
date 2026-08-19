---
name: Arise Asset Management
colors:
  surface: '#f7f9fc'
  surface-dim: '#d8dadd'
  surface-bright: '#f7f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f7'
  surface-container: '#eceef1'
  surface-container-high: '#e6e8eb'
  surface-container-highest: '#e0e3e6'
  on-surface: '#191c1e'
  on-surface-variant: '#414755'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f4'
  outline: '#727786'
  outline-variant: '#c1c6d7'
  surface-tint: '#0059c7'
  primary: '#0057c2'
  on-primary: '#ffffff'
  primary-container: '#006ef2'
  on-primary-container: '#fefcff'
  inverse-primary: '#afc6ff'
  secondary: '#466082'
  on-secondary: '#ffffff'
  secondary-container: '#bcd6fe'
  on-secondary-container: '#435d7f'
  tertiary: '#256a00'
  on-tertiary: '#ffffff'
  tertiary-container: '#308600'
  on-tertiary-container: '#f8ffee'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#afc6ff'
  on-primary-fixed: '#001a43'
  on-primary-fixed-variant: '#004398'
  secondary-fixed: '#d3e4ff'
  secondary-fixed-dim: '#aec8f0'
  on-secondary-fixed: '#001c38'
  on-secondary-fixed-variant: '#2e4869'
  tertiary-fixed: '#88fd54'
  tertiary-fixed-dim: '#6de039'
  on-tertiary-fixed: '#062100'
  on-tertiary-fixed-variant: '#1a5200'
  background: '#f7f9fc'
  on-background: '#191c1e'
  surface-variant: '#e0e3e6'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  card-gap: 24px
  stack-sm: 12px
  stack-md: 20px
---

## Brand & Style
The brand personality is authoritative yet modern, positioning itself as a premier partner in wealth management. It targets high-net-worth individuals and institutional investors who value precision and clarity. 

The design style is **Corporate / Modern** with a focus on **Tonal Layers**. It prioritizes extreme legibility and a sense of "digital craftsmanship." The interface uses high-end finishes—such as subtle light flares and micro-gradients—to elevate the standard financial dashboard into a premium experience. The emotional goal is to evoke a sense of security, upward mobility, and effortless control over complex data.

## Colors
The palette is anchored by a vibrant blue (#1677FF) which represents intelligence and stability. This is balanced against a deep navy secondary color for text and heavy navigation elements, ensuring high contrast and a professional "fintech" feel.

- **Backgrounds**: Use the light gray neutral (#F5F7FA) for the main application background to make white cards pop.
- **Accents**: The tertiary green (#52C41A) is reserved strictly for positive financial growth indicators and success states.
- **Surface**: Pure white (#FFFFFF) is used for all primary content containers to maintain a clean, airy aesthetic.

## Typography
Manrope is the sole typeface, utilized for its modern geometric construction and excellent legibility in data-dense environments. 

- **Hierarchy**: Use `display-lg` for portfolio totals and major section headers. 
- **Data Display**: Numbers in data tables should use `body-md` with tabular lining figures if available, ensuring columns of currency align perfectly.
- **Letter Spacing**: Headlines use slight negative tracking to feel tighter and more premium, while small labels use increased tracking for better readability in uppercase.

## Layout & Spacing
This design system utilizes a **12-column fluid grid** for desktop and a **4-column grid** for mobile. 

- **Grid Logic**: Content lives inside white cards that span 3, 4, 6, or 12 columns.
- **Rhythm**: All spacing is derived from an 8px base unit. 
- **Margins**: Mobile uses 16px side margins, while Desktop scales up to 32px or 48px depending on the screen width to maintain a sense of luxury and "breathing room."
- **Stacking**: Vertical spacing between card groups should be generous (stack-md) to prevent the dashboard from feeling cluttered.

## Elevation & Depth
Hierarchy is established through **Tonal Layers** and **Ambient Shadows**.

- **Base Layer**: The #F5F7FA gray background.
- **Mid Layer (Cards)**: White surfaces with a very soft, diffused shadow (Blur: 20px, Y: 4px, Color: rgba(0, 33, 64, 0.05)).
- **Top Layer (Modals/Popovers)**: White surfaces with a more pronounced shadow to indicate focus.
- **Interactive Depth**: Buttons use a subtle "pressed" state where the shadow Y-offset reduces, simulating a physical push.
- **Hero Accents**: Hero cards feature a subtle linear gradient (Primary color to a slightly lighter blue) and a 15% opacity white "light flare" in the top right corner to suggest a glass-like reflection.

## Shapes
The shape language is sophisticated and friendly. 

- **Cards**: Large cards use `rounded-xl` (1.5rem / 24px) to create a soft, modern container.
- **Buttons & Inputs**: Use `rounded-lg` (1rem / 16px) for a comfortable touch target and a cohesive look with the cards.
- **Status Tags**: Use fully pill-shaped (rounded-full) corners to distinguish them from interactive buttons.
- **Visual Elements**: Data bars and charts should also feature rounded caps to maintain the soft-premium aesthetic.

## Components
- **Hero Cards**: Large-format containers for primary balance. Apply a gradient (Primary to Primary-Light) and a subtle 1px inner white stroke to simulate a beveled edge. Add a "light flare" graphic as a background element.
- **List Items**: Clean rows with 1px border-bottom dividers (#E5E7EB). Each row should have a hover state with a subtle light gray background.
- **Status Tags**: Low-saturation backgrounds with high-saturation text (e.g., light green background with dark green text) to indicate "Growth," "Stable," or "Pending."
- **Input Fields**: White background with a 1px gray border. On focus, the border changes to Primary Blue with a 3px soft blue outer glow (halo).
- **Buttons**:
    - *Primary*: Solid #1677FF with white text.
    - *Secondary*: Transparent with #1677FF border and text.
- **Data Visualization**: Charts should use a thickened line stroke (2px - 3px) with a soft gradient area-fill underneath the line for a contemporary, "App-like" feel.