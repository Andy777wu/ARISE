---
name: Arise Asset Management
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
  tertiary-container: '#bf551c'
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
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb595'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#fcf8fb'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
  surface-canvas: '#fcf8fb'
  outline-muted: '#c1c6d7'
  selection-bg: '#e6f7ff'
  success: '#52c41a'
  warning: '#faad14'
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
  tree-node:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  tree-indent: 24px
  gutter-md: 16px
  margin-lg: 24px
  node-gap: 8px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

The design system is rooted in a **Modern Corporate** aesthetic, prioritizing clarity, precision, and trust. The system is engineered to handle complex hierarchical data while maintaining a "clean and refreshing" environment for homeowners and property managers. 

The visual narrative is driven by **Minimalism** and **High-Utility** layouts. By leveraging expansive whitespace and a structured grid, the system transforms dense asset inventories into a manageable and secure experience. The focus is on functional elegance—where every element serves a purpose in the asset lifecycle.

## Colors

The color strategy uses a restrained palette to promote professionalism and systematic organization. 

- **Primary Blue:** Used for high-emphasis actions, active tree node selections, and primary "Merge" functions.
- **Surface Strategy:** The system uses a multi-tiered surface approach. Pure white is reserved for content cards and tree nodes, while the background canvas uses a subtle off-white to provide structural contrast.
- **Selection States:** For multi-select and merge operations, a low-opacity blue tint is applied to selected rows to provide clear visual feedback without obscuring text.
- **Tertiary Palette:** Used sparingly for specialized warnings or administrative actions that sit outside the primary asset management flow.

## Typography

This design system utilizes **Manrope** exclusively to maintain a geometric and highly readable interface.

- **Hierarchical Clarity:** Headlines use tighter letter-spacing and heavier weights to anchor large category views.
- **Data Readability:** Body text is optimized at 14px and 16px to handle the density of asset descriptions and category metadata.
- **System Labels:** `label-caps` are used for table headers, category tags, and "Merge" status indicators to differentiate administrative metadata from user-generated content.
- **Tree Typography:** Specific `tree-node` settings provide a slightly more compact vertical footprint for nested lists while maintaining clickability.

## Layout & Spacing

The layout follows a **Fluid Grid** model with strict maximum widths to ensure readability of tabular and tree-based data.

- **Tree Structures:** Nested categories utilize a `24px` horizontal indentation per level to visually communicate parent-child relationships.
- **Rhythm:** All spacing is based on a `4px` baseline. Elements within category cards use `16px` padding to maintain a breathable feel.
- **Merge View:** When the "Merge" mode is active, the layout shifts to a split-pane or multi-column selection view, utilizing `stack-md` for vertical spacing between selected items.
- **Responsiveness:** On mobile, nested trees flatten into breadcrumb-led stacks or accordion-style drill-downs to prevent horizontal overflow.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Low-Contrast Outlines** rather than heavy drop shadows, reinforcing the clean, architectural aesthetic.

- **Canvas (Level 0):** Uses the `surface-canvas` color as the base layer.
- **Tree & List Nodes (Level 1):** Defined by a `1px` solid border (`#E8E8E8`) on a white background. These elements sit flat against the canvas.
- **Active State (Level 2):** During "Merge" selection, selected items maintain Level 1 depth but gain a `surface-tint` or subtle ambient shadow to indicate they are "picked up" or active.
- **Modals & Overlays:** Use an extra-diffused shadow (`0px 4px 20px rgba(0, 0, 0, 0.04)`) to float above the primary data layers without introducing visual heaviness.

## Shapes

The shape language balances approachability with professional structure.

- **Category Cards:** Use `rounded-lg` (16px) for major modules and asset groupings.
- **Interactive Elements:** Buttons, checkboxes, and input fields use the `rounded` (8px) base to appear more focused and functional.
- **Selection Markers:** Checkboxes for multi-select functionality are strictly rounded-sm (4px) to align with the geometric Manrope font.

## Components

### Hierarchical Lists & Trees
- **Tree Nodes:** White surface, 1px border. Use chevron icons for expansion. The entire node row should be hoverable with a light grey background.
- **Indentation Guide:** Use a subtle vertical line (`outline-variant`) to visually connect nested children to their parents.

### Selection & Merge
- **Checkboxes:** Standardized 8px corner radius. When checked, the background is `primary-blue` with a white checkmark.
- **Merge Action Bar:** A floating or fixed footer component that appears when multiple categories are selected, using Level 2 elevation.
- **Multi-select State:** Selected rows use `selection-bg` (#E6F7FF) as a fill to differentiate from the default state.

### Buttons
- **Primary:** Solid #1677FF fill for "Apply Merge" or "Save Category."
- **Secondary:** Light grey fill with blue text for "Cancel" or "Reset."
- **Tertiary:** Ghost style (transparent background) with blue text and no border, used for low-priority actions like "View Details" or "Add Sub-category."

### Input Fields
- **Search & Filter:** 8px corner radius, #F5F6F7 background. The border transitions to the primary blue on focus to provide a strong visual cue for active data entry.