---
thread_name: "jagriti-hr-mcp-qa-improvement"
user: "innovation_interns"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## HR MCP QA Improvement

User: hey i need to do a QA in 3 different tasks so can you tell me how i can improve my QA and improve the question patterns and also how can i try to be more to the point what i am asking about and how to get the things done in a manner that i can flag 80 - 90 percent of the issues in just a couple go

Claude: I need clarity on your specific situation before giving you actionable advice on QA. Generic QA frameworks won't help you catch 80-90% of issues faster—the leverage is in understanding what you're actually testing and where your blind spots are.

[... conversation continues as before ...]

---

User: also what kind of information data i can ask it to give me an answer which will pull some more questioning path to it

Claude: Good question. Here's what information to request that naturally leads to deeper testing paths:

[... previous response on 7 types of queries ...]

---

User: * Links to other data (manager → does manager exist?)
* Combines constraints (AND filters → interaction bugs?)
* Scales large (ALL records → performance cliff?)
* Changes over time (before/after snapshots?)
* Requires permissions (who can see what?)
* Fails partway (timeout, incomplete, rollback?)

give me some information on these points that how can i improve QA quality on these topics

Claude: Here's how to improve QA quality on each of these 6 critical dimensions:

---

## 1. LINKS TO OTHER DATA (Manager → Does manager exist?)

**What can go wrong:**
- Manager ID references non-existent employees
- Broken chains (A manages B, B manages C, but C doesn't exist)
- Circular dependencies (A manages B who manages A)
- Orphaned records (employee has manager_id but manager was deleted)

**Test Prompts to Catch These:**

```
Test 1 - Reference Validation:
"Fetch emp-001 and show their manager_id. Then fetch that manager_id directly. Does the manager record exist with matching details?"

Expected: Manager record found with consistent data
Bad result: manager_id = "emp-9999" but that employee doesn't exist
→ Issue: MCP returns invalid reference
```

```
Test 2 - Circular Dependencies:
"Fetch emp-001's manager (emp-002). Fetch emp-002's manager. Continue chain. Does it loop back to emp-001?"

Expected: Chain ends at top executive (no manager)
Bad result: emp-001 → emp-002 → emp-003 → emp-001 (cycle)
→ Issue: MCP allows impossible reporting structure
```

```
Test 3 - Bulk Reference Check:
"List all employees and their manager_ids. Count how many manager_ids don't match any employee in the list."

Expected: 0 missing managers (or only CEO has null manager)
Bad result: 15 employees reference non-existent managers
→ Issue: Data integrity broken
```

**Quality Checklist:**
- [ ] Every manager_id in employee records exists as valid employee
- [ ] No circular reporting structures
- [ ] Manager chain has clear terminus (CEO/head)
- [ ] Deleted managers handled (set to null vs orphan?)
- [ ] Manager's department matches team's department

**Document as:**
```
Test: Reference Validation
Issue Found: emp-050 references manager_id=emp-9999 which doesn't exist
Severity: High (breaks org chart)
Reproducible: Yes (100%)
```

---

## 2. COMBINES CONSTRAINTS (AND Filters → Interaction bugs?)

**What can go wrong:**
- Filters don't combine correctly (OR instead of AND)
- One filter overrides another silently
- Invalid filter value breaks entire query
- Filter order affects results (should be order-independent)

**Test Prompts to Catch These:**

```
Test 1 - Filter Combination Logic:
"List employees WHERE department=Engineering AND status=active
Then separately: List active employees, count how many are in Engineering
Do both queries return same count?"

Expected: Same count both ways
Bad result: First query = 12, second = 15
→ Issue: AND not working, returning OR instead
```

```
Test 2 - Invalid Filter Handling:
"List employees WHERE department=Engineering AND role=FAKE_ROLE_XYZ
What happens? Error, empty list, or ignores bad filter?"

Expected: Either error "Invalid role" OR empty list (both valid)
Bad result: Returns all Engineering employees (ignores role filter)
→ Issue: Bad filter silently ignored, dangerous
```

```
Test 3 - Filter Order Independence:
"Query A: WHERE status=active AND department=Eng AND hire_date > 2020
Query B: WHERE hire_date > 2020 AND status=active AND department=Eng
Same results?"

Expected: Identical results regardless of order
Bad result: Different counts
→ Issue: Filter order matters (shouldn't)
```

```
Test 4 - Multiple Same-Field Filters:
"List employees WHERE status=active AND status=inactive
What's returned? Employees matching both? None? Error?"

Expected: Error or empty (can't be active AND inactive)
Bad result: Returns active employees (ignores second filter)
→ Issue: Duplicate constraints not validated
```

**Quality Checklist:**
- [ ] All filters applied with AND logic (not OR)
- [ ] Invalid filter values caught with specific errors
- [ ] Filter order doesn't affect results
- [ ] Conflicting filters handled (status=active AND status=inactive)
- [ ] No silent filter dropping
- [ ] AND combined filters reduce result set (never increase)

**Document as:**
```
Test: Filter Combination
Issue Found: WHERE status=active AND role=FAKE returns all active (ignores invalid role)
Expected: Should error "Invalid role value"
Severity: High (silent data loss)
```

---

## 3. SCALES LARGE (ALL records → Performance cliff?)

**What can go wrong:**
- Query OK with 10 records, fails with 1000
- Response time degrades sharply
- Data structure breaks/truncates at scale
- Memory limits hit, partial data returned
- Pagination broken or missing

**Test Prompts to Catch These:**

```
Test 1 - Pagination Behavior:
"List ALL active employees without pagination. How many returned?
Then list with limit=100, offset=0. Then offset=100. Do counts match?
Can you reach all employees via pagination?"

Expected: Consistent totals, no data loss
Bad result: Total = 500 but limit=100 × 5 = only 400 accessible
→ Issue: Pagination loses records
```

```
Test 2 - Response Structure at Scale:
"Fetch 1 employee emp-001 (record fields: name, id, dept, role, hire_date, status, manager_id)
Then list 10 employees.
Then list 100 employees.
Does each record have same fields in same format?"

Expected: Identical structure at all scales
Bad result: 100-employee list drops manager_id field (too large)
→ Issue: Structure degrades at scale
```

```
Test 3 - Performance Cliff:
"Time these queries:
1. List 10 employees → X ms
2. List 100 employees → Y ms
3. List 1000 employees → Z ms
Is degradation linear or exponential?"

Expected: Linear growth (10→100 = 10x slower, 100→1000 = 10x slower)
Bad result: 10→100 = 5x, 100→1000 = 100x (exponential cliff at 1000)
→ Issue: Unoptimized query, timeout risk
```

```
Test 4 - Field Truncation:
"List 1000 employees. Check if any have:
- name field cut off mid-word
- role field empty/null when should be filled
- hire_date malformed
Does data integrity hold at scale?"

Expected: All fields complete and valid across all records
Bad result: Names truncated to 50 chars at record 500+
→ Issue: Buffer overflow or encoding issue
```

**Quality Checklist:**
- [ ] Results consistent at 1, 10, 100, 1000+ records
- [ ] Pagination covers all data without overlap
- [ ] Response time < 5s for 1000 records (adjust per SLA)
- [ ] Data structure unchanged at any scale
- [ ] No field truncation or data corruption
- [ ] Memory usage doesn't spike unexpectedly

**Document as:**
```
Test: Scale Performance
Issue Found: List 1000 employees takes 45s, times out (limit 30s)
Severity: Critical (blocks production)
First appearance: At ~500 employees
```

---

## 4. CHANGES OVER TIME (Before/After snapshots?)

**What can go wrong:**
- Updates not reflected immediately
- Audit trail missing
- Timestamp not updated on change
- Rollback doesn't restore old state
- Historical data lost

**Test Prompts to Catch These:**

```
Test 1 - Update Visibility:
"Fetch emp-001 current department = 'Eng'
Update emp-001 department to 'Sales'
Immediately fetch emp-001 again. Department = 'Sales'?
Then list Sales department. Is emp-001 included?"

Expected: Update visible immediately in all queries
Bad result: Fetch shows 'Sales' but list Sales still doesn't include emp-001
→ Issue: Write-read consistency broken
```

```
Test 2 - Timestamp Tracking:
"Fetch emp-001, note updated_at timestamp (T1)
Wait 2 seconds
Update emp-001's role
Fetch emp-001 again. Is updated_at now > T1?"

Expected: Timestamp advances on every update
Bad result: Timestamp unchanged after update
→ Issue: Can't detect which records changed when
```

```
Test 3 - Partial Failure Handling:
"Try update: Change emp-001 department to 'Sales' AND change status to 'inactive'
Update fails (permission denied on status change)
Fetch emp-001. Did department change or roll back?"

Expected: Consistent state - all or nothing (ACID)
Bad result: Department changed to Sales but status unchanged (partial update)
→ Issue: Transaction not atomic
```

```
Test 4 - Change History:
"Get emp-001 audit log. Shows all changes with timestamps?
Example: 2024-01-01 hired as Engineer, 2024-06-01 promoted to Manager, 2024-09-01 moved to Sales"

Expected: Complete chronological record
Bad result: Only current state visible, no history
→ Issue: Can't trace what changed when
```

**Quality Checklist:**
- [ ] Updates visible in subsequent reads immediately
- [ ] updated_at timestamp advances on every change
- [ ] Updates are atomic (all succeed or all fail)
- [ ] Deleted records don't ghost (removed from all queries)
- [ ] Audit log tracks all changes with user + timestamp
- [ ] Rollback restores exact previous state

**Document as:**
```
Test: Update Visibility
Issue Found: Update emp-001 role, but list by role=Manager doesn't include emp-001 for 5s
Severity: Medium (eventual consistency, but should be immediate)
```

---

## 5. REQUIRES PERMISSIONS (Who can see what?)

**What can go wrong:**
- Readonly users can update data
- Users see other department's private data
- Manager sees all employees (should only see direct reports)
- Salary data visible to non-finance roles
- Permissions checked too late (after data leak)

**Test Prompts to Catch These:**

```
Test 1 - Write Permission Enforcement:
"As readonly user, try to update emp-001's department
What happens? Error before/after attempting change?"

Expected: Error "Permission denied" before any change
Bad result: Change succeeds or data gets partially updated then rolled back
→ Issue: Permission checked too late
```

```
Test 2 - Data Visibility by Role:
"Fetch emp-001 as:
- HR Admin: Should see name, id, dept, role, hire_date, manager, incentive_structure
- Engineering Manager: Should see name, id, dept, role, hire_date, manager (NO salary/incentive)
- Finance: Should see name, id, dept, role, hire_date, incentive_structure (NO manager info)

Does each role see exactly what they should?"

Expected: Consistent data filtering per role
Bad result: All roles see all fields
→ Issue: No data masking by role
```

```
Test 3 - Scope Boundary (Manager can only see reports):
"Manager emp-050 (manages eng team) tries to:
- Fetch their direct reports: emp-051, 052, 053 → Success?
- Fetch unrelated emp-100 (finance): Success?
- List all employees across all departments: Success?"

Expected: Can fetch reports, can't fetch unrelated, can't list all
Bad result: Manager can see all employees
→ Issue: Scope not enforced
```

```
Test 4 - Permission Escalation:
"Readonly user tries to:
1. Fetch data normally (works)
2. Request write permission (denied)
3. Update field via workaround (e.g., fetch, modify locally, fake re-submit)
Can they escalate or is blocked?"

Expected: Blocked at each escalation attempt
Bad result: Clever request format bypasses checks
→ Issue: Permission logic flawed
```

**Quality Checklist:**
- [ ] Readonly role cannot write, update, or delete
- [ ] Admin role can do everything
- [ ] Manager role limited to own department + direct reports
- [ ] Finance role sees incentive/payroll, not hierarchy
- [ ] Salary/incentive fields hidden from non-authorized roles
- [ ] Permissions checked BEFORE action, not after
- [ ] Denied actions logged for audit

**Document as:**
```
Test: Permission Enforcement
Issue Found: Readonly user successfully updates emp-001 department (should be denied)
Severity: Critical (security breach)
```

---

## 6. FAILS PARTWAY (Timeout, incomplete, rollback?)

**What can go wrong:**
- Timeout mid-query returns partial data (corrupts)
- Incomplete list sent without warning
- No retry mechanism
- Rollback leaves stale state
- Error message doesn't explain what failed

**Test Prompts to Catch These:**

```
Test 1 - Timeout Handling:
"List 1000 employees with timeout=100ms (system needs 2s to respond)
Does request timeout? Does it:
a) Error with 'timeout'
b) Return partial list (first 100)
c) Hang indefinitely
d) Retry automatically?"

Expected: Error 'timeout' with 0 records returned (safe fail)
Bad result: Partial list returned (app thinks it's complete)
→ Issue: Silent data loss
```

```
Test 2 - Incomplete Data Detection:
"List employees. Response says 'returned 100 of 500 total' OR returns 500?"

Expected: Clear indication of completeness OR full data
Bad result: Returns 100 but claims that's all (app doesn't know)
→ Issue: Incomplete data treated as complete
```

```
Test 3 - Failed Update Rollback:
"Update emp-001: Change dept to Sales, change status to Inactive
Update fails (status change not permitted)
Fetch emp-001. Is dept back to original or changed to Sales?"

Expected: Dept unchanged (all-or-nothing rollback)
Bad result: Dept changed to Sales but status unchanged (partial)
→ Issue: Atomic transaction failed
```

```
Test 4 - Error Message Clarity:
"Trigger these failures and check error messages:
1. Timeout: Does it say 'timeout' or generic 'error'?
2. Permission denied: Does it say 'readonly user' or generic?
3. Invalid input: Does it say which field is invalid?
4. Not found: Does it say 'employee not found' or 'error'?"

Expected: Specific errors naming the problem
Bad result: All errors say 'An error occurred' (useless)
→ Issue: Can't debug failures
```

```
Test 5 - Retry Behavior:
"Start list operation on 1000 records, timeout at record 500
Immediately retry same query
Does retry:
a) Start fresh from record 1
b) Resume from record 500
c) Return cached partial result
d) Error (last attempt failed)?"

Expected: Start fresh from record 1 (safe retry)
Bad result: Resume from 500 (client doesn't know, data mismatch)
→ Issue: Resume creates duplicates/gaps
```

**Quality Checklist:**
- [ ] Timeout returns 0 records + error (never partial)
- [ ] Response indicates if data is complete (total_count field)
- [ ] Failed updates rollback completely (ACID)
- [ ] Error messages specific (not generic)
- [ ] Retry starts fresh (no resume without explicit pagination)
- [ ] Failed operations logged with reason
- [ ] No hung/zombie requests

**Document as:**
```
Test: Timeout Handling
Issue Found: List 1000 employees with 500ms timeout returns 350 records (no error) app crashes
Severity: Critical (data corruption)
```

---

## INTEGRATED STRATEGY: Running All 6 Together

This is how to test them in sequence to catch cascading issues:

```
Session 1: Setup References
→ Create test: emp-001 (manager = emp-002), emp-002 (manager = null)

Session 2: Single Operations
→ Test 1-3 filters individually work
→ Test manager reference exists

Session 3: Combined Complexity
→ Test (dept=Eng AND status=active AND manager=emp-002)
→ Verify manager reference still valid in filtered results

Session 4: Scale It
→ Same query but for 1000 employees
→ Check if structure holds, no truncation

Session 5: Change & Consistency
→ Update emp-001's manager to emp-003
→ Verify change visible immediately in all queries
→ Check timestamp updated

Session 6: Permission Layers
→ Run same queries as different roles
→ Verify salary/hierarchy hidden appropriately

Session 7: Failure Modes
→ Add timeout constraint
→ Try update that partially fails
→ Verify rollback and error messages
```

---

## FINAL QA QUALITY SCORECARD

For each of the 6 dimensions, score:

```
1. Links to Other Data
   ☐ All references resolve (manager exists)
   ☐ No circular dependencies
   ☐ Broken links handled (null vs error)
   Score: ___ / 3

2. Combines Constraints
   ☐ Filters combine with AND logic
   ☐ Invalid filters error specifically
   ☐ Filter order irrelevant
   Score: ___ / 3

3. Scales Large
   ☐ Results consistent at 1, 100, 1000 records
   ☐ Response time < SLA
   ☐ Pagination works, no data loss
   Score: ___ / 3

4. Changes Over Time
   ☐ Updates visible immediately
   ☐ Timestamps track changes
   ☐ Updates atomic (all or nothing)
   Score: ___ / 3

5. Requires Permissions
   ☐ Readonly blocked from writes
   ☐ Role-based field masking works
   ☐ Scope enforcement (can't see all)
   Score: ___ / 3

6. Fails Gracefully
   ☐ Timeout = error + 0 data (never partial)
   ☐ Errors specific (not generic)
   ☐ Failed updates rollback
   Score: ___ / 3

Total: ___ / 18
Pass Threshold: 15+ (83%)
```

Which of these 6 should we build a detailed test plan for first?
