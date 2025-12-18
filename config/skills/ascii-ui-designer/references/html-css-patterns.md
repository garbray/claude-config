# HTML/CSS Patterns Reference

Common component structures and CSS approaches for translating ASCII designs into production code.

## Navigation Bar

**ASCII Pattern**:
```
┌─────────────────────────────────────────────┐
│ Logo    Home  About  Services     [Search] │
└─────────────────────────────────────────────┘
```

**HTML Structure**:
```html
<header>
  <nav class="navbar">
    <div class="navbar-brand">Logo</div>
    <ul class="navbar-menu">
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/services">Services</a></li>
    </ul>
    <button class="navbar-search">🔍 Search</button>
  </nav>
</header>
```

**CSS Strategy**:
- Use Flexbox: `display: flex; justify-content: space-between; align-items: center;`
- Sticky positioning: `position: sticky; top: 0;`
- Logo width: auto or fixed (60-100px)
- Menu: flex with gap spacing
- Responsive: Stack vertically on mobile with hamburger menu

## Sidebar Navigation

**ASCII Pattern**:
```
┌────────────┬─────────────────┐
│ ★ Logo     │ Main Content    │
│ ──────     │                 │
│ ► Dashboard│                 │
│ ► Users    │                 │
│ ► Settings │                 │
└────────────┴─────────────────┘
```

**HTML Structure**:
```html
<div class="container">
  <aside class="sidebar">
    <div class="sidebar-brand">★ Logo</div>
    <nav class="sidebar-nav">
      <a href="/dashboard" class="nav-item">Dashboard</a>
      <a href="/users" class="nav-item">Users</a>
      <a href="/settings" class="nav-item">Settings</a>
    </nav>
  </aside>
  <main class="content">
    <!-- Main content here -->
  </main>
</div>
```

**CSS Strategy**:
- Container: `display: grid; grid-template-columns: 250px 1fr;`
- Sidebar: `position: sticky; top: 0; height: 100vh; overflow-y: auto;`
- Active nav item: highlight with background color
- Responsive: Collapse sidebar to icons on tablet, hamburger on mobile

## Card Grid

**ASCII Pattern**:
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Card Title   │  │ Card Title   │  │ Card Title   │
│ ────────     │  │ ────────     │  │ ────────     │
│ Content      │  │ Content      │  │ Content      │
│ ────────     │  │ ────────     │  │ ────────     │
│ [Action]     │  │ [Action]     │  │ [Action]     │
└──────────────┘  └──────────────┘  └──────────────┘
```

**HTML Structure**:
```html
<section class="card-grid">
  <article class="card">
    <h3 class="card-title">Card Title</h3>
    <div class="card-content">Content here</div>
    <button class="card-action">Action</button>
  </article>
  <!-- Repeat for more cards -->
</section>
```

**CSS Strategy**:
- Grid: `display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;`
- Card: `border: 1px solid #ccc; border-radius: 8px; padding: 20px;`
- Hover effect: `transform: translateY(-4px); box-shadow: 0 8px 16px rgba(0,0,0,0.1);`
- Responsive: Automatically adjusts columns based on screen size

## Form Layout

**ASCII Pattern**:
```
┌────────────────────────────┐
│ Form Title                 │
│ ──────────────────────     │
│ [Label]                    │
│ [________________]         │
│                            │
│ [Label]                    │
│ [________________]         │
│                            │
│ [Submit] [Cancel]          │
└────────────────────────────┘
```

**HTML Structure**:
```html
<form class="form-container">
  <h2 class="form-title">Form Title</h2>
  
  <div class="form-group">
    <label for="field1">Label</label>
    <input type="text" id="field1" name="field1" required>
  </div>
  
  <div class="form-group">
    <label for="field2">Label</label>
    <input type="text" id="field2" name="field2" required>
  </div>
  
  <div class="form-actions">
    <button type="submit" class="btn-primary">Submit</button>
    <button type="button" class="btn-secondary">Cancel</button>
  </div>
</form>
```

**CSS Strategy**:
- Form group: `margin-bottom: 20px;` with flex layout
- Labels: `display: block; margin-bottom: 8px; font-weight: 600;`
- Inputs: `width: 100%; padding: 10px 12px; border: 1px solid #ccc; border-radius: 4px;`
- Focus state: `outline: none; border-color: #0066cc; box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);`
- Actions: `display: flex; gap: 12px; justify-content: flex-end;`

## Data Table

**ASCII Pattern**:
```
┌────────┬─────────┬──────────┐
│ Name   │ Email   │ Status   │
├────────┼─────────┼──────────┤
│ John   │ j@ex.cm │ Active   │
│ Jane   │ j@ex.cm │ Inactive │
└────────┴─────────┴──────────┘
```

**HTML Structure**:
```html
<table class="data-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>john@example.com</td>
      <td><span class="badge-active">Active</span></td>
    </tr>
    <tr>
      <td>Jane</td>
      <td>jane@example.com</td>
      <td><span class="badge-inactive">Inactive</span></td>
    </tr>
  </tbody>
</table>
```

**CSS Strategy**:
- Table: `width: 100%; border-collapse: collapse;`
- Header: `background-color: #f5f5f5; font-weight: 600;`
- Cells: `padding: 12px; text-align: left; border-bottom: 1px solid #e0e0e0;`
- Row hover: `background-color: #f9f9f9;`
- Responsive: Use horizontal scroll on mobile or transform to cards

## Modal Dialog

**ASCII Pattern**:
```
┌─────────────────────────────┐
│ Modal Title             [×] │
├─────────────────────────────┤
│ Modal content here          │
│                             │
├─────────────────────────────┤
│ [Cancel]              [OK] │
└─────────────────────────────┘
```

**HTML Structure**:
```html
<div class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h2>Modal Title</h2>
      <button class="modal-close" aria-label="Close">&times;</button>
    </div>
    <div class="modal-body">
      Modal content here
    </div>
    <div class="modal-footer">
      <button class="btn-secondary">Cancel</button>
      <button class="btn-primary">OK</button>
    </div>
  </div>
</div>
```

**CSS Strategy**:
- Overlay: `position: fixed; inset: 0; background: rgba(0, 0, 0, 0.5); display: flex; align-items: center; justify-content: center;`
- Modal: `background: white; border-radius: 8px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2); max-width: 500px; width: 90%;`
- Header: `padding: 20px; border-bottom: 1px solid #e0e0e0;`
- Body: `padding: 20px;`
- Footer: `padding: 20px; border-top: 1px solid #e0e0e0; display: flex; justify-content: flex-end; gap: 10px;`

## Button States & Styles

**Common Button Variants**:

```css
/* Primary Button */
.btn-primary {
  background-color: #0066cc;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
}

.btn-primary:hover {
  background-color: #0052a3;
}

.btn-primary:active {
  background-color: #003d7a;
}

/* Secondary Button */
.btn-secondary {
  background-color: transparent;
  color: #0066cc;
  border: 1px solid #0066cc;
  padding: 10px 20px;
}

.btn-secondary:hover {
  background-color: #f0f7ff;
}

/* Disabled State */
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

## Responsive Breakpoints

Standard breakpoint strategy:

```css
/* Mobile-first approach */
/* Default: mobile (< 640px) */

/* Tablet */
@media (min-width: 768px) {
  /* Tablet-specific styles */
}

/* Desktop */
@media (min-width: 1024px) {
  /* Desktop-specific styles */
}

/* Large Desktop */
@media (min-width: 1280px) {
  /* Large screen-specific styles */
}
```

Use percentage or viewport-relative units for fluid layouts:
- Widths: percentages or `max-width` constraints
- Font sizes: `rem` units (relative to root font-size)
- Spacing: `rem` or `em` units for consistent scaling
