# Storyboard: &lt;Animation Title&gt;

> Copy this template into the animation's directory as `storyboard.md` and
> fill **every** field before writing any animation code. A storyboard that
> has not passed technical validation (step 5.4 of the workflow) must not
> enter implementation. Method: [references/storyboard-method.md](../../references/storyboard-method.md)

## Identification

| Field | Value |
|---|---|
| Animation ID | `anim-<domain>-<slug>` (unique, stable identifier) |
| Knowledge Point | e.g. "USB control transfer data stage" |
| Learning Objective | What the learner can explain or predict after viewing |
| Technical Basis | Standard + clause, datasheet section, or app note (see Evidence Table) |
| Animation Type | protocol-sequence \| data-flow \| state-machine \| physical-mechanism \| interactive-simulation |
| Source Tutorial | path/URL of the page this animation belongs to (or "standalone") |

## Scene

| Field | Value |
|---|---|
| Scene | Overall setting: devices shown, canvas layout, viewpoint |
| Objects | Every visual object: id, label, visual role (device / data / signal / state) |
| Initial State | Exactly what is visible at t=0, before play |

## Steps

| # | Step ID | Trigger / Condition | Duration (story time) | State Changes | Visual Action | Caption Text |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

One row per step. Step IDs are stable identifiers reused as `data-tae-step`
values and referenced by tests. Exception branches must be present as steps
or as scenario variants — an animation that only shows the happy path is
incomplete.

## Data Flow / Timing

| Field | Value |
|---|---|
| Data Flow | source -> intermediate nodes -> destination, with payloads |
| Timing | ordering constraints, timeouts, retries; real values vs story-time scaling factor |
| Exception Branches | timeouts, NAK/retry, error states — which step shows each |

## Interaction

| Field | Value |
|---|---|
| User Interaction | which controls apply (play/pause/step/reset/speed/timeline/scenario/parameters) |
| Scenarios | named scenario presets and what each demonstrates |
| Expected Result | what the learner should be able to observe and conclude |

## Evidence Table

| Claim shown in the animation | Tag | Source (spec clause / datasheet / doc + URL) |
|---|---|---|
| | SPEC / VENDOR / CHIP / SDK / TEACHING / VERIFIED / UNVERIFIED | |

Rules:
- Every important behavior needs a row in the Evidence Table.
- `TEACHING` rows must state what was simplified and why the simplification is safe.
- `UNVERIFIED` rows are release blockers (see references/technical-accuracy.md).
- If a claim cannot be sourced, the animation must not present it as fact.
