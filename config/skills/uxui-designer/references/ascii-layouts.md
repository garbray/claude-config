# ASCII UI Layout Reference Guide

ASCII layouts are powerful design tools because they force clarity: without visual details (colors, shadows, images), you must communicate through structure, spacing, and hierarchy. They're fast to create, easy to iterate, and make layout decisions explicit.

## ASCII Layout Syntax & Conventions

### Basic Elements

```
[Button Text]           - Interactive button
[Text Input Field]      - Input field (shows placeholder or label)
( Radio )               - Radio button
[✓] Checkbox            - Checkbox
[Dropdown ▼]            - Dropdown/select
─────────────────       - Divider/line
│ Content │             - Box/card boundary
║ Important ║           - Emphasized box
╔═════════╗             - Heavy border (header/modal)
┌─────────┐             - Light border (section)
ⓘ                       - Icon placeholder
[Icon] Label            - Icon with label
...                     - Truncated content/overflow
→ Action                - Link or navigation
```

### Spacing & Alignment

```
Tight grouping:
  Element A
  Element B
(no blank line = related elements)

Loose grouping:
  Element A

  Element B
(blank line = separate elements)

Column alignment:
  Label .... [Input]     (dots show alignment)
  Name ..... [Input]
  Email .... [Input]
```

## Common ASCII Layout Patterns

### Pattern 1: Basic Form Layout

**When to use**: Data entry, sign-up, settings, checkout

```
╔════════════════════════════════════════╗
║  Create Account                        ║
╚════════════════════════════════════════╝

[Name ...........................]
[Email ..........................]
[Password ........................]
[Confirm Password ................]

( ) I agree to terms and conditions

[Create Account]  [Cancel]
```

**Variations**:
- Horizontal layout for wide screens
- Stacked buttons for mobile
- Inline labels vs. floating labels
- Error states (show errors below fields)

### Pattern 2: List/Table Layout

**When to use**: Data tables, search results, content lists, dashboards

```
╔════════════════════════════════════════╗
║  Recent Orders                [Filter] ║
╚════════════════════════════════════════╝

Order ID    Date        Amount    Status
─────────────────────────────────────────
#12345      Dec 20      $99.99    ✓ Delivered
#12344      Dec 18      $49.99    ⚙ Processing
#12343      Dec 15      $199.99   ⚙ Processing

[← Previous]  [1] [2] [3]  [Next →]
```

**Variations**:
- Compact vs. spacious rows
- Show/hide columns based on viewport
- Sortable headers
- Hover states (show more details)
- Empty state (when list is empty)

### Pattern 3: Card/Grid Layout

**When to use**: Products, projects, articles, recommendations

```
┌──────────────────┐  ┌──────────────────┐
│ [Product Image]  │  │ [Product Image]  │
│                  │  │                  │
│ Product Name     │  │ Product Name     │
│ ⭐⭐⭐⭐⭐ (243)    │  │ ⭐⭐⭐⭐ (89)      │
│ $99.99           │  │ $49.99           │
│ [Add to Cart]    │  │ [Add to Cart]    │
└──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│ [Product Image]  │  │ [Product Image]  │
│ Product Name     │  │ Product Name     │
│ ⭐⭐⭐ (45)        │  │ ⭐⭐⭐⭐⭐ (512)    │
│ $34.99           │  │ $149.99          │
│ [Add to Cart]    │  │ [Add to Cart]    │
└──────────────────┘  └──────────────────┘

← Previous  Page 1 of 5  Next →
```

**Variations**:
- 1-column (mobile), 2-column (tablet), 3-4 column (desktop)
- Aspect ratio (1:1 square, 16:9 wide, etc.)
- Hover states
- Selection/multi-select

### Pattern 4: Sidebar Navigation

**When to use**: Apps with navigation, dashboards, admin panels

```
╔════════════════════════════════╦═══════════════════════════════════╗
║ ☰ Logo         [User ▼]        ║                                   ║
║ ─────────────────────────────── ║                                   ║
║ › Dashboard                     ║  Dashboard                        ║
║ › Projects                      ║  ─────────────────────────────── ║
║ › Inbox                         ║                                   ║
║ › Settings                      ║  Welcome back, Sarah!             ║
║                                 ║                                   ║
║ Workspace                       ║  ⓘ Activity Summary               ║
║ › My Team                       ║  • 12 new messages                ║
║ › Invite Members                ║  • 3 pending tasks                ║
║                                 ║  • 2 project updates              ║
╚════════════════════════════════╩═══════════════════════════════════╝
```

**Variations**:
- Collapsible sidebar
- Top navbar instead of sidebar
- Icons only (collapsed)
- Active state highlighting

### Pattern 5: Modal/Dialog

**When to use**: Confirmations, detailed views, forms in context, error alerts

```
╔════════════════════════════════════════╗
║ Delete Project              [✕]        ║
╠════════════════════════════════════════╣
║                                        ║
║ Are you sure you want to delete        ║
║ "Marketing Campaign Q1"?               ║
║                                        ║
║ This action cannot be undone.          ║
║                                        ║
╠════════════════════════════════════════╣
║  [Cancel]                  [Delete]    ║
╚════════════════════════════════════════╝
```

**Variations**:
- Size (small, medium, large)
- Destructive actions (red button)
- Form modals (larger, scrollable content)
- Alert vs. confirmation

### Pattern 6: Top Navigation (Header)

**When to use**: Most web apps, responsive alternative to sidebar

```
╔═══════════════════════════════════════════════════════════╗
║ Logo    Home  Products  Pricing  About  [Search] [Login] ║
╚═══════════════════════════════════════════════════════════╝
```

**Variations**:
- Sticky/floating header
- Hamburger menu for mobile
- Search in header vs. separate
- Icons vs. text labels
- Dropdown menus

### Pattern 7: Loading State

**When to use**: Asynchronous operations, data fetching, file uploads

```
╔════════════════════════════════════════╗
║ Loading Project Data...                ║
╠════════════════════════════════════════╣
║                                        ║
║  ◴ Fetching files...                   ║
║                                        ║
║  [████████░░] 60% Complete             ║
║                                        ║
║  Est. time: 2 minutes remaining        ║
║                                        ║
║                    [Cancel]            ║
╚════════════════════════════════════════╝
```

**Variations**:
- Progress bar vs. spinner
- Skeleton loading (shows layout with placeholders)
- Percentage display
- Estimated time
- Cancellation option

### Pattern 8: Empty State

**When to use**: No content to show, no results, first-time experience

```
╔════════════════════════════════════════╗
║ Your Projects                          ║
╠════════════════════════════════════════╣
║                                        ║
║            ⓘ [folder icon]             ║
║                                        ║
║  No projects yet                       ║
║                                        ║
║  Get started by creating your first    ║
║  project or importing existing work.   ║
║                                        ║
║  [New Project]  [Import]               ║
║                                        ║
╚════════════════════════════════════════╝
```

**Variations**:
- Illustration (simple, minimal)
- Helpful guidance
- Call-to-action buttons
- Tone (friendly, not sad or apologetic)

### Pattern 9: Error State

**When to use**: Validation failures, network errors, permission denied

```
╔════════════════════════════════════════╗
║ Update Profile                         ║
╠════════════════════════════════════════╣
║                                        ║
║ ✗ Unable to save changes               ║
║   Please check your connection and     ║
║   try again.                           ║
║                                        ║
║ [Name ...........................]      ║
║                                        ║
║ [Email .........................]      ║
║ ✗ This email is already in use         ║
║                                        ║
║             [Retry]  [Cancel]          ║
║                                        ║
╚════════════════════════════════════════╝
```

**Variations**:
- Error message placement (inline vs. top)
- Tone (helpful, not blaming)
- Next steps (how to fix)
- Retry option

### Pattern 10: Success/Confirmation

**When to use**: Action completion, confirmation, positive feedback

```
╔════════════════════════════════════════╗
║ ✓ Profile Updated                      ║
╠════════════════════════════════════════╣
║                                        ║
║ Your changes have been saved.          ║
║                                        ║
║ [View Profile]  [Done]                 ║
║                                        ║
╚════════════════════════════════════════╝
```

**Variations**:
- Toast (small, dismissible)
- Modal (requires action)
- Inline (within page content)
- Auto-dismiss duration

## Responsive Breakpoints

Design for three viewpoints minimum:

### Mobile (320px - 480px)
```
Full-width layouts
Stacked elements
Single column
Tab navigation or hamburger menu
Touch-friendly (44px+ tap targets)
```

### Tablet (480px - 768px, and 768px - 1024px)
```
2-column layouts possible
Sidebar navigation optional
Spacious but not overly wide
```

### Desktop (1024px+)
```
Multi-column layouts
Sidebar or full-width navigation
Maximum width constraint (often 1200px-1400px)
Hover states show additional content
```

## Layout Quality Checklist

**Hierarchy**
- [ ] Is the most important information most prominent?
- [ ] Can users scan the layout in 2 seconds?
- [ ] Is the visual weight distributed appropriately?

**Grouping**
- [ ] Are related elements grouped together?
- [ ] Is whitespace used to separate distinct sections?
- [ ] Does the layout show the information structure?

**Alignment**
- [ ] Are elements aligned to a grid?
- [ ] Are left edges, right edges, or centers aligned consistently?
- [ ] Does alignment feel intentional, not accidental?

**Density**
- [ ] Is there enough space or is it cramped?
- [ ] Is there too much space or is it sparse?
- [ ] Does density match the use case?

**Clarity**
- [ ] Is it immediately clear what this screen does?
- [ ] Are interactive elements obvious?
- [ ] Are labels clear and concise?

**States**
- [ ] Are all major states shown? (Empty, loading, filled, error)
- [ ] Is the current state obvious?
- [ ] Are transitions clear?

## Designing for Content

**Design principle**: Content leads design, not the reverse.

1. **Inventory the content**: What information must be shown?
2. **Establish hierarchy**: What's critical vs. nice-to-have?
3. **Design structure**: How should it be organized?
4. **Create layout**: Now design the visual structure to match

**Example**:
- Content: Product name, price, rating, reviews, images, description, variants, shipping info
- Hierarchy: Name/price/rating most important; shipping info less critical
- Structure: Main product info at top, details below, reviews on sidebar or further down
- Layout: Hero image, product info, details, reviews

## Designing for Different Content Scenarios

**Single item** (detail view, post)
- Full width
- Generous whitespace
- Deep content available

**Multiple items** (list, grid)
- Compact representation
- Scannable rows/cards
- Pagination or infinite scroll

**Complex data** (table, dashboard)
- Dense but organized
- Sortable/filterable
- Clear headers and categories

**Dynamic content** (search, live updates)
- Loading states
- Empty states
- Transition states

## Common Layout Mistakes

**Mistake 1: Unclear Hierarchy**
- Everything is equally prominent
- User doesn't know where to look first
- Fix: Use size, color, spacing to guide attention

**Mistake 2: Poor Grouping**
- Related elements scattered
- Whitespace doesn't show relationships
- Fix: Use proximity to show connections

**Mistake 3: Ignoring Mobile**
- Layout doesn't work on small screens
- Text unreadable, buttons too small
- Fix: Design mobile-first, then scale up

**Mistake 4: Too Much Content**
- Screen feels cramped and overwhelming
- User doesn't know what to do
- Fix: Prioritize ruthlessly; hide secondary content

**Mistake 5: Inconsistent Alignment**
- Elements don't align to any grid
- Layout feels chaotic
- Fix: Establish a grid (8px, 16px, 24px) and stick to it

## Layout Iteration Process

1. **Start loose**: Rough ASCII, focus on structure
2. **Test readability**: Can someone understand this?
3. **Refine hierarchy**: Adjust spacing and grouping
4. **Test responsiveness**: Does it work on all viewports?
5. **Finalize**: Polish and document variations
6. **Hand off**: Provide clear specifications for development

## Responsive Design Patterns

### Stack on Mobile, Alongside on Desktop
```
Mobile:           Desktop:
┌────────┐       ┌─────────────┬─────────────┐
│ Panel  │       │   Panel     │   Details   │
│   A    │       │      A      │      B      │
└────────┘       └─────────────┴─────────────┘
┌────────┐
│ Panel  │
│   B    │
└────────┘
```

### Hide/Show Based on Viewport
```
Mobile:
- Show: Essential info, primary action
- Hide: Sidebar, secondary actions

Desktop:
- Show: Everything
- Sidebar visible
```

### Change Grid Columns
```
Mobile: 1 column
Tablet: 2 columns
Desktop: 3-4 columns
```

### Adjust Spacing & Typography
```
Mobile: Tighter spacing, smaller type
Desktop: Generous spacing, larger type
```
