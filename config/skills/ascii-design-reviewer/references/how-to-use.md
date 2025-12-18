# How to Use ASCII Design Reviewer

A practical guide for product owners and stakeholders reviewing Phase 1 ASCII designs.

## Quick Start

### What You Need
- An approved ASCII design from Phase 1
- Understanding of the feature's purpose
- Time to answer clarifying questions

### What You'll Get
- Critical questions to answer
- Mermaid diagrams (flowcharts, sequences, state charts)
- Step-by-step behavior documentation
- Comprehensive error handling plan
- Recommendations and improvements

## Three Ways to Use This Skill

### Way 1: Quick Review (15 minutes)

**Use when**: You need fast feedback on a design

**Request**:
```
"Please review this ASCII design quickly:

[Paste ASCII]

Key questions:
1. Are all user paths shown?
2. What's missing?
3. Any concerns?"
```

**You get**:
- Critical questions (3-5)
- Major gaps identified
- Quick recommendations

### Way 2: Comprehensive Review (1 hour)

**Use when**: Design is important, need thorough analysis

**Request**:
```
"Please provide a comprehensive review of this design:

Design Context:
- Feature: [What is it?]
- Users: [Who uses it?]
- Goal: [What problem does it solve?]
- Constraints: [Any limitations?]

Design:
[Paste ASCII]

Please provide:
1. Critical questions
2. User journey flowchart
3. Sequence diagrams
4. State chart
5. Error handling plan
6. Recommendations"
```

**You get**:
- All the above
- Complete documentation
- Ready for implementation

### Way 3: Expert Review (2 hours)

**Use when**: Complex feature, want expert guidance

**Request**:
```
"As an expert reviewer, please deep-dive this design:

Feature: [Name]
Users: [Description]
Context: [Business context]
Constraints: [Technical/business]

Design:
[Paste ASCII]

Special focus on:
1. [Your biggest concern]
2. [Your biggest question]
3. [What you're uncertain about]

Please provide complete analysis including:
- Questions
- All diagrams
- Full behavior documentation
- Error scenarios (at least 10)
- Edge cases
- Security considerations
- Performance implications
- Recommendations"
```

**You get**:
- Deep expert analysis
- Comprehensive documentation
- Ready for implementation + security review

## Step-by-Step Review Process

### Step 1: Prepare the Design

Before requesting review, make sure:
- ✓ ASCII design is finalized
- ✓ All sections are clear
- ✓ All interactions are marked
- ✓ Design is properly formatted
- ✓ You understand the feature goal

### Step 2: Provide Context

Always include:
- **Feature name**: What is this?
- **User description**: Who uses it?
- **Problem solved**: Why do they need it?
- **Constraints**: Any limitations?
- **Your questions**: What are you unsure about?

### Step 3: Request Review

Paste your request with:
- Context information
- ASCII design
- Specific focus areas (if any)
- Your known concerns

### Step 4: Receive Diagrams

You'll get Mermaid diagrams:
- **Flowchart**: All possible user paths
- **Sequence diagram**: Step-by-step interactions
- **State chart**: System states and transitions
- **Data flow**: Where data goes

### Step 5: Review Behavior Documentation

Read detailed documentation:
- What happens at each step
- What users see
- What the system does
- What validations apply
- What data flows

### Step 6: Review Error Handling

Understand error scenarios:
- What can go wrong
- How to detect it
- How to recover
- How to prevent it

### Step 7: Review Recommendations

Consider suggestions:
- Design improvements
- Missing features
- Security concerns
- Performance implications
- Accessibility issues

### Step 8: Iterate if Needed

If issues found:
- Go back to Phase 1
- Refine the ASCII design
- Request another review
- Iterate until design is solid

### Step 9: Approve & Move Forward

When design passes review:
- Mark as "Approved"
- Move to Phase 2 (Implementation)
- Use review as specification
- Build with confidence

## Example: Review a Simple Feature

### Feature: Email Verification

**ASCII Design**:
```
┌──────────────────────────────┐
│ Verify Your Email            │
│                              │
│ We sent a link to:           │
│ john@example.com             │
│                              │
│ Enter verification code:     │
│ [○ ○ ○ ○ ○ ○]              │
│                              │
│ [Verify] [Resend] [Change]  │
│                              │
└──────────────────────────────┘
```

**Request**:
```
"Please review this email verification design.

Context:
- Feature: Email verification for signup
- Users: New users during signup
- Goal: Verify user owns the email
- Constraints: Must be secure, simple

Questions:
1. What happens if user never receives email?
2. How long is code valid?
3. What if user tries wrong code?
4. Can user change email?

Design: [ASCII above]"
```

**You might get back**:
- Questions about code expiry
- Questions about rate limiting
- Flowchart showing all paths
- Sequence diagram showing backend flow
- State chart showing states
- Error handling for 10+ scenarios
- Recommendations

**Then you can**:
- Answer the questions
- Get clarity on unknowns
- Move to implementation
- Build with confidence

## Review Template

Copy and use this template:

```
DESIGN REVIEW REQUEST
─────────────────────

FEATURE: [Feature name]

USERS: [Who uses this?]

PROBLEM: [What does it solve?]

CONTEXT: [Business context, constraints]

ASCII DESIGN:
[Paste your design]

QUESTIONS FOR REVIEWER:
1. [Your question 1]
2. [Your question 2]
3. [Your question 3]

MY CONCERNS:
- [Concern 1]
- [Concern 2]

PLEASE PROVIDE:
□ Critical questions to answer
□ User journey flowchart
□ Sequence diagram of key interaction
□ State chart
□ Behavior documentation for steps:
  □ Step 1: [name]
  □ Step 2: [name]
  □ Step 3: [name]
□ Error handling for:
  □ [Error scenario 1]
  □ [Error scenario 2]
  □ [Error scenario 3]
□ Recommendations
□ Missing requirements
```

## Common Questions During Review

### About the Diagrams

**Q: Why do I need a flowchart if I have the ASCII?**
A: Flowchart shows all possible paths including errors. ASCII shows one happy path.

**Q: What's a sequence diagram?**
A: Shows step-by-step what happens between user, frontend, backend, database.

**Q: What does state chart show?**
A: All valid states and how you move between them (important for complex features).

### About Errors

**Q: Why plan for errors if it usually works?**
A: Planning now prevents bad UX and data loss later. Easy to plan, hard to fix after.

**Q: Should I handle every possible error?**
A: No, focus on likely ones (network errors, validation, timeouts, permissions).

**Q: How many error scenarios?**
A: Usually 5-15 depending on complexity. More for financial/critical features.

### About Implementation

**Q: Can I skip the review and go straight to Phase 2?**
A: You can, but you'll likely hit more unknowns during coding. Review saves time.

**Q: When is design "good enough" for implementation?**
A: When: all questions answered, all paths documented, all errors planned, team aligned.

**Q: Should developers see this review?**
A: Yes! This review becomes the spec. Developers use it to understand what to build.

## Collaboration Workflow

### Product Owner → Designer
```
"Here's feedback on your ASCII design:
[Feedback from review]

Please update the design to address these issues"
```

### Designer → Product Owner
```
"I updated the design based on feedback:
[New ASCII]

Ready for another review?"
```

### Product Owner → Engineering
```
"Design is approved. Here's the review documentation:
[Complete review with diagrams]

Use this as your specification.
Questions? Let me know."
```

### Engineering → Product Owner
```
"Building this. Found ambiguity in:
[Specific scenario]

Should we [option A] or [option B]?"
```

**Product Owner responds** (using review as reference):
```
"Looking at the state chart, we should [option].
Because [reason from review]"
```

## Review Checklist

Before approving a design, verify:

✓ User goals understood
✓ User paths complete
✓ Entry/exit points clear
✓ All interactions defined
✓ Data flow documented
✓ Error scenarios covered
✓ State transitions valid
✓ Performance considered
✓ Security addressed
✓ Accessibility planned
✓ Team aligned
✓ Ready for implementation

## Red Flags During Review

Watch for:

🚩 **"I'm not sure what happens if..."**
→ This scenario must be designed

🚩 **"It depends on..."**
→ Get specifics before proceeding

🚩 **"Users will figure it out"**
→ Design should be clear, not confusing

🚩 **"We'll handle this in code"**
→ Design now, easier than coding later

🚩 **"No one needs to worry about..."**
→ Every error scenario matters for UX

🚩 **Conflicting opinions**
→ Review is the spec - use it to align

## Next Steps After Review

### If design is approved:
1. ✓ Mark review as "Approved"
2. ✓ Share with engineering team
3. ✓ Move to Phase 2 (Implementation)
4. ✓ Use review as specification
5. ✓ Build the feature

### If issues found:
1. ⚠ Note specific issues
2. ⚠ Go back to Phase 1
3. ⚠ Update ASCII design
4. ⚠ Address issues
5. ⚠ Request review again
6. ⚠ Iterate until solid

### If uncertain:
1. ❓ Ask clarifying questions
2. ❓ Request specific scenarios
3. ❓ Get expert input
4. ❓ Resolve before proceeding

## Tips for Better Reviews

### Be Specific
```
GOOD: "What happens if user tries to verify with wrong code 5 times?"
BAD: "What about errors?"
```

### Ask "Why"
```
GOOD: "Why do we need this field?"
BAD: [Just accepting the design]
```

### Think Like a User
```
GOOD: "Could a user get stuck here?"
BAD: "The design looks nice"
```

### Document as You Go
```
GOOD: "I'll note this question in the review"
BAD: [Forgetting questions later]
```

### Involve the Team
```
GOOD: "Let me get engineering's input on this"
BAD: [Solo reviewing without team]
```

## Time Estimates

| Review Type | Time | When |
|-------------|------|------|
| Quick | 15 min | Simple features |
| Standard | 1 hour | Normal features |
| Comprehensive | 2 hours | Complex features |
| Expert | 3+ hours | Critical features |

## Success Criteria

A good review results in:

✓ Clear understanding of feature
✓ Confidence to implement
✓ Fewer bugs during development
✓ Fewer design changes mid-development
✓ Better product UX
✓ Faster time to ship
✓ Fewer surprises in QA

---

**The ASCII Design Reviewer skill helps you catch issues early when they're cheap to fix, before engineers write code.** 🎯
