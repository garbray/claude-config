# Sprint Management & Velocity Guide

Sprint management is how you turn great stories into great delivery. This guide covers planning, execution, and continuous improvement.

## Sprint Lifecycle

### Sprint Planning (1-2 hours, at start of sprint)

**Prepare Before Meeting**:
- Product Owner has prioritized backlog
- Stories are refined (written, estimated)
- Team knows what's coming
- No surprises in the meeting

**During Planning**:
1. Review sprint goal (from PO)
2. Review team velocity (from past sprints)
3. Pull stories from top of backlog
4. Discuss each story: any questions? Estimation fair?
5. Count story points until hitting velocity target
6. Stop (don't over-commit)
7. Get team agreement: "Are you confident in this sprint?"
8. Clarify: Who is working on what?

**After Planning**:
- Backlog is loaded with committed stories
- Each engineer knows their assignments (rough)
- Team knows the sprint goal
- Definition of Done is clear

### Daily Standup (15 minutes, every morning)

**Structure**:
1. Each engineer: "Yesterday I did X, today I'll do Y, no blockers" (or "I'm blocked on Z")
2. Scrum Master: Identify blockers, resolve if possible
3. Done

**Red Flags to Catch**:
- Engineer blocked for 2+ days → help immediately
- Scope creeping → remind of sprint goal
- Velocity trending down → investigate
- Team looks unmotivated → ask what's wrong

**Not a Status Report**:
- Don't go through each story
- Don't let it become a meeting (it's a sync)
- Don't solve problems here (solve offline)

### Sprint Refinement (1 hour, mid-sprint or before next sprint starts)

**Purpose**: Prepare next sprint's backlog

**During Refinement**:
1. Walk through top 10-15 stories on backlog
2. Clarify requirements with Product Owner
3. Estimate with team
4. Break down if too large
5. Identify dependencies
6. Ready for sprint planning

**Don't**:
- Get stuck on minor details
- Spend more than 1 hour (timebox it)
- Over-refine stories that won't be sprinted for months

### Sprint Review (1 hour, end of sprint)

**Purpose**: Demonstrate work, get feedback

**During Review**:
1. Demonstrate each story that's "Done"
2. Product Owner accepts or asks for revisions
3. Get stakeholder/user feedback
4. Discuss: what's working? what's not?
5. Answer: are we shipping value?

**Don't**:
- Show incomplete work
- Make excuses
- Skip this (it's how you get feedback)

### Sprint Retrospective (1 hour, end of sprint)

**Purpose**: Improve the process

**During Retro**:
1. What went well?
2. What didn't go well?
3. What will we do differently?
4. Pick 1-2 changes for next sprint

**Good Changes**:
- "Add code review checklist" (concrete)
- "Daily standup 15 min instead of 30" (concrete)
- "Pair on setup to reduce friction" (concrete)

**Bad Changes**:
- "Be better" (too vague)
- "Everyone work harder" (guilt-based)
- Too many changes (pick 1-2 max)

**Track Improvements**:
- Are we shipping faster?
- Is quality improving?
- Is team happier?

---

## Velocity Tracking & Forecasting

### Calculating Velocity

```
Velocity = Story points completed in a sprint (only "Done" stories count)

Example:
Sprint 1:
  Story A (3pt): DONE ✓
  Story B (3pt): DONE ✓
  Story C (2pt): DONE ✓
  Story D (5pt): Not started ✗
  Story E (1pt): DONE ✓
  Velocity: 3+3+2+1 = 9 points

Sprint 2:
  Story F (3pt): DONE ✓
  Story G (2pt): DONE ✓
  Story H (3pt): DONE ✓
  Story I (2pt): DONE ✓
  Story J (5pt): DONE ✓
  Velocity: 3+2+3+2+5 = 15 points

Sprint 3:
  Story K (3pt): DONE ✓
  Story L (3pt): DONE ✓
  Story M (2pt): DONE ✓
  Story N (5pt): In progress (doesn't count)
  Velocity: 3+3+2 = 8 points

Average velocity (3 sprints): (9+15+8)/3 = 10.7 → use 10 or 11 for forecasting
```

### Using Velocity for Planning

```
Known: Average team velocity is 15 points per sprint

Planning for Q1 (13 weeks, 3 sprints):
- Feature A: 25 points
- Feature B: 15 points
- Feature C: 20 points
- Feature D: 15 points
- Total: 75 points

Timeline:
Sprint 1 (15pt): Feature A (start)
Sprint 2 (15pt): Feature A (finish) + Feature B
Sprint 3 (15pt): Feature B (finish) + Feature C + Feature D (start)

Need 5 sprints (75pt ÷ 15pt/sprint) to complete all 4 features
→ Tell PM: "We can do Features A and B in Q1, Features C and D in Q2"
```

### Velocity Trends

```
Velocity Over Time:

Sprint 1: 8pt (new team, learning)
Sprint 2: 12pt (ramping up)
Sprint 3: 15pt (hitting stride)
Sprint 4: 16pt (experienced)
Sprint 5: 15pt (consistent)
Sprint 6: 14pt (one person out)
Sprint 7: 15pt (back to normal)
Sprint 8: 15pt (stable)

Interpretation:
- First 3 sprints: ramp-up phase (expect increasing velocity)
- Sprints 3-8: stable phase (velocity consistent ~15pt)
- Spike down in sprint 6: explain it (illness, vacation, etc)
- Trend: Healthy, stable, predictable

Red flags:
- Velocity keeps decreasing (team struggling? scope creeping? process broken?)
- Velocity spikes unpredictably (estimates inconsistent? different definition of "done"?)
- Velocity stays near zero (team blocked? waiting for resources? unmotivated?)
```

### Adjusting Velocity

```
If velocity increases:
- Good! But verify it's real (not changed estimation, not cutting corners)
- Can we sustain it? (If yes, great; if no, revert to conservative estimate)
- Plan conservatively (use historical average, not current high)

If velocity decreases:
- Investigate cause
  - New team member (ramp-up, normal)
  - More complex work (expected, adjust future planning)
  - More interruptions (fire-fighting, investigate)
  - Process changes (validate they're helping)
  - Morale issue (address immediately)
- Plan conservatively (use lower velocity until stable)
- Don't blame team ("You slowed down!")
- Do ask team ("What's making this sprint harder?")

If velocity is erratic:
- Estimation is inconsistent (recalibrate during refinement)
- Definition of Done changing (clarify DoD, stick to it)
- Stories too big (stories >5pt don't fit in sprints)
- Too many interruptions (protect sprint from interrupts)
- Team inexperienced (velocity stabilizes over time)
```

---

## Sprint Execution Best Practices

### 1. Protect the Sprint

**Interruptions kill velocity.** Protect team from mid-sprint surprises.

```
GOOD:
"Fire! We have a critical production bug!"
Decide: Is this truly critical (affects many users, revenue loss, security)?
- Yes: One engineer pulls out, works on bug, rest of team continues sprint
- No: Add to backlog, handle in next sprint or after this sprint

BAD:
"Can you just quickly do X? It'll only take 30 minutes"
→ Engineer context-switches
→ Loses 15 minutes on context switch
→ Takes 1 hour instead of 30 minutes
→ Cascades to other work
→ Sprint derailed
```

**Solution**: 
- Only genuine emergencies are "drop everything"
- Everything else waits for sprint to finish
- If truly urgent, defer one story from sprint to make room

### 2. Encourage Pair Programming

**When to pair**:
- Story with unknowns (investigate together)
- Story with high risk (reduce risk with two minds)
- Onboarding new team member (knowledge transfer)
- Tricky codebase (two brains > one)

**Benefits**:
- Higher quality (two people catch issues)
- Knowledge sharing (both people learn)
- Faster problem-solving (brainstorm together)

**Don't force it**:
- Not every story needs a pair
- Some engineers prefer solo work (respect that)
- If team is against pairing, don't mandate it

### 3. Code Review During Sprint

**Review frequently**:
- Don't wait until end of sprint
- Review every PR the day it's opened
- Keep PRs small (easier to review)
- Provide feedback same-day

**Review quality**:
- Is code clear?
- Do tests cover the story?
- Does it match Definition of Done?
- Are there edge cases missing?
- Is it performant?

**Red flag**: PR sitting unreviewed for 2+ days
→ Prioritize reviews
→ Block stories if code isn't reviewed

### 4. Test Throughout Sprint

**Don't test at the end**:
- Test while building
- Stories should come with tests
- Run tests daily
- Fix failures immediately

**Test coverage**:
- Happy path: must test
- Error cases: must test
- Edge cases: must test
- Performance: test as relevant

### 5. Manage Technical Debt

**Avoid accumulation**:
- Don't skip tests to go fast ("We'll test later")
- Don't ignore warnings ("We'll fix later")
- Don't leave TODOs everywhere ("We'll refactor later")

**"Later" often never comes.**

**Solution**:
- Make time in sprint for tech debt (1-2 stories)
- Or dedicate 20% of sprint capacity to tech debt
- Examples: refactoring, upgrade dependencies, improve tests

### 6. Stay Communicative

**Keep PO informed**:
- Share progress daily (standup notes)
- If sprint goal is at risk, flag early
- If team is struggling, be honest
- If you'll deliver early, plan next work

**Keep engineers informed**:
- Clarify stories in refinement
- Unblock immediately
- Celebrate wins
- Learn from misses

---

## Sprint Anti-Patterns

### Anti-Pattern 1: The Overstuffed Sprint

```
❌ BAD:
Velocity: 15 points per sprint
Commitment: 25 points ("We'll work extra hard")
→ Sprint fails
→ Team demoralizes
→ Actually completes fewer points next sprint

✓ GOOD:
Velocity: 15 points per sprint
Commitment: 15 points
→ Sprint succeeds
→ Team confident
→ Velocity improves
```

**Key**: Under-commit, over-deliver. Better to finish early than finish late.

### Anti-Pattern 2: The Mid-Sprint Scope Change

```
❌ BAD:
Sprint commitment: Stories A, B, C (15pt)
Wednesday: "Oh, we also need to do Story X!"
→ Pull in new story
→ Drop other story
→ Sprint chaotic
→ Nothing gets done

✓ GOOD:
Sprint commitment: Stories A, B, C (15pt)
Wednesday: "We need Story X"
PO: "Understood. It goes on backlog. We'll prioritize for next sprint."
→ Sprint remains focused
→ Everything gets done
```

**Key**: Commitment is sacred. Changes go on backlog, not mid-sprint.

### Anti-Pattern 3: The Sprint Dedicated to "Fixes"

```
❌ BAD:
Sprint 1: 15pt of features
Bugs found: 10
Sprint 2: Dedicated to bug fixes
→ No new features
→ Velocity drops to zero
→ Cycle repeats

✓ GOOD:
Sprint 1: 15pt of features
Bugs found: 3-5
Sprint 2: 12pt features + 3pt bug fixes (incorporated into sprint)
→ Consistent velocity
→ Quality and new work both happen
→ Bugs handled quickly, don't pile up
```

**Key**: Quality is built in, not added later. Fix bugs immediately, don't defer.

### Anti-Pattern 4: The Unestimated Story

```
❌ BAD:
"How many points is this?"
"Uh, I don't know yet"
→ Sprint starts
→ Story size unknown
→ Can't forecast if it fits
→ Sprint overruns

✓ GOOD:
Stories refined and estimated before sprint starts
→ Know upfront what fits
→ Can forecast accurately
→ Sprint sticks to plan
```

**Key**: Refinement happens before planning. No surprises.

### Anti-Pattern 5: The "Almost Done" Story

```
❌ BAD:
Story has: Code ✓, Tests ✓, But: Code review ✗, Integration test ✗
Status: "Almost done, we'll finish tomorrow"
→ Tomorrow: Engineer starts new story
→ Old story lingers
→ Definition of Done ignored
→ "Done" doesn't mean "done"

✓ GOOD:
Story has: Code ✓, Tests ✓, Code review ✓, Integration tests ✓, Deployed to staging ✓
Status: DONE (meets Definition of Done)
→ Can be closed
→ Counts toward velocity
→ Trust what "done" means
```

**Key**: Definition of Done is non-negotiable. "Almost done" is not done.

---

## Velocity FAQs

**Q: Why does velocity matter?**
A: Velocity lets you forecast. "We do 15 points per sprint, so this 60-point feature takes 4 sprints." Without velocity, you're guessing.

**Q: Should we use velocity in performance reviews?**
A: No. "Engineer A completed 20 points, Engineer B completed 10 points" is misleading.
- Points aren't hours
- Different stories, different complexity
- Some engineers mentor (don't count as velocity)
- This metric destroys trust

Instead, review: "Did they deliver quality? Do they communicate? Do they grow?"

**Q: What if our velocity is zero?**
A: That's a serious problem.
- Team is blocked (what's blocking them? Fix it)
- Stories are broken (can't be completed; rewrite them)
- Team is unmotivated (what's wrong? Address it)
- Definition of Done too strict (clarify it)
Something is broken. Find and fix it.

**Q: Our velocity is inconsistent (8pt, 20pt, 15pt, 9pt). Why?**
A: Inconsistent estimation, unclear Definition of Done, or interruptions.
- Estimation: Stories >5pt get broken; team discusses estimates
- DoD: Clarify "done"; stick to it
- Interruptions: Protect sprint from mid-sprint changes

---

## Team Health Signals

Track these to understand team health:

**Green Signals**:
- ✓ Velocity stable (±2pt)
- ✓ Sprint goals consistently met
- ✓ Defect rate low
- ✓ Team morale good (people want to be there)
- ✓ Collaboration happens naturally
- ✓ Retros are constructive

**Yellow Signals**:
- ⚠ Velocity trending down
- ⚠ Estimates consistently wrong (over or under)
- ⚠ Some team members quiet in standups
- ⚠ Code review taking >2 days
- ⚠ Tech debt accumulating
- ⚠ Retros are blaming ("Why didn't you...")

**Red Signals**:
- ✗ Velocity near zero
- ✗ Multiple stories blocked
- ✗ High defect rate
- ✗ Turnover (people leaving)
- ✗ Conflict in team
- ✗ Retros are silent (no one wants to talk)

---

## Improving Velocity

**Don't aim to increase velocity.** Aim to improve quality, reduce waste, and let velocity naturally improve.

```
Ways velocity improves:
✓ Better stories (more clarity → less guessing)
✓ Better process (less waste → more building time)
✓ Better team (more experience → faster decisions)
✓ Better tools (faster builds → faster iteration)
✓ Better codebase (less fighting → faster coding)

Ways velocity SHOULDN'T improve:
✗ Work harder (unsustainable)
✗ Skip tests (quality suffers)
✗ Cut corners (debt accumulates)
✗ Pressure (backfires)
```

**Focus on the fundamentals**. When fundamentals are good, velocity naturally improves.

---

## Key Takeaways

- **Velocity is a forecast tool, not a performance metric**
- **Stories must be small (1-3pt) and clear to maintain velocity**
- **Protect sprints from mid-sprint changes**
- **Measure success by: features shipped, quality maintained, team health**
- **Velocity stabilizes over time; don't obsess over it early**
- **Improve process, not pressure; velocity follows**
