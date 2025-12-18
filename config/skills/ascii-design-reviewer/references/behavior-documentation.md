# Behavior Documentation Templates

Reference templates for documenting step-by-step system behavior during design reviews.

## Basic Step Documentation Template

```
STEP: [Step Name / Screen Name]
───────────────────────────────────────────────

WHEN THIS HAPPENS:
- User does X
- System detects Y
- Condition Z is met

USER SEES:
- What appears on screen
- What elements are visible
- What's disabled/enabled
- Visual state

WHAT USER CAN DO:
- Action 1 and what happens
- Action 2 and what happens
- Keyboard shortcuts
- Mouse actions
- Touch actions

DATA DISPLAYED:
- Where data comes from
- How it's formatted
- What if no data
- Data validation rules

VALIDATIONS:
- What must be true
- What checks happen
- When checks happen
- What if invalid

BACKEND OPERATIONS:
- API call: [METHOD] /path
- Query: [Database query]
- Side effects: [What changes]
- Timing: [How long expected]

TRANSITIONS:
- What happens next
- Alternative paths
- Error paths
- Back button

EDGE CASES:
- Empty state
- Full data
- Partial data
- Errors
- Slow network
- Offline

PERFORMANCE:
- Expected load time
- Acceptable delay
- Loading indicators
- Timeouts
```

## Complete User Journey Documentation

### Example: Password Reset Flow

```
FEATURE: Password Reset
────────────────────────

ENTRY POINT:
- User clicks "Forgot Password" link
- User is logged out
- User sees login screen

STEP 1: Request Password Reset
───────────────────────────────

USER SEES:
┌─────────────────────────────┐
│ Forgot Your Password?       │
│ ─────────────────────────   │
│ Email Address:              │
│ [____________________]      │
│ [Reset Password]            │
│ [Back to Login]             │
└─────────────────────────────┘

USER CAN:
- Enter email address
- Click "Reset Password" button
- Click "Back to Login" link
- Press Enter to submit
- Press Tab to navigate

DATA:
- Email field accepts: valid email format
- Max length: 255 characters
- Trimmed of whitespace
- Converted to lowercase

VALIDATIONS:
Client-side (before submit):
- Email is not empty
- Email matches valid format (RFC 5322)
- Instant feedback on format

Server-side (processing):
- Email exists in system
- Account is active
- User not already resetting
- Rate limit check (max 3/hour)

BACKEND:
POST /api/auth/forgot-password
Headers: Content-Type: application/json
Body: { "email": "user@example.com" }

WHAT HAPPENS:
1. Validate email format
2. Lookup user by email
3. Generate reset token (32 chars, random)
4. Set token expiry (1 hour)
5. Store in database: user_id, token, expires_at
6. Send email with reset link
7. Log action: user_id, timestamp, ip_address
8. Return 200 OK (regardless of email found)

WHY REGARDLESS: Security - don't reveal if email exists

TIMING:
- Validation: < 50ms
- Database lookup: < 100ms
- Email send: < 2s (async)
- Total user experience: < 1s

USER SEES AFTER:
✓ "Check your email for a link to reset your password"
✓ "Link will expire in 1 hour"
✓ "Didn't receive email? [Resend] [Try another email] [Contact Support]"

STATES:
- Initial: Empty form
- Typing: Real-time format feedback
- Submitting: Button disabled, spinner shown
- Success: Confirmation message
- Error: Error message with recovery

ERRORS:
- Email format invalid: "Please enter a valid email"
- Rate limit exceeded: "Too many attempts. Try again in 1 hour"
- Server error: "Something went wrong. Please try again later"
- Timeout: "Request timed out. Please try again"

RECOVERY:
- Fix and resubmit: User can change email and retry
- Rate limit: Must wait 1 hour
- Resend: Can request new email
- Alternative: Contact support


STEP 2: Receive and Verify Email
─────────────────────────────────

EMAIL CONTAINS:
Subject: Reset Your Password
Body:
  "Click the link below to reset your password:
   https://app.com/reset?token=abc123def456
   
   This link expires in 1 hour.
   
   Didn't request this? Ignore this email.
   
   Support: support@app.com"

LINKS:
- Reset link includes: user_id (encrypted), token
- Link valid for: 1 hour
- Link one-time use: Yes
- After used: Must request new link

USER SEES:
- Email in inbox
- Can open on any device
- Can click link
- Can copy link

WHAT IF:
- Email in spam: Instructions to check spam
- Email not received: "Resend Email" option
- User closed email: Can go to login "Need help?" link


STEP 3: Reset Password Page
──────────────────────────────

USER ARRIVES AT:
GET /reset?token=abc123def456

TOKEN VALIDATION:
- Token must be in database
- Token must not be expired
- Token must not be already used
- Associated user must exist and be active

INVALID TOKEN SHOWS:
"This link is invalid or has expired.
[Send new reset link]"

VALID TOKEN SHOWS:
┌──────────────────────────────┐
│ Set New Password             │
│ ──────────────────────────   │
│ New Password:                │
│ [____________________]       │
│                              │
│ Confirm Password:            │
│ [____________________]       │
│                              │
│ ✓ At least 8 characters     │
│ ✗ Include uppercase         │
│ ✗ Include number            │
│ ✗ Include special char      │
│                              │
│ [Reset Password]             │
│ [Cancel]                     │
└──────────────────────────────┘

USER CAN:
- Type new password
- See real-time strength indicator
- Toggle password visibility
- Submit when valid
- Cancel to go back to login

PASSWORD REQUIREMENTS:
- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 number
- At least 1 special character (!@#$%^&*)
- Cannot be same as old password
- Cannot contain username

VALIDATIONS (Real-time):
✓ Shows each requirement status
✓ Updates as user types
✓ Shows when all requirements met
✓ Color-coded: red (fail), green (pass)
✓ Submit enabled only when valid

WHAT IF:
- Empty password: Error on submit
- Passwords don't match: "Passwords do not match"
- Too weak: Show requirements
- Same as old: "Cannot reuse previous password"


STEP 4: Reset Confirmation
────────────────────────────

USER CLICKS "Reset Password":

BACKEND:
1. Validate token again
2. Hash new password
3. Update user password
4. Mark token as used
5. Invalidate all sessions (force re-login)
6. Send confirmation email
7. Log: user_id, timestamp, ip_address, success

TIMING:
- Hashing: ~500ms (bcrypt)
- Database update: ~100ms
- Email send: ~2s (async)
- Total: ~600ms

USER SEES:
✓ "Password reset successfully!"
✓ "You can now login with your new password"
✓ [Login Now] button
✓ Countdown timer (5 sec) before auto-redirect

THEN:
- Redirect to login page
- All sessions invalidated
- User must login again with new password

EMAIL SENT:
Subject: Password Changed
"Your password was recently changed. If you didn't do this, contact support immediately."


STEP 5: Alternative - "Resend Email"
──────────────────────────────────────

USER CLICKS "Resend Email" on step 1 confirmation:

VALIDATIONS:
- User not on rate limit
- Email still exists
- Account still active

BACKEND:
1. Generate new token
2. Invalidate old token
3. Set new expiry (1 hour from now)
4. Send new email
5. Log action

USER SEES:
✓ "Email sent! Check your inbox"
✓ Link to same confirmation page
✓ Can request again after 5 minutes

ERRORS:
- Rate limit: "Too many resend requests. Try again in 5 minutes"
- Email not found: "Email not found in system"
- Account disabled: "This account is not active"


ERROR SCENARIOS
────────────────

ERROR: User Clicks Link 2 Hours Later
- Token has expired
- User sees: "Link expired. [Send new reset link]"
- User must restart process

ERROR: User Clicks Link Twice
- First click: Works
- Second click: Token already used
- User sees: "Link already used. [Get new link]"

ERROR: User Resets Password, Then Another Device Tries Old Link
- Original token: Already used
- Second attempt: "Link already used"
- Security: Prevents token reuse

ERROR: Server Down During Reset
- User clicks submit
- Timeout after 30 seconds
- User sees: "Request timed out. [Retry]"
- Form data preserved
- User can retry

ERROR: Email Service Down
- Password hash succeeds
- Email send fails
- User sees: Success (email may arrive later)
- Background job retries email 5 times
- Logged for monitoring
- Notification sent to ops team

ERROR: User Resets Password While Other Session Active
- First: Password changed
- Other sessions: All invalidated
- User notified on all devices
- Must login again


EXIT POINTS
────────────

SUCCESS:
- User resets password
- User logs in with new password
- Flow complete

ABANDONMENT:
- User closes email
- User forgets token after 1 hour
- User clicks back to login
- User requests new link

ERRORS:
- Decides not to reset
- Can login from backup codes instead
- Can contact support


SECURITY CONSIDERATIONS
──────────────────────────

WHAT WE PREVENT:
- Email enumeration (don't reveal if email exists)
- Brute force (rate limit)
- Token reuse (mark as used)
- Token theft (expires after 1 hour)
- Man-in-the-middle (HTTPS only)
- Session fixation (invalidate all sessions)

WHAT WE LOG:
- All reset requests
- All successes
- All errors
- IP address (for security monitoring)
- Timestamp (for audit trail)

MONITORING:
- Alert if >10 resets/hour for user
- Alert if >100 resets/hour total
- Alert if token reuse attempted
- Alert if rate limit exceeded
```

## Data Flow Documentation

```
DATA FLOW: [Feature Name]
──────────────────────────

1. USER INPUT
   └─ Enter [data]
      Format: [type]
      Constraints: [rules]
      Storage: [temporary in form]

2. CLIENT VALIDATION
   └─ Check: [validation 1]
      Check: [validation 2]
      Status: [show user feedback]

3. TRANSMISSION
   └─ Method: POST /api/endpoint
      Payload: { … }
      Headers: [auth headers]
      Encryption: [TLS/HTTPS]

4. SERVER RECEPTION
   └─ Receive: Parse JSON
      Check: [auth token valid]
      Log: [request received]

5. SERVER VALIDATION
   └─ Check: [validation 1]
      Check: [validation 2]
      Check: [authorization]

6. DATABASE OPERATION
   └─ Query: [SQL or NoSQL]
      Transaction: [ACID properties]
      Constraints: [database rules]

7. PROCESSING
   └─ Transform: [any changes]
      Enrich: [add derived data]
      Validate: [business rules]

8. PERSISTENCE
   └─ Save to: [primary DB]
      Cache: [update cache]
      Log: [audit trail]

9. SIDE EFFECTS
   └─ Trigger: [background jobs]
      Notify: [send emails]
      Event: [emit event]

10. RESPONSE
    └─ Generate: [response data]
       Format: [JSON, XML, etc]
       Status: [200, 201, 400, etc]

11. TRANSMISSION BACK
    └─ Encrypt: [TLS/HTTPS]
        Send: [to client]

12. CLIENT RECEPTION
    └─ Receive: Parse response
       Check: [status code]
       Update: [UI state]

13. USER SEES
    └─ Display: [success/error]
       Action: [next step]
       Feedback: [confirmation]
```

## State Transition Documentation

```
STATE MACHINE: [Feature Name]
────────────────────────────────

STATES:
┌─────────────────┐
│ Empty           │  Initial state, no data
│ Loading         │  Fetching data
│ Ready           │  Data loaded, ready for action
│ Editing         │  User editing data
│ Validating      │  Checking for errors
│ Saving          │  Persisting to database
│ Saved           │  Successfully persisted
│ Error           │  Error occurred
└─────────────────┘

TRANSITIONS:
Empty → Loading: User opens page or clicks load
Loading → Ready: Data fetched successfully
Loading → Error: Fetch failed
Ready → Editing: User clicks edit button
Editing → Validating: User clicks save
Validating → Saving: Validation passed
Validating → Error: Validation failed
Saving → Saved: Save succeeded
Saving → Error: Save failed
Error → Ready: User clicks retry/refresh
Error → Editing: User fixes and retries

INVALID TRANSITIONS (Not allowed):
Editing → Saved (must go through Validating → Saving)
Loading → Editing (must go through Ready first)
Error → Saved (must retry the process)

ENTRY ACTIONS:
→ Ready: Display data, enable buttons
→ Editing: Show form, enable inputs
→ Validating: Disable buttons, show spinner
→ Saving: Show progress
→ Error: Show error message, enable retry
→ Loading: Show spinner

EXIT ACTIONS:
← Ready: Clear display updates
← Editing: Preserve or clear form
← Error: Clear error state
← Saving: Remove progress

TIMEOUTS:
Loading: 30 seconds → Error
Saving: 60 seconds → Error
Validating: 5 seconds → Error
```

## Accessibility & Performance Notes

```
ACCESSIBILITY CHECKS:
─────────────────────
□ Keyboard navigable (Tab, Enter, Escape)
□ Screen reader compatible (aria labels)
□ Color not only indicator (icons/text too)
□ Focus visible (outline/highlight)
□ Touch targets ≥ 44x44 px
□ Text contrast ≥ 4.5:1
□ Error messages associated with fields
□ Form labels present
□ Alt text for images
□ Semantic HTML structure

PERFORMANCE TARGETS:
────────────────────
□ Initial load: < 3s
□ Interaction: < 200ms
□ Data fetch: < 2s
□ Form submit: < 1s
□ Error recovery: < 500ms
□ Animation: 60 FPS

MOBILE CONSIDERATIONS:
──────────────────────
□ Touch-friendly buttons
□ Readable font size (≥ 16px)
□ Proper spacing
□ Scrollable content
□ No horizontal scroll
□ Mobile keyboard handling
□ Responsive images
```

---

**Use these templates to document comprehensive behavior during design reviews.**
