# Animation Taxonomy: Types & When to Animate

Five animation types cover the technical-teaching space. One animation has
one **primary** type; secondary patterns inside it (a state strip in a
sequence, a buffer view in a data flow) are fine.

## Type A — Protocol Sequence

**Use for:** USB enumeration, USB control transfer, Ethernet frame
transmission, EtherCAT communication, BLE advertising / connection
establishment, Wi-Fi association — anything with an ordered message
exchange between named parties.

**Must show:** participants (lanes/devices); message direction (arrow);
message order (numbering/position); trigger conditions; response conditions;
at least one timeout and one retry/exception; state changes that result
(side panel or state strip).

**Recommended forms:** sequence diagram; timeline; packet animation along a
wire; message-exchange table that fills in.

**Accuracy bar:** message order and conditions are `SPEC` material — they
may not be reordered or dropped for visual convenience
([technical-accuracy.md](technical-accuracy.md)).

## Type B — Data Flow

**Use for:** Ethernet/USB packet structure and travel, DMA transfers,
memory copy, CPU data path, SPI/I2C/UART byte exchange, buffer management.

**Must show:** data source; destination; intermediate processing nodes;
the data structure itself (fields/bits/bytes); data transformation at each
node; direction; buffer/queue contents changing.

**Recommended forms:** packet moving through stages; field-level structure
view (highlight the field being processed); buffer cells draining/filling;
pipeline view.

## Type C — State Machine

**Use for:** USB device states, BLE connection states, FreeRTOS task
states, driver init, boot processes — anything where the *state* is the
knowledge and transitions are the lesson.

**Must show:** all key states; transition conditions (labels on edges);
trigger events; current-state highlight; exception branches; return paths
(back-edges are first-class, not afterthoughts).

**Recommended forms:** node-edge diagram with a moving "you are here"
highlight; event log panel; timeline of events driving transitions.

**QA note:** state machines get transition-path tests
([animation-testing.md](animation-testing.md) §4).

## Type D — Physical Mechanism

**Use for:** FOC / Clarke / Park, motor control, PWM, ADC sampling,
magnetic fields, power electronics — continuous physical processes.

**Must show:** the physical objects; spatial relations; directions
(current, field, rotation — with sign conventions); the change process;
the mathematical relationships; how quantities relate to each other.

**Hard rule:** never depict something that violates physics or the stated
sign convention. The displayed math and the displayed picture must be
computed from the **same data** — a rotating arrow that is not the vector
sum of the plotted phase currents is a blocker.

## Type E — Interactive Simulation

**Use for:** PWM, sampling, motor control, protocol timing, buffer
management, scheduling — where the lesson is *parameter sensitivity*.

**Must provide:** user-changeable parameters; immediate, consistent updates
of graphics **and** every dependent number; a live formula with real
numbers; a default case that matches the textbook.

**Bar:** changing duty must change the waveform, the number, and the text
explanation together. Graphics-only updates are a bug.

## When to animate vs when to go static

Evidence base (see project `RESEARCH.md` / `SOURCES.md` for full citations):
Tversky, Morrison & Bétrancourt 2002 (apprehension + congruence principles),
Mayer & Moreno 2003, Mayer & Chandler 2001 (segmenting), Sweller 1988
(cognitive load).

| Content kind | Recommendation |
|---|---|
| Discrete handshake / ordered steps with few states | **Static diagram with numbered steps first**; add a *stepwise* animation (pause/step controls), not continuous playback |
| Continuous dynamics (fields, charging, rotation, waveforms) | **Animation** — this is where animation genuinely beats static |
| Structure with no time dimension (memory map, register fields, taxonomy) | **Static**; animation adds nothing |
| "How big / how fast" sensitivity questions | **Interactive simulation** |
| Process spread over devices (packet travels, frame loops) | **Animation + step controls** (order & causality are the point) |
| Anything the learner must *operate*, not watch | **Simulation / guided experiment** |

Two governing principles:

- **Apprehension:** if the learner can't accurately perceive what changed,
  the animation fails — pace, pause, step, and replay are not luxuries.
- **Congruence:** the animation form must match the content form; discrete
  content wants discrete (stepped) display, continuous content wants motion.

## Design rules baked into this skill (with their evidence)

1. Step controls + captions are the primary interface; continuous playback
   is the option, not the default lesson (segmenting — Mayer & Chandler 2001).
2. Highlight exactly the element being explained; don't make learners search
   the frame (signaling).
3. No decorative motion, no spinning/bouncing filler (coherence; seductive
   details harm retention).
4. Caption sits adjacent to what it describes and stays in sync (spatial +
   temporal contiguity).
5. Legend/labels are established before the story plays (pre-training).
6. Default pace is slow enough to read; speed control exists for experts
   (apprehension).
7. One subsystem at a time; simple scenario before exception scenario
   (managing intrinsic load).
8. Interactive parameter manipulation is a deliberate, designed mode
   (Type E), not unconstrained "learner control" everywhere — broad learner
   control shows near-zero average effect; purposeful control (pause/step/
   replay) is the reliably beneficial kind (Karich et al. 2014; Bétrancourt
   2005).
