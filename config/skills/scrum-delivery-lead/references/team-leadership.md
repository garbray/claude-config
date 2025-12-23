# Story Validation & Team Leadership Guide

As a technical Scrum Master, you're not just writing stories—you're coaching a team to execute with excellence. This guide covers validating stories, developing your team, and maintaining delivery quality.

## Story Validation Checklist

Before a story enters a sprint, validate it meets all criteria:

### Clarity Check

- [ ] **Title is specific**: Not "Favorites" but "Backend: POST /favorites endpoint"
- [ ] **Anyone on team can read and understand**: No jargon, clear language
- [ ] **No ambiguity about what to build**: Reader knows exactly what's being built
- [ ] **Why it matters is clear**: Why is this story important?
- [ ] **Success is obvious**: "Done" is clear, not subjective

### Completeness Check

- [ ] **Acceptance criteria are specific**: "User can click button" → "Click button, see POST request sent, see success message"
- [ ] **All error cases documented**: Not just happy path
- [ ] **Edge cases identified**: What unusual scenarios should we handle?
- [ ] **Test expectations defined**: What tests should exist?
- [ ] **Dependencies explicit**: What blocks this? What does this block?

### Technical Check

- [ ] **API contract matches TDD**: If API story, does it match Technical Design Document?
- [ ] **Data model is clear**: What fields? What types? What constraints?
- [ ] **Implementation approach is reasonable**: Not asking for impossible things
- [ ] **No hidden complexity**: Unknowns are flagged, not hidden
- [ ] **Constraints are realistic**: Rate limits, performance, etc. are achievable

### Design Check (if UI story)

- [ ] **Story matches design spec**: Is the UI exactly as designed?
- [ ] **Responsive design included**: Mobile, tablet, desktop all specified?
- [ ] **Accessibility included**: Keyboard nav, ARIA labels, contrast?
- [ ] **All component states included**: Loading, error, success, empty, etc.?
- [ ] **Micro-interactions included**: Transitions, animations, feedback?

### Estimation Check

- [ ] **Size is 1-5 points**: Never estimate 8+ (break down further)
- [ ] **Team agrees**: Estimation isn't unilateral (team discusses, agrees)
- [ ] **Rationale documented**: Why this size? What's it compared to?
- [ ] **Reasonable for 1 engineer**: Can one person complete in 1-2 days?
- [ ] **Consistent with past stories**: Similar complexity should get similar size

### Definition of Done Check

- [ ] **DoD is explicit**: What does "done" mean for this story?
- [ ] **DoD is testable**: Can you verify each criterion was met?
- [ ] **DoD includes code review**: Minimum one review before merging
- [ ] **DoD includes testing**: Unit tests, integration tests, edge cases
- [ ] **DoD includes quality checks**: No console errors, linting passes, performance ok

### Story Ready Checklist

Story is ready for sprint when:
- [ ] Title is clear and specific
- [ ] Description explains context and value
- [ ] Acceptance criteria are detailed (3-5 criteria)
- [ ] Edge cases / test expectations defined
- [ ] Dependencies are explicit
- [ ] Estimated (1-5 points, team agreed)
- [ ] Definition of Done is clear
- [ ] Design and PM approved (if relevant)
- [ ] No questions from team

---

## Developing Your Team

As a technical Scrum Master, you develop people. Here's how:

### Coaching Better Estimation

**Early in team formation**:
- Estimation is guessing
- Variance is high (some 2-pointers, turn out to be 5-pointers)
- Team learning what accuracy feels like

**After 5-10 sprints**:
- Estimation stabilizes
- Team knows "what a 3-pointer feels like"
- Variance decreases

**Your job**:
- Reference past work: "Story X was a 3, this is similar, so it's also a 3"
- Discuss outliers: "Why do you think this is an 8? Is there something unknown?"
- Validate estimates: "Does the team agree?" (don't let one person estimate alone)
- Track accuracy: "We estimated 3, actual was 5. Why? Let's learn for next time."

### Coaching Clearer Writing

**Early**: Stories are vague, ambiguous, missing context
**Your job**: Model excellent stories, review and improve stories together

**Example Coaching**:
```
Engineer writes: "Create favorite button"

You: "Good start. Let's make it clearer.
What does 'create' mean specifically?
Does it mean:
  a) Build React component from scratch?
  b) Create component + integrate with Redux?
  c) Create component + API integration?
  d) All of above?

Let's rewrite: 'Frontend: FavoriteButton component with Redux integration'

Also, the acceptance criteria: 'Button works' is vague.
What does 'works' mean? Let's be specific:
- User can click button
- Button shows loading state while request in flight
- Success shows 'Saved' text
- Error shows error message and retry button
- Offline shows 'will save when online' message"

Engineer learns: Be specific, not vague
```

### Coaching Better Testing

**Early**: Engineers skip edge cases, don't test errors
**Your job**: Help them understand test value

**Example Coaching**:
```
Engineer: "Story is done. Tests pass, happy path works."

You: "Great. Let's review the test expectations from the story:
✓ Happy path: covered
✓ User not authenticated: did you test 401?
✓ Rate limit exceeded: did you test 429?
✓ Network timeout: did you test retry?
✓ Concurrent requests: did you test two simultaneous clicks?

Let's add tests for these cases. Here's why:
- 401 case: real users without auth token will hit this
- 429 case: real users hitting rate limit will see this
- Timeout: real users with slow networks will experience this
- Concurrent: mobile users might double-tap

Without these tests, we ship broken code that real users will hit.
That's why test coverage matters."

Engineer learns: Edge cases and error cases are as important as happy path
```

### Coaching Collaboration

**Early**: Engineers work in silos, don't ask for help
**Your job**: Encourage pairing, knowledge sharing, communication

**Example Coaching**:
```
Engineer A working on Story X (complex API design)
Engineer B about to start Story Y (frontend integration with Story X API)

You: "B, before you start, let's pair with A for 30 minutes.
A can explain the API design, you ask questions early.
This prevents misalignment later."

Result: 30 minutes now prevents 2 days of rework later.
Both engineers learn: Invest in communication upfront.
```

### Coaching Code Quality

**Model excellence**: Code review fairly, point out issues constructively

**Example Code Review**:
```
Engineer submits PR with issue

BAD FEEDBACK:
"This is bad code."

GOOD FEEDBACK:
"This function is doing 3 things (parse request, validate, save to DB).
Can we split it into 3 functions?
Each function would be easier to test and reuse.
Here's an example of how I'd refactor this..."

Engineer learns: How to write better code, not just what was wrong
```

---

## Managing Difficult Situations

### Situation: Engineer Says Story is Too Big

**Engineer**: "This story is a 5, but it's too much for me to do in 2 days"

**Response**:
- "Let's break it down. What's the biggest chunk?"
- "Can we do the happy path in the first story, edge cases in a second story?"
- "Let's make two 3-pointers instead of one 5-pointer"

**Outcome**: Stories that fit in sprints, engineer confident

### Situation: Story Takes Longer Than Estimated

**Engineer**: "I estimated 3 points but I'm at hour 20 and not done"

**Response** (don't panic, don't blame):
- "What's the blocker?"
  - If technical: help unblock
  - If unknown complexity: acknowledge learning
  - If wrong estimation: that's okay, we learn for next time
- "What's left?"
  - Can the remaining work be a separate story?
  - Can we "done-ish" this one and finish next sprint?
- "Next time we know this type of work is bigger. We'll estimate differently"

**Don't**:
- Blame engineer ("You should have estimated better")
- Push to finish tonight ("Just power through")
- Make them feel bad ("This is embarrassing")

**Do**:
- Unblock them
- Learn from miss
- Help them complete or defer gracefully

### Situation: Too Many Incomplete Stories

**At sprint review**: 5 stories started, only 2 completed

**Diagnosis**:
- Stories too big? (Break down)
- Team distracted? (Protect from interrupts)
- Team stuck? (Unblock them)
- Not working together? (Pair engineers)

**Action**:
- Next sprint: smaller stories (1-2pt), don't take on so many
- Next sprint: pair engineers to unblock faster
- Next sprint: protect from interrupts

**Don't blame team. Diagnose root cause, fix process.**

### Situation: Team Disagrees on Estimation

**You propose**: Story is 3 points
**Engineer A**: "No, that's 5 at least"
**Engineer B**: "I think it's 2, it's straightforward"

**Response**:
- Listen to each perspective
- Ask questions: "What makes you think it's 5?" vs "What makes you think it's 2?"
- If unknowns exist: do a spike story (1-2pt) to investigate
- If no unknowns: decide as a team
- Example: "I hear the unknowns about X. Let's estimate 5 to be safe. If it's easier, great. If it's as complex, we were right."

**Key**: Estimation is discussion, not votes. Everyone's perspective matters.

### Situation: Quality Slipping

**Symptoms**: More bugs in staging, test coverage dropping, engineers cutting corners

**Root cause analysis**:
- Pressure? ("Meet the deadline at any cost")
- Velocity too high? ("We're over-committing")
- Morale issue? ("No one cares")
- Skills gap? ("We don't know how to test this")

**Response**:
- Address root cause, not symptoms
- If pressure: reset expectations, commit to lower velocity
- If over-committed: reduce commitment, finish fewer stories
- If morale: address what's wrong (ask team)
- If skills: train team, pair for learning

**Quality isn't negotiable. Fix the process, not the symptoms.**

---

## Building Trust With Your Team

Trust is earned. Here's how:

### Be Honest

```
✓ Good:
"That deadline is unrealistic. We can do 15 points per sprint.
That feature is 40 points. That's 3 sprints minimum.
We can commit to 2.5 sprints (stretch) but not faster."

✗ Bad:
"Sure, we can do it in 1 sprint" (knowing it's impossible)
→ Team fails
→ Team loses trust
```

### Protect the Team

```
✓ Good:
PM: "Can you also do Story X mid-sprint?"
You: "No. We have a commitment. Story X goes on backlog for next sprint."
→ Team focuses on sprint goal
→ Team delivers on commitment

✗ Bad:
You: "Sure, we'll do it" (mid-sprint scope change)
→ Team context-switches
→ Story commitments fail
→ Team trusts you less
```

### Unblock Quickly

```
✓ Good:
Engineer: "I'm blocked on X"
You: "Let's solve this now" (within hours)
→ Engineer gets unblocked
→ Work continues

✗ Bad:
Engineer: "I'm blocked on X"
You: "We'll deal with it next week"
→ Engineer waits
→ Sprint velocity suffers
```

### Celebrate Wins

```
✓ Good:
Sprint ends, all stories done
You: "Great work team. You delivered exactly what you committed to.
That's consistency. That's excellence. Great job."
→ Team feels accomplished

✗ Bad:
Sprint ends, all stories done
You: "Moving on to next sprint..."
→ No recognition
→ Motivation drops
```

### Learn From Mistakes

```
✓ Good:
Sprint review: story failed
You: "What happened? Let's understand. Not to blame anyone,
but to learn. What will we do differently next time?"
→ Team learns
→ Team trusts you won't blame them

✗ Bad:
Sprint review: story failed
You: "Why did you mess this up?"
→ Blame, not learning
→ Team defensive
```

---

## Maintaining Delivery Excellence

Excellence is a practice, not a destination. Here's how to maintain it:

### Weekly Rituals

**Monday 9am**: Sprint planning / Refinement
- New stories ready for sprint
- Team knows what's coming
- Goal is clear

**Daily 10am**: Standup (15 min)
- Synced on progress
- Blockers identified and addressed
- Team aligned

**Friday 4pm**: Sprint closing (if needed)
- Stories completed, reviewed, merged
- Sprint metrics tracked (velocity, cycle time, etc)
- Team winds down with clarity

### Monthly Rituals

**Sprint Review** (Friday, every 2 weeks)
- Show progress to stakeholders
- Get feedback
- Celebrate wins

**Sprint Retro** (Friday, every 2 weeks)
- Team reflects on process
- Identify 1-2 improvements
- Commit to changes

**Backlog Refinement** (Thursday, every 2 weeks)
- Next sprint's backlog prepared
- Stories estimated
- No surprises on Monday

### Quarterly Rituals

**Team health check**
- Are people happy?
- Is quality good?
- Is velocity stable?
- What's not working?

**Skills assessment**
- What skills is team missing?
- What training would help?
- Are people growing?

**Process review**
- Is Scrum working for us?
- What's working well?
- What should we change?

---

## Leadership Principles

As a technical Scrum Master, adopt these principles:

**1. Serve the Team**
You're not above the team, you're there to help them succeed.
Unblock, coach, remove obstacles.

**2. Facilitate, Don't Command**
You don't tell people what to do.
You help them figure out what needs doing, and how to do it well.

**3. Continuous Improvement**
Each sprint, each month, each quarter: get better.
Small improvements compound.

**4. Quality First**
Velocity matters, but quality is non-negotiable.
A fast team that ships bugs is a slow team.

**5. People First**
The team is people. Treat them well.
Happy, healthy teams deliver.

---

## Key Reminders

**You don't know everything.** Ask the team. They're smart.

**Your best tool is curiosity.** "Why?" more than "Do this."

**Celebrate small wins.** Day-to-day excellence is built incrementally.

**Protect your team.** They need focus. Give them focus.

**Be honest about capacity.** "No, we can't do that" is stronger than false commitment.

**Lead by example.** If you care about quality, they will too.

**Remember: Great teams deliver great products. Your job is building great teams.**
