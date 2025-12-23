# High-Impact Clarifying Questions Guide

This guide provides question patterns organized by scenario. Use these as templates to craft precise questions that unblock decisions and reduce ambiguity.

## Question Principles

**Good clarifying questions**:
- Reference specific parts of the spec, not abstract concepts
- Offer 2-3 concrete options when helpful
- Explain why the answer matters ("This affects whether...")
- Drive toward a specific, testable decision
- Are open-ended, not yes/no (unless a binary decision is truly needed)

**Weak questions**:
- "Tell me more about..." (too vague)
- "What about error handling?" (too broad)
- "Is this okay?" (yes/no, doesn't advance clarity)
- Make assumptions ("Should we use Redis for...?" when the store isn't decided)

## Question Patterns by Scenario

### Scenario 1: Unclear Ownership or Responsibility

**Problem**: "The user is notified," "the data is validated," "the order is created" without saying who/what does it.

**Precise question template**:
"You say [behavior]. Should [responsible party] do this on [client/server/both], and what are the implications?"

**Example questions**:
- "You say email validation happens. Should this be (a) client-side only for speed, (b) server-side only for security, or (c) both? This affects whether invalid emails briefly appear in the UI."
- "You mention the profile picture is resized. Should this happen (a) in the browser before upload, (b) on the backend after upload, or (c) both? This affects file size, bandwidth, and user experience on slow connections."
- "The system should check for duplicates. Should this validation happen (a) while the user is typing, (b) on submit, (c) on the backend? Each has different UX trade-offs."

### Scenario 2: Vague Timing or Sequencing

**Problem**: "Eventually," "immediately," "after," "once" without precision.

**Precise question template**:
"Should [event 1] happen [before/after/simultaneously with] [event 2], and what happens if [event 2] completes first?"

**Example questions**:
- "Should the order confirmation be shown to the user (a) before the payment is fully processed, (b) after payment succeeds, or (c) after the order is created in inventory? This affects whether users see a loading state and how disconnects are handled."
- "When a user uploads a file, should the progress bar show (a) upload progress only, (b) upload + processing, or (c) wait until processing is done before allowing the user to proceed? What if processing takes longer than upload?"
- "Should the email be sent (a) the instant the action completes, (b) after a delay (batching), or (c) only on a schedule? This affects bounce rates and user experience for time-sensitive actions."

### Scenario 3: Missing Failure Modes

**Problem**: Spec describes the success case but not what happens when it fails.

**Precise question template**:
"When [precondition] fails or [error event] occurs, should the system (a) [option 1], (b) [option 2], or (c) [option 3]? What does the user see?"

**Example questions**:
- "If the payment processing times out, should we (a) charge the user and ask them to verify later, (b) not charge and ask them to retry, or (c) charge with a 30-minute delay buffer? How does each affect trust?"
- "If two users edit the same document simultaneously, should the system (a) lock it for the second user, (b) merge changes automatically, or (c) warn of conflicts? What's the consequence of each?"
- "If the user's session expires while they're filling out a form, should we (a) save a draft, (b) clear the form for security, or (c) require re-authentication and restore the form? What's the privacy vs. convenience trade-off?"

### Scenario 4: Unhandled Edge Cases

**Problem**: Boundary conditions, empty states, or unusual inputs aren't documented.

**Precise question template**:
"What happens when [edge case]? Should the system [behavior]?"

**Example questions**:
- "What if a user enters 10,000 characters in a field with a 100-character limit? Do we (a) enforce on client-side only, (b) truncate on server, (c) show an error? What's the UX?"
- "What if search returns zero results? Do we show (a) an empty state, (b) a 'no results' message with suggestions, (c) previous search results?"
- "What if the user's role changes while they're in the middle of a workflow? Should we (a) complete the action with their old permissions, (b) cancel and ask them to restart, (c) update permissions mid-workflow?"
- "What if an item is deleted while someone is viewing it? Should they see (a) an error, (b) a 'this item was deleted' message, (c) be redirected?"

### Scenario 5: Undefined States

**Problem**: An entity can be in a state, but it's unclear what can happen in that state.

**Precise question template**:
"When something is in [state], can the user/system [action]? If yes, what's the outcome? If no, what message do they see?"

**Example questions**:
- "Can a user edit their profile while their account is suspended? If yes, which fields? If no, what message do they see?"
- "Can a user cancel an order that's already shipped? If yes, what are the refund implications? If no, what option do we show them?"
- "Can an admin delete a user who has active sessions? If yes, are their sessions terminated immediately? If no, what message do they see?"

### Scenario 6: Ambiguous Acceptance Criteria

**Problem**: Success criteria are subjective ("fast," "seamless," "works well").

**Precise question template**:
"How do we measure [criteria]? Is success [quantifiable metric]?"

**Example questions**:
- "You mention the page should load 'quickly.' Is success (a) < 1s, (b) < 2s, (c) < 5s? Does it vary by network condition?"
- "The search should return 'relevant' results. Does that mean (a) exact keyword match, (b) semantic match, (c) ranked by popularity? What's the fallback if we can't find anything?"
- "You want the payment to be 'seamless.' Does that mean (a) one-click, (b) minimal form fields, (c) pre-filled data? What's acceptable friction?"

### Scenario 7: Missing Integrations or Dependencies

**Problem**: External systems are mentioned but not fully specified.

**Precise question template**:
"You mention [external system]. What happens if it's [unavailable/slow/returns unexpected data]?"

**Example questions**:
- "You mention we integrate with Stripe for payments. What's our behavior if Stripe is down? Do we (a) show an error immediately, (b) queue the payment for later, (c) use a fallback payment method?"
- "You reference a 'third-party shipping API.' What if it doesn't have rate information for a given address? Do we (a) show an error, (b) use estimated rates, (c) not allow checkout?"
- "The notification service has a 99.9% SLA. What's our expected behavior for that 0.1% downtime? Should users still complete actions?"

### Scenario 8: Conflicting Requirements

**Problem**: Two parts of the spec seem to contradict.

**Precise question template**:
"In section [X], you say [statement 1]. In section [Y], you say [statement 2]. These seem to conflict when [scenario]. Which takes priority?"

**Example questions**:
- "You state users must verify their email before accessing content (section 2), but also that guest users can view public content without signup (section 5). Do anonymous users bypass email verification?"
- "You mention fast API response times (section 3), but also batch operations for efficiency (section 7). If a user performs a bulk action, do we respond immediately or after processing completes?"
- "You require role-based access control (security section), but also want seamless sharing (collaboration section). Can a user with 'view' permission share a document with 'edit' permission?"

## Domain-Specific Question Sets

### For Payments & Transactions

- What's the happy path for a successful payment? (Processing, confirmation, receipt)
- What happens if authorization succeeds but settlement fails?
- Can a user retry a failed payment immediately, or is there a cooldown?
- How long do we retry a failed payment before giving up?
- What's the user experience during processing (loading state, estimated time)?
- How do we handle partial refunds or disputed charges?
- Are payment details saved? If yes, how securely? Can users manage saved methods?

### For User Authentication & Authorization

- Can a user be in multiple roles simultaneously?
- Can permissions change mid-workflow? How do we handle that?
- What happens if a user's permissions are revoked while they're using the system?
- Is there a session timeout? What happens when it expires?
- Can an admin impersonate a user? What are the audit implications?
- What happens if a user is logged in on multiple devices?

### For Data & Content

- Can data be edited after creation? If yes, by whom, and is there an audit trail?
- How long is deleted data kept? Is it recoverable?
- Can users export their data? In what formats?
- What's the maximum data size or usage per user?
- Is there versioning or rollback capability?
- How is data synchronized across devices or sessions?

### For Notifications & Communication

- What's the channel? (Email, SMS, in-app, push)
- Is notification optional or mandatory?
- Can users control notification frequency or preferences?
- What if notification fails (bounce, undeliverable)? Do we retry?
- Is there a digest/batching strategy?
- What's the timing? (Real-time, batched, on-demand)

### For Multi-User Collaboration

- Can two users edit the same resource simultaneously?
- How do we resolve conflicts? (Last write wins, merge, lock, version)
- Is there real-time collaboration or eventual consistency?
- Can a user see others' changes instantly?
- What permissions do collaborators need?

## Using This Guide

When reviewing a specification or designing a flow:

1. **Identify the scenario** that applies: ownership, timing, failure, edge case, etc.
2. **Pick the relevant question pattern**
3. **Customize it** for your specific context (replace placeholders)
4. **Add context**: Explain why this matters for implementation
5. **Offer options** when helpful to guide thinking
6. **Prioritize questions** by impact: What decision blocks the most work?

Group related questions together and ask them in conversation rather than as a list. This maintains engagement and allows follow-up based on answers.
