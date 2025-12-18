# Design Tokens Reference

Consistent design systems for translating ASCII designs into cohesive, professional interfaces.

## Color System

### Primary Colors
```
Primary Blue:      #0066cc (RGB: 0, 102, 204)
Primary Blue Hover: #0052a3
Primary Blue Dark:  #003d7a

Use for: Buttons, links, active states, focus indicators
```

### Neutral Colors
```
White:         #ffffff
Light Gray:    #f5f5f5
Border Gray:   #e0e0e0
Medium Gray:   #999999
Dark Gray:     #666666
Text Black:    #333333

Use for: Backgrounds, borders, text, disabled states
```

### Semantic Colors
```
Success Green:  #22c55e (RGB: 34, 197, 94)
Warning Yellow: #eab308 (RGB: 234, 179, 8)
Error Red:      #ef4444 (RGB: 239, 68, 68)
Info Blue:      #0ea5e9 (RGB: 14, 165, 233)

Use for: Status badges, alerts, validation feedback
```

### Color Usage in ASCII Design

When showing colors in ASCII mockups:
```
✓ Success  (green background)
⚠ Warning (yellow background)
✗ Error   (red background)
ℹ Info    (blue background)
```

## Spacing Scale

Consistent spacing creates visual harmony and readability.

```
xs: 4px   (use for small gaps, tight layouts)
sm: 8px   (use for button padding, small margins)
md: 16px  (use for form groups, component gaps)
lg: 24px  (use for section spacing)
xl: 32px  (use for major sections)
2xl: 48px (use for page margins on large screens)
```

### Spacing Applications

**Form Fields**:
- Vertical spacing between fields: 16px (md)
- Input padding: 10px 12px
- Label to input: 8px (sm)

**Cards**:
- Card padding: 16-20px (md)
- Card gap in grid: 24px (lg)
- Gap between title and content: 12px

**Page Layout**:
- Section margins: 32px (xl)
- Page margins (mobile): 16px (md)
- Page margins (desktop): 32-48px (xl-2xl)

## Typography System

### Font Families
```
Primary (UI): -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
Monospace (code): "Monaco", "Courier New", monospace
```

### Font Sizes

**Base**: 16px (1rem)

```
Display:     48px (3rem)  - Page titles, hero sections
Heading 1:   32px (2rem)  - Section headers
Heading 2:   24px (1.5rem) - Subsection headers
Heading 3:   20px (1.25rem) - Card titles, form sections
Heading 4:   18px (1.125rem) - Sub-headings
Body:        16px (1rem)  - Default text
Small:       14px (0.875rem) - Secondary text, labels
Tiny:        12px (0.75rem) - Metadata, helper text
```

### Font Weights

```
Light:   300
Regular: 400
Medium:  500
Semibold: 600
Bold:    700
```

### Font Weight Usage

```
Headings (H1-H4):    600-700 (Semibold to Bold)
Labels & Form Text:  600 (Semibold)
Body Text:          400 (Regular)
Secondary Text:     400-500 (Regular)
Metadata:           400 (Regular), 12-14px size
```

### Line Height

```
Headings:  1.2
Body Text: 1.5-1.6
Tight:     1.1
Loose:     1.8
```

## Border & Shadows

### Border Styles

```
Thin:   1px solid
Medium: 2px solid
Thick:  4px solid

Border Radius:
None:      0px
Small:     4px
Medium:    8px (buttons, cards)
Large:     12px
Full:      9999px (pills, avatars)
```

### Elevation (Shadows)

Use box-shadow for depth perception:

```css
/* Subtle shadow (cards, dropdowns) */
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);

/* Medium shadow (hover states) */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

/* Prominent shadow (modals, overlays) */
box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);

/* Focus indicator */
box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);
```

## Component-Specific Tokens

### Buttons

```
Padding: 10px 20px (default/medium)
Height: 40px (medium)
Border Radius: 4px-8px
Font Weight: 600
Font Size: 14-16px
Min Touch Target: 44px (accessibility)
```

**Button States**:
```
Default:  bg-#0066cc, text-white
Hover:    bg-#0052a3
Active:   bg-#003d7a
Disabled: opacity-50, cursor-not-allowed
Focus:    ring-2 ring-offset-2 ring-#0066cc
```

### Input Fields

```
Padding: 10px 12px
Height: 40px
Border: 1px solid #e0e0e0
Border Radius: 4px
Font Size: 14-16px
Font Family: monospace for code inputs

States:
Default:  border-#e0e0e0
Focus:    border-#0066cc, ring-2 ring-#0066cc/10%
Error:    border-#ef4444, ring-2 ring-#ef4444/10%
Disabled: bg-#f5f5f5, cursor-not-allowed
```

### Cards

```
Padding: 16-20px
Border: 1px solid #e0e0e0
Border Radius: 8px
Background: white or light gray
Shadow: 0 1px 3px rgba(0, 0, 0, 0.1)

Hover Shadow: 0 4px 6px rgba(0, 0, 0, 0.1)
Transform: translateY(-4px) on hover
Transition: all 200ms ease-out
```

### Navigation Bar

```
Height: 64px (desktop), 56px (mobile)
Padding: 0 24px (desktop), 0 16px (mobile)
Background: white or primary color
Border Bottom: 1px solid #e0e0e0
Font Size: 14-16px
Link Padding: 12px (vertical)

Active Link Indicator: 3px bottom border in primary color
```

### Sidebar

```
Width: 256px (standard), 64px (collapsed)
Height: 100vh
Background: #333 or #ffffff
Padding: 16px
Transition: width 200ms ease-out

Nav Item Height: 40px
Nav Item Padding: 12px 16px
Hover Background: rgba(0, 0, 0, 0.05) or lighter shade
Active Background: primary color or highlighted shade
```

### Modal Dialog

```
Max Width: 500px (default)
Min Width: 300px
Background: white
Border Radius: 8px
Box Shadow: 0 10px 25px rgba(0, 0, 0, 0.15)
Overlay: rgba(0, 0, 0, 0.5)

Header Padding: 20px
Body Padding: 20px
Footer Padding: 20px
Header Border: 1px solid #e0e0e0
Footer Border: 1px solid #e0e0e0
```

### Badge / Status Indicator

```
Padding: 6px 12px
Border Radius: 12px (pill)
Font Size: 12px
Font Weight: 600

Colors by Type:
Active:    bg-#22c55e, text-white
Inactive:  bg-#e0e0e0, text-#666
Pending:   bg-#eab308, text-black
Error:     bg-#ef4444, text-white
```

## Responsive Token Adjustments

Tokens adjust across breakpoints for optimal display:

### Mobile (< 640px)
```
Body Font Size: 14-16px
Padding: 12px (compact)
Spacing: md (16px) between sections
Min Touch Target: 44x44px required
```

### Tablet (640px - 1024px)
```
Body Font Size: 15-16px
Padding: 16px
Spacing: lg (24px) between sections
Navigation: Sidebar or hamburger menu
```

### Desktop (> 1024px)
```
Body Font Size: 16px
Padding: 20-24px
Spacing: xl (32px) between sections
Navigation: Full horizontal or sidebar
```

## Accessibility Considerations

### Color Contrast

Minimum WCAG AA compliance:
```
Normal Text:       4.5:1 contrast ratio
Large Text (18+px): 3:1 contrast ratio
UI Components:     3:1 contrast ratio
```

### Focus Indicators

Always provide clear focus states:
```css
/* Standard focus ring */
outline: 2px solid #0066cc;
outline-offset: 2px;

/* Alternative with box-shadow */
box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);
border-color: #0066cc;
```

### Touch Targets

Minimum 44×44px for touch interactions on mobile devices.

## Implementation Example

Using these tokens in CSS:

```css
:root {
  /* Colors */
  --color-primary: #0066cc;
  --color-primary-hover: #0052a3;
  --color-success: #22c55e;
  --color-error: #ef4444;
  
  /* Spacing */
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  
  /* Typography */
  --font-size-body: 16px;
  --font-weight-semibold: 600;
  --line-height-body: 1.5;
  
  /* Borders */
  --border-radius-md: 8px;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.card {
  padding: var(--spacing-md);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
}

.btn-primary {
  background-color: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
}
```

Using these tokens with Tailwind CSS:

```jsx
<button className="px-5 py-2 bg-blue-600 hover:bg-blue-700 rounded-md font-semibold text-white">
  Submit
</button>
```

Map these token values to your Tailwind configuration for consistency across the project.
