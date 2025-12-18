# React Patterns Reference

Component organization and patterns for building ASCII-designed UIs as React applications.

## Component Structure

**Directory Organization**:
```
src/
├── components/
│   ├── Navigation/
│   │   └── Navigation.jsx
│   ├── Sidebar/
│   │   └── Sidebar.jsx
│   ├── CardGrid/
│   │   ├── CardGrid.jsx
│   │   └── Card.jsx
│   ├── Forms/
│   │   └── FormComponent.jsx
│   └── shared/
│       ├── Button.jsx
│       ├── Input.jsx
│       └── Modal.jsx
├── pages/
│   ├── Dashboard.jsx
│   ├── Users.jsx
│   └── Settings.jsx
├── hooks/
│   ├── useForm.js
│   └── useModal.js
└── App.jsx
```

## Reusable Button Component

**ASCII Design Context**:
Buttons appear in ASCII designs as `[Label]` with visual emphasis.

**React Implementation**:
```jsx
export function Button({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  onClick,
  className,
  ...props
}) {
  const baseStyles = 'font-semibold rounded transition-colors duration-200';
  
  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 disabled:bg-gray-400',
    secondary: 'border-2 border-blue-600 text-blue-600 hover:bg-blue-50 disabled:border-gray-400',
    danger: 'bg-red-600 text-white hover:bg-red-700 disabled:bg-gray-400',
  };
  
  const sizes = {
    small: 'px-3 py-1 text-sm',
    medium: 'px-4 py-2 text-base',
    large: 'px-6 py-3 text-lg',
  };
  
  return (
    <button
      className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${className}`}
      disabled={disabled}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
}
```

**Usage**:
```jsx
<Button>Submit</Button>
<Button variant="secondary">Cancel</Button>
<Button disabled>Disabled</Button>
```

## Reusable Input Component

**ASCII Design Context**:
Inputs appear as `[________________]` with labels above or adjacent.

**React Implementation**:
```jsx
export function Input({
  label,
  id,
  type = 'text',
  placeholder,
  error,
  required = false,
  onChange,
  value,
  ...props
}) {
  return (
    <div className="form-group">
      {label && (
        <label htmlFor={id} className="block text-sm font-medium mb-2">
          {label}
          {required && <span className="text-red-500">*</span>}
        </label>
      )}
      <input
        id={id}
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className={`
          w-full px-3 py-2 border rounded-md
          focus:outline-none focus:ring-2 focus:ring-blue-500
          ${error ? 'border-red-500' : 'border-gray-300'}
        `}
        {...props}
      />
      {error && <p className="text-red-500 text-sm mt-1">{error}</p>}
    </div>
  );
}
```

**Usage**:
```jsx
const [email, setEmail] = useState('');

<Input
  label="Email"
  id="email"
  type="email"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
  required
/>
```

## Navigation Component

**ASCII Design Context**:
```
┌──────────────────────────────────────┐
│ Logo    Home  About  Services   🔍   │
└──────────────────────────────────────┘
```

**React Implementation**:
```jsx
import { useState } from 'react';

export function Navigation() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  
  const navItems = [
    { label: 'Home', href: '/' },
    { label: 'About', href: '/about' },
    { label: 'Services', href: '/services' },
  ];
  
  return (
    <header className="bg-white shadow">
      <nav className="max-w-7xl mx-auto px-4 flex items-center justify-between h-16">
        <div className="text-2xl font-bold">★ Logo</div>
        
        {/* Desktop Menu */}
        <ul className="hidden md:flex gap-6">
          {navItems.map((item) => (
            <li key={item.href}>
              <a href={item.href} className="hover:text-blue-600">
                {item.label}
              </a>
            </li>
          ))}
        </ul>
        
        {/* Mobile Menu Button */}
        <button
          className="md:hidden p-2"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          ☰
        </button>
        
        {/* Mobile Menu */}
        {isMenuOpen && (
          <ul className="absolute top-16 left-0 right-0 bg-white flex flex-col border-t">
            {navItems.map((item) => (
              <li key={item.href}>
                <a href={item.href} className="block px-4 py-2 hover:bg-gray-100">
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        )}
      </nav>
    </header>
  );
}
```

## Custom Form Hook

**ASCII Design Context**:
Multiple form fields grouped together with validation and submission.

**React Implementation**:
```jsx
import { useState } from 'react';

export function useForm(initialValues, onSubmit) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues(prev => ({ ...prev, [name]: value }));
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    try {
      await onSubmit(values);
    } catch (error) {
      setErrors(error.validationErrors || {});
    } finally {
      setIsSubmitting(false);
    }
  };
  
  return {
    values,
    errors,
    isSubmitting,
    handleChange,
    handleSubmit,
  };
}
```

**Usage**:
```jsx
function LoginForm() {
  const { values, errors, handleChange, handleSubmit } = useForm(
    { email: '', password: '' },
    async (data) => {
      await loginUser(data);
    }
  );
  
  return (
    <form onSubmit={handleSubmit}>
      <Input
        label="Email"
        name="email"
        value={values.email}
        onChange={handleChange}
        error={errors.email}
      />
      <Input
        label="Password"
        name="password"
        type="password"
        value={values.password}
        onChange={handleChange}
        error={errors.password}
      />
      <Button type="submit">Login</Button>
    </form>
  );
}
```

## Sidebar Navigation Component

**ASCII Design Context**:
```
┌──────────┬───────────────┐
│ ★ Logo   │ Main Content  │
│ ──────   │               │
│ ► Home   │               │
│ ► Users  │               │
└──────────┴───────────────┘
```

**React Implementation**:
```jsx
import { useState } from 'react';
import { useLocation } from 'react-router-dom';

export function Sidebar({ isOpen, onClose }) {
  const location = useLocation();
  
  const navItems = [
    { label: 'Dashboard', icon: '📊', href: '/dashboard' },
    { label: 'Users', icon: '👥', href: '/users' },
    { label: 'Settings', icon: '⚙', href: '/settings' },
  ];
  
  return (
    <>
      {/* Overlay for mobile */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 md:hidden"
          onClick={onClose}
        />
      )}
      
      <aside
        className={`
          fixed md:relative
          top-0 left-0 h-screen
          w-64 bg-gray-900 text-white
          transform transition-transform md:translate-x-0
          ${isOpen ? 'translate-x-0' : '-translate-x-full'}
        `}
      >
        <div className="p-4 text-2xl font-bold">★ Logo</div>
        
        <nav className="mt-8">
          {navItems.map((item) => (
            <a
              key={item.href}
              href={item.href}
              className={`
                block px-4 py-3 flex items-center gap-3
                hover:bg-gray-800 transition-colors
                ${location.pathname === item.href ? 'bg-blue-600' : ''}
              `}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </a>
          ))}
        </nav>
      </aside>
    </>
  );
}
```

## Card Grid Component

**ASCII Design Context**:
```
┌──────────┐  ┌──────────┐
│ Title    │  │ Title    │
│ Content  │  │ Content  │
└──────────┘  └──────────┘
```

**React Implementation**:
```jsx
export function Card({ title, children, onAction, actionLabel = 'Action' }) {
  return (
    <div className="border rounded-lg p-6 hover:shadow-lg transition-shadow">
      <h3 className="text-lg font-semibold mb-4">{title}</h3>
      <div className="mb-4">{children}</div>
      {onAction && (
        <button
          onClick={onAction}
          className="text-blue-600 hover:text-blue-700 font-medium"
        >
          {actionLabel}
        </button>
      )}
    </div>
  );
}

export function CardGrid({ children, columns = 3 }) {
  return (
    <div
      className={`grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-${columns}`}
    >
      {children}
    </div>
  );
}
```

**Usage**:
```jsx
<CardGrid columns={3}>
  <Card title="Statistics" onAction={() => {}}>
    <p>Value: 42</p>
  </Card>
  <Card title="Activity" onAction={() => {}}>
    <p>Last updated: Today</p>
  </Card>
  <Card title="Users" onAction={() => {}}>
    <p>Active: 128</p>
  </Card>
</CardGrid>
```

## Modal Component with Hook

**ASCII Design Context**:
Modal dialog with header, content, and footer buttons.

**React Implementation**:
```jsx
import { useState } from 'react';

export function useModal() {
  const [isOpen, setIsOpen] = useState(false);
  
  return {
    isOpen,
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
    toggle: () => setIsOpen(!isOpen),
  };
}

export function Modal({ isOpen, onClose, title, children, onConfirm }) {
  if (!isOpen) return null;
  
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div className="bg-white rounded-lg shadow-lg max-w-md w-full mx-4">
        <div className="flex justify-between items-center p-6 border-b">
          <h2 className="text-xl font-semibold">{title}</h2>
          <button onClick={onClose} className="text-gray-500 text-2xl">
            ×
          </button>
        </div>
        
        <div className="p-6">{children}</div>
        
        <div className="flex gap-3 justify-end p-6 border-t">
          <button
            onClick={onClose}
            className="px-4 py-2 border rounded hover:bg-gray-100"
          >
            Cancel
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  );
}
```

**Usage**:
```jsx
function DeleteUser({ userId }) {
  const modal = useModal();
  
  const handleDelete = async () => {
    await deleteUser(userId);
    modal.close();
  };
  
  return (
    <>
      <Button onClick={modal.open}>Delete</Button>
      <Modal
        isOpen={modal.isOpen}
        onClose={modal.close}
        title="Confirm Delete"
        onConfirm={handleDelete}
      >
        <p>Are you sure you want to delete this user?</p>
      </Modal>
    </>
  );
}
```

## Layout Container Component

**React Implementation**:
```jsx
export function PageLayout({ sidebar = true, children }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  
  return (
    <div className="flex h-screen">
      {sidebar && <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />}
      
      <main className="flex-1 overflow-auto">
        <header className="bg-white border-b p-4 flex items-center gap-4">
          {sidebar && (
            <button
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="md:hidden p-2"
            >
              ☰
            </button>
          )}
        </header>
        
        <div className="max-w-7xl mx-auto p-6">
          {children}
        </div>
      </main>
    </div>
  );
}
```

These patterns provide a foundation for building React applications based on ASCII UI designs. Customize styling, add additional features, and compose them together to create complete applications.
