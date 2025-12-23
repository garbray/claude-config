# Story Writing & Sprint Planning Guide

Creating great stories is a skill. This guide shows how to write stories that teams can execute efficiently.

## Story Anatomy: The Perfect Story

### Title (2-5 words, specific, verb-based)

```
✓ GOOD:
- Backend: Create favorite endpoint
- Frontend: Build favorites list page
- Testing: Implement edge case tests

✗ BAD:
- Favorites
- Feature implementation
- Stuff related to favorites
```

### Description (Why does this story exist?)

```
GOOD:
"Creates the REST API endpoint to add items to user's favorites.
Implements the 'Add Favorite' use case from the product spec.
Enables the favorite button on the content page to persist user's choice."

BAD:
"Implement favorite feature"
"Make favorites work"
```

The description answers: What does this story do? Why does it matter? How does it fit into the bigger feature?

### Technical Context (What architecture does this implement?)

```
GOOD:
"Implements the POST /users/{id}/favorites endpoint from the TDD.
Data model: Favorite(userId, itemId, itemType, createdAt).
Related endpoints: GET /users/{id}/favorites (list), DELETE /users/{id}/favorites/{id} (remove).
Rate limit: 100 requests/hour per user.
Cache invalidation: Redis cache for user's favorites cleared on add/remove."

BAD:
"Create an API"
```

This context helps engineers understand what they're implementing and why, not just what code to write.

### Acceptance Criteria (How do I know this is done?)

```
GOOD:
✓ POST /api/users/{userId}/favorites accepts JSON with itemId and itemType
✓ Valid request returns 201 Created with favorite object
✓ Response includes id, userId, itemId, itemType, createdAt fields
✓ Duplicate favorite returns 409 Conflict
✓ Missing required fields returns 400 Bad Request
✓ Unauthenticated request returns 401 Unauthorized
✓ Non-existent item returns 404 Not Found
✓ Redis cache is invalidated after adding favorite
✓ Request rate limit (100/hour) is enforced, returns 429 if exceeded
✓ Endpoint is documented in API docs

BAD:
✓ The endpoint works
✓ Tests pass
✓ Code is clean
```

Good criteria are specific and testable. Bad criteria are vague. When in doubt, make it more specific.

### Constraints (What must be true?)

```
GOOD:
- Authentication required (Bearer token, user_id from token must match path)
- Authorization: User can only add/remove their own favorites
- Rate limit: 100 requests per hour per user
- Item must exist in database (validate against Items table)
- ItemType must be one of: 'article', 'video', 'project'
- Cannot favorite same item twice (unique constraint)
- Request timeout: 3 seconds max
- Response size: < 1 KB (small payload)

BAD:
- "Must work"
- "Should be fast"
```

Constraints are the "must-haves" that frame the implementation. Be specific about what's required.

### Edge Cases / Test Expectations (What else should we test?)

```
GOOD:
HAPPY PATH:
- Valid request with all required fields → 201 Created

ERROR CASES:
- Missing itemId → 400 Bad Request
- Invalid itemType → 400 Bad Request
- Non-existent item → 404 Not Found
- Duplicate favorite → 409 Conflict
- Rate limit exceeded → 429 Too Many Requests
- Unauthenticated → 401 Unauthorized
- Wrong user trying to favorite → 403 Forbidden

EDGE CASES:
- Concurrent requests (same item from same user) → one succeeds, one returns 409
- Item deleted after favorited → favorite kept but item_id points to nothing
- Network timeout → client retries with backoff
- Very large payload → request rejected
- Empty string for itemId → 400 Bad Request
- SQL injection attempt in itemId → safely escaped

PERFORMANCE:
- Response time < 100ms (cached)
- Response time < 500ms (cold)
- Can handle 1000 concurrent requests

BAD:
- "Test thoroughly"
- "Check edge cases"
```

Edge cases are the "what if" scenarios. Be specific about what should happen.

### Dependencies

```
GOOD:
BLOCKED BY:
- Story X: "Database schema for favorites" (must create table first)

BLOCKS:
- Story Y: "Frontend favorite button" (needs API endpoint)
- Story Z: "Integration tests" (needs both frontend and backend)

RELATES TO:
- Story W: "GET /users/{id}/favorites" (same API, different method)

BAD:
- "Depends on other stuff"
```

Make dependencies explicit so sprint planning accounts for them.

### Definition of Done (What must be true before closing?)

```
✓ Code written
✓ Code reviewed by [minimum one person]
✓ Linting/formatting passed
✓ Unit tests written and passing (>80% coverage)
✓ Integration tests passing
✓ No test failures in existing tests (no regression)
✓ Deployed to staging
✓ Tested in staging environment
✓ API documentation updated
✓ [Acceptance criteria] met
✓ Tech Lead approval (optional, if high risk)
```

Definition of Done is non-negotiable. Stories aren't done until DoD is met.

---

## Story Examples: Real Implementations

### Example 1: Backend API Story

```
TITLE: Backend: POST /users/{id}/favorites endpoint

DESCRIPTION
Implements the API endpoint to add an item to user's favorites.
Users click "Save" button → frontend sends POST request → item added to database.
This enables the core "save for later" use case described in the product spec.

TECHNICAL CONTEXT
Implements the "Add Favorite" API from the Technical Design Document, section 5.
- Entity: Favorite (userId, itemId, itemType, createdAt)
- Table: favorites (id UUID, user_id UUID, item_id UUID, item_type VARCHAR, created_at TIMESTAMP)
- Related endpoints: GET /users/{id}/favorites (list), DELETE /users/{id}/favorites/{id} (remove)
- Rate limit: 100 requests/hour per user (per TDD)
- Cache: Redis cache for user's favorites list (1-hour TTL), invalidate on add/remove
- Authentication: Bearer token from HTTP Authorization header
- Authorization: User can only add to their own favorites

ACCEPTANCE CRITERIA
✓ Endpoint POST /api/users/{userId}/favorites exists and is callable
✓ Valid request (itemId, itemType) returns 201 Created
✓ Response body includes: id, userId, itemId, itemType, createdAt (per TDD example)
✓ Response content-type is application/json
✓ Required fields (itemId, itemType) present and valid → request succeeds
✓ Missing required field → 400 Bad Request with error details
✓ Invalid itemType (not in ['article', 'video', 'project']) → 400 Bad Request
✓ Non-existent item (itemId not in Items table) → 404 Not Found
✓ Duplicate favorite (user already favorited item) → 409 Conflict
✓ Unauthenticated request (no Bearer token) → 401 Unauthorized
✓ Authentication invalid/expired (bad token) → 401 Unauthorized
✓ User authorization: Token's user_id must match path's {userId} → 403 Forbidden if not
✓ Rate limit: User exceeds 100 requests/hour → 429 Too Many Requests
✓ Favorite is persisted in database (SELECT from favorites table confirms)
✓ Redis cache is invalidated (next GET request hits DB, not cache)
✓ Endpoint response time < 500ms (measured in load test)
✓ Endpoint documented in API documentation

CONSTRAINTS
- Authentication required (Bearer token)
- User can only add favorites to their own account
- ItemType must be one of exact values: 'article', 'video', 'project' (no typos, no unknowns)
- Item must exist and be owned by the user (or be public)
- Rate limit is per-user (100/hour), not per-IP
- Request timeout: 3 second maximum
- Database write must be atomic (all or nothing, no partial writes)
- No soft deletes for favorites (DELETE means remove, not mark as deleted)

EDGE CASES / TEST EXPECTATIONS
UNIT TESTS (test the function in isolation):
- testAddFavorite_ValidInput_Returns201: Call with valid data, expect 201
- testAddFavorite_MissingItemId_Returns400: Call without itemId, expect 400
- testAddFavorite_InvalidItemType_Returns400: Call with itemType='unknown', expect 400
- testAddFavorite_DuplicateFavorite_Returns409: Add same twice, second returns 409
- testAddFavorite_InvalidToken_Returns401: Call with bad token, expect 401
- testAddFavorite_WrongUser_Returns403: Token for user A trying to add to user B, expect 403

INTEGRATION TESTS (test with database and other services):
- testAddFavorite_FromEndToEnd: Full request → database write → response
- testAddFavorite_CacheInvalidation: Add favorite → verify cache cleared → next GET hits DB
- testAddFavorite_RateLimiting: Make 101 requests → 101st returns 429
- testAddFavorite_IgnoresExtraFields: Request includes extra fields → ignored, no error
- testAddFavorite_LargePayload: Request with very large itemId → still works or rejected gracefully

EDGE CASES:
- itemId is empty string "" → 400 Bad Request
- itemId is null → 400 Bad Request
- itemId exceeds max length → 400 Bad Request
- Concurrent requests (same user, same item, simultaneous) → one succeeds, one returns 409
- Item deleted between request validation and write → 404 Not Found
- User deleted between auth check and write → 403 Forbidden
- Database connection timeout → 503 Service Unavailable
- Request takes > 3 seconds → client timeout, retry
- Response exceeds memory limit → return error

PERFORMANCE:
- Average response time: 100ms (cached), 500ms (cold)
- P99 response time: < 1000ms
- Can handle 100+ concurrent requests
- Database query uses indices (user_id, created_at)

DEPENDENCY NOTES
BLOCKED BY:
- Story 1: "Database schema for favorites" (must create table before endpoint can write)

BLOCKS:
- Story 5: "Frontend favorite button" (frontend needs working endpoint)
- Story 8: "Integration tests" (tests need both backend and frontend)

RELATES TO:
- Story 3: "DELETE /users/{id}/favorites/{id}" (same API, different method)
- Story 4: "GET /users/{id}/favorites" (same API, different method)

DEFINITION OF DONE
- [ ] Code written (endpoint function, rate limiting, error handling)
- [ ] Code reviewed by [one engineer], approved
- [ ] Linting passed (eslint, prettier)
- [ ] Unit tests written, all passing
- [ ] Integration tests written, all passing
- [ ] No regression in existing tests (run full test suite)
- [ ] Built and deployed to staging environment
- [ ] Tested in staging (Postman, manual requests, load test)
- [ ] API documentation updated (endpoint path, params, response, errors)
- [ ] All acceptance criteria verified
- [ ] [Optional] Performance validated (response time < 500ms under load)

STORY POINTS: 3
ESTIMATE RATIONALE:
- Simple CRUD operation (moderate complexity)
- Clear contract in TDD (low unknowns)
- Standard rate limiting and caching patterns (known approach)
- Moderate test coverage needed (happy path + errors + edge cases)
- Total effort: ~1 day
```

### Example 2: Frontend Component Story

```
TITLE: Frontend: FavoriteButton component

DESCRIPTION
Creates the button component that users click to save items to favorites.
Button shows "Save" initially, "Saved" after clicking, with loading state during request.
Clicking saved button removes the favorite.
Users see immediate visual feedback (optimistic update) before server confirms.

TECHNICAL CONTEXT
Implements the "Favorite Button" from the UI design spec.
- Component location: /src/components/FavoriteButton.jsx
- Props: itemId (string), itemType (string), onFavoriteChange (callback)
- State management: Receives isFavorited from parent Redux store
- API calls: POST /api/users/{userId}/favorites, DELETE /api/users/{userId}/favorites/{id}
- Design system: Uses Button component from design system, Heart icon from icon library
- Styling: Tailwind CSS, respects dark mode via theme provider
- Accessibility: Keyboard accessible (Space/Enter to toggle), proper ARIA labels

ACCEPTANCE CRITERIA
✓ Component renders with initial state (unfavorited or favorited, per prop)
✓ Button text: "Save" when not favorited, "Saved" when favorited
✓ Button icon: Empty heart when not favorited, filled heart when favorited
✓ Clicking button sends appropriate API call (POST if not favorited, DELETE if favorited)
✓ While request in flight, button shows loading state (disabled, spinner)
✓ Optimistic update: UI updates immediately (before server response)
✓ Success: Button shows final state, confirms via Redux state update
✓ Error: Button shows error state, displays error message, offers retry
✓ Offline: Shows "Will save when online" message, queues action locally
✓ Accessible: Keyboard navigable (Tab), activatable (Space/Enter)
✓ Accessible: Screen reader announces "Save [item]" or "Saved, click to remove"
✓ Responsive: Works on mobile, tablet, desktop (same appearance)
✓ Dark mode: Colors adjust per theme
✓ Performance: Click to visual feedback < 100ms

CONSTRAINTS
- Must use Button component from design system (not custom button)
- Must use Heart icon from icon library (Material Icons or similar)
- Must dispatch Redux actions (not direct state mutation)
- Must handle both favorited and unfavorited states
- Must show loading state while request in flight
- Must show error state with recoverable message (not technical error)
- Must work when offline (queue action for later)
- Cannot make multiple simultaneous requests (disable button while loading)
- Must respect accessibility standards (WCAG AA)
- Must not cause layout shift (loading state same size as normal state)

EDGE CASES / TEST EXPECTATIONS
UNIT TESTS:
- testFavoriteButton_Renders_Unfavorited: Initial render, not favorited
- testFavoriteButton_Renders_Favorited: Initial render, already favorited
- testFavoriteButton_Click_CallsAPI: Click triggers POST request
- testFavoriteButton_Loading_DisablesButton: While request, button disabled
- testFavoriteButton_Success_UpdatesState: Request succeeds, Redux updates
- testFavoriteButton_Error_ShowsMessage: Request fails, error shown

INTEGRATION TESTS:
- testFavoriteButton_AddFavorite_EndToEnd: Click unfavorited button → API call → favorited
- testFavoriteButton_RemoveFavorite_EndToEnd: Click favorited button → API call → unfavorited
- testFavoriteButton_Error_AllowsRetry: Request fails → shows error → retry succeeds
- testFavoriteButton_Offline_QueuesAction: Offline → click → shows queued message
- testFavoriteButton_Loading_ConcurrentClicks: Click while loading → second click ignored

EDGE CASES:
- Offline when clicking → show "Will save when online", queue action, sync when online
- Network error on save → show error message, allow retry
- Rate limit (429) → show "Too many requests", allow retry after delay
- Permission denied (403) → show "You don't have permission" (shouldn't happen)
- Item deleted after button rendered → error on save "Item no longer exists"
- Concurrent requests → only one active at a time, disable button
- User logs out while request in flight → cancel request
- Very large itemId → gracefully handle (still works)
- Rapid click-click-click → only one request sent (debounce or disable)
- Mobile tap: two-finger tap, long-press, etc → only activate on intentional tap

PERFORMANCE:
- Initial render: < 50ms
- Click to visual feedback: < 100ms (optimistic update)
- Network request: typical 100-500ms
- Memory: no memory leaks on repeated mount/unmount

ACCESSIBILITY:
- Tab navigable: button receives focus
- Enter/Space: both activate button
- Screen reader announces: "Save article" or "Saved, press to remove"
- Keyboard visible when focused: standard focus ring
- Color not only indicator: icon fills or empties in addition to color change
- Sufficient color contrast: WCAG AA compliant

RESPONSIVE:
- Mobile: Button size suitable for touch (min 44×44px)
- Tablet/Desktop: Same visual, might be larger context
- No text wrapping: "Save" and "Saved" are same width

DEPENDENCY NOTES
BLOCKED BY:
- Backend story: "POST /api/users/{id}/favorites" (needs working API)
- Design story: "FavoriteButton design spec" (needs design from designer)

BLOCKS:
- Integration tests (needs component built)

RELATES TO:
- Frontend story: "Favorites list page" (same component might be reused there)
- Backend story: "DELETE /api/users/{id}/favorites/{id}" (used by this button)

DEFINITION OF DONE
- [ ] Component implemented per design spec
- [ ] Component stories written (Storybook for all states)
- [ ] Unit tests written and passing (>90% coverage)
- [ ] Integration tests written and passing
- [ ] Responsive tested (mobile, tablet, desktop)
- [ ] Accessibility tested (keyboard, screen reader)
- [ ] Dark mode tested
- [ ] Component doesn't cause console warnings
- [ ] Lighthouse accessibility score >= 95
- [ ] Peer review approved
- [ ] Deployed to staging and manually tested

STORY POINTS: 2
ESTIMATE RATIONALE:
- Component is straightforward (moderate complexity)
- Design is clear (low unknowns about appearance)
- API contract is clear (low unknowns about behavior)
- Standard React patterns (loading, error, success states)
- Moderate testing needed (happy path, error, offline)
- Total effort: ~1 day (code ~4 hours, tests ~2 hours, review ~1 hour)
```

### Example 3: Integration Testing Story

```
TITLE: Testing: Favorite feature end-to-end tests

DESCRIPTION
Creates comprehensive end-to-end tests for the favorites feature.
Tests the complete flow: user navigates to article → clicks save → sees favorite in list.
Tests error scenarios: network failure, permission denied, rate limit.
Ensures frontend and backend work together correctly.

TECHNICAL CONTEXT
Test framework: Playwright (end-to-end), Jest (unit)
Test scenarios:
- Happy path: Add favorite, view list, remove favorite
- Error paths: Network error, permission denied, rate limit
- Edge cases: Offline sync, concurrent requests
- Performance: Load time, responsiveness
Database setup: Test database with seed data
Users: Create test user for auth
Items: Create test articles/videos for favoriting

ACCEPTANCE CRITERIA
✓ Test suite runs and all tests pass
✓ Happy path test: user can favorite, see in list, remove
✓ Error test: network failure shows error, allows retry
✓ Error test: permission denied shows message
✓ Error test: rate limit shows appropriate message
✓ Edge case: offline favoriting queues and syncs when online
✓ Performance: favorite action completes within 3 seconds
✓ Tests are deterministic (no flaky tests, all pass consistently)
✓ Tests cover both frontend and backend together
✓ Test data cleaned up after tests run
✓ Tests run in CI/CD pipeline
✓ Coverage includes happy path, error paths, and edge cases

CONSTRAINTS
- Must test with real browser (not headless, or headless if faster)
- Must use production-like test data (realistic items, users)
- Must clean up after each test (no test pollution)
- Must not depend on external services (mock 3rd party if needed)
- Must not leave orphan data in test database
- Must run in < 5 minutes total (or break into smaller test suites)
- Each test must be independent (can run in any order)

EDGE CASES / TEST EXPECTATIONS
HAPPY PATH TESTS:
- testFavoritesFlow_AddAndRemove: Add favorite → see in list → remove → gone
- testFavoritesFlow_MultipleItems: Favorite 5 items → all appear in list
- testFavoritesFlow_Pagination: Favorite 25+ items → pagination works

ERROR TESTS:
- testFavoritesFlow_NetworkTimeout: Timeout on save → show error → retry → works
- testFavoritesFlow_PermissionDenied: Try to favorite without auth → error
- testFavoritesFlow_RateLimited: Hit rate limit → show message
- testFavoritesFlow_ItemDeleted: Favorite deleted item → error

EDGE CASE TESTS:
- testFavoritesFlow_OfflineSync: Favorite offline → sync when online
- testFavoritesFlow_ConcurrentRequests: Click twice rapidly → only one request
- testFavoritesFlow_LargeList: 1000 favorites → list still responsive
- testFavoritesFlow_CrossDeviceSync: Favorite on device A → appears on device B

PERFORMANCE TESTS:
- testFavoritesPerformance_SaveUnder1s: Save favorite < 1 second
- testFavoritesPerformance_LoadListUnder2s: Load list of 50 < 2 seconds

DEFINITION OF DONE
- [ ] Tests written and all passing
- [ ] Happy path, error, and edge cases covered
- [ ] Test data setup and cleanup works
- [ ] No flaky tests (run 10 times, all pass)
- [ ] Tests documented (describe what each test does)
- [ ] Team reviews test approach and approves
- [ ] Tests run in CI/CD
- [ ] Developers can run tests locally
- [ ] Coverage includes frontend and backend

STORY POINTS: 3
ESTIMATE RATIONALE:
- Complex: covers multiple scenarios (happy, error, edge cases)
- Test framework setup needed
- Creating test data and cleaning up
- Making tests deterministic and non-flaky
- Moderate unknowns (do tests work reliably?)
- Total effort: ~1 day
```

---

## Sprint Planning Examples

### Example Sprint Plan

```
SPRINT GOAL: Complete favorites feature MVP

TARGET VELOCITY: 16 points (based on historical 15-17 average)

PRIORITY BACKLOG (PO-prioritized):
1. Story A: Backend schema (3pt)
2. Story B: Backend POST endpoint (3pt)
3. Story C: Backend GET endpoint (2pt)
4. Story D: Frontend button (2pt)
5. Story E: Frontend list page (3pt)
6. Story F: Integration tests (3pt)
7. Story G: Performance optimization (2pt)
8. Story H: Fix bug from last sprint (1pt)

SPRINT PLANNING:
Select stories in order until hitting velocity target:

Story A (3pt): Total 3
Story B (3pt): Total 6
Story C (2pt): Total 8
Story D (2pt): Total 10
Story E (3pt): Total 13
Story F (3pt): Total 16 ← Stop here, hit target

SELECTED SPRINT STORIES (16 points):
✓ Story A: Backend schema (3pt)
✓ Story B: Backend POST endpoint (3pt)
✓ Story C: Backend GET endpoint (2pt)
✓ Story D: Frontend button (2pt)
✓ Story E: Frontend list page (3pt)
✓ Story F: Integration tests (3pt)

DEFERRED (for future sprint):
- Story G: Performance optimization
- Story H: Fix bug

DEPENDENCY ANALYSIS:
Story A (schema) → Story B (POST) → Story D (button) → Story F (tests)
                → Story C (GET)  → Story E (list)  → Story F (tests)

Critical path: A → B → E → F (3+3+3+3 = 12 points, 4 stories)
Can parallelize: C and D while B is in progress

SPRINT START:
- Day 1: Assign A to backend engineer
- Day 1: Assign B and C to backend engineer (after A done)
- Day 1: Assign D to frontend engineer
- Day 2-3: While backend works, frontend can build D
- Day 3+: Assign E to frontend engineer
- Day 4: Assign F (tests) to QA/test engineer
- End of sprint: All stories in Definition of Done

EXPECTED OUTCOME:
- All 16 points completed
- Feature is testable
- Ready for next sprint (real-time sync, offline, etc.)
```

---

## Estimation Calibration Worksheet

Use this to calibrate your team's estimates:

```
Reference Story: "Add name field to user profile"
Previous estimate: 2 points
Previous actual: 1 day (2 hours code, 2 hours test, 2 hours code review)
Status: Accurate

NEW STORY: "Create favorite button component"
Complexity vs reference: Similar structure, but more state (loading, error)
Unknowns vs reference: More unknowns (offline handling)
Testing vs reference: More testing (accessibility, responsive, multiple states)

Comparison:
- Code complexity: Similar (similar amount of code)
- Test complexity: More (more cases to test)
- Unknowns: More (offline behavior not fully specified)
- Overall: More complex than reference

Estimate: 2 points? 3 points?
→ Go with 3 points (account for extra testing and unknowns)
```

Use past stories as reference points. "This is like Story X (which was a 2) but more complex, so it's a 3."

---

## Common Story Antipatterns

### Antipattern 1: The Epic Disguised as a Story

```
❌ BAD:
"Build favorites feature"
(Includes: database, API, frontend, testing, real-time, offline, etc.)

✓ GOOD:
"Backend: Create favorite endpoints" (3pt)
"Frontend: Build favorite button" (2pt)
"Testing: Integration tests" (3pt)
(Each story is independent, small, testable)
```

### Antipattern 2: The Vague Acceptance Criteria

```
❌ BAD:
- "Favorite functionality works"
- "User can save favorites"
- "API is fast"

✓ GOOD:
- "POST /api/users/{id}/favorites returns 201 Created"
- "Response includes favorite object with id, createdAt, itemId"
- "Endpoint response time < 500ms under load"
```

### Antipattern 3: The Hidden Dependency

```
❌ BAD:
Story 1: "Frontend favorite button" (2pt)
→ Hidden dependency: Needs Story X (backend endpoint) which isn't in sprint
→ Story 1 blocked entire sprint

✓ GOOD:
Story 1: "Frontend favorite button" (2pt) — BLOCKED BY Story X
Story X: "Backend favorite endpoint" (3pt) — in same sprint
→ Explicit dependency, planned for
```

### Antipattern 4: The Estimate Guessing

```
❌ BAD:
PM: "How long will this take?"
Engineer: "Um... 3 points?"
(No discussion, no reference to past work)

✓ GOOD:
PM: "Here's the story"
Engineer: "Last time we did something similar (Story Y), it was a 3. 
This is slightly more complex (add offline support), so I'd say 5."
Other Engineer: "I agree, 5 seems right"
PM: "Approved, 5 points"
(Discussion, reference to past work, team agreement)
```

### Antipattern 5: The Over-Scoped Sprint

```
❌ BAD:
Velocity: 15 points per sprint (historical)
Sprint commitment: 25 points ("We can do it if we really push")
→ Miss sprint goal, team demoralized, velocity suffers

✓ GOOD:
Velocity: 15 points per sprint
Sprint commitment: 15 points ("We'll hit this consistently")
→ Meet sprint goal, team confident, velocity improves
```

---

## Story Writing Checklist

Before a story goes into a sprint, verify:

**Clarity**
- [ ] Title is specific and clear (verb-based)
- [ ] Description explains why this story matters
- [ ] A new engineer could read this and understand

**Completeness**
- [ ] Acceptance criteria are specific and testable (5 or fewer)
- [ ] Constraints are explicit
- [ ] Edge cases / test expectations are documented
- [ ] Dependencies are identified

**Implementation-Ready**
- [ ] No questions about what to build
- [ ] API contract is clear (from TDD)
- [ ] Data model is clear (from TDD)
- [ ] Design is clear (from design spec)
- [ ] No ambiguity about behavior

**Estimation**
- [ ] Story points assigned (1-5 only, never 8+)
- [ ] Rationale documented
- [ ] Team agrees with estimate

**Testability**
- [ ] Clear how to verify story is complete
- [ ] Acceptance criteria are testable (not "code is clean")
- [ ] Edge cases have test expectations
- [ ] Definition of Done is clear

**Value**
- [ ] Story delivers user or business value
- [ ] Or story enables other valuable stories
- [ ] Not busywork or unnecessary

---

## Sprint Success Metrics

Track these to understand sprint health:

**Velocity**: Story points completed per sprint
- Aim for consistency (±2-3 points variation acceptable)
- Trend indicates health (going up = team improving, going down = investigate why)

**Estimate Accuracy**: How well do estimates match actual?
- Target: Within ±1 point (90% of stories)
- If consistently over/under-estimating, recalibrate

**Sprint Goal Completion**: Did we achieve the sprint goal?
- Target: 90%+ completion
- If regularly missing, might be planning issue (too ambitious) or execution issue (interruptions)

**Team Happiness**: Are engineers happy?
- Clear stories? Yes or no
- Able to execute without blockers? Yes or no
- Sprint goals achievable? Yes or no

**Defect Rate**: How many bugs found post-release?
- Low defect rate = good story quality and testing
- High defect rate = stories weren't clear, or testing insufficient

---

## Key Takeaways

**Great stories enable great execution.** When stories are clear, small, and testable, engineers can move fast with confidence.

**Small is better.** 1-3 point stories can be completed quickly, tested thoroughly, and provide fast feedback.

**Clarity beats perfection.** A story doesn't have to be perfect, but it must be clear enough to code from.

**Stories are a team responsibility.** Scrum Master writes them, but team refines and estimates them together.

**Estimation improves with practice.** First few sprints estimation is rough; by sprint 10, you're consistently accurate.

**Done is non-negotiable.** Definition of Done protects quality. Don't ship stories that aren't fully done.
