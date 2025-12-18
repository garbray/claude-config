# Complete Dashboard Example

This file shows a full dashboard design in ASCII art with implementation guidance.

## Desktop Dashboard Layout

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ ★ Analytics Dashboard    Stats  Reports  Settings  🔍 Search       👤 Profile │
└────────────────────────────────────────────────────────────────────────────────┘

┌────────────┬──────────────────────────────────────────────────────────────────┐
│ Dashboard  │ Welcome Back, Admin!                                             │
│ ──────     │ ────────────────────────────────────────────────────────────     │
│ ► Home     │                                                                  │
│ ► Analytics│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│ ► Users    │ │ Total Revenue │ │ Active Users │ │ Conversions  │            │
│ ► Reports  │ │ ────────────  │ │ ────────────  │ │ ────────────  │            │
│ ► Settings │ │      $48.2K   │ │      1,284    │ │      12.4%    │            │
│ ► Logout   │ │ [View Details]│ │ [View Details]│ │ [View Details]│            │
│            │ └──────────────┘  └──────────────┘  └──────────────┘            │
│            │                                                                  │
│            │ Recent Activity                                                 │
│            │ ─────────────────────────────────────────────────────────       │
│            │ ┌──────────┬──────────┬──────────┬──────────┐                    │
│            │ │ Date     │ User     │ Action   │ Status   │                    │
│            │ ├──────────┼──────────┼──────────┼──────────┤                    │
│            │ │ 2024-01-15│ john@ex  │ Login    │ ✓ Active │                    │
│            │ │ 2024-01-15│ jane@ex  │ Upload   │ ✓ Success│                    │
│            │ │ 2024-01-14│ bob@ex   │ Comment  │ ✓ Active │                    │
│            │ └──────────┴──────────┴──────────┴──────────┘                    │
│            │                                                                  │
│            │ [Load More]                                                      │
│            │                                                                  │
└────────────┴──────────────────────────────────────────────────────────────────┘
```

## Mobile Dashboard Layout

```
┌──────────────────────────────┐
│ ★ Dashboard        ☰         │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Welcome Back, Admin!         │
│ ──────────────────────       │
│                              │
│ ┌──────────────────────────┐ │
│ │ Total Revenue            │ │
│ │ ────────────────────     │ │
│ │ $48.2K                   │ │
│ │ [View Details]           │ │
│ └──────────────────────────┘ │
│                              │
│ ┌──────────────────────────┐ │
│ │ Active Users             │ │
│ │ ────────────────────     │ │
│ │ 1,284                    │ │
│ │ [View Details]           │ │
│ └──────────────────────────┘ │
│                              │
│ ┌──────────────────────────┐ │
│ │ Conversions              │ │
│ │ ────────────────────     │ │
│ │ 12.4%                    │ │
│ │ [View Details]           │ │
│ └──────────────────────────┘ │
│                              │
│ Recent Activity              │
│ ──────────────────────       │
│                              │
│ ┌──────────────────────────┐ │
│ │ john@ex - Login          │ │
│ │ 2024-01-15 - ✓ Active    │ │
│ └──────────────────────────┘ │
│                              │
│ ┌──────────────────────────┐ │
│ │ jane@ex - Upload         │ │
│ │ 2024-01-15 - ✓ Success   │ │
│ └──────────────────────────┘ │
│                              │
│ ┌──────────────────────────┐ │
│ │ bob@ex - Comment         │ │
│ │ 2024-01-14 - ✓ Active    │ │
│ └──────────────────────────┘ │
│                              │
│ [Load More]                  │
│                              │
└──────────────────────────────┘
```

## Implementation Steps

### Step 1: HTML Structure

```html
<div class="dashboard-container">
  <!-- Header Navigation -->
  <header class="navbar">
    <div class="navbar-brand">★ Analytics Dashboard</div>
    <nav class="navbar-menu">
      <a href="#stats">Stats</a>
      <a href="#reports">Reports</a>
      <a href="#settings">Settings</a>
    </nav>
    <div class="navbar-search">
      <input type="search" placeholder="Search...">
    </div>
    <button class="navbar-profile">👤 Profile</button>
  </header>

  <div class="main-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="sidebar-brand">Dashboard</div>
      <nav class="sidebar-nav">
        <a href="#home" class="nav-item active">Home</a>
        <a href="#analytics" class="nav-item">Analytics</a>
        <a href="#users" class="nav-item">Users</a>
        <a href="#reports" class="nav-item">Reports</a>
        <a href="#settings" class="nav-item">Settings</a>
        <a href="#logout" class="nav-item logout">Logout</a>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="dashboard-content">
      <section class="welcome-section">
        <h1>Welcome Back, Admin!</h1>
      </section>

      <!-- Stats Cards Grid -->
      <section class="stats-grid">
        <div class="stat-card">
          <h3>Total Revenue</h3>
          <div class="stat-value">$48.2K</div>
          <button class="card-button">View Details</button>
        </div>
        
        <div class="stat-card">
          <h3>Active Users</h3>
          <div class="stat-value">1,284</div>
          <button class="card-button">View Details</button>
        </div>
        
        <div class="stat-card">
          <h3>Conversions</h3>
          <div class="stat-value">12.4%</div>
          <button class="card-button">View Details</button>
        </div>
      </section>

      <!-- Activity Table -->
      <section class="activity-section">
        <h2>Recent Activity</h2>
        <table class="activity-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>User</th>
              <th>Action</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2024-01-15</td>
              <td>john@example.com</td>
              <td>Login</td>
              <td><span class="status-badge active">✓ Active</span></td>
            </tr>
            <tr>
              <td>2024-01-15</td>
              <td>jane@example.com</td>
              <td>Upload</td>
              <td><span class="status-badge success">✓ Success</span></td>
            </tr>
            <tr>
              <td>2024-01-14</td>
              <td>bob@example.com</td>
              <td>Comment</td>
              <td><span class="status-badge active">✓ Active</span></td>
            </tr>
          </tbody>
        </table>
        <button class="load-more-button">Load More</button>
      </section>
    </main>
  </div>
</div>
```

### Step 2: CSS Styling Strategy

**Flexbox Layout for Main Structure**:
- Use `display: grid` for the sidebar + content layout: `grid-template-columns: 250px 1fr`
- Navbar: `display: flex; justify-content: space-between; align-items: center`
- Stats grid: `display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`

**Color Scheme**:
- Primary Blue: #0066cc (buttons, active states)
- Light Gray: #f5f5f5 (backgrounds)
- Border Gray: #e0e0e0
- Text Black: #333
- Success Green: #22c55e (status badges)

**Responsive Design**:
- Desktop (1024px+): Full layout with sidebar
- Tablet (768px-1024px): Sidebar collapses to icons
- Mobile (<768px): Hamburger menu, full-width layout

### Step 3: Interactive Elements

**Sidebar Navigation**:
- Highlight active link with background color
- Hover effect: background lightens
- Logout link: Different color (red) to indicate caution

**Stat Cards**:
- Hover: Lift effect with shadow, transform: translateY(-4px)
- "View Details" button: Opens modal or navigates to detailed page
- Show loading state while fetching updated data

**Activity Table**:
- Alternating row colors (white and light gray) for readability
- Hover row: highlight entire row
- Status badges: Color-coded (green for success, orange for warning)
- "Load More" button: Lazy loads additional entries

**Search Bar**:
- Real-time filtering as user types
- Auto-complete suggestions for common searches

### Step 4: Responsive Adaptation

**Mobile View (< 768px)**:
```
- Hide sidebar by default
- Add hamburger menu button to navbar
- Stack stat cards vertically
- Make table horizontal-scrollable or convert to cards
- Reduce padding/spacing for compact layout
```

**Tablet View (768px - 1024px)**:
```
- Collapse sidebar to icon-only view
- Show stat cards in 2 columns
- Adjust font sizes for medium screens
- Tooltip hover on sidebar icons
```

**Desktop View (> 1024px)**:
```
- Full sidebar with text labels
- 3-column stat card grid
- Full table view
- Larger padding and spacing for breathing room
```

### Step 5: Code Template - React Version

```jsx
import { useState } from 'react';

export function Dashboard() {
  const [activities, setActivities] = useState([
    { id: 1, date: '2024-01-15', user: 'john@example.com', action: 'Login', status: 'Active' },
    { id: 2, date: '2024-01-15', user: 'jane@example.com', action: 'Upload', status: 'Success' },
    { id: 3, date: '2024-01-14', user: 'bob@example.com', action: 'Comment', status: 'Active' },
  ]);

  const [sidebarOpen, setSidebarOpen] = useState(true);

  const stats = [
    { label: 'Total Revenue', value: '$48.2K' },
    { label: 'Active Users', value: '1,284' },
    { label: 'Conversions', value: '12.4%' },
  ];

  return (
    <div className="dashboard">
      <header className="navbar">
        <div className="navbar-brand">★ Analytics Dashboard</div>
        <nav className="navbar-menu">
          <a href="#stats">Stats</a>
          <a href="#reports">Reports</a>
          <a href="#settings">Settings</a>
        </nav>
        <input type="search" placeholder="Search..." className="navbar-search" />
        <button className="navbar-profile">👤 Profile</button>
      </header>

      <div className="main-layout">
        <aside className={`sidebar ${sidebarOpen ? 'open' : 'closed'}`}>
          <div className="sidebar-brand">Dashboard</div>
          <nav className="sidebar-nav">
            <a href="#home" className="nav-item active">Home</a>
            <a href="#analytics" className="nav-item">Analytics</a>
            <a href="#users" className="nav-item">Users</a>
            <a href="#reports" className="nav-item">Reports</a>
            <a href="#settings" className="nav-item">Settings</a>
          </nav>
        </aside>

        <main className="dashboard-content">
          <section className="welcome-section">
            <h1>Welcome Back, Admin!</h1>
          </section>

          <section className="stats-grid">
            {stats.map((stat) => (
              <div key={stat.label} className="stat-card">
                <h3>{stat.label}</h3>
                <div className="stat-value">{stat.value}</div>
                <button className="card-button">View Details</button>
              </div>
            ))}
          </section>

          <section className="activity-section">
            <h2>Recent Activity</h2>
            <table className="activity-table">
              <thead>
                <tr>
                  <th>Date</th>
                  <th>User</th>
                  <th>Action</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {activities.map((activity) => (
                  <tr key={activity.id}>
                    <td>{activity.date}</td>
                    <td>{activity.user}</td>
                    <td>{activity.action}</td>
                    <td>
                      <span className={`badge ${activity.status.toLowerCase()}`}>
                        ✓ {activity.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            <button className="load-more-button">Load More</button>
          </section>
        </main>
      </div>
    </div>
  );
}
```

### Key Implementation Features

1. **Data Structure**: Stats as array, activities as state
2. **State Management**: Using useState for sidebar toggle and data
3. **Responsiveness**: CSS media queries handle mobile/tablet/desktop
4. **Accessibility**: Proper semantic HTML, ARIA labels, keyboard navigation
5. **Performance**: Lazy loading with "Load More" button instead of loading all data
6. **Error States**: Handle empty states, loading states, error messages
7. **Interactions**: Click handlers for buttons, table row interactions, sidebar toggle
