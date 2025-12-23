# Failure Scenarios, Edge Cases & Recovery Patterns

Systems fail. Networks timeout. Users do unexpected things. Databases go down. Plan for these scenarios explicitly.

## Common Failure Categories

### Network Failures

**Scenario: Request Timeout**
```
Precondition: User takes action (save, submit, etc.)

What Happens:
1. Client sends request
2. No response after 3 seconds
3. Network error detected

Client Behavior:
- Show loading state during request
- After 3s timeout: show error message
- Offer retry button
- Optionally: queue action for later (offline support)

Backend Behavior:
- May or may not have received request
- Request might be processing in background
- Database change might have been applied

Recovery:
- User clicks retry
- Client sends same request again
- If original request completed: duplicate prevention (409)
- If original request failed: try again

Code Example:
fetch(url, { timeout: 3000 })
  .then(response => {
    if (response.ok) {
      // Success
    } else if (response.status === 409) {
      // Already done, show "Already saved"
    } else {
      // Error, show error message
    }
  })
  .catch(error => {
    // Network error or timeout
    // Queue for retry, show error message
  })
```

**Scenario: Slow Network**
```
Precondition: User on slow network (3G, rural, congested)

What Happens:
1. Request takes 5-10 seconds
2. User perceives slowness
3. User might click multiple times

Client Behavior:
- Show immediate loading state (reassures user)
- Disable button to prevent double-clicks
- Show progress indication if available
- Keep UI responsive despite slow network

Backend Behavior:
- Process slowly but correctly
- Ensure idempotent operations (safe to retry)

Recovery:
- Show that something is happening
- Provide realistic timeout (not 1 second on slow network)
- Allow user to cancel long-running operations
- Queue offline for true offline support

Strategy:
- Optimistic updates (show result immediately)
- Background sync (request happens behind scenes)
- Don't block UI (operation is non-blocking)
```

**Scenario: Connection Dropped**
```
Precondition: Disconnects during request (user leaves WiFi, plane mode, etc.)

What Happens:
1. Request in flight
2. Connection lost
3. Response never arrives
4. Timeout eventually
5. User comes back online

Client Behavior:
- Show offline indicator
- Queue unsent operations
- Show "Will sync when online"
- Queue any user actions

Recovery When Online:
1. Detect online status
2. Process queued operations in order
3. Implement exponential backoff if retries fail
4. Merge results (last-write-wins? merge? user chooses?)
5. Update UI with final state

Implementation:
- Detect online/offline: `navigator.onLine`
- Queue operations: IndexedDB
- Retry with backoff: exponential (1s, 2s, 4s, 8s)
- Sync on reconnect: listen for 'online' event
```

### Validation Failures

**Scenario: Invalid Input**
```
Precondition: User submits form with invalid data

What Happens:
1. User enters invalid email
2. User clicks submit
3. Validation fails

Validation Strategy:
- Real-time validation (while typing): Show help, don't block
- Submit validation (on submit): Show all errors, block submit
- Server validation: Always validate, return detailed errors

Client Behavior:
- Show error immediately (< 100ms)
- Highlight error field
- Show helpful error message
- Keep error message visible until fixed
- Disable submit button

Server Behavior:
- Validate even if client validated
- Return specific error per field
- Return HTTP 400
- Don't log failed attempt (normal user behavior)

Response Format:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Please fix the following errors",
    "details": [
      {
        "field": "email",
        "message": "Must be valid email",
        "value": "invalid-email"
      }
    ]
  }
}

User Recovery:
- Correct invalid field
- Submit again
- See success

Code Example:
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

if (!validateEmail(email)) {
  showError('email', 'Must be valid email address');
  return;
}
```

**Scenario: Duplicate Entry**
```
Precondition: User tries to create duplicate (same email, same favorite, etc.)

What Happens:
1. Uniqueness constraint defined (e.g., unique email)
2. User submits duplicate
3. Database rejects with constraint violation

Server Behavior:
- Catch constraint violation
- Detect it's a duplicate, not a real error
- Return 409 Conflict (not 500 error!)
- Explain which field is duplicate
- Suggest recovery

Response:
{
  "error": {
    "code": "DUPLICATE_ENTRY",
    "message": "This email is already registered",
    "field": "email",
    "conflictingValue": "existing@example.com"
  }
}

Client Behavior:
- Show helpful error: "Email already in use"
- Offer recovery: "Try a different email" or "Sign in instead"
- Pre-fill field if helpful

User Recovery:
- Option 1: Use different email
- Option 2: Sign in if already have account
```

### Authorization & Permission Failures

**Scenario: No Permission**
```
Precondition: User tries to access/modify resource they don't own

What Happens:
1. User A tries to delete User B's favorite
2. Backend checks authorization
3. User A owns favorite? No
4. Return 403 Forbidden

Server Behavior:
- Always check ownership before allowing modification
- Return 403, not 404 (don't leak that resource exists)
- Log attempt (potential security issue)
- Don't expose details of what failed

Response:
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You don't have permission to perform this action"
  }
}

Client Behavior:
- Hide delete/edit buttons if not owned
- Show "Not your resource" if user tries anyway
- Don't allow direct API calls to bypass UI

Security:
- Authorization must be in backend (client can't be trusted)
- Check before every operation
- Use consistent checks (don't check authorization in one place, miss it in another)

Testing:
- Test unauthorized access explicitly
- Verify 403 returned (not 500, not 200)
- Verify no operation occurred
```

**Scenario: Session Expired**
```
Precondition: User's session expires (token old, timed out, logged out elsewhere)

What Happens:
1. User performs action
2. API returns 401 Unauthorized
3. User's session is invalid
4. User needs to log in again

Server Behavior:
- Check token on every request
- Return 401 if invalid/expired
- Include hint about expiration

Response:
{
  "error": {
    "code": "AUTH_EXPIRED",
    "message": "Your session has expired. Please log in again"
  }
}

Client Behavior:
- Detect 401 response
- Clear stored auth token
- Redirect to login page
- Preserve user's location (return after login)
- Show message: "Your session has expired. Please log in again."

User Recovery:
- Redirect to login page
- User logs in
- Redirect back to original location
- Retry original action

Implementation:
- Add interceptor to catch 401
- Clear auth state
- Redirect to login
- Restore location on successful login
```

### Concurrent Modification

**Scenario: Two Users Edit Simultaneously**
```
Precondition: User A and User B both edit same resource

What Happens:
1. User A loads article
2. User B loads article
3. User A edits title, saves
4. User B edits body, saves
5. One change might be lost (last-write-wins)

Strategies:

STRATEGY 1: Last-Write-Wins (Simplest)
- No detection, no conflict
- Last change wins, earlier change lost
- Only works if conflicts rare and acceptable

STRATEGY 2: Last-Write-Wins with Notification
- Detect concurrent modifications
- Show user: "Article was updated. Your changes were saved, but others also changed it. View differences?"
- User chooses: keep mine, adopt theirs, merge

STRATEGY 3: Optimistic Locking (Version Numbers)
- Entity has version number
- User A: version 5 → version 6
- User B: tries version 5 → version 6
- User B fails: 409 Conflict
- User B must reload and retry

STRATEGY 4: Operational Transformation
- Track all changes as operations
- Merge changes mathematically
- Complex but handles concurrent edits well

Implementation (Optimistic Locking):

1. Client sends with version:
   PUT /api/articles/123
   {
     "title": "New title",
     "version": 5
   }

2. Server checks version:
   if (article.version !== 5) {
     return 409 Conflict
   }
   
3. Update and increment version:
   article.version = 6
   article.title = "New title"
   save()

4. Client handles 409:
   - Show "Article has changed"
   - Option to reload and retry
   - Option to see changes
   - Option to force update (lose their changes)

Testing:
- Simulate concurrent requests
- Verify no data loss (is either A or B's change, not merged incorrectly)
- Verify user is notified
```

**Scenario: Race Condition in State Machine**
```
Precondition: System in state A, operation assumes state B

What Happens:
1. State transitions: Draft → Published
2. Concurrent request: Draft → Archived
3. One transition succeeds, one fails
4. What's the final state?

Solution:

1. Use Transaction:
   BEGIN
   SELECT status FROM articles WHERE id = 123 FOR UPDATE
   IF status != 'Draft':
     ROLLBACK; RETURN ERROR
   UPDATE articles SET status = 'Published' WHERE id = 123
   COMMIT

2. Check on every operation:
   - What state must I be in?
   - Is precondition met?
   - Fail if not

3. Return clear error:
   {
     "error": {
       "code": "INVALID_STATE_TRANSITION",
       "message": "Cannot publish. Article is already archived",
       "currentState": "archived",
       "attemptedState": "published"
     }
   }

4. Client shows helpful message:
   - "Can't publish archived article. Unarchive first?"
   - Offer recovery action
```

### External Service Failures

**Scenario: External API is Down**
```
Precondition: Your system calls third-party API (payment, email, SMS, etc.)

What Happens:
1. Your service calls external API
2. External API returns 500 or times out
3. What do you do?

Strategy:

Option 1: FAIL FAST (simplest)
- External API down → User gets error
- User retries when service recovers
- Risk: Can't use feature at all

Option 2: GRACEFUL DEGRADATION (better)
- Feature degrades but still works
- Example: Recommendations API down → show generic recommendations
- Example: Analytics API down → no tracking, but app works

Option 3: CIRCUIT BREAKER (production)
- Track failures from external API
- After N failures in timeframe: "circuit opens"
- Stop calling external API temporarily
- Return cached response or default behavior
- Periodically test if service recovered

Implementation:

class CircuitBreaker {
  failureCount = 0;
  failureThreshold = 5;
  successThreshold = 2;
  state = 'CLOSED'; // or 'OPEN' or 'HALF_OPEN'
  lastFailureTime = null;
  timeout = 60000; // 1 minute
  
  async call(fn) {
    if (this.state === 'OPEN') {
      // Too many failures, stop trying
      if (Date.now() - this.lastFailureTime > this.timeout) {
        // Try again (HALF_OPEN)
        this.state = 'HALF_OPEN';
      } else {
        throw new Error('Circuit is OPEN');
      }
    }
    
    try {
      const result = await fn();
      if (this.state === 'HALF_OPEN') {
        // Success! Close circuit
        this.state = 'CLOSED';
        this.failureCount = 0;
      }
      return result;
    } catch (error) {
      this.failureCount++;
      this.lastFailureTime = Date.now();
      
      if (this.failureCount >= this.failureThreshold) {
        this.state = 'OPEN';
      }
      throw error;
    }
  }
}

Client Behavior:
try {
  recommendations = await getRecommendations(userId);
} catch (error) {
  // Fallback: generic recommendations
  recommendations = await getGenericRecommendations();
}

// User gets recommendations either way
```

### Data Consistency Issues

**Scenario: Partial Failure (Some Succeed, Some Fail)**
```
Precondition: Operation affects multiple entities

What Happens:
1. Create order: create order record
2. Debit account: success
3. Send confirmation email: fails
4. Part succeeded, part failed
5. System is in inconsistent state

Solution: Transactions

BEGIN TRANSACTION
  INSERT INTO orders (id, user_id, total) VALUES (...)
  UPDATE accounts SET balance = balance - amount WHERE user_id = ...
  INSERT INTO emails (user_id, type) VALUES (...)
COMMIT

If ANY step fails: ROLLBACK all steps
Either all succeed or all fail
No partial completion

If Email Service Unreliable:
- Don't include email in transaction
- Send email asynchronously, after order is created
- If email fails: retry queue, alert ops
- Don't block order creation on email

Pattern:
1. Core transaction (critical data)
2. Side effects (email, analytics, webhooks)
3. Retry failed side effects asynchronously

Client Behavior:
- If transaction fails: show error, don't show success
- If side effects fail: show success anyway (core data committed)
  - Example: "Order created. Confirmation email failed. Check spam folder."
  - Example: "Article saved. Analytics failed. We're working on it."
```

## Edge Cases

### Boundary Conditions

```
EMPTY STATE
- List with zero items
- Show helpful empty state, not blank screen
- Offer action to create first item

MAXIMUM LIMITS
- User has 10,000 favorites (exceeds display limit)
- Return paginated results
- Warn if approaching limit

VERY LONG INPUT
- User pastes 100,000 character string
- Truncate or reject with helpful error
- Document max length

SPECIAL CHARACTERS
- User enters emoji, Unicode, emoji in names
- Handle correctly or reject gracefully
- Don't crash on special characters

NULL/MISSING DATA
- Optional field not provided
- Use defaults or handle gracefully
- Document what happens

STALE DATA
- User's local copy is out of date
- Show "article was updated, reload?"
- Merge or show both versions
```

### Time-Based Edge Cases

```
TIMESTAMPS
- Timezone handling (store UTC, display local)
- Daylight saving time transitions
- Leap seconds
- Year 2038 problem (32-bit timestamps)

ORDERING
- Two items created in same millisecond
- Use tie-breaker (ID, order field)
- Guarantee consistent ordering

RETRIES WITH TIME
- User retries after 1 hour
- Original request might have succeeded
- Detect duplicates (idempotency keys)

SCHEDULED TASKS
- Retry at specific time
- Task hasn't run yet
- Task ran multiple times

RATE LIMITS
- Reset at specific time
- User just hit limit
- User can retry after reset
```

## Testing Failure Scenarios

### Unit Tests for Failures

```
test('handles timeout gracefully', async () => {
  const timeout = new Promise((_, reject) => 
    setTimeout(() => reject(new Error('Timeout')), 3000)
  );
  
  try {
    await timeout;
  } catch (error) {
    expect(error.message).toBe('Timeout');
    // App should show error, allow retry
  }
});

test('detects duplicate entry', async () => {
  const duplicate = await createFavorite(userId, itemId);
  
  const response = await createFavorite(userId, itemId);
  
  expect(response.status).toBe(409);
  expect(response.body.code).toBe('DUPLICATE_ENTRY');
});

test('authorization check prevents access', async () => {
  const userA_favorite = await createFavorite(userAId, itemId);
  
  const response = await deleteFavorite(userBId, userA_favorite.id);
  
  expect(response.status).toBe(403);
  expect(response.body.code).toBe('FORBIDDEN');
});
```

### Integration Tests for Failures

```
test('recovers from network timeout', async () => {
  // Simulate network delay
  mockApi.delayResponse(5000);
  
  // User clicks button
  const action = favoriteItem(itemId);
  
  // Request times out
  await delay(3000);
  expect(showError).toBeCalledWith('Network timeout');
  
  // User retries
  mockApi.delayResponse(0);
  const retry = favoriteItem(itemId);
  
  // Should succeed
  await expect(retry).resolves.toBeTruthy();
});

test('handles offline gracefully', async () => {
  // Simulate offline
  navigator.onLine = false;
  
  // User clicks button
  const action = favoriteItem(itemId);
  
  // Action queued, not immediately succeeded
  expect(getQueue().length).toBe(1);
  expect(showMessage).toBeCalledWith('Will sync when online');
  
  // User comes online
  navigator.onLine = true;
  window.dispatchEvent(new Event('online'));
  
  // Queue processes
  await delay(1000);
  expect(getQueue().length).toBe(0);
});
```

## Monitoring Failure Scenarios

After launching, monitor for failures:

```
Metrics to Track:
- API error rate (target: < 1%)
- Timeout rate (target: < 0.1%)
- 4xx errors by type (validation, auth, not found)
- 5xx errors (server errors)
- Network failures (timeouts, dropped connections)
- External service failure rates

Alerts:
- Error rate > 1% → page on-call engineer
- Timeout rate > 0.1% → investigate performance
- 503 from external service → escalate
- Duplicate entry errors increasing → data quality issue

Recovery:
- Monitor for recovery time
- Alert if recovery takes > 5 minutes
- Auto-failover to backup service
- Graceful degradation if recovery slow
```
