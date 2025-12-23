# Design Critique, Feedback & Iteration Guide

Design improves through feedback. This guide explains how to give and receive critique, iterate quickly, and refine designs based on real insights.

## The Critique Framework

Effective critiques focus on the work, not the person. They identify what works, what doesn't, and why.

### Structure of a Critique

**1. Understand First**
Before critiquing, understand:
- What problem does this design solve?
- Who is the user?
- What are the constraints?
- What's the goal (conversion, clarity, engagement)?

Ask clarifying questions: "I see you chose a card layout—what's the user benefit? Are there other options to consider?"

**2. Acknowledge Strengths**
Start with what works:
- "The visual hierarchy is clear—users immediately see the main action"
- "The color contrast is excellent throughout"
- "Error messages are specific and helpful"

Identify at least one strength before suggesting improvements.

**3. Identify Gaps & Concerns**
Ask constructive questions:
- "I'm unclear about [specific thing]. How should users understand this?"
- "I don't see error handling for [scenario]. How should we address that?"
- "This works well on desktop, but I'm concerned about mobile—can we walk through it?"

Focus on specifics, not vague critiques. "I don't like this" is feedback; "The button label is unclear in context" is critique.

**4. Propose Alternatives**
When critiquing, offer direction:
- "This could work better if we tried [approach] because [reason]"
- "Would it be clearer to [change]? Here's why: [rationale]"
- "Other products handle this with [pattern]. Should we explore that?"

Show alternatives when helpful. "I don't think this works" is criticism; "I wonder if we could show the error like [example] to make it clearer" is constructive.

**5. Agree on Next Steps**
End with clarity on what's next:
- "Let's iterate on the mobile experience next"
- "I think this direction is strong. Let's prototype to test"
- "Should we get user feedback on these two approaches?"

## Specific Critique Patterns

### Clarity Critique
```
Pattern: "I'm unclear about [specific element/flow]"

Example:
  "I understand the happy path, but I'm unclear what happens 
   if payment fails. Should the user retry immediately, wait, 
   or contact support? This affects the design."

Result: Forces clarity on edge cases, incomplete flows
```

### Hierarchy Critique
```
Pattern: "I'm not sure what [element A] vs [element B] is more important"

Example:
  "Both the 'Save' and 'Delete' buttons are prominent. 
   Which is the primary action? Maybe 'Save' should be primary 
   (blue) and 'Delete' secondary (gray)?"

Result: Refines visual hierarchy, prevents mistakes
```

### Usability Critique
```
Pattern: "I'm concerned a user might [problem]. How do we prevent that?"

Example:
  "I'm concerned a user might accidentally delete their entire 
   project without realizing it. Should we require a confirmation 
   or make 'Delete' less prominent?"

Result: Identifies user friction, improves safety
```

### Accessibility Critique
```
Pattern: "How does this work for [accessibility need]?"

Example:
  "How does screen reader experience this? The color alone shows 
   error (red), but someone with colorblindness might miss it. 
   Should we add an icon or text?"

Result: Improves inclusive design
```

### Consistency Critique
```
Pattern: "This works differently than [other part of product]. Should they be consistent?"

Example:
  "In the settings, we use toggles for on/off. Here we use checkboxes. 
   Should we be consistent? Or is the difference intentional?"

Result: Establishes consistent patterns, reduces cognitive load
```

## Receiving Feedback Well

When receiving critique:

**1. Listen Without Defending**
Don't explain why you made decisions while feedback is being given. Listen first.

**2. Ask Clarifying Questions**
- "Can you give me an example?"
- "What specifically felt unclear?"
- "How would you approach this?"

**3. Acknowledge Without Dismissing**
- "That's a good point about the mobile experience"
- "I hadn't considered that error case"
- "I see your concern about consistency"

**4. Explore, Don't Implement Immediately**
Don't assume feedback means "change it." Sometimes feedback helps you refine your original direction. Sometimes it reveals a better approach.

**5. Document Feedback**
Note the feedback even if you don't implement it immediately. It might be relevant later.

## Iteration Workflow

### Iteration Round 1: Exploratory
**Goal**: Validate approach and gather feedback before investing in detail

**What to show**:
- Rough ASCII layouts
- Key user flows
- Major decisions (layout approach, information hierarchy)
- Questions you want answered

**What NOT to show**:
- Fully detailed designs
- All edge cases and states
- Final styling/polish

**Feedback to gather**:
- Is the approach right?
- Does the information architecture make sense?
- Are there missing flows or states?
- Do the decisions align with the product?

**Output**: Direction to pursue, questions to answer

### Iteration Round 2: Refinement
**Goal**: Work out details and edge cases

**What to show**:
- Detailed ASCII layouts (all major states)
- Component specifications
- Micro-interactions and transitions
- Error states and edge cases

**What NOT to show**:
- Full visual polish (colors, illustrations)
- Animations implemented
- Marketing copy (focus on UX copy)

**Feedback to gather**:
- Are layouts clear?
- Are all states covered?
- Are components well-specified?
- What's missing or unclear?

**Output**: Refined direction ready for high-fidelity design

### Iteration Round 3: Polish (Optional)
**Goal**: Finalize visual design and interactions

**What to show**:
- High-fidelity designs or interactive prototypes
- Actual colors, typography, illustrations
- Micro-interactions and animations
- Responsive behavior

**What NOT to show**:
- Highly polished pixel-perfect work (if feedback is still being gathered)
- Complex interactions not yet implemented

**Feedback to gather**:
- Does the visual direction feel right?
- Do animations feel appropriate?
- Are there any usability issues at this level?
- Ready to hand off to development?

**Output**: Ready for development, or final adjustments

### Iteration Round 4: Validate (Post-Implementation)
**Goal**: Test with real users and refine based on usage

**What to test**:
- Can users accomplish key tasks?
- Are there unexpected friction points?
- Is the experience as intuitive as designed?
- Do error states communicate clearly?

**Feedback to gather**:
- Usability issues
- Terminology problems
- Unexpected user behaviors
- Edge cases not anticipated

**Output**: Bug list, iterative improvements for next version

## Feedback Templates

### When You're the Designer Asking for Feedback

**Exploratory Stage**:
```
I'm exploring [problem]. I'm considering [approach] because [reasoning].

Here's my layout approach:
[ASCII layouts]

My questions:
1. Does this information structure make sense?
2. Am I missing any key flows?
3. Should we handle [edge case] this way?

What feedback would be most helpful right now?
```

**Refinement Stage**:
```
I've refined the layouts and added edge case handling:
[Detailed ASCII layouts with all states]

I've specified:
- Component variations
- Micro-interactions
- Error handling

What's unclear or missing?

Am I ready to move to visual design, or should I refine further?
```

### When You're Giving Feedback

**Strength-based**:
```
I really like how you've handled [specific thing]. 
The [aspect] is clear and [positive outcome].

One thing I'm wondering about is [specific concern]. 
[Question or suggestion]. How would you approach that?
```

**Issue-focused**:
```
I see a potential issue here: [specific scenario].

Currently, the design [describes what happens]. 

I think it could be better if [suggestion], because [reason].

What do you think? Are there constraints I'm missing?
```

## Common Feedback Pitfalls

### Pitfall 1: Vague Feedback
```
BAD:   "This doesn't feel right"
GOOD:  "I'm concerned the error message feels like it's blaming 
        the user. Could it say 'Email already in use' instead of 
        'Invalid email'?"
```

### Pitfall 2: Preference Over Rationale
```
BAD:   "I don't like blue, use red"
GOOD:  "The blue button is hard to see against the background. 
        Let's test with a darker color or better contrast."
```

### Pitfall 3: Suggesting Implementation, Not Problem
```
BAD:   "Use a modal instead"
GOOD:  "I'm concerned this inline error could be missed. How 
        could we make it more prominent?"
```

### Pitfall 4: Changing Direction Without Context
```
BAD:   [Feedback: "Redesign this completely"]
GOOD:  "This direction is clear, but let me check: are we 
        prioritizing simplicity or feature richness here? That 
        affects whether we go this way or explore [alternative]."
```

## Iteration Checklist

After each iteration, assess:

**Clarity**
- [ ] Is the design's purpose clear?
- [ ] Can users understand what to do?
- [ ] Are all states, flows, and edge cases documented?

**Completeness**
- [ ] Are all major user flows documented?
- [ ] Have error cases been addressed?
- [ ] Is accessibility considered?
- [ ] Are constraints documented?

**Consistency**
- [ ] Does it align with the product's design system?
- [ ] Are patterns consistent internally?
- [ ] Is terminology consistent?

**Feasibility**
- [ ] Can this be built as designed?
- [ ] Are technical constraints documented?
- [ ] Have performance implications been considered?

**Feedback Loop**
- [ ] Have key stakeholders reviewed?
- [ ] Have edge cases been validated?
- [ ] Is there alignment on direction?

## Feedback Integration

**Step 1: Categorize Feedback**
- Critical (must address, blocks handoff)
- Important (should address, impacts experience)
- Nice-to-have (consider, but not essential)
- Out of scope (acknowledge, defer for later)

**Step 2: Identify Themes**
- Do multiple people mention the same concern?
- Are there conflicting opinions?
- What's the underlying issue?

**Step 3: Prioritize Changes**
- Address critical issues first
- Group related changes together
- Plan iteration sequence

**Step 4: Iterate Visibly**
- Show what changed and why
- Explain trade-offs
- Get feedback on iterations

**Step 5: Document**
- Record what changed
- Note why changes were made
- Build knowledge for future work

## Know When to Stop Iterating

**Signs You're Ready to Hand Off**:
- Key stakeholders are aligned on direction
- All major states and flows are documented
- Edge cases have been addressed
- No new feedback is being raised
- The team is confident in implementation

**Signs You Need More Iteration**:
- Feedback is contradictory (need alignment)
- Major flows are still unclear
- Critical edge cases not addressed
- High risk of implementation issues
- Team expresses doubt

**Signs You're Over-Iterating**:
- Feedback is about personal preference, not usability
- Changes are micro-refinements without impact
- Original problem is being lost in iterations
- Timeline is becoming constrained

## Iteration & Feedback in Practice

**Real Example**:
```
Round 1 - Exploratory:
  Show: ASCII layout, information hierarchy
  Feedback: "Clear layout, but unclear how payment flow works"
  Action: Specify payment error handling

Round 2 - Refinement:
  Show: Detailed layouts, all states, payment error cases
  Feedback: "Good! Mobile layout could be improved for payment form"
  Action: Redesign mobile payment flow

Round 3 - Polish:
  Show: High-fidelity design, animations
  Feedback: "Looks great. One small thing: error message color is hard to read"
  Action: Adjust error color for better contrast

Round 4 - Handoff:
  Ready for development with full specification
```

## Documentation During Iteration

Keep track of:
- What feedback was given
- Why changes were made
- What alternatives were considered
- What questions remain
- What was intentionally deferred

This becomes invaluable for:
- Understanding design decisions later
- Onboarding new team members
- Defending design choices
- Improving for next version
