# Interview Workflow

Use this workflow to clarify an idea without turning the session into a questionnaire.

## First Pass

Extract these facts from the user's prompt before asking anything:

- Problem or opportunity
- Target user
- Desired outcome
- Project type
- Platform expectation
- Any named stack, service, file, repo, or deadline
- Appetite for building now versus brainstorming

If a fact is missing but a reasonable assumption is low-risk, state the assumption and continue.

## Question Budget

Ask 0 questions when the idea can be shaped with assumptions.
Ask 1 question when one answer changes the direction.
Ask 2-3 questions only when the missing details affect stack, scope, data, or deployment.
Never ask broad intake forms.

Good questions:

- "Who is the first real user: you, a client, a team, or public users?"
- "Should this be a quick local tool, a deployable web app, a mobile app, or an automation?"
- "What is the one workflow that must work in v1?"
- "Does this need real accounts, payments, persistent data, or can v1 avoid them?"
- "What existing repo, API, dataset, or design reference should constrain the plan?"

Weak questions:

- "What features do you want?"
- "What tech stack should we use?"
- "What is your budget?"
- "Do you want it to be user-friendly?"

## Clarifying Pattern

Use this structure when the idea is still rough:

```text
Here is how I read the idea:
- One-line concept:
- First user:
- Core workflow:
- Likely output:

Good side:
- ...

Bad side:
- ...

Assumptions I will use:
- ...

Questions that change the plan:
1. ...
2. ...
3. ...
```

## Good And Bad Sides

The good side should identify why the idea might be worth building:

- Clear pain
- Repeated workflow
- Personal leverage
- Strong demo potential
- Valuable automation
- Useful data capture
- Low-cost MVP

The bad side should identify why it might fail or sprawl:

- Unclear buyer or user
- Too many workflows
- Hard integrations
- Unbounded AI behavior
- Data quality risk
- Design-heavy surface without a core loop
- Deployment or auth complexity too early

## When To Stop Interviewing

Stop asking and produce the plan when:

- The first user is known or reasonably assumed.
- The first workflow is named.
- The MVP boundary is clear enough.
- The largest risk is explicit.
- The next artifact can be written without inventing critical facts.
