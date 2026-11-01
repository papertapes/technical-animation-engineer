/* Browser runner for the in-repo benchmark examples (skill repository). */
import { chromium } from "playwright";
import { mkdirSync, writeFileSync, readdirSync } from "node:fs";
import { join, dirname, resolve, basename } from "node:path";
import { fileURLToPath } from "node:url";
const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..", "..");
const DIR = join(ROOT, "examples");
const SHOTS = join(ROOT, "benchmarks", "results", "screenshots");
mkdirSync(SHOTS, { recursive: true });
const files = readdirSync(DIR).filter(f => !f.startsWith(".")).map(f => join(DIR, f, "index.html"));
/* per-page exception beat: fraction of the story where the injected fault is visible */
const EXC_SEEK = { "usb-enumeration": 0.34, "usb-packet-structure": 0.55, "usb-transfer-types": 0.62 };
const browser = await chromium.launch();
const report = []; let failures = 0;
for (const file of files) {
  const name = basename(dirname(file));
  const dir = join(SHOTS, name); mkdirSync(dir, { recursive: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 950 } });
  const errs = [];
  page.on("pageerror", e => errs.push(String(e).slice(0, 120)));
  page.on("console", c => { if (c.type() === "error") errs.push(c.text().slice(0, 120)); });
  const entry = { page: name, errors: errs, checks: [] };
  try {
    await page.goto("file:///" + file.split("\\").join("/"));
    await page.waitForTimeout(500);
    await page.screenshot({ path: join(dir, "01-initial.png"), fullPage: true });
    await page.click('[data-tae-action="play-pause"]');
    await page.waitForTimeout(1700);
    await page.screenshot({ path: join(dir, "02-playing.png"), fullPage: true });
    await page.click('[data-tae-action="play-pause"]');
    await page.click('[data-tae-action="step-fwd"]'); await page.waitForTimeout(200);
    await page.evaluate(() => {
      const el = document.querySelector('[data-tae-timeline]');
      el.value = "500"; el.dispatchEvent(new Event("input", { bubbles: true }));
    });
    await page.waitForTimeout(250);
    await page.screenshot({ path: join(dir, "03-mid.png"), fullPage: true });
    const det = await page.evaluate(() => {
      const T = window.__TAE__; if (!T) return { ok: false };
      const t1 = T.duration * 0.4; T.seek(t1);
      const v1 = document.getElementById("stage").getAttribute("viewBox") || "n/a";
      T.seek(T.duration * 0.9); T.seek(t1);
      return { ok: true, same: (document.getElementById("stage").getAttribute("viewBox") || "n/a") === v1 };
    });
    entry.checks.push({ name: "scrub determinism", ok: det.ok && det.same !== false, detail: JSON.stringify(det) });
    if (await page.$('[data-tae-action="scenario"]')) {
      const opts = await page.$eval('[data-tae-action="scenario"]', el => Array.from(el.options).map(o => o.value));
      if (opts.length > 1) {
        await page.selectOption('[data-tae-action="scenario"]', opts[opts.length - 1]);
        await page.waitForTimeout(300);
        const frac = EXC_SEEK[name] || 0.5;
        await page.evaluate(f => { const T = window.__TAE__; T.seek(T.duration * f); }, frac);
        await page.waitForTimeout(300);
        await page.screenshot({ path: join(dir, "04-exception.png"), fullPage: true });
        await page.selectOption('[data-tae-action="scenario"]', opts[0]);
        await page.evaluate(() => window.__TAE__.reset());
        await page.waitForTimeout(200);
      }
    }
    await page.click('[data-tae-action="reset"]'); await page.waitForTimeout(200);
    await page.screenshot({ path: join(dir, "05-reset.png"), fullPage: true });
    await page.setViewportSize({ width: 720, height: 950 }); await page.waitForTimeout(300);
    await page.screenshot({ path: join(dir, "06-narrow-720.png"), fullPage: true });
  } catch (e) { errs.push("runner: " + String(e).slice(0, 150)); }
  await page.close();
  entry.ok = errs.length === 0 && entry.checks.every(c => c.ok);
  if (!entry.ok) failures++;
  report.push(entry);
  console.log((entry.ok ? "PASS " : "FAIL ") + name +
    (entry.checks.length ? " [" + entry.checks.map(c => (c.ok ? "✓" : "✗") + " " + c.name).join("; ") + "]" : "") +
    (errs.length ? " ERR: " + errs.join("|").slice(0, 160) : ""));
}
await browser.close();
writeFileSync(join(ROOT, "benchmarks", "results", "browser-tests.json"), JSON.stringify(report, null, 2));
console.log(`${report.length - failures}/${report.length} benchmarks passed`);
process.exit(failures ? 1 : 0);
