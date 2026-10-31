# Accessibility

Technical animations must be usable by everyone, including keyboard-only
users, screen-reader users, low-vision users, and motion-sensitive users.

## 1. Reduced motion (`prefers-reduced-motion`)

Define behavior in CSS *and* JS:

```css
@media (prefers-reduced-motion: reduce) {
  .tae-decorative { animation: none !important; transition: none !important; }
}
```

- Decorative motion (pulses, glows, easing flourishes) is disabled.
- The **teaching content stays available** — the animation does not vanish;
  it either starts paused with a clear caption, or plays at reduced speed
  without non-essential motion. The learner controls progression via step
  buttons.
- Never flash content faster than ~3 Hz (seizure safety).

## 2. Themes & contrast

- Implement light + dark with CSS custom properties
  (`:root { --bg: …; } @media (prefers-color-scheme: dark) { … }`).
- Text contrast ≥ 4.5:1 (WCAG AA); graphical objects ≥ 3:1 against
  adjacent colors. Verify **both themes** — a palette that works on white
  often fails on near-black.
- Never encode meaning by color alone: pair with label, shape, or pattern
  (e.g. error = red + "ERR" text + dashed outline).

## 3. Keyboard

- All controls focusable and operable: Tab order = visual/logical order;
  Enter/Space activate buttons; arrow keys on range inputs work natively.
- Add `space = play/pause, ←/→ = step` on the stage (with `tabindex="0"` and
  documented behavior) unless focus conflicts arise.
- Visible focus indicators (`:focus-visible`), never `outline: none` without
  a replacement.

## 4. Screen readers

- `<html lang="…">` correct.
- SVG: `role="img"` + `<title>` (and `<desc>` for complex stages) on the
  root; `aria-hidden="true"` on purely decorative nodes.
- Captions are real text (`aria-live="polite"` on the caption container) —
  the narrative is available without watching motion.
- Controls labeled (`aria-label`); speed/scenario selects labeled; timeline
  range input labeled with its meaning.
- State changes that matter are reflected in text (caption/evidence footer),
  not only visually.

## 5. Text and language

- Define abbreviations at first use (ESC, Wc, PID…); keep a short legend on
  the page.
- Font sizes ≥ 14 px for body text in HTML overlays; SVG labels sized to
  remain legible when the SVG scales down.

## QA hooks

`validate_animation.py` warns on missing `prefers-reduced-motion` handling
and unlabeled buttons; the visual review (visual-review.md) checks contrast
in both themes; the Playwright suite exercises keyboard-operable controls.
