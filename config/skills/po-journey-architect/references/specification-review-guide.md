# Specification Review Reference Guide

## Validation Checklist

Use this checklist when reviewing specifications to ensure systematic coverage.

### Completeness Check

- [ ] **User Roles & Personas**: Are all actors clearly identified? (End users, admins, external systems, etc.)
- [ ] **Use Cases**: Is each user intent and outcome documented?
- [ ] **System Boundaries**: What's in scope? What's out of scope? Are integrations documented?
- [ ] **Data Flow**: What data enters? What exits? What's persisted? What's deleted?
- [ ] **Lifecycle**: Are object lifecycles documented? (Creation, updates, archival, deletion)
- [ ] **Non-functional Requirements**: Performance targets, scalability needs, security requirements, compliance constraints?
- [ ] **Accessibility & Localization**: Any special requirements?

### Clarity & Precision Check

- [ ] **Consistent Terminology**: Is each concept referred to with one name? (Not "user," "customer," "person" interchangeably)
- [ ] **Clear Ownership**: For each behavior, is it clear which system or role owns it?
- [ ] **Explicit Assumptions**: Are all "we assume..." statements called out explicitly?
- [ ] **Defined Terms**: Are vague terms like "quickly," "seamlessly," "eventually" defined precisely?
- [ ] **Acceptance Criteria**: Can you write a test that passes/fails for each requirement?

### Feasibility Check

- [ ] **Buildability**: Can this be implemented as written without builder ambiguity?
- [ ] **Dependencies**: Are all required technologies, APIs, or capabilities explicitly required?
- [ ] **Timing & Sequencing**: Are deadlines, ordering, and triggers clear?
- [ ] **Constraints**: Are resource limits, rate limits, and thresholds documented?

### Consistency Check

- [ ] **Alignment with Goals**: Do the flows serve the stated business goals?
- [ ] **Alignment within Features**: Do individual features work together without conflicts?
- [ ] **Technical Feasibility**: Are timelines and dependencies technically realistic?
- [ ] **Regulatory Compliance**: Do flows comply with stated legal/compliance requirements?

## Identifying Gaps: Patterns to Look For

### Missing Flows

**Pattern**: Happy path only. No alternatives.
**What to ask**: "You've shown me the success case. What happens when [precondition fails / user chooses differently / system error occurs]?"

**Pattern**: Multi-user scenarios with unclear ordering.
**What to ask**: "If two users try to perform this action simultaneously, what should happen?"

**Pattern**: External dependencies mentioned but not specified.
**What to ask**: "You mention 'integrating with Stripe.' What happens if Stripe is down? What's the timeout?"

### Missing Details

**Pattern**: Passive language ("the order is created") without specifying the trigger.
**What to ask**: "Who/what initiates this step? What's the exact trigger condition?"

**Pattern**: Vague user language ("the user sees feedback").
**What to ask**: "What feedback? A dialog? Toast? In-line text? How long does it persist?"

**Pattern**: Undefined error states.
**What to ask**: "For each data validation, what error message does the user see? Can they recover?"

### Unhandled Edge Cases

Look for these common blind spots:

- **Empty states**: What if there are zero items? (Search results, list pages, data tables)
- **Boundary violations**: What if the user enters the maximum character limit, maximum quantity, maximum file size?
- **Stale data**: What if the user's cached version is out of sync with the server?
- **Permissions changes**: What if the user's role changes mid-workflow?
- **Resource exhaustion**: What if we hit storage limits, API rate limits, or concurrent user limits?
- **State conflicts**: What if the system is in state A but the user's action assumes state B?

## Question Patterns for Clarity

### For Unclear Ownership

**Pattern**: "The system should validate the email."
**Precise question**: "Should this validation happen (a) on the client before submission, (b) on the backend when received, or (c) both? What's the user experience in each case?"

### For Vague Timing

**Pattern**: "Notify the user when the order ships."
**Precise question**: "Should the notification be sent (a) immediately when the status changes, (b) after confirmation from the carrier, or (c) on a schedule? What's the user expectation?"

### For Missing Failure Modes

**Pattern**: "Search returns results."
**Precise question**: "What happens if (a) no results match, (b) the search times out, (c) the service is unavailable? What does each state show?"

### For State Ambiguity

**Pattern**: "Users can edit their profile."
**Precise question**: "Can a user edit their profile while their account is suspended? If not, what message do they see? If yes, which fields?"

## Review Feedback Structure

When documenting findings, organize by severity and impact:

### Critical (Blocks Implementation)
- Issues where builders cannot proceed without clarification
- Missing core flows or undefined states
- Conflicting requirements

### High (Requires Decision)
- Ambiguous ownership or responsibility
- Missing error handling specifications
- Undefined edge cases that affect user experience

### Medium (Needs Refinement)
- Consistency improvements
- Precision improvements in language
- Clarity improvements for implementation

### Low (Nice to Have)
- Additional context or examples
- Suggested alternative approaches
- Optimization opportunities

## Common Specification Failures

### Failure 1: The Assumption Gap
**Problem**: Spec is written assuming builders know the business context.
**Symptom**: "The system should work like Shopify" without explaining which Shopify behavior.
**Fix**: Be explicit about every assumption. Call them out. Explain why they matter.

### Failure 2: The Happy Path Trap
**Problem**: Only the success case is documented.
**Symptom**: No mention of what happens when validation fails, data is missing, or users disconnect.
**Fix**: For every path, document the failure modes and recovery behavior.

### Failure 3: The Terminology Tornado
**Problem**: Same concept is called different things throughout the spec.
**Symptom**: "User" and "customer" and "account holder" used interchangeably; "delete," "remove," and "archive" unclear.
**Fix**: Create and maintain a term list. Use it consistently.

### Failure 4: The Responsibility Void
**Problem**: Who does what isn't clear. Is it the frontend? Backend? User? External service?
**Symptom**: "The data is validated" without saying where; "The user is notified" without saying how.
**Fix**: For every behavior, assign responsibility clearly. Frontend validates AND backend validates? Say it.

### Failure 5: The Concurrency Silence
**Problem**: Spec assumes single-user or linear workflows.
**Symptom**: No mention of what happens when two users act simultaneously.
**Fix**: Identify race conditions explicitly. Document the resolution strategy.
