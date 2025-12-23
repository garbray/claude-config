# Design System & Component Specification Guide

A design system is a living collection of reusable components, patterns, and principles that scale design and reduce inconsistency. Good design systems compound over time: each new design leverages existing components, making future designs faster and more coherent.

## Design System Structure

A complete design system includes:

```
Design System
├── Principles (philosophy, values)
├── Design Tokens (typography, colors, spacing, shadows)
├── Components (buttons, inputs, cards, etc.)
├── Patterns (workflows, layouts, interactions)
└── Guidelines (when to use what, accessibility, writing)
```

## Design Tokens

Design tokens are atomic design decisions (colors, sizes, spacing) that are consistent across the product.

### Typography Tokens

```
Font Family
  Body: System fonts (San Francisco, Segoe UI, Roboto, -apple-system)
    Reason: Fast loading, familiar, accessible
  Headings: Same as body (optional: different weight)
  Monospace: Monaco, Courier New (code blocks, data)

Font Sizes
  Xs: 12px (secondary labels, hints)
  Sm: 14px (labels, small text)
  Base: 16px (body text, default)
  Lg: 18px (prominent labels)
  Xl: 20px (secondary headings)
  2xl: 24px (main headings)
  3xl: 32px (page titles)

Font Weights
  Regular: 400 (body text)
  Medium: 500 (labels, emphasis)
  Bold: 700 (headings, strong emphasis)
  (Avoid ultra-light or ultra-heavy; harder to read)

Line Height
  Tight: 1.2 (headings, short text)
  Normal: 1.5 (body text, default)
  Relaxed: 1.75 (when text is dense)

Letter Spacing
  Normal: default (most text)
  Tight: -0.02em (headings, occasional emphasis)
  Relaxed: 0.05em (all-caps labels, special emphasis)
```

### Color Tokens

```
Primary Color
  Base: #0066cc (main action, primary button)
  Light: #e6f0ff (hover, background)
  Dark: #0052a3 (pressed, darker context)
  Darkest: #003d7a (disabled, minimal contrast)

Secondary Color
  Base: #666666 (secondary actions, secondary text)
  Light: #f5f5f5 (background, secondary inputs)
  Dark: #333333 (strong contrast, accents)

Success Color
  Base: #28a745 (confirmations, success states)
  Background: #e8f5e9 (success context)
  Text: #1b7530 (success messaging)

Warning Color
  Base: #ff9800 (warnings, alerts)
  Background: #fff3e0 (warning context)
  Text: #e65100 (warning messaging)

Error Color
  Base: #dc3545 (errors, destructive actions)
  Background: #ffebee (error context)
  Text: #b71c1c (error messaging)

Neutral Colors
  White: #ffffff
  Bg-light: #fafafa (subtle backgrounds)
  Bg-default: #f5f5f5 (default background)
  Border: #e0e0e0 (borders, dividers)
  Disabled: #cccccc (disabled state)
  Text-light: #999999 (secondary text, hints)
  Text-default: #333333 (primary text)
  Text-dark: #000000 (high contrast)
```

### Spacing Tokens

```
Spacing Scale (8px base)
  Xs: 4px (micro-spacing within components)
  Sm: 8px (tight spacing, gaps)
  Base: 16px (default spacing, padding)
  Md: 24px (section spacing)
  Lg: 32px (large spacing, vertical rhythm)
  Xl: 48px (major section breaks)
  2xl: 64px (page-level spacing)

Padding (internal spacing)
  Button: 8px vertical, 16px horizontal (vertical × horizontal)
  Input: 8px vertical, 12px horizontal
  Card: 24px
  Modal: 24px header, 32px body
  Page: 24px (mobile), 32px (tablet), 48px (desktop)

Margin (external spacing)
  Elements: 16px between major elements
  Sections: 32px between section breaks
  Vertical rhythm: Consistent vertical spacing throughout

Gap (spacing between grid items)
  Tight: 8px (compact grids)
  Normal: 16px (default grid)
  Relaxed: 24px (spacious grids)
```

### Shadow & Elevation Tokens

```
Subtle (Elevation 1)
  Shadow: 0 1px 3px rgba(0,0,0,0.12)
  Use: Cards in normal context, slight emphasis

Moderate (Elevation 2)
  Shadow: 0 4px 6px rgba(0,0,0,0.1)
  Use: Dropdown menus, popovers

Strong (Elevation 3)
  Shadow: 0 10px 15px rgba(0,0,0,0.1)
  Use: Modals, floating buttons

Extra Strong (Elevation 4)
  Shadow: 0 20px 25px rgba(0,0,0,0.1)
  Use: Major modals, top-level overlays

No elevation (Elevation 0)
  Shadow: none
  Use: Flat buttons, text-only interactions
```

## Component Specifications

When specifying a component, include:

### Component: Button

```
Purpose
  Primary interactive element for actions

Variants
  - Primary (main action)
  - Secondary (alternative action)
  - Tertiary/Text (low emphasis)
  - Danger (destructive action)
  - Ghost (no background)

States
  - Resting
  - Hover
  - Active/Pressed
  - Loading
  - Disabled
  - Success
  - Error

Sizes
  - Small: 32px height, 8px vertical padding, 12px horizontal
  - Medium: 40px height, 10px vertical padding, 16px horizontal (default)
  - Large: 48px height, 12px vertical padding, 24px horizontal

Density
  - Compact: Smaller padding, 8px margins
  - Normal: Standard padding, 16px margins (default)
  - Spacious: Larger padding, 24px margins

Properties
  - Minimum touch target: 44px × 44px (mobile accessibility)
  - Text: 14px font, medium weight
  - Icon size: Match button height
  - Border radius: 4px (slight rounding, modern feel)

Behavior
  - Resting: Base color, clear shape
  - Hover: Slightly darker background (100ms ease-out)
  - Active: Darker still, optional scale (0.98x)
  - Loading: Show spinner, disable interactions
  - Disabled: Reduced opacity (50%), cursor: not-allowed
  - Success: Green background, checkmark icon, 1-2s duration
  - Error: Red background, error icon, stay until retry

Accessibility
  - Keyboard: Tab-focusable, activatable with Enter/Space
  - Focus indicator: 2px solid border, matches primary color
  - Screen reader: Clear button label (not just "Submit")
  - Touch: 44px minimum target size

Example HTML Structure
  <button class="btn btn-primary">
    <span class="btn-text">Save Changes</span>
  </button>

Example CSS Outline
  .btn {
    padding: 10px 16px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    transition: all 150ms ease-out;
    min-height: 44px;
    min-width: 44px;
  }
  
  .btn-primary {
    background-color: #0066cc;
    color: white;
  }
  
  .btn-primary:hover {
    background-color: #0052a3;
  }
  
  .btn-primary:active {
    background-color: #003d7a;
    transform: scale(0.98);
  }
  
  .btn-primary:disabled,
  .btn-primary.loading {
    opacity: 0.5;
    cursor: not-allowed;
  }

Testing Checklist
  [ ] Button is keyboard accessible
  [ ] Focus state is visible
  [ ] Hover state works
  [ ] Loading state blocks interaction
  [ ] Success/error states communicate outcome
  [ ] Works on mobile (44px tap target)
  [ ] Text is clear and actionable
```

### Component: Input Field

```
Purpose
  User data entry field

Variants
  - Text (default)
  - Email
  - Password
  - Number
  - Search
  - Textarea (multi-line)

States
  - Resting (unfocused)
  - Focused
  - Filled
  - Disabled
  - Read-only
  - Invalid
  - Valid

Properties
  - Height: 40px (standard), 36px (compact), 48px (large)
  - Padding: 8px vertical, 12px horizontal
  - Border: 1px #e0e0e0 (resting)
  - Border-radius: 4px
  - Font size: 14px (match button size)
  - Line-height: 1.5

Behavior
  - Resting: Gray border, placeholder text visible
  - Focused: Blue border (2px), placeholder fades, optional background tint
  - Filled: Keep focus styling, remove placeholder
  - Validation (real-time): Show errors after field blur
  - Validation (on submit): Show all errors on attempt
  - Invalid: Red border, error message below
  - Valid: Green border or checkmark (optional)
  - Disabled: Reduced opacity, cursor: not-allowed
  - Read-only: Normal appearance, no edits allowed

Interactions
  - Clear button (✕) appears on hover when field has value
  - Show/hide password toggle for password fields
  - Character count for textarea (if max length)
  - Live validation for specific fields (email, date)

Accessibility
  - Label associated with input (for attribute)
  - Error messages linked with aria-describedby
  - Focus indicator visible (not removed)
  - Screen reader announces label and error

Example HTML Structure
  <div class="form-group">
    <label for="email">Email Address</label>
    <input 
      id="email" 
      type="email" 
      placeholder="name@example.com"
      aria-describedby="email-error"
    />
    <span id="email-error" class="error">Invalid email format</span>
  </div>

Testing Checklist
  [ ] Keyboard focus visible
  [ ] Placeholder text clear
  [ ] Validation timing correct (on blur, not during typing)
  [ ] Error message displays inline
  [ ] Clear button works
  [ ] Password field toggle works
  [ ] Works on mobile (adequate font size, padding)
  [ ] Accessible to screen readers
```

### Component: Modal / Dialog

```
Purpose
  Focused interaction or confirmation in overlay context

Variants
  - Confirmation (simple yes/no)
  - Form (data entry)
  - Alert (information, error, warning)
  - Custom (flexible content)

Sizes
  - Small: 360px (mobile), 400px (desktop)
  - Medium: 480px (mobile), 600px (desktop) [default]
  - Large: 600px (mobile), 800px (desktop)

Structure
  - Header (optional title, close button)
  - Body (content)
  - Footer (optional actions)

Properties
  - Border radius: 8px (more rounded than inputs)
  - Shadow: Elevation 3 (strong presence)
  - Background: White (#ffffff)
  - Padding: 24px header, 32px body, 24px footer

Behavior
  - On open: Overlay fades in (200ms), modal slides up or scales in (250ms)
  - On close: Modal fades/slides out (150ms), overlay fades (150ms)
  - Escape key: Close (if safe, not destructive)
  - Click overlay: Close (optional, not for important confirmations)
  - Focus trap: Keep keyboard focus within modal
  - Return focus: After close, focus returns to trigger element

Responsive
  - Mobile: Full width minus padding, bottom-sheet style
  - Desktop: Centered, fixed max-width

Accessibility
  - Modal dialog with aria-modal="true"
  - Aria-labelledby for title
  - Aria-describedby for description
  - Focus management (trap within modal)
  - Escape key closes
  - Return focus after close

Example HTML Structure
  <div class="modal-overlay" aria-hidden="true">
    <div class="modal" role="dialog" aria-labelledby="modal-title">
      <div class="modal-header">
        <h2 id="modal-title">Confirm Delete</h2>
        <button aria-label="Close" class="modal-close">✕</button>
      </div>
      <div class="modal-body">
        Are you sure? This cannot be undone.
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary">Cancel</button>
        <button class="btn btn-danger">Delete</button>
      </div>
    </div>
  </div>

Testing Checklist
  [ ] Opens and closes smoothly
  [ ] Escape key closes
  [ ] Focus trapped within modal
  [ ] Overlay prevents interaction with background
  [ ] Return focus works on close
  [ ] Works on mobile (responsive sizing)
  [ ] Accessible to screen readers
  [ ] Buttons are reachable and large enough
```

## Common Component Patterns

### Empty State Pattern
```
When: No content to display
Show: Icon/illustration, helpful message, action button

Example:
  ┌────────────────────┐
  │      [folder]      │  ← Simple icon/illustration
  │                    │
  │  No items yet      │  ← Clear message
  │                    │
  │  Create your first │  ← Helpful guidance
  │  item or import    │
  │  existing files.   │
  │                    │
  │  [Create Item]     │  ← Clear action
  └────────────────────┘

Guidelines:
  - Icon: Simple, 64x64px or larger
  - Message: 1-2 short sentences
  - Action: Clear call-to-action button
  - Tone: Friendly, not sad
  - Don't overuse illustration (can feel unprofessional)
```

### Error State Pattern
```
When: Error or failure condition
Show: Error icon, message, recovery action

Example:
  ⚠ Connection Error
  Unable to load. Please check your internet and try again.
  [Retry]

Guidelines:
  - Icon: Warning/error symbol in red
  - Message: What happened + how to fix
  - Action: Clear next step (retry, contact support)
  - Tone: Helpful, not blaming
  - Visibility: Prominent but not alarmist
```

### Success State Pattern
```
When: Action completed successfully
Show: Confirmation message, next step

Example:
  ✓ Project saved
  View project [>] or create new [+]

Guidelines:
  - Icon: Checkmark in green
  - Message: What was accomplished
  - Duration: Show 1-3 seconds then auto-dismiss (or require action)
  - Next step: Where to go next
  - Tone: Celebratory but professional
```

## Accessibility in Design Systems

### Color Contrast
```
Normal text: Minimum 4.5:1 ratio (AA)
Large text (18px+, 14px bold): 3:1 ratio
UI components: 3:1 ratio for borders, edges

Test with: WebAIM Contrast Checker
```

### Keyboard Navigation
```
Tab order: Logical, top-to-bottom, left-to-right
Focus visible: Always show focus indicator
Skip links: Skip to main content
ARIA labels: Describe interactive elements
```

### Screen Readers
```
Semantic HTML: Use <button>, <input>, <label>, not <div>
Labels: Associate labels with inputs
ARIA: Use when semantic HTML insufficient
Announcements: Use aria-live for dynamic updates
```

## Design System Documentation

A well-documented design system includes:

1. **Principles**: Philosophy and values
2. **Tokens**: Colors, typography, spacing
3. **Components**: Each component's specification
4. **Patterns**: Common layouts and workflows
5. **Guidelines**: When to use which component
6. **Accessibility**: WCAG standards and implementation
7. **Examples**: Real-world usage of each component
8. **Changelog**: Updates and deprecations

## Evolution & Maintenance

Design systems should evolve, not stagnate.

**Add components when**:
- Same pattern is used 3+ times
- Pattern solves a common problem
- Pattern can be reused across products

**Update components when**:
- Feedback shows poor usability
- Accessibility gaps are discovered
- Performance can be improved
- Brand evolves

**Deprecate when**:
- Component is replaced by better alternative
- Component has low usage
- Component creates maintenance burden

**Communication**:
- Document all changes
- Announce deprecations in advance
- Provide migration path
- Gather feedback from designers/developers
