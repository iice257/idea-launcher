#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const launcher = join(here, "launch_project.py");
const args = process.argv.slice(2);

const candidates = process.platform === "win32" ? ["python", "py"] : ["python3", "python"];
let result;

for (const command of candidates) {
  result = spawnSync(command, [launcher, ...args], { stdio: "inherit" });
  if (result.error?.code === "ENOENT") {
    continue;
  }
  process.exit(result.status ?? 1);
}

console.error("Idea Launcher requires Python 3 on PATH.");
process.exit(1);
