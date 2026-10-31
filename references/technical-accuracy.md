# Technical Accuracy & Evidence Management

Highest-priority reference. Nothing else in this skill matters if the
animation teaches something wrong.

## 1. The evidence tag system

Every important claim or behavior shown in an animation gets exactly one tag
in the storyboard's Evidence Table, and the page itself carries an evidence
footer listing its tags.

| Tag | Definition | Examples |
|---|---|---|
| `SPEC` | Behavior defined by a public standard | USB 2.0 §9.1 device states; ETG.1000 datagram layout; Bluetooth Core Vol 6 advertising |
| `VENDOR` | One vendor's implementation choice | TI's amplitude-invariant Clarke convention; STM32 DMA request mapping |
| `CHIP` | Silicon-specific behavior or limit | ESC RAM size, an MCU's ADC sampling time, errata workarounds |
| `SDK` | Behavior of a software stack | FreeRTOS Blocked→Ready on delay expiry; HAL callback order |
| `TEACHING` | Deliberate simplification for pedagogy | Scaling time so a 100 µs cycle takes 10 s; showing 3 slaves instead of 30 |
| `VERIFIED` | Confirmed against a citable source | — (status, not a category; pair with one of the above) |
| `UNVERIFIED` | Could not be confirmed | Must be resolved before release |

`VERIFIED` / `UNVERIFIED` are statuses applied to a `SPEC`/`VENDOR`/`CHIP`/
`SDK`/`TEACHING` claim. A storyboard row must therefore look like
`SPEC · VERIFIED` or `TEACHING · (by definition, disclosed)`.

## 2. Source hierarchy

When sources conflict, prefer in this order:

1. The official standard/specification (USB-IF, ETG, Bluetooth SIG, IEEE).
2. The chip vendor's datasheet / reference manual / errata.
3. The SDK/framework's own documentation or source code.
4. Reputable secondary sources (books like *USB Complete*, tool vendor
   app notes) — usable, but cite as secondary.
5. Nothing else counts as a source. Forum posts and AI-generated pages are
   not sources; they are leads to verify.

## 3. Verification procedure

For each claim:

1. Classify: is this standard behavior, vendor behavior, chip behavior,
   SDK behavior, or my simplification?
2. Find a source for it (record title + clause/section + URL or file path).
3. If found → tag `VERIFIED` with the source.
4. If not found → tag `UNVERIFIED` and either (a) research further,
   (b) mark the content as `TEACHING` with an honest on-screen label, or
   (c) remove the claim.
5. If the animation cannot proceed without an unconfirmed claim → **stop**
   and tell the user what is unconfirmed.

## 4. Rules that must never be broken

- **Protocol order is sacred.** Do not reorder messages, do not skip steps
  silently, do not shorten timeouts without labeling. If real timing is too
  fast to see, scale time *uniformly* and state the scaling factor.
- **Vendor ≠ standard.** "TI computes Clarke as Iβ = (Ia + 2·Ib)/√3" is a
  VENDOR/TEACHING statement about a convention, not physics.
- **Simplification ≠ reality.** A labeled `TEACHING` simplification must not
  change the conclusions the learner draws.
- **No invented sources.** Never fabricate clause numbers, URLs, or
  datasheet values. An unsourced claim stays `UNVERIFIED`.
- **No silent uncertainty.** `UNVERIFIED` content is a release blocker:
  resolve it or cut it.
- **Same data everywhere.** Every number displayed (duty cycle, RMS current,
  working counter, descriptor bytes) must be computed from the same state
  that drives the graphics. Decorative numbers are technical errors.
- **Respect physical law.** Arrows, field directions, current directions,
  and rotations must be consistent with the actual physics/sign conventions.

## 5. Known misconception traps (from real technical reviews)

| Domain | Wrong (seen in the wild) | Right |
|---|---|---|
| EtherCAT | "The master polls each slave" / slaves forward like Ethernet switches | The frame travels slave-to-slave; each ESC reads/writes its data **on the fly** and the frame continues; slave processing adds nanoseconds-to-µs, not store-and-forward delay |
| USB | "The device sends its descriptor when connected" | The **host** initiates every transfer; the device only responds on endpoint 0 |
| USB | Skipping that the host reads only 8 descriptor bytes first (to learn bMaxPacketSize0) | Show the 8-byte read, then SET_ADDRESS, then the full descriptor read |
| FOC | A rotating arrow that is not the vector sum of the plotted phase currents | Compute Clarke/Park from the same ia/ib/ic plotted; display the intermediate αβ components |
| State machines | Missing exception branches (timeout, NAK/retry, error) | Every real protocol has failure paths; show at least one |
| PWM | "Changing duty changes frequency" | Duty and frequency are independent parameters; compute Vavg = D·Vsupply live |

## 6. Quoting and rewriting

- Short quotes from standards with citation are acceptable ("USB 2.0,
  §8.5.3: …"). Copying long passages is not — and never copy another
  tutorial's text or code.
- Rewrite all technical explanation in your own words. The standard is the
  *authority*; your page is the *explanation*.
- Record every consulted source in the project's `SOURCES.md` with category
  (standard / datasheet / SDK doc / open-source project / academic /
  teaching reference) and access date.
