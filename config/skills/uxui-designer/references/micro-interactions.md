# Micro-Interactions & Behavior Design Guide

Micro-interactions are the small animations, transitions, and feedback states that make interfaces feel responsive and polished. They communicate state changes, guide user attention, and elevate the overall experience. Every micro-interaction should serve a purpose—never decoration.

## Micro-Interaction Principles

**Principle 1: Communicate State Change**
Animations should show that something happened. When a button is clicked, something changes. When data loads, show progress.

**Principle 2: Provide Feedback**
Users need to know their action was received. Immediate visual feedback (highlight, load indication) reassures them.

**Principle 3: Guide Attention**
Motion draws the eye. Use animation to guide users to the next step or important information.

**Principle 4: Maintain Continuity**
Transitions should feel connected and logical. Elements should appear to move through space, not teleport.

**Principle 5: Keep It Brief**
Most micro-interactions should be fast (150-300ms). Longer animations feel sluggish. Shorter animations might be missed.

**Principle 6: Intentionality Over Delight**
Every animation should have a purpose. Avoid decorative animation that doesn't communicate anything.

## Timing & Easing

### Duration Guidelines

```
Micro-interactions (fast feedback)
└─ Hover highlights, button feedback
└─ Duration: 100-150ms
└─ Easing: ease-out (feels snappy)

Standard transitions (state changes)
└─ Modal open/close, element fade
└─ Duration: 200-300ms
└─ Easing: ease-in-out (feels natural)

Longer transitions (dramatic changes)
└─ Page transitions, large layout shifts
└─ Duration: 300-500ms
└─ Easing: cubic-bezier for custom feel

Long animations (progress indication)
└─ Looping spinners, progress bars
└─ Duration: 1-3s per loop
└─ Easing: linear (steady, predictable)
```

### Easing Functions

```
Linear
└─ Constant speed throughout
└─ Use for: Continuous animations (spinners, progress bars)
└─ Feels: Robotic, mechanical

Ease-in (accelerate)
└─ Slow start, fast end
└─ Use for: Exiting elements, disappearing content
└─ Feels: Natural, energetic

Ease-out (decelerate)
└─ Fast start, slow end
└─ Use for: Entering elements, appearing content
└─ Feels: Snappy, responsive

Ease-in-out (accelerate then decelerate)
└─ Slow start, fast middle, slow end
└─ Use for: General state transitions
└─ Feels: Smooth, considered

Custom cubic-bezier
└─ Fine-tuned curves for specific feels
└─ Use for: Brand-specific animations
└─ Feels: Polished, intentional
```

## Common Micro-Interactions

### 1. Button Press Feedback

**Purpose**: Communicate that a click was received

**Behavior**:
```
Resting
  └─ Normal appearance
  
Hover
  └─ Slight background color change
  └─ Optional: slight scale up (1.02x)
  └─ Duration: 150ms ease-out
  
Active/Pressed
  └─ Darker background
  └─ Optional: slight scale down (0.98x)
  └─ Duration: 100ms ease-in
  
Loading
  └─ Disabled appearance (opacity reduced)
  └─ Spinner or loading text
  └─ Duration: until complete
  
Success
  └─ Checkmark or success icon
  └─ Optional: green highlight
  └─ Duration: 300ms fade
  └─ Then: Return to normal or navigate
  
Disabled
  └─ Reduced opacity
  └─ Cursor: not-allowed
  └─ No hover state
```

**Example CSS Concept**:
```
Button at rest:
  background: #0066cc
  transform: scale(1)

Button on hover:
  background: #0052a3
  transform: scale(1.02)
  transition: all 150ms ease-out

Button on active (clicked):
  background: #003d7a
  transform: scale(0.98)
  transition: all 100ms ease-in
```

### 2. Input Field Focus & Validation

**Purpose**: Communicate which field is active and whether input is valid

**Behavior**:
```
Resting (unfocused)
  └─ Gray border
  └─ Placeholder text visible
  └─ Duration: instant

Focused
  └─ Blue border (primary color)
  └─ Placeholder fades
  └─ Optional: background color change
  └─ Duration: 150ms ease-out
  └─ Cursor: text

Typing/Filled
  └─ Still focused state
  └─ Remove placeholder
  └─ Optional: show clear (✕) button on hover

Validation (Real-time)
  └─ Invalid: Red border
  └─ Show error message below field
  └─ Duration: 150ms
  └─ Icon: ✗ with red color

Validation (On blur)
  └─ Check when user leaves field
  └─ Show error after blur, not during typing
  └─ Allows user to complete entry

Valid
  └─ Green border or checkmark
  └─ Duration: 300ms ease-out
  └─ Optional: subtle success animation
  └─ Remove auto on new edits

Focus with error
  └─ Red border maintained
  └─ Error message shown
  └─ User can correct
```

**Example**:
```
Email field, empty:
  border: 1px solid #ccc
  color: #999 (placeholder)

Email field, focused:
  border: 2px solid #0066cc
  outline: none
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1)
  transition: all 150ms ease-out

Email field, invalid:
  border: 2px solid #dc3545
  (show error message below)

Email field, valid:
  border: 2px solid #28a745
  (show checkmark icon)
```

### 3. Loading States

**Pattern 1: Skeleton Loading**
```
Use when: Layout is predictable (content fills fixed spaces)
Show: Gray placeholder elements matching layout
Duration: Until real content arrives
Benefit: Feels faster than spinner; user sees layout immediately

Example:
  ┌──────────────────┐
  │ ░░░░░░░░░░░░░░░░│  ← Placeholder image
  │ ░░░░░░░░░░░░░░░░│
  ├──────────────────┤
  │ ░░░░░░░░ Title   │  ← Placeholder text
  │ ░░░░░░░░░░░░░░░░│
  │ ░░░░░░░░░░░░░░░░│
  └──────────────────┘
  
Behavior:
  └─ Subtle shimmer animation (left to right)
  └─ Duration: 400-600ms
  └─ Opacity: 60% gray
  └─ Easing: ease-in-out
```

**Pattern 2: Spinner Loading**
```
Use when: Layout is unpredictable (variable content size)
Show: Centered spinner with label
Duration: Until real content arrives
Benefit: Works for any content size

Example:
  ◴ Loading...
  
  or
  
  ⟳ Fetching data...

Behavior:
  └─ Spinner rotates continuously
  └─ Duration: 1 second per rotation
  └─ Easing: linear (steady, predictable)
  └─ Optional: Color shift for branded feel
```

**Pattern 3: Progress Bar**
```
Use when: Process has known duration or multiple steps
Show: Linear bar with percentage or step indicator
Duration: Until complete
Benefit: Shows progress; users know it's not frozen

Example:
  Uploading file... [████████░░] 60%
  
  or for multi-step:
  
  Step 1 of 3: Validating...
  [████████░░░░░░░░░░]

Behavior:
  └─ Bar fills smoothly
  └─ Duration: tied to actual process
  └─ Optional: Show estimated time remaining
  └─ Allow cancellation if user-initiated action
```

**Pattern 4: Indeterminate Spinner**
```
Use when: Duration is completely unknown
Show: Subtle animated spinner
Duration: Until complete (don't know when)
Benefit: Minimal, unobtrusive

Example:
  ⟳ (endless rotation)

Behavior:
  └─ Subtle rotation or shimmer
  └─ Duration: 2-3 seconds per loop
  └─ Easing: linear
  └─ Optional: Multiple spinners for complex loading
```

### 4. Modal Open/Close

**Purpose**: Focus user attention on modal content

**On Open**:
```
Background overlay
  └─ Fade in: 0 → 0.5 opacity
  └─ Duration: 200ms
  └─ Easing: ease-out
  └─ Color: dark with reduced opacity

Modal itself
  └─ Appear at center (scale 0.9 → 1)
  └─ Duration: 250ms
  └─ Easing: cubic-bezier(0.34, 1.56, 0.64, 1) [bounce-out]
  └─ Or fade in: 0 → 1 opacity
  └─ Or slide up from bottom (on mobile)
  
Behavior:
  └─ Overlay: Click to close (optional)
  └─ Escape key: Close modal (if safe)
  └─ Focus trap: Keep focus within modal
```

**On Close**:
```
Modal itself
  └─ Fade out OR scale to 0.9 and fade
  └─ Duration: 150ms
  └─ Easing: ease-in

Background overlay
  └─ Fade out: 0.5 → 0
  └─ Duration: 150ms
  └─ Easing: ease-in
  
Behavior:
  └─ Return focus to trigger element
```

### 5. Dropdown Menu

**Purpose**: Show/hide menu options smoothly

**On Open**:
```
Menu items appear
  └─ Slide down from top: opacity 0, transform: scaleY(0.8)
  └─ To: opacity 1, transform: scaleY(1)
  └─ Duration: 150ms
  └─ Easing: ease-out
  └─ Transform origin: top

Behavior:
  └─ Trap focus within menu
  └─ Arrow keys to navigate items
  └─ Click item or Enter to select
```

**On Close**:
```
Menu items disappear
  └─ Reverse animation: scaleY(1) → scaleY(0.8), opacity 1 → 0
  └─ Duration: 100ms
  └─ Easing: ease-in
```

### 6. Tab Switching

**Purpose**: Show content change between tabs smoothly

**Behavior**:
```
Tab label clicked
  └─ Underline animates to new tab
  └─ Duration: 200ms
  └─ Easing: ease-out

Content transition
  └─ Fade out (opacity 1 → 0): 100ms
  └─ Change content (instantly at 50ms mark)
  └─ Fade in (opacity 0 → 1): 100ms
  └─ Or slide: outgoing slides left, incoming slides in from right

Button focus styling
  └─ Underline color change
  └─ Duration: 150ms
  └─ Easing: ease-out
```

### 7. Toast/Notification

**Purpose**: Notify user of action result without interrupting

**Behavior**:
```
Appears
  └─ Slide up from bottom: translateY(100px) → translateY(0)
  └─ Fade in: opacity 0 → 1
  └─ Duration: 200ms
  └─ Easing: ease-out

Visible
  └─ Auto-dismiss: 3-4 seconds (or until action)
  └─ Exception: Error toasts stay until manually dismissed

Disappears
  └─ Slide down: translateY(0) → translateY(20px)
  └─ Fade out: opacity 1 → 0
  └─ Duration: 150ms
  └─ Easing: ease-in
  └─ Or just fade (simpler)

Positioning
  └─ Bottom right (standard)
  └─ Top center (alternative)
  └─ Don't block important content
```

### 8. Form Submission

**Purpose**: Communicate that form is processing and eventually completed

**Behavior**:
```
On submit click
  └─ Button shows spinner: [⟳ Submitting...]
  └─ Button disabled (no multiple submissions)
  └─ Duration: until response

On success
  └─ Show checkmark: [✓ Saved]
  └─ Button styling: green background
  └─ Duration: 1-2 seconds
  └─ Then: Navigate or reset form

On error
  └─ Show error icon: [✗ Error]
  └─ Button color: red
  └─ Show error message below form
  └─ Duration: until user retries
  └─ User can correct and resubmit

Validation errors
  └─ Don't submit on validation error
  └─ Highlight invalid fields (red border)
  └─ Show error messages inline
  └─ Don't proceed until fixed
```

## Error Message Design

Error messages are micro-interactions. They must be clear, helpful, and not accusatory.

### Error Message Formula

**Good**: [Problem] [How to fix] [Optional action]

Examples:
```
❌ BAD:
  "Invalid input"
  "Error occurred"
  "Failed"

✓ GOOD:
  "Password must be at least 8 characters"
  "Email address already in use. Try a different one or reset your password."
  "No internet connection. Check your connection and try again."
  "Upload failed. File is too large (max 10MB). Try a smaller file."
```

### Error Messaging by Scenario

**Validation Error**
```
Field: Email
Error: "Please enter a valid email address (e.g., name@example.com)"
Placement: Below field, red text
Duration: Until user fixes
Action: Enable submit when fixed
```

**Network Error**
```
"Unable to connect to server. Check your internet and try again."
Placement: Top of form or modal
Color: Orange/warning
Action: Retry button
```

**Server Error**
```
"Something went wrong. Please try again in a moment."
Placement: Modal or prominent banner
Color: Red
Action: Retry button, contact support link
```

**Permission Error**
```
"You don't have permission to edit this. Ask the owner for access."
Placement: Where action was attempted
Color: Orange/warning
Action: Contact owner link
```

**Timeout Error**
```
"Request took too long. Check your connection and try again."
Placement: Inline or modal
Color: Orange/warning
Action: Retry button
```

### Error Messaging Principles

1. **Be specific**: "Email already in use" not "Error"
2. **Be helpful**: Explain how to fix it
3. **Be kind**: Don't blame the user ("You entered wrong..." → "This didn't match...")
4. **Be visible**: Use color, icons, strategic placement
5. **Be discoverable**: Show inline first, then error summary if multiple

## Transition Between States

Every major state change should have a clear transition.

```
States:
  Idle → Editing → Saving → Saved/Error

Transitions:
  Idle to Editing
    └─ Fields unlock (opacity 1, enabled)
    └─ Save/Cancel buttons appear
    └─ Duration: 150ms fade-in

  Editing to Saving
    └─ Submit button shows spinner
    └─ Other inputs disabled (opacity 0.5)
    └─ Duration: instant

  Saving to Saved
    └─ Button shows checkmark
    └─ Color changes to green
    └─ Duration: 250ms
    └─ Then: Auto-return to Idle (1-2s delay)

  Saving to Error
    └─ Button shows error icon
    └─ Color changes to red
    └─ Error message appears
    └─ Duration: instant
    └─ Stays until user retries
```

## Accessibility in Micro-Interactions

**Principle 1: Provide Alternatives**
- Use animations to enhance, not communicate critical information
- Provide text equivalents for animated feedback

**Principle 2: Respect User Preferences**
- Respect `prefers-reduced-motion` media query
- Disable animations for users who prefer them off

**Principle 3: Ensure Contrast**
- Animated elements must meet WCAG contrast ratios
- Don't rely solely on color to communicate state

**Principle 4: Keep It Fast**
- Animations under 300ms are less problematic for vestibular issues
- Avoid large moving elements

**Example: Respecting Motion Preferences**
```
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Performance Considerations

**Good Performance Practices**:
- Use `transform` and `opacity` (GPU-accelerated)
- Avoid animating `width`, `height`, `position` (triggers layout recalculation)
- Keep animations under 300ms for most micro-interactions
- Use `will-change` sparingly for elements you're animating

**Bad Practices**:
- Animating `left`, `top`, `width`, `height` (layout thrashing)
- Complex JavaScript animations (use CSS)
- Long durations that feel sluggish
- Multiple simultaneous animations on same element

## Documenting Micro-Interactions

When specifying micro-interactions for developers:

```
Interaction: Button hover state
Trigger: Mouse enters button
Animation: Background color change + scale
  - From: #0066cc, scale 1
  - To: #0052a3, scale 1.02
  - Duration: 150ms
  - Easing: ease-out
On hover exit:
  - Return to initial state
  - Duration: 150ms
  - Easing: ease-out
Accessibility: Include focus state (keyboard navigation)
```

## Common Mistakes

**Mistake 1: Animation for decoration only**
- Spinning icons that don't mean anything
- Fade-ins on every element
- Fix: Every animation should communicate something

**Mistake 2: Animations too long**
- 500ms+ for button hover (feels sluggish)
- Slow transitions (annoys users)
- Fix: Keep micro-interactions fast (100-300ms)

**Mistake 3: No feedback for user actions**
- Click button, nothing happens visually
- Form submits with no indication
- Fix: Always provide immediate visual feedback

**Mistake 4: Ignoring accessibility**
- Animations can't be disabled
- No text alternative for animated feedback
- Fix: Test with `prefers-reduced-motion`

**Mistake 5: Inconsistent timing**
- Some buttons respond in 100ms, others 300ms
- Loading spinners have different speeds
- Fix: Establish a timing standard for your product
